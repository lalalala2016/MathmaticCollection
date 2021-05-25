# ===================================
# @Time : 2021/5/24 21:34
# 隐函数
# ===================================
from sympy.abc import x, y, u, v, z
from sympy import Eq, diff, simplify, latex, symbols, solve
from sympy import sin

a = symbols('a', real=True)


def make_sure_implicit_existence(F):
    '''判断隐含是是存在的'''
    print('不是所有方程都能确定出隐函数的')
    result = True
    return result


def test1():
    '''课本例题1'''
    F_func = y - x - 1 / 2 * sin(y)
    F_value = 0
    exist = make_sure_implicit_existence(F_func)
    F_x = F_func.diff(x)
    F_y = F_func.diff(y)
    y_diff = -F_x / F_y
    desc = r"y'=f'(x)=-\frac{F_x}{F_y}"
    print('${} = {}$'.format(desc, latex(y_diff)))


def test2():
    '''课本例题2'''
    F_func = x ** 3 + y ** 3 - 3 * a * x * y
    F_value = 0

    # 一阶偏导数
    print('隐函数一阶导数')
    F_x = F_func.diff(x)
    F_y = F_func.diff(y)
    print('$F_x,F_y: {},{}$'.format(latex(F_x), latex(F_y)))
    y_diff = simplify(-F_x / F_y)
    desc = r"y'=f'(x)=-\frac{F_x}{F_y}"
    print('${} = {}$'.format(desc, latex(y_diff)))

    # 二阶偏导数
    print('隐函数二阶导数')
    F_xy = F_x.diff(y)
    F_xx = F_x.diff(x)
    F_yy = F_y.diff(y)
    desc1 = 'F_{xx},F_{xy},F_{yy}'
    print(r'${}: {},{},{}$'.format(desc1, latex(F_xx), latex(F_xy), latex(F_yy)))
    part_1 = 2 * F_x * F_y * F_xy
    part_2 = F_y ** 2 * F_xx
    part_3 = F_x ** 2 * F_yy
    y_2diff = (part_1 - part_2 - part_3) / F_y ** 3
    desc2 = r"y'=f'(x) = \frac{2F_xF_yF_{xy} - F_y^2F_{xx} - F_x^2F_{yy}}{F_y^3}"
    print('${} = {}$'.format(desc2, latex(y_2diff)))

    # 求极值点
    new_f = F_func.subs(y, 1 / a * x ** 2)
    print('${}$'.format(latex(new_f)))
    solve(new_f, x)  # 默认等于0


def test3():
    '''偏导数与全微分
    d和\delta分别表示导数和偏导数, 符号上是有差异的
    '''
    # 关于z的隐函数
    F_func = x * y * z ** 3 + x ** 2 + y ** 3 - z
    F_value = 0

    # 一阶偏导数
    F_x = F_func.diff(x)
    F_y = F_func.diff(y)
    F_z = F_func.diff(z)

    # z_x
    print('z关于x的偏导数： $F_x,F_z: {},{}$'.format(latex(F_x), latex(F_z)))
    z_x_diff = simplify(-F_x / F_z)
    desc = r"\frac{\delta z}{\delta x}=-\frac{F_x}{F_z}"
    print('${} = {}$'.format(desc, latex(z_x_diff)))

    # z_y
    print('z关于y的偏导数： $F_y,F_z: {},{}$'.format(latex(F_y), latex(F_z)))
    z_y_diff = simplify(-F_y / F_z)
    desc = r"\frac{\delta z}{\delta y}=-\frac{F_y}{F_z}"
    print('${} = {}$'.format(desc, latex(z_y_diff)))

    # 全微分： dz = f_x(x-x_0) + f_y(y-y_0)
    subs_dict = {x: 0, y: 1, z: 1}
    z_x = z_x_diff.subs(subs_dict)
    z_y = z_y_diff.subs(subs_dict)
    print(r"$\frac{\delta z}{\delta x}=" + latex(z_x) + "$")
    print(r"$\frac{\delta z}{\delta y}=" + latex(z_y) + "$")


if __name__ == '__main__':
    test3()
