# ===================================
# @Time : 2021/2/25 21:32
# 曲线函数
# ===================================
import re
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, integrate
from sympy import sin, cos, sqrt,exp
from sympy import pi


def plot_line(X, Y, title):
    plt.title(title)  # markdown
    plt.plot(X, Y, c='g')
    plt.show()


def trans_func_to_markdown(f):
    'x*sqrt(4 - x**2)'
    # 找出函数
    f_str = str(f)
    new = '$' + str(f).replace('**', '^').replace('sqrt(', '\\sqrt{').replace(')', '}') + '$'
    return new


def test_1():
    # 课本P208 例一（5）
    a, b = 0, 2
    # 定义函数
    x = symbols('x')
    f = x * (sqrt(4 - x ** 2))
    X = np.linspace(a, b, 1000)
    Y = [f.evalf(subs={x: t}) for t in X]  # evalf传入参数
    title = trans_func_to_markdown(f)
    plot_line(X, Y, title)

    # 原函数
    F = integrate(f, x)
    print('原函数F', F)
    integ = integrate(f, (x, a, b))  # #参数传入：函数，积分变量和范围
    print('定积分', integ)


def test_2():
    # 课本 P219 例一
    x = symbols('x')
    # 分段函数1
    a1,b1 = -1,0
    f1 = 2*x-1

    # 分段函数2
    a2, b2 = 0,1
    f2 = exp(-x)

    # 画图
    X = np.linspace(a1, b2, 1000)
    Y = []
    for i in X:
        if i<0:
            Y.append(f1.evalf(subs={x: i}))
        else:
            Y.append(f2.evalf(subs={x: i}))

    title = trans_func_to_markdown(f1)
    plot_line(X, Y, title)


if __name__ == '__main__':
    test_2()
