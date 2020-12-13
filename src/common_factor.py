# ===================================
# @Time : 2020/12/4 21:04
# 计算公因式——辗转相除法
# ===================================
from scipy import poly1d

class CommonFactor():
    def __init__(self):
        self.book_example()

    # 整数辗转相除法求解最大公因式
    def gcd(self, a, b):
        '''
        整数的辗转相除法，是个递归
        '''
        print('gcd({},{})'.format(a, b))
        if a % b == 0:
            return b
        return self.gcd(b, a % b)

    # 同理：多项式求解
    def poly_gcd(self, p1, p2):
        '''
        整除时的余弦是 poly1d([-1.86517468e-14]))
        '''
        print('========================')
        q, r = p1 / p2
        print('gcd(\n {},\n {})'.format(p1,p2))
        if r.r.__len__()==0:
            return p2
        return self.poly_gcd(p2,r)

    def gcd_example(self):
        '''
        gcd(213,22) = gcd(22,15) = gcd(15,7) = gcd(7,1) = 1
        :return:
        '''
        common_f = self.gcd(213, 22)
        print('common factor: ', common_f)

    def book_example(self):
        '''
        书籍P15多项式的辗转相除案例
        f = x^4 + 3x^3 - x^2 - 4x - 3
        g = 3x^3 + 10x^2 + 2x - 3
        :return:
        '''
        f = poly1d([1, 3, -1, -4, -3])
        g = poly1d([3, 10, 2, -3])
        common_func = self.poly_gcd(f, g)
        print('最大公因式为： ',common_func)

if __name__ == '__main__':
    CommonFactor()

