# ===================================
# @Time : 2020/11/30 22:55
# 求积分
# ===================================
from sympy import Symbol, symbols
from sympy import integrate, Integral, simplify, latex
from sympy.abc import x, y, z, u, v, s, theta
from sympy.integrals.manualintegrate import integral_steps
from sympy import sin, cos, atan, pi, sqrt, diff
from sympy.plotting import plot, plot3d, PlotGrid, plot_parametric, plot3d_parametric_surface, plot3d_parametric_line

a, L = symbols('a,L', constant=True)


def basement_func(steps):
    content = steps.context
    base_f = '$' + latex(Integral(content, x)) + '$'
    result = '$' + latex(integrate(content, x)) + '$'
    steps_str = str(steps)
    if 'PowerRule' in steps_str:
        print('基本初等函数_指数函数: ' + base_f + '=' + result)
    if 'ArcsinRule' in steps_str:
        print('基本初等函数_Arcsin: ' + base_f + '=' + result)


def analysis_steps(steps):
    try:
        # 目标函数
        context = steps.context
        field = steps._fields
    except:
        for line in steps:
            analysis_steps(line)
    else:
        if 'alternatives' in field:
            print('函数变更：$' + latex(Integral(context, x)) + '$')
            new_steps = steps.alternatives[0]
            f1 = '$' + latex(Integral(new_steps.rewritten, x)) + '$'
            print('=' + f1 + '\n')
            analysis_steps(new_steps)
        if 'rewritten' in field:
            new_f = '$' + latex(Integral(steps.rewritten, x)) + '$'
            print('函数Rewritten：$' + latex(Integral(context, x)) + '$ =' + new_f + '\n')
            new_steps = steps.substep.substeps
            analysis_steps(new_steps)
        if 'substeps' in field:
            new_steps = steps.substeps
            analysis_steps(new_steps)
        if 'other' in field:
            result = simplify(integrate(context, x))
            out4 = '$' + latex(Integral(context, x)) + '=' + latex(result) + '$'
            print('分项积分：' + out4 + '\n')
        basement_func(steps)


def test():
    f_x = atan(x)
    out_f = '$' + latex(Integral(f_x, x)) + '$'
    steps = integral_steps(f_x, x)
    analysis_steps(steps)
    f_x_result = '$' + latex(simplify(integrate(f_x, x))) + '$'
    print('结果为：' + out_f + '=' + f_x_result)


def get_filename(f):
    f_str = str(f)
    if '/' in f_str:
        f_str = f_str.replace('/', '_')
    if '**' in f_str:
        f_str = f_str.replace('**', '^')
    f_str = f_str.replace(' ', '')
    filename = '../images/' + f_str + '.jpg'
    return filename


def plot_line(f, a, b):
    # 函数
    p1 = plot(f, (x, a, b), title=f, ylabel='', show=False)

    # 不定积分函数
    indefinite_f = integrate(f, x)
    p2 = plot(indefinite_f, (x, a, b), title=indefinite_f, ylabel='', show=False)
    file_name = get_filename(f)
    PlotGrid(2, 1, p1, p2).save(file_name)


def explore_p_func():
    a = -2
    b = 2
    f1 = 1 / (x ** 0.2)
    f2 = 1 / (x ** 0.5)
    f3 = 1 / (x ** 0.8)
    p1 = plot(f1, (x, a, b), title=str(f1), ylabel='', show=False)
    p2 = plot(f2, (x, a, b), title=str(f2), ylabel='', show=False)
    p3 = plot(f3, (x, a, b), title=str(f3), ylabel='', show=False)
    PlotGrid(3, 1, p1, p2, p3)


def ball():
    # x^2+y^2+z^2=a^2
    # plot3d(x**2+y**2+z**2,(x,-2,2),(y,-2,2),(z,-2,z))
    plot3d_parametric_surface(cos(u + v), sin(u - v), u - v, (u, -5, 5), (v, -5, 5))
    plot3d_parametric_line((cos(u), sin(u), u, (u, -5, 5)), (sin(u), u ** 2, u, (u, -5, 5)))
    # 圆
    plot_parametric((cos(u), sin(u), (u, -5, 5)), (cos(u), u, (u, -5, 5)))


class FuncDatabase:
    def test1(self):
        # L曲线 P212 第一曲线积分例一
        x_subs = a * cos(t)  # 控制半圆半径
        y_subs = a * sin(t)
        t_min = 0
        t_max = pi
        func = x ** 2 + y ** 2


def first_form_curvilinear_integral():
    '''第一型曲线积分：曲线质量
    '''
    x_subs = a * cos(t)  # 控制半圆半径
    y_subs = a * sin(t)
    t_min = -pi / 2
    t_max = pi / 2
    func = (x ** 2 + y ** 2) ** (1 / 2)
    # plot_parametric((x_subs.subs(a, 1), y_subs.subs(a, 1)), (t, t_min, t_max), title='curvi linear: L')

    # 曲线L在t的坐标系上
    L_trans = r'$set L: \begin{cases} ' + \
              r'x={}\\y={} & t \in [{},{}]'.format(latex(x_subs), latex(y_subs), t_min, t_max) + \
              r'\end{cases}$'
    print(L_trans)

    # 密度函数
    print('计算第一型曲线积分：$' + latex(Integral(func, (s, L,))) + '$')

    # 第一型曲线积分求解
    new_func = func.subs({x: x_subs, y: y_subs})
    diff1 = diff(x_subs, t)
    diff2 = diff(y_subs, t)
    new_ds = sqrt(diff1 ** 2 + diff2 ** 2)
    cal_func = simplify(new_func) * simplify(new_ds)
    print(r'$= \int_{}^{} {}'.format(t_min, t_max, latex(new_func)) + latex(new_ds) + 'd{}$'.format(t))
    print('$=' + latex(Integral(cal_func, (t, t_min, t_max))) + '$')
    result = integrate(cal_func, (t, t_min, t_max))
    print('$={}$'.format(latex(result)))


def second_form_curvilinear_integral():
    '''第二型曲线积分'''

    def analysis_result(P_func, Q_func, x_subs, y_subs, t_min, t_max, t):
        # 曲线L在x的坐标系上
        L_trans = r'解：$set L: \begin{cases} ' + \
                  r'x={}\\y={} & t \in [{},{}]'.format(latex(x_subs), latex(y_subs), t_min, t_max) + \
                  r'\end{cases}$'
        print(L_trans)

        print('计算第二型曲线积分：$\int_L {}dx + ({})dy$'.format(latex(P_func), latex(Q_func)))
        # 第一型曲线积分求解
        new_P_func = P_func.subs({x: x_subs, y: y_subs})
        new_Q_func = Q_func.subs({x: x_subs, y: y_subs})
        diff1 = diff(x_subs, t)
        diff2 = diff(y_subs, t)

        cal_func = simplify(new_P_func * diff1 + new_Q_func * diff2)
        simpy_submit = latex(Integral(cal_func, (t, t_min, t_max)))
        print(r'替换y: $= \int_{}^{} {}*{}d{}+{}*{}d{} = {}$'.format(t_min, t_max,
                                                                   latex(new_P_func), latex(diff1), t,
                                                                   latex(new_Q_func), latex(diff2), t, simpy_submit))
        # 不定积分求原函数F(x)
        result = integrate(cal_func, (t, t_min, t_max))
        latex_result = latex(result)
        print('= 原函数: $F(x)|_a^b={}|_{}^{} = {}$'.format(latex(integrate(cal_func, t)), t_min, t_max, latex_result))

    def y_about_x():
        # y是关于x的显函数
        # PQ的操作比较稳定的，就是替换掉就好
        P_func = y
        Q_func = x
        # 基于L得到x_subs，y_subs
        x_subs = x
        y_subs = 2*x
        x_min = 0
        x_max = 1
        analysis_result(P_func, Q_func, x_subs, y_subs, x_min, x_max, x)

    def x_about_y():
        '''x关于y的显函数'''
        P_func = y
        Q_func = x
        # 基于L得到x_subs，y_subs
        x_subs = 1
        y_subs = y
        y_min = 0
        y_max = 2

        analysis_result(P_func, Q_func, x_subs, y_subs, y_min, y_max, y)

    def three_dim_about_t():
        '''关于t的三维曲线积分'''
        
    y_about_x()
    # x_about_y()


if __name__ == '__main__':
    second_form_curvilinear_integral()
