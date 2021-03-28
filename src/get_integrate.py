# ===================================
# @Time : 2020/11/30 22:55
# 求积分
# ===================================
from sympy import Symbol, symbols
from sympy import integrate, Integral, simplify, latex
from sympy.abc import x, y, u, v
from sympy.integrals.manualintegrate import integral_steps
from sympy import atan
from sympy.plotting import plot, plot3d, PlotGrid


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
