# ===================================
# @Time : 2021/5/15 17:12
# 多重积分求解：二重积分、三重积分
# ===================================
from sympy.abc import x, y, z, u, v, s, t, theta
from sympy.integrals.manualintegrate import integral_steps
from sympy import sin, cos, atan, pi, sqrt, diff
from sympy.plotting import plot, plot3d, PlotGrid, plot_parametric, plot3d_parametric_surface, plot3d_parametric_line
from sympy import S
from sympy.abc import x, y, z, s, u, v, r
from sympy.abc import pi, theta
from sympy.functions import beta, gamma, exp, sqrt
from sympy import integrate, latex, Integral, symbols, expand, Eq, diff, simplify
from sympy.solvers.solveset import solveset, solveset_real
from sympy.plotting import plot, plot3d, PlotGrid, plot_parametric
from sympy import sin, cos, tan, cot, sec, csc, atan

a, b, c, m, n, L, k, R = symbols('a,b,c,m,n,L,k,R', constant=True)


class IterateApprocah:
    # 累次积分，基础方法
    def __init__(self, func, x_min, x_max, y_min, y_max, t1, t2):
        self.x_range_str = r'\int_{' + latex(x_min) + '}^{' + latex(x_max) + '}'
        self.y_range_str = r'\int_{' + latex(y_min) + '}^{' + latex(y_max) + '}'
        self.F_x = '|_{' + latex(x_min) + '}^{' + latex(x_max) + '}'
        self.F_y = '|_{' + latex(y_min) + '}^{' + latex(y_max) + '}'
        self.iterated_approach(func, x_min, x_max, y_min, y_max, t1, t2)

    def first_xy(self, func, x_min, x_max, y_min, y_max, t1, t2):
        '''优先对dx处理？还是优先对dy处理？

        '''
        if t1 in func.free_symbols and t2 not in func.free_symbols:
            # 如果f是关于x的函数，优先x处理
            first_x = True
        else:
            # 如果f(x,y)x,y都有，看[x_min, x_max], [y_min, y_max]哪个复杂，优先哪个
            if x_min.__class__ == 'int' and x_max.__class__ == 'int':
                first_x = False
            else:
                # x是关于y的函数，优先处理x
                first_x = True
        if first_x:
            print('优先对d{}处理'.format(t1))
        else:
            print('优先对d{}处理'.format(t2))
        return first_x

    def first_x_analysis(self, func, x_min, x_max, y_min, y_max, t1, t2):
        step1 = '$={} d{} {} {} d{}$'.format(self.y_range_str, t2, self.x_range_str, latex(func), t1)
        print(step1)
        # func原函数
        part_1_Func = simplify(integrate(func, t1))
        part_1 = simplify(simplify(part_1_Func.subs(t1, x_max)) - simplify(part_1_Func.subs(t1, x_min)))
        print('首先： ${} {} d{} = {}{} = {}$'.format(self.x_range_str,
                                                   latex(func), t1,
                                                   latex(part_1_Func), self.F_x,
                                                   latex(part_1)))
        # 有时候算不出来
        part_2_Func = integrate(part_1, t2)
        part_2 = simplify(part_2_Func.subs(t2, y_max) - part_2_Func.subs(t2, y_min))
        print('此时： ${} {} d{} = {}{}={}$'.format(self.y_range_str,
                                                 latex(part_1), t2,
                                                 latex(part_2_Func), self.F_y,
                                                 latex(part_2)))

        # result = simplify(integrate(part_2_Func, (y, y_min, y_max)))
        step3 = '原积分=${}$'.format(latex(part_2))
        print(step3)

    def first_y_analysis(self, func, x_min, x_max, y_min, y_max, t1, t2):
        step1 = '$={} d{} {} {} d{}$'.format(self.x_range_str, t1, self.y_range_str, latex(func), t2)
        print(step1)

        # 步骤一：对dy部分求原函数，得到定积分结果函数（关于x）
        part_1_Func = simplify(integrate(func, t2))
        part_1_result = simplify(part_1_Func.subs(t2, y_max) - part_1_Func.subs(t2, y_min))
        print('首先： ${} {} d{} = {}{} = {}$'.format(self.y_range_str,
                                                   latex(func), t2,
                                                   latex(part_1_Func), self.F_y,
                                                   latex(part_1_result)))

        # 步骤二：对dx部分求原函数，得到最终结果
        part_2_Func = simplify(integrate(part_1_result, t1))
        # part_2_result = simplify(part_2_Func.subs(x, x_max) - part_2_Func.subs(x, x_min))
        part_2_result = part_2_Func.subs(t1, x_max) - part_2_Func.subs(t1, x_min)
        print('然后： ${} {} d{} = {}{} = {}$'.format(self.x_range_str,
                                                   latex(part_1_result), t1,
                                                   latex(part_2_Func), self.F_x,
                                                   latex(part_2_result)))

        # 结果
        print('结果：$={}$'.format(latex(part_2_result)))

    def iterated_approach(self, func, x_min, x_max, y_min, y_max, t1, t2):
        # X型的累次叠加法
        print('解：使用累次积分')
        # 优先顺序决定计算的难易程度
        # 也不一定是D的先难后易，看整体哪个复杂的
        first_x = self.first_xy(func, x_min, x_max, y_min, y_max, t1, t2)
        if first_x:
            self.first_x_analysis(func, x_min, x_max, y_min, y_max, t1, t2)
        else:
            self.first_y_analysis(func, x_min, x_max, y_min, y_max, t1, t2)


class SubstitutionApproach:
    def __init__(self, func, new_x, new_y, u_min, u_max, v_min, v_max):
        self.u_range_str = r'\int_{' + latex(u_min) + '}^{' + latex(u_max) + '}'
        self.v_range_str = r'\int_{' + latex(v_min) + '}^{' + latex(v_max) + '}'
        self.F_u = '|_{' + latex(u_min) + '}^{' + latex(u_max) + '}'
        self.F_v = '|_{' + latex(v_min) + '}^{' + latex(v_max) + '}'
        if 'cos' not in str(new_x):
            self.rectangular_coordinate_substution(func, new_x, new_y, u_min, u_max, v_min, v_max)
        else:
            self.polar_coordinate_substution(func, new_x, new_y, u_min, u_max, v_min, v_max)

    # 变量替换法
    def cal_Jacobian(self, new_x, new_y):
        if str(new_x) == 'r*cos(theta)':
            print(r'极坐标变换的雅可比行列式$J(r,\theta)=r$')
            cal_func = r
        elif str(new_x) == 'a*r*cos(theta)':
            print(r'广义极坐标变换的雅可比行列式$J(r,\theta)=rab$')
            cal_func = r * a * b
        else:
            # j(u,v) = [[xu,xv],[yu,yv]]
            x_diff_u = diff(new_x, u)
            x_diff_v = diff(new_x, v)
            y_diff_u = diff(new_y, u)
            y_diff_v = diff(new_y, v)

            jacobian_value = r'{}&{}\\{}&{}'.format(latex(x_diff_u), latex(x_diff_v), latex(y_diff_u), latex(y_diff_v))
            step1 = r"\left|\begin{matrix}x'_u&x'_v\\y'_u&y'_v\end{matrix}\right|=\left|\begin{matrix}" + jacobian_value + r'\end{matrix}\right|'
            cal_func = x_diff_u * y_diff_v - x_diff_v * y_diff_u
            print('其中，雅可比行列式$J(u,v)={}={}$'.format(step1, latex(cal_func)))
        return cal_func

    def rectangular_coordinate_substution(self, func, new_x, new_y, u_min, u_max, v_min, v_max, t1, t2):
        '''直角坐标系的替换'''
        # 设坐标变换
        T_change = r'x={}\\y={} & u \in [{},{}],v \in [{},{}]'.format(latex(new_x), latex(new_y),
                                                                      latex(u_min), latex(u_max),
                                                                      latex(v_min), latex(v_max))
        step1 = r'$set T: \begin{cases}' + T_change + '\end{cases}$'
        print(step1)

        # 原函数等于
        try:
            new_func = func.subs({x: new_x, y: new_y})
        except:
            # 'int' object has no attribute 'subs'
            new_func = func
        step2 = r'变量替换：$\iint_D {}dxdy = \iint_{} {}J(u,v)dudv$'.format(latex(func), '{D2}', latex(new_func))
        print(step2)

        jaco_func = self.cal_Jacobian(new_x, new_y)
        cal_func = new_func * jaco_func
        step3 = '替换后原函数；$={}{} {} dudv$'.format(self.u_range_str,
                                                self.v_range_str,
                                                latex(cal_func)
                                                )
        print(step3)

        IterateApprocah(cal_func, u_min, u_max, v_min, v_max, u, v)

    def polar_coordinate_substution(self, func, new_x, new_y, r_min, r_max, theta_min, theta_max):
        '''极坐标系的变量替换'''
        T_change = r'x={}\\y={} & r \in [{},{}],\theta \in [{},{}]'.format(latex(new_x), latex(new_y),
                                                                           latex(r_min), latex(r_max),
                                                                           latex(theta_min), latex(theta_max))
        step1 = r'$set T: \begin{cases}' + T_change + '\end{cases}$'
        print(step1)

        # 原函数等于
        try:
            new_func = simplify(func.subs({x: new_x, y: new_y}))
        except:
            # 'int' object has no attribute 'subs'
            new_func = func
        step2 = r'变量替换：$\iint_D {}dxdy = \iint_{} {}J(r,\theta)dudv$'.format(latex(func), '{D2}', latex(new_func))
        print(step2)

        # jaco_func = r
        jaco_func = self.cal_Jacobian(new_x, new_y)
        #

        cal_func = new_func * jaco_func
        step3 = r'替换后原函数；$={}{} {} drd\theta$'.format(self.u_range_str, self.v_range_str, latex(cal_func))
        print(step3)

        IterateApprocah(cal_func, r_min, r_max, theta_min, theta_max, r, theta)


class database:
    def test1(self):
        # 例1
        func = y * sin(x * y)
        x_min = 0
        x_max = pi
        y_min = 0
        y_max = 1
        D = [[x_min, x_max], [y_min, y_max]]
        print('计算$\iint_D{}dxdy$，其中D=[{},{}]*[{},{}]'.format(latex(func), x_min, x_max, y_min, y_max))
        IterateApprocah(func, x_min, x_max, y_min, y_max)

    def test2(self):
        func = x ** 2 * exp(-y ** 2)
        x_min = 0
        x_max = y
        y_min = 0
        y_max = 1
        D_split = True  # 有时候D可以拆分，分区域求解
        IterateApprocah(func, x_min, x_max, y_min, y_max)


if __name__ == '__main__':
    func = c * sqrt(1 - x ** 2 / a ** 2 - y ** 2 / b ** 2)
    # u, v = x - y, x + y
    new_x = r * a * cos(theta)
    new_y = r * b * sin(theta)
    # u_min, u_max, v_min, v_max = m, n, a, b
    r_min, r_max, theta_min, theta_max = 0, 1, 0, 0.5 * pi
    SubstitutionApproach(func, new_x, new_y, r_min, r_max, theta_min, theta_max)
    # IterateApprocah(func, x_min, x_max, y_min, y_max)
