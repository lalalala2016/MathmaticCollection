# ===================================
# @Time : 2021/4/11 11:32
# ===================================
from sympy import Matrix, factor, simplify, latex, solve, expand, eye, diag
from sympy.abc import x, y, z, lamda
import pprint
import numpy as np


def inverse_matrix():
    # 矩阵的逆计算
    aug_matrix = np.mat([[1, 1, 1, 1],
                         [1, 1, -1, -1],
                         [1, -1, 1, -1],
                         [1, -1, -1, 1]], dtype=float)
    inv_matrix = np.linalg.inv(aug_matrix)
    import fractions

    np.set_printoptions(formatter={'all': lambda x: str(fractions.Fraction(x).limit_denominator())})
    print(inv_matrix)

    B = np.mat([[1, 2, 1, 0],
                [1, 1, 1, 1],
                [0, 3, 0, -1],
                [1, 1, 0, -1]], dtype=float)
    C = np.dot(inv_matrix, B)
    C_inv = np.linalg.inv(C)
    print(C_inv)


def elementary_row_c(A):
    # 基本初等变换，某一行*c
    A = Matrix([[3, 2], [5, 6]])
    # ================乘上c =====================
    # 第二行*-1
    P1 = Matrix([[1, 0], [0, -1]])
    pprint.pprint(P1 * A)

    # 第二行*-5
    P2 = Matrix([[1, 0], [0, -5]])
    pprint.pprint(P2 * A)

    #  第一行*-1
    P3 = Matrix([[-1, 0], [0, 1]])
    pprint.pprint(P3 * A)

    # 第一行*-5
    P4 = Matrix([[-5, 0], [0, 1]])
    pprint.pprint(P4 * A)

    # 两行全乘上-k倍
    P5 = Matrix([[-1, 0], [0, -1]])
    pprint.pprint(P5 * A)
    # 换个乘法的顺序就是列的操作


def elementary_change_rows(A):
    # 只是交换
    Q1 = Matrix([[0, 1], [1, 0]])
    # 交换两行
    pprint.pprint(Q1 * A)
    # 交换两列
    pprint.pprint(A * Q1)

    # 乘上-1然后交换顺序
    Q2 = Matrix([[0, -1], [-1, 0]])
    pprint.pprint(Q2 * A)

    # 乘上k值然后交换顺序
    Q3 = Matrix([[0, 4], [2, 0]])
    pprint.pprint(Q3 * A)


def elementary_two_row(A):
    # 一行的k倍加到另一行
    # 第一行+第二行
    M1 = Matrix([[1, 1], [0, 1]])
    pprint.pprint(M1 * A)
    # 第二列+第一列
    pprint.pprint(A * M1)

    # 第一行+2*第二行
    M2 = Matrix([[1, 2], [0, 1]])
    pprint.pprint(M2 * A)
    # 第二列+2*第一列
    pprint.pprint(A * M2)

    # 第二行+第一行
    M3 = Matrix([[1, 0], [1, 1]])
    pprint.pprint(M3 * A)

    # 第二行+k第一行
    M4 = Matrix([[1, 0], [2, 1]])
    pprint.pprint(M4 * A)


class StandMatrix:
    def test1(self):
        '''初等变换角度求解标准型'''
        change_m = Matrix([[0, 1], [1, 0]])  # 交换位置的初等矩阵，左乘交换两行，右乘交换两列
        A = Matrix([[(lamda ** 3 - lamda), 2 * lamda ** 2], [lamda ** 2 + 5 * lamda, 3 * lamda]])
        A = change_m * A * change_m
        # pprint.pprint(A)
        print('互换两行，互换两列：$={}$'.format(latex(A)))

        k = 2 * lamda / 3
        add_m = Matrix([[1, 0], [-k, 1]])
        A = add_m * A
        print('第二行+$-{}$第一行：$={}$'.format(latex(k), latex(A)))

        k = 5 / 3
        add_m = Matrix([[1, -k], [0, 1]])
        A = A * add_m
        print('第二列+$-{}$第一列：$={}$'.format(latex(k), latex(A)))

        k = 1 / 3 * lamda
        add_m = Matrix([[1, -k], [0, 1]])
        A = A * add_m
        print('第二列+$-{}$第一列：$={}$'.format(latex(k), latex(A)))

        # 系数为1
        k_matrx1 = Matrix([[1 / 3, 0], [0, 1]])
        A = k_matrx1 * A
        k_matrx2 = Matrix([[1, 0], [0, 3]])
        A = k_matrx2 * A
        A = simplify(A)
        print('对角线值系数为1：${}$'.format(latex(A)))

    def test2(self):
        '''初等变换角度求解标准型'''
        A = Matrix([[1 - lamda, lamda ** 2, lamda], [lamda, lamda, -lamda], [1 + lamda ** 2, lamda ** 2, -lamda ** 2]])
        print('计算${}$的标准型'.format(latex(A)))
        k = 1
        add_m = Matrix([[1, 0, 0], [0, 1, 0], [k, 0, 1]])
        A = A * add_m
        print('第一列+${}$第三列：$={}$'.format(latex(k), latex(A)))

        k = -1
        add_m = Matrix([[1, 0, 0], [0, 1, 0], [k, 0, 1]])
        A = add_m * A
        print('第三行+${}$第一行：$={}$'.format(latex(k), latex(A)))

        k = -lamda
        add_m = Matrix([[1, k, 0], [0, 1, 0], [0, 0, 1]])
        A = add_m * A
        print('第一行+${}$第二行：$={}$'.format(latex(k), latex(A)))

        k = 1
        add_m = Matrix([[1, 0, 1], [0, 1, 0], [0, 0, 1]])
        A = add_m * A
        print('第一行+${}$第三行：$={}$'.format(latex(k), latex(A)))

        k = 1
        add_m = Matrix([[1, 0, 0], [0, 1, k], [0, 0, 1]])
        A = A * add_m
        print('第三列+${}$第二列：$={}$'.format(latex(k), latex(A)))

        k_matrx = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -1]])
        A = k_matrx * A
        print('系数为1：$={}$'.format(latex(A)))

    def test3(self):
        '''不变因子角度求解标准型'''
        A = Matrix([[lamda ** 2 + lamda, 0, 0], [0, lamda, 0], [0, 0, (lamda + 1) ** 2]])
        print('计算${}$的标准型'.format(latex(A)))

        # 一阶行列式因子
        f1 = lamda ** 2 + lamda
        f2 = lamda
        f3 = (lamda + 1) ** 2
        print('1级子式: ${},{},{}$'.format(latex(f1), latex(f2), latex(f3)))
        D_1 = 1
        print('首项系数为1的最大公因式$D_1(\lambda)={}$'.format(latex(D_1)))

        # 二阶行列式因子
        g1 = factor(Matrix([[f1, 0], [0, f2]]).det())
        g2 = factor(Matrix([[f1, 0], [0, f3]]).det())
        g3 = factor(Matrix([[f2, 0], [0, f3]]).det())
        print('2级子式: ${},{},{}$'.format(latex(g1), latex(g2), latex(g3)))
        D_2 = lamda * (lamda + 1)
        print('首项系数为1的最大公因式$D_2(\lambda)={}$'.format(latex(D_2)))

        # 三阶行列式因子
        h = factor(A.det())
        print('3级子式: ${}$'.format(latex(h)))
        D_3 = h
        print('首项系数为1的最大公因式$D_3(\lambda)={}$'.format(latex(D_3)))

        # 行列式因子
        print('矩阵的行列式因子为：$D_1={},D_2={},D_3={}$'.format(latex(D_1), latex(D_2), latex(D_3)))

        # 不变因子
        d_1 = D_1
        d_2 = D_2 / D_1
        d_3 = D_3 / D_2
        print('则对应的不变因子为：$d_1={},d_2={},d_3={}$'.format(latex(d_1), latex(d_2), latex(d_3)))

        stand_A = Matrix([[d_1, 0, 0], [0, d_2, 0], [0, 0, d_3]])
        print('矩阵的标准型为：${}$'.format(latex(stand_A)))

    def test4(self):
        f1 = lamda ** 2
        f2 = factor(lamda ** 2 - lamda)
        f3 = (lamda - 1) ** 2
        f4 = factor(lamda ** 2 - lamda)
        A = Matrix([[0, 0, 0, f1], [0, 0, f2, 0], [0, f3, 0, 0], [f4, 0, 0, 0]])
        print('计算${}$的标准型'.format(latex(A)))

        # 一阶子式
        print('1级子式: ${},{},{},{}$'.format(latex(f1), latex(f2), latex(f3), latex(f4)))
        D_1 = 1
        print('首项系数为1的最大公因式$D_1(\lambda)={}$'.format(latex(D_1)))

        # 二阶子式
        g1 = factor(Matrix([[f1, 0], [0, f2]]).det())
        g2 = factor(Matrix([[f1, 0], [0, f3]]).det())
        g3 = factor(Matrix([[f1, 0], [0, f4]]).det())
        g4 = factor(Matrix([[f2, 0], [0, f3]]).det())
        g5 = factor(Matrix([[f2, 0], [0, f4]]).det())
        g6 = factor(Matrix([[f3, 0], [0, f4]]).det())
        print('2级子式: ${},{},{},{},{},{}$'.format(latex(g1), latex(g2), latex(g3), latex(g4), latex(g5), latex(g6)))
        D_2 = lamda * (lamda - 1)
        print('首项系数为1的最大公因式$D_2(\lambda)={}$'.format(latex(D_2)))

        # 三阶子式
        h1 = factor(Matrix([[f1, 0, 0], [0, f2, 0], [0, 0, f3]]).det())
        h2 = factor(Matrix([[f1, 0, 0], [0, f2, 0], [0, 0, f4]]).det())
        h3 = factor(Matrix([[f1, 0, 0], [0, f3, 0], [0, 0, f4]]).det())
        h4 = factor(Matrix([[f2, 0, 0], [0, f3, 0], [0, 0, f4]]).det())
        print('3级子式: ${},{},{},{}$'.format(latex(h1), latex(h2), latex(h3), latex(h4)))
        D_3 = lamda ** 2 * (1 - lamda) ** 2
        print('首项系数为1的最大公因式$D_3(\lambda)={}$'.format(latex(D_3)))

        # 四阶子式
        D_4 = factor(A.det())
        print('四阶子式为|A|，最大公因式为本身，$D_4(\lambda)={}$'.format(latex(D_4)))

        # 行列式因子
        print('矩阵的行列式因子为：$D_1={},D_2={},D_3={}，D_4={}$'.format(latex(D_1), latex(D_2), latex(D_3), latex(D_4)))

        # 不变因子
        d_1 = D_1
        d_2 = D_2 / D_1
        d_3 = D_3 / D_2
        d_4 = D_4 / D_3
        print('则对应的不变因子为：$d_1={},d_2={},d_3={},d_4={}$'.format(latex(d_1), latex(d_2), latex(d_3), latex(d_4)))

        # 标准型
        stand_A = Matrix([[d_1, 0, 0, 0], [0, d_2, 0, 0], [0, 0, d_3, 0], [0, 0, 0, d_4]])
        print('矩阵的标准型为：${}$'.format(latex(stand_A)))

    def test5(self):
        row_1 = [3 * lamda ** 2 + 2 * lamda - 3, 2 * lamda - 1, lamda ** 2 + 2 * lamda - 3]
        row_2 = [4 * lamda ** 2 + 3 * lamda - 5, 3 * lamda - 2, lamda ** 2 + 3 * lamda - 4]
        row_3 = [lamda ** 2 + lamda - 4, lamda - 2, lamda - 1]
        A = Matrix([row_1, row_2, row_3])
        print('计算${}$的标准型'.format(latex(A)))

        # 把lamda-1变成1
        # 第三列-第二列
        k = -1
        add_m = Matrix([[1, 0, 0], [0, 1, k], [0, 0, 1]])
        A = A * add_m
        print('第三列+${}$第二列：$={}$'.format(latex(k), latex(A)))

        # 第一列-第二列
        k = -1
        add_m = Matrix([[1, 0, 0], [k, 1, 0], [0, 0, 1]])
        A = A * add_m
        print('第一列+${}$第二列：$={}$'.format(latex(k), latex(A)))

        k = -1
        add_m = Matrix([[1, 0, 0], [k, 1, 0], [0, 0, 1]])
        A = add_m * A
        print('第二行+${}$第一行：$={}$'.format(latex(k), latex(A)))

        k = -1
        add_m = Matrix([[1, 0, 0], [0, 1, 0], [0, k, 1]])
        A = add_m * A
        print('第三行+${}$第二行：$={}$'.format(latex(k), latex(A)))

        k = 1
        add_m = Matrix([[1, 0, 0], [0, 1, 0], [0, k, 1]])
        A = A * add_m
        print('第二列+${}$第三列：$={}$'.format(latex(k), latex(A)))

        k = 1
        add_m = Matrix([[1, 0, 0], [0, 1, 0], [k, 0, 1]])
        A = A * add_m
        print('第一列+${}$第三列：$={}$'.format(latex(k), latex(A)))

        k = -(lamda + 1)
        add_m = Matrix([[1, 0, 0], [k, 1, 0], [0, 0, 1]])
        A = simplify(A * add_m)
        print('第一列+${}$第二列：$={}$'.format(latex(k), latex(A)))

        k1 = -(lamda ** 2 - 2)
        k2 = -(lamda ** 2 + 2 * lamda - 3) / (lamda - 1)
        add_m = Matrix([[1, k2, k1], [0, 1, 0], [0, 0, 1]])
        A = add_m * A
        print('然后把第一行的2，3弄成0: $={}$'.format(latex(A)))

        # 转换成标准型
        change_m = Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
        A = change_m * A * change_m
        print('转换成标准型: $={}$'.format(latex(A)))

    def factor_expolre(self, factor_list):
        f_num = len(factor_list)
        print('1级子式: ${},{},{},{},{}$'.format(latex(factor_list[0]), latex(factor_list[1]),
                                              latex(factor_list[2]), latex(factor_list[3]),
                                              latex(factor_list[4])))
        D_1 = 1
        print('首项系数为1的最大公因式$D_1(\lambda)={}$'.format(latex(D_1)))

        second_factor = []
        for i in range(f_num):
            for j in range(i + 1, f_num):
                g1 = factor(Matrix([[factor_list[i], 0], [0, factor_list[j]]]).det())
                second_factor.append(g1)
        print('2级子式: ${}$'.format(','.join(list(set([latex(f) for f in second_factor])))))
        D_2 = 1
        print('首项系数为1的最大公因式$D_2(\lambda)={}$'.format(latex(D_2)))

        # 三阶子式
        third_factor = []
        for i in range(f_num):
            for j in range(i + 1, f_num):
                for k in range(j + 1, f_num):
                    g1 = factor(Matrix([[factor_list[i], 0, 0], [0, factor_list[j], 0], [0, 0, factor_list[k]]]).det())
                    third_factor.append(g1)
        print('3级子式: ${}$'.format(','.join(list(set([latex(f) for f in third_factor])))))
        D_3 = 1
        print('首项系数为1的最大公因式$D_3(\lambda)={}$'.format(latex(D_3)))

        # 四阶子式
        forth_factor = []
        for i in range(f_num):
            for j in range(i + 1, f_num):
                for k in range(j + 1, f_num):
                    for t in range(k + 1, f_num):
                        g1 = factor(Matrix([[factor_list[i], 0, 0, 0], [0, factor_list[j], 0, 0],
                                            [0, 0, factor_list[k], 0], [0, 0, 0, factor_list[t]]]).det())
                        forth_factor.append(g1)
        print('4级子式: ${}$'.format(','.join(list(set([latex(f) for f in forth_factor])))))
        D_4 = lamda * (1 - lamda)
        print('首项系数为1的最大公因式$D_4(\lambda)={}$'.format(latex(D_4)))

        D_5 = factor(diag(factor_list[0], factor_list[1], factor_list[2], factor_list[3], factor_list[4]).det())
        print('五阶子式为|A|，最大公因式为本身，$D_5(\lambda)={}$'.format(latex(D_5)))

        print('矩阵的行列式因子为：${},{},{},{},{}$'.format(latex(D_1), latex(D_2), latex(D_3), latex(D_4), latex(D_5)))
        d_1 = D_1
        d_2 = D_2 / D_1
        d_3 = D_3 / D_2
        d_4 = D_4 / D_3
        d_5 = factor(D_5 / D_4)
        print('则对应的不变因子为：${},{},{},{},{}$'.format(latex(d_1), latex(d_2), latex(d_3), latex(d_4), latex(d_5)))

        stand_A = diag(d_1, d_2, d_3, d_4, d_5)
        print('矩阵的标准型为：${}$'.format(latex(stand_A)))

    def test6(self):
        row_1 = [2 * lamda, 3, 0, 1, lamda]
        row_2 = [4 * lamda, 3 * lamda + 6, 0, lamda + 2, 2 * lamda]
        row_3 = [0, 6 * lamda, lamda, 2 * lamda, 0]
        row_4 = [lamda - 1, 0, lamda - 1, 0, 0]
        row_5 = [3 * lamda - 3, 1 - lamda, 2 * lamda - 2, 0, 0]
        A = Matrix([row_1, row_2, row_3, row_4, row_5])
        print('计算${}$的标准型'.format(latex(A)))

        k1 = -2
        k2 = -3
        # diag([1,1,1,1,1])
        add_m = Matrix([[1, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0],
                        [0, 0, 1, 0, 0],
                        [0, k2, 0, 1, 0],
                        [k1, 0, 0, 0, 1]])
        A = A * add_m
        print('第一列+${}$第五列，第二列+${}$第四列：$={}$'.format(latex(k1), latex(k2), latex(A)))

        k1 = 3
        k2 = 2
        add_m = Matrix([[1, 0, 0, 0, 0],
                        [k1, 1, k2, 0, 0],
                        [0, 0, 1, 0, 0],
                        [0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 1]])
        A = A * add_m
        print('第一列+${}$第二列，第三列+${}$第二列：$={}$'.format(latex(k1), latex(k2), latex(A)))

        k = -2
        add_m = Matrix([[1, 0, 0, 0, 0],
                        [k, 1, 0, 0, 0],
                        [0, 0, 1, 0, 0],
                        [0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 1]])
        A = add_m * A
        print('第二行+{}第一行：$={}$'.format(latex(k), latex(A)))

        k = -1
        add_m = Matrix([[1, 0, k, 0, 0],
                        [0, 1, 0, 0, 0],
                        [0, 0, 1, 0, 0],
                        [0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 1]])
        A = A * add_m
        print('第三列+{}第一列：$={}$'.format(latex(k), latex(A)))

        choose = 1
        if choose == 1:
            k = -lamda
            add_m = Matrix([[1, 0, 0, 0, 0],
                            [k, 1, 0, 0, 0],
                            [0, 0, 1, 0, 0],
                            [0, 0, 0, 1, 0],
                            [0, 0, 0, 0, 1]])
            A = add_m * A
            print('第二行+${}$第一行：$={}$'.format(latex(k1), latex(A)))

            k = -2
            add_m = Matrix([[1, 0, 0, 0, 0],
                            [0, 1, 0, 0, 0],
                            [0, 0, 1, k, 0],
                            [0, 0, 0, 1, 0],
                            [0, 0, 0, 0, 1]])
            A = A * add_m
            print('第四列+{}第三列：$={}$'.format(latex(k), latex(A)))

            k = -lamda
            add_m = Matrix([[1, 0, 0, 0, 0],
                            [0, 1, 0, 0, 0],
                            [0, 0, 1, 0, 0],
                            [0, 0, 0, 1, k],
                            [0, 0, 0, 0, 1]])
            A = A * add_m
            print('第五列+${}$第四列：$={}$'.format(latex(k), latex(A)))

            change_m = Matrix([[0, 0, 0, 1, 0],
                               [0, 0, 0, 0, 1],
                               [0, 0, 1, 0, 0],
                               [1, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0]])
            A = A * change_m
            print('第1列第4列互换，2、5列互换，转换为对角矩阵：$={}$'.format(latex(A)))

            f1 = 1
            f2 = -lamda ** 2
            f3 = lamda
            f4 = lamda - 1
            f5 = 1 - lamda
            self.factor_expolre([f1, f2, f3, f4, f5])


def test_1():
    '''不变因子'''
    v_1 = lamda - 2
    v_2 = -1
    A = Matrix([[v_1, v_2, 0], [0, v_1, v_2], [0, 0, v_1]])
    print('计算${}$的不变因子'.format(latex(A)))

    f1 = -1
    f2 = lamda - 2
    # 次数少，直接上
    D_1 = 1
    print('1级子式:${},{}$,首项系数为1的最大公因式$D_1={}$'.format(latex(f1), latex(f2), latex(D_1)))

    # 二级子式
    A1 = Matrix([[A[0, 0], A[0, 1]], [A[1, 0], A[1, 1]]])
    A1_det = factor(A1.det())
    print('2阶子式12：${}={}$'.format(latex(A1), latex(A1_det)))

    A2 = Matrix([[A[0, 0], A[0, 2]], [A[1, 0], A[1, 2]]])
    A2_det = factor(A2.det())
    print('2阶子式13：${}={}$'.format(latex(A2), latex(A2_det)))

    A3 = Matrix([[A[0, 1], A[0, 2]], [A[1, 1], A[1, 2]]])
    A3_det = factor(A3.det())
    print('2阶子式23：${}={}$'.format(latex(A3), latex(A3_det)))

    A4 = Matrix([[A[1, 0], A[1, 2]], [A[2, 0], A[2, 2]]])
    A4_det = factor(A4.det())
    print('2阶子式21：${}={}$'.format(latex(A4), latex(A4_det)))



    D_3 = factor(A.det())
    print('三阶子式为|A|，最大公因式为本身，$D_3 = {}$'.format(latex(D_3)))
    # print('2级子式:${},{}$,首项系数为1的最大公因式$D_1={}$'.format(latex(f1), latex(f2), latex(D_1)))
    # print('矩阵的行列式因子为：${},{},{}$'.format(latex(D_1), latex(D_2), latex(D_3)))

    # 不变因子
    # d_1 = D_1
    # d_2 = D_2 / D_1
    # d_3 = D_3 / D_2
    # print('矩阵的不变因子为：${},{},{}$'.format(latex(d_1), latex(d_2), latex(d_3)))


if __name__ == '__main__':
    test_1()
