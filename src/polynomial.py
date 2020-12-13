# ===================================
# @Time : 2020/11/30 22:06
# 多项式的处理
# https://bbs.pinggu.org/thread-5989030-1-1.html
# ===================================

from scipy import poly1d


class basement():
    def simple_example(self):
        # p1=x^3+2x^2+3x+4
        p1 = poly1d([1, 2, 3, 4])
        print(p1)

        # p2=(x-1)(x-2)(x-3)(x-4)
        p2 = poly1d([1, 2, 3, 4], True)
        # 多项式求值
        p2(0)
        # 方程的根
        p1.r
        # 最高阶
        p1.order
        # 一阶求导
        p1.deriv()
        # 二阶求导
        p1.deriv(2)


class QandR():
    # 获得商和余数
    def __init__(self):
        self.func_1()

    def count_q_r(self, f, g):
        q, r = f / g
        print('q(x)=', q)
        print('r(x)=', r)

    def book_example(self):
        '''
        课本P8
        '''
        # f1 = 3x^3+4x^2-5x+6
        f1 = poly1d([3, 4, -5, 6])

        # f2 = x^2-3x+1
        f2 = poly1d([1, -3, 1])
        self.count_q_r(f1, f2)

    def func_1(self):
        '''书本P44习题1.1
        答案为
        q(x) = 0.3333 x - 0.7778
        r(x) = -2.889 x - 0.2222
        '''
        f1 = poly1d([1, -3, -1, -1])  # f1 = x^3 -3x^2 -x -1
        g1 = poly1d([3, -2, 1])  # g1 = 3x^2 -2x +1
        self.count_q_r(f1, g1)

    def func_2(self):
        '''书本P44习题1.2
        答案为
        q(x)= x^2 + x - 1
        r(x)= -5 x + 7
        '''
        f2 = poly1d([1, 0, 0, -2, 5])  # f = x^4-2x+5
        g2 = poly1d([1, -1, 2])  # g=x^2-x+2
        self.count_q_r(f2, g2)


