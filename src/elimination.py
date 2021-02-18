# ===================================
# @Time : 2021/2/6 18:14
# 消元法
# 参考资料：https://blog.csdn.net/qq_21149391/article/details/84556283
# ===================================
import numpy as np


def change_row_index(i, aug_matrix):
    '''当前运行第i行方程'''
    # 下三角值
    index_value = [np.abs(m[0]) for m in aug_matrix[i:, i].tolist()]
    if 1 in index_value:
        # 如果有1，优先交换1
        change_index = i + index_value.index(1)
    elif index_value[1]>0:
        # 如果下一行值不为0，则与下一行交换
        change_index = i+1
    else:
        change_index = i
    return change_index


def SequentialGauss(aug_matrix):
    '''
    构造类梯形的矩阵：对角上有值，下三角全为0
    '''
    print('========= 转换为类梯形矩阵 ==============')
    number = aug_matrix.shape[0]  # 方程数
    for i in range(0, number - 1):
        if aug_matrix[i, i] == 0:
            # 如果对角线上值为0则与下一行交换
            # 选择交换的行
            change = change_row_index(i, aug_matrix)
            aug_matrix[[i, change], :] = aug_matrix[[change, i], :]
            print('交换第{}行与第{}行'.format(i + 1, change + 1))
            print(aug_matrix)
        for j in range(i + 1, number):
            # 下三角索引
            mul_value = - aug_matrix[j, i] / aug_matrix[i, i]  # 乘数
            print('{}({})'.format(mul_value, j + 1))
            new_line = aug_matrix[j:j + 1, :] + mul_value * aug_matrix[i, :]
            deal_inf = [v if np.abs(v) > 0.00000001 else 0 for v in new_line.tolist()[0]]
            aug_matrix[j, :] = deal_inf
        print(aug_matrix)
    return aug_matrix


def reback_matrix(new_mat):
    '''往上消元，
    主角仍旧是(i,i)上的值
    消到全是线性无关向量为止
    '''
    print('========= 往上走，做线性无关向量组合 ==============')
    number = new_mat.shape[0]  # 方程数
    for i in range(number - 1, 0, -1):
        # 4,3,2,1
        main_v = new_mat[i, i]
        if main_v == 0:
            # 如果最后一行全是0，则继续
            continue
        for j in range(0, i):
            # 上面的所有行,第j列都变成0
            mul_value = - new_mat[j, i] / new_mat[i, i]  # 乘数
            print('{}({})'.format(mul_value, j + 1))
            new_line = new_mat[j, :] + mul_value * new_mat[i, :]
            deal_inf = [v if np.abs(v) > 0.00000001 else 0 for v in new_line.tolist()[0]]
            # 如果其他值都为0，只有对角线不为0，则该值变成1即可
            zero_num = len([z for z in deal_inf if z != 0])
            if zero_num == 1:
                max_v = max(deal_inf)
                if max_v != 0:
                    deal_inf = [n / max_v for n in deal_inf]
            new_mat[j, :] = deal_inf
        print(new_mat)
    return new_mat


def revert(new_mat):
    '''回带过程，求解参数
    '''
    # 存放答案
    x = np.mat(np.zeros(new_mat.shape[0], dtype=float))  # matrix([[0., 0., 0., 0.]])
    number = x.shape[1] - 1  # 变量的索引，从0开始故减1  # new_mat最后一列是b故减1
    b = new_mat.shape[1] - 1  # 等号后值的索引，从0开始故减1

    if new_mat[number, number] != 0:
        x[0, number] = new_mat[number, b] / new_mat[number, number]
        # 其他变量求解
        for i in range(number - 1, -1, -1):
            try:
                # 等号左侧已知参数的和
                sum_1 = np.sum(np.multiply(new_mat[i, i + 1:b], x[0, i + 1:b]))
                # b-sum1/系数
                x[0, i] = (new_mat[i, b] - sum_1) / (new_mat[i, i])
            except:
                print("错误")
        print(x)
    elif new_mat[number, b] > 0:
        # 如果系数都为0，但是d不为0
        print('方程无解')
    else:
        print('有无穷多解')


def stand_matrix(new_mat):
    # 对角上都为1，方便对答案
    print('========= 标准化 ==============')
    number = new_mat.shape[0]  # 方程数
    for i in range(number):
        main_v = new_mat[i, i]
        if main_v == 0:
            # 如果最后一行全是0，则继续
            continue
        deal_inf = [n / main_v if n != 0 else 0 for n in new_mat[i, :].tolist()[0]]
        new_mat[i, :] = deal_inf
    return new_mat


def main_run(aug_matrix):
    new_mat = SequentialGauss(aug_matrix)
    new_mat = reback_matrix(new_mat)
    stand_mat = stand_matrix(new_mat)
    print('================ 重点回顾 ======================')
    print("增广矩阵")
    print(stand_mat)
    print("线性无关的矩阵")
    print(new_mat)
    print("方程的解")
    revert(new_mat)


def matrix_collection(choose=1):
    if choose == 1:
        mat_a = np.mat([[2, 3, 11, 5],
                        [1, 1, 5, 2],
                        [2, 1, 3, 2],
                        [1, 1, 3, 4]], dtype=float)
        mat_b = np.mat([2, 1, -3, -3])
        aug_matrix = np.hstack((mat_a, mat_b.T))
    elif choose == 2:
        mat_a = np.mat([[1, 3, 5, -4, 0],
                        [1, 3, 2, -2, 1],
                        [1, -2, 1, -1, -1],
                        [1, -4, 1, 1, -1],
                        [1, 2, 1, -1, 1]], dtype=float)
        mat_b = np.mat([1, -1, 3, 3, -1])
        aug_matrix = np.hstack((mat_a, mat_b.T))
    elif choose == 3:
        mat_a = np.mat([[1, 2, 0, -3, 2],
                        [1, -1, -3, 1, -3],
                        [2, -3, 4, -5, 2],
                        [9, -9, 6, 16, 2]], dtype=float)
        mat_b = np.mat([1, 2, 7, 25])
        aug_matrix = np.hstack((mat_a, mat_b.T))
    elif choose == 4:
        # 题目3,与答案一样
        mat_a = np.mat([[1, -2, 3, -4],
                        [0, 1, -1, 1],
                        [1, 3, 0, 1],
                        [0, -7, 3, 1]], dtype=float)
        mat_b = np.mat([4, -3, 1, -3])
        aug_matrix = np.hstack((mat_a, mat_b.T))
    elif choose == 5:
        # 题目4
        mat_a = np.mat([[3, 4, -5],
                        [2, -3, 3],
                        [4, 11, -13],
                        [7, -2, 1]], dtype=float)
        mat_b = np.mat([7, -2, 16, 3])
        aug_matrix = np.hstack((mat_a, mat_b.T))
    elif choose == 6:
        # 第4题答案
        aug_matrix = np.mat([[1, 7, -8, 9],
                             [0, -17, 19, -20],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0]], dtype=float)
    elif choose == 7:
        # 题目5
        mat_a = np.mat([[2, 1, -1, 1],
                        [3, -2, 2, -3],
                        [5, 1, -1, 2],
                        [2, -1, 1, -3]], dtype=float)
        mat_b = np.mat([1, 2, -1, 4])
        aug_matrix = np.hstack((mat_a, mat_b.T))  # 增广矩阵
    elif choose == 8:
        # 第5题的答案
        aug_matrix = np.mat([[2, 1, -1, 1, 1],
                             [7, 0, 0, -1, 4],
                             [10, 0, 0, 0, 2],
                             [0, 0, 0, 0, -1]], dtype=float)
    elif choose == 9:
        # 第6题
        aug_matrix = np.mat([[1, 2, 3, -1, 1],
                             [3, 2, 1, -1, 1],
                             [2, 3, 1, 1, 1],
                             [2, 2, 2, -1, 1],
                             [5, 5, 2, 0, 2]], dtype=float)
    else:
        # 第6题答案
        aug_matrix = np.mat([[0, 0, 0, 0, 0],
                             [0, 5, 7, 0, 2],
                             [0, 0, -1.2, 1, -0.2],
                             [-1, 0, 1, 0, 0],
                             [0, 0, 0, 0, 0]], dtype=float)
    return aug_matrix


def second_part(choose=0):
    if choose==1:
        # 课本第二题（1）
        # 计算正确的
        aug_matrix = np.mat([[1, 1, 1, 1, 1],
                             [1, 1, -1, -1, 2],
                             [1, -1, 1, -1, 1],
                             [1, -1, -1, 1, 1]], dtype=float)
    else:
        # 课本第二题（2）
        aug_matrix = np.mat([[1, 2, 1, 0, 0],
                             [1, 1, 1, 1, 0],
                             [0, 3, 0, -1, 0],
                             [1, 1, 0, -1, 1]], dtype=float)
    return aug_matrix


if __name__ == "__main__":
    aug_matrix = second_part()
    main_run(aug_matrix)
