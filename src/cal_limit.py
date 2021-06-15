# ===================================
# @Time : 2021/5/28 19:44
# ===================================
import sympy
from sympy.abc import x, y, u, v, z, n
from sympy import Eq, diff, simplify, latex, symbols, solve, Symbol, limit, Limit, sqrt, exp, oo, pi
from sympy import sin, cos, tan, cot, asin, acos, atan, ln

a = Symbol('a', real=True)
b = Symbol('b', real=True)

# 等价无穷小代换
A_Dict = {sin(x): x,
          tan(x): x,
          asin(x): x,
          atan(x): x,
          1 - cos(x): 1 / 2 * x ** 2,
          exp(x) - 1: x,
          ln(1 + x): x,
          sqrt(1 + x) - 1: 1 / 2 * x,
          # 变形
          1 - exp(x): -x
          }


# 函数变形


# 基本初等函数
def baserule(func, t, trend):
    '''基本四则运算，能处理就先处理掉'''
    # 只能加减乘除，指数形式不行的
    print('步骤一：先考虑能否直接四则运行，能消去一个是一个')
    if func.func != sympy.power.Pow:
        change = False
        new_func = []
        for part_i in func.args:
            cal_limit = limit(part_i, t, trend)
            if cal_limit not in [0, oo, -oo]:
                new_func.append(cal_limit)
                change = True
            else:
                new_func.append(part_i)
        if change:
            func = 1
            for i in new_func:
                func *= i
            print('四则运算后原函数为：${}$'.format(latex(func)))
        else:
            print('四则运算无法消去任意部分')
    else:
        print('指数形式须变形后才能使用四则运算')
    return func


class Substitution:
    def __init__(self, func, t):
        self.value = t
        self.newfunc = self.inf_subsititution(func, t)

    def get_func_values(self, part_i):
        '''例如得到cos(x**2)的值为x**2
        ln(1+sin(x))得到sin(x)
        '''
        func_Set = [sympy.sin, sympy.cos, sympy.log]
        num = part_i.args.__len__()
        func_type = part_i.func
        if num > 0 and func_type not in func_Set:
            for part in part_i.args:
                if part.free_symbols == set():
                    continue
                else:
                    num2 = part.args.__len__()
                    if num2 > 1:
                        self.get_func_values(part)
                    else:
                        if part.args:
                            self.value = part.args[0]
        elif num > 0:
            relative_value = part_i.args[0]
            if relative_value.func not in func_Set:
                self.value = part_i.args[0]
            else:
                self.value = part_i.args[0].args[1]

    def get_part_i_subs(self, part_i, t, A_Set):
        if part_i in A_Set:
            # 如果在集合里直接替换
            change = True
            sim_value = A_Dict[part_i]
            result = sim_value
            print('等价无穷小：${} \sim {}$'.format(latex(part_i), latex(sim_value)))
        else:
            # 如果不在集合中，尝试变形
            self.get_func_values(part_i)  # 更新获得value
            if self.value != t:
                # 变量替换
                subs_func = part_i.subs(self.value, x)
                # 变形完是否在集合里？
                if subs_func in A_Set:
                    change = True
                    sim_value = A_Dict[subs_func]
                    sim_value = sim_value.subs(x, self.value)
                    result = sim_value
                    print('等价无穷小：${} \sim {}$'.format(latex(part_i), latex(sim_value)))
                else:
                    change = False
                    result = part_i
            else:
                change = False
                result = part_i
        return result, change

    def inf_subsititution(self, func, t):
        print('步骤二：等价无穷小代换')
        A_Set = A_Dict.keys()
        change = False
        if func.func != sympy.power.Pow:
            top = []
            bottom = []
            if func.func == sympy.mul.Mul:
                # sympy.power.Pow
                # 只处理乘除，除法在计算机里是a^-1的指数形式表示的
                new_func = []
                for part_i in func.args:
                    if part_i.func == sympy.power.Pow and part_i.exp < 0:
                        # 分母
                        bottom_part_i = 1 / part_i
                        result, change = self.get_part_i_subs(bottom_part_i, t, A_Set)
                        bottom.append(result)
                    else:
                        # 分子
                        result, change = self.get_part_i_subs(part_i, t, A_Set)
                        top.append(result)
            else:
                print('等价无穷代换只处理乘法/除法')

            if change:
                # 分子
                top_func = 1
                top_desc = ''
                for i in top:
                    top_func *= i
                    top_desc += latex(i)
                # 分母
                bottom_func = 1
                bottom_desc = ''
                for j in bottom:
                    bottom_func *= j
                    bottom_desc += latex(j)
                desc_str1 = r'\frac{' + top_desc + '}{' + bottom_desc + '}'
                desc_str2 = r'\frac{' + latex(top_func) + '}{' + latex(bottom_func) + '}'
                func = top_func / bottom_func
                if desc_str1 == desc_str2:
                    print('等价无穷小代换后：$={}={}$'.format(desc_str1, latex(func)))
                else:
                    print('等价无穷小代换后：$={}={}={}$'.format(desc_str1, desc_str2, latex(func)))
            else:
                print('无等价无穷小代换的部分')
        else:
            print('指数形式须变形后才能使用等价无穷小代换')
        return func


def sinx_x_funx(func, t, trend):
    print(r'步骤三：利用已知函数，因为$\lim_{x \to 0}\frac{sinx}{x}=1')
    # 函数变形


def limit_e_func(func, t, trend):
    '''利用已知极限：lim_{x \to 0}(1+x)^{1/x} = e'''
    print(r'步骤三：利用已知函数，因为函数是$f(x)^{g(x)}$形式，或许可以利用$\lim_{x \to 0}(1+x)^{1/x}=e$')
    if func.func == sympy.power.Pow:
        base_func = func.base
        exp_func = func.exp
        base_value = base_func.args[1]
        aim_value = 1 / base_value
        add_value = exp_func / aim_value
        desc_str = '{' + latex(aim_value) + latex(add_value) + '}'
        print('函数变形：原函数$=({})^{}$'.format(latex(base_func), desc_str))


# 等价无穷小替换
def test1():
    part1 = sqrt(1 - cos(x ** 2))
    part2 = 1 - cos(x)
    func = (1+a/x) ** (b*x)
    x_trend = oo
    print('计算${}$'.format(latex(Limit(func, x, x_trend))))
    # 如果是加减乘除形式
    func = baserule(func, x, x_trend)
    func = Substitution(func, x).newfunc
    # 指数形式
    limit_e_func(func, x, x_trend)

func = 1/(x+1)-3/(x**3+1)
simplify(func)
limit(func,x,-1)


if __name__ == '__main__':
    # func = 1/sin(x**2)
    # Substitution(func, x)
    test1()
