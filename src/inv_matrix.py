# ===================================
# @Time : 2021/4/11 11:32
# ===================================
# 矩阵的逆计算
import numpy as np

if __name__ == "__main__":
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