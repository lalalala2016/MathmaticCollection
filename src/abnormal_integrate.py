# ===================================
# @Time : 2021/3/27 12:22
# 反常积分：无穷积分、瑕积分
# ===================================
from sympy import symbols, latex
from sympy import Integral, integrate, limit, Limit
from sympy.abc import x, y, u
from sympy import pi, oo
from sympy import sin, cos, tan, asin, sqrt
from sympy.integrals.manualintegrate import integral_steps

from get_integrate import analysis_steps, plot_line

p = symbols('p', real=True, constant=True)


# def limit_convergence():
#     '''极限是否收敛'''
def count_limit(f, a, b):
    print('求极限：$' + latex(Limit(f, a, b)) + '$')
    try:
        limit(f, a, b)
    except:
        # 可能极限发散，没有结果吧
        print('算不出来，和发散有关')


def in_class():
    '''课内习题'''
    math_func = {}

    # 等比 x^{-p}
    p_f = 1 / (x ** p)
    math_func['p_f'] = {'func': p_f, 'a': 1, 'b': +oo}

    # 瑕积分
    for_arcsin_f = 1 / (sqrt(1 - x ** 2))
    math_func['for_arcsin_f'] = {'func': for_arcsin_f, 'a': 0, 'b': 1}
    return math_func


def analysis_indefinite_integral(f):
    '''不定积分的计算'''
    # 寻找原函数
    steps = integral_steps(f, x)
    analysis_steps(steps)

# def abnormal_convergence(f):
#     '''反常积分是否收敛？'''


# def analysis_definite_integrate():
#     '''定积分的计算'''

def testss():
    math_func = in_class()
    # 反常积分载入
    f_info = math_func['for_arcsin_f']
    f = f_info['func']
    a = f_info['a']
    b = f_info['b']
    # 反常积分结果
    f_str = '$' + latex(Integral(f, (x, a, b))) + '$'
    result = '$' + latex(integrate(f, (x, a, b))) + '$'
    print('反常积分: ' + f_str + '=' + result)
    plot_line(f, a, b)


def test():
    # 先搞成定积分的计算，引入u
    define_integrate = integrate(f, (x, a, u))  # 定积分计算
    define_f_str = '$' + latex(Integral(f, (x, a, u))) + '$'
    print('首先求定积分：' + define_f_str)

    # 定积分结果
    result_out = '$' + latex(define_integrate) + '$'
    print('相应定积分计算：' + define_f_str + '=' + result_out)

    # 如果是多个函数
    if define_integrate.args.__len__() > 1:
        f1 = define_integrate.args[0]
        count_limit(f1, u, oo)
        f2 = define_integrate.args[1]
        count_limit(f2, u, oo)

limit(x**2.5/sqrt(x**5+1),x,oo)