# ===================================
# @Time : 2021/3/2 21:34
# 矩阵带来的变化
# ===================================
import numpy as np
import matplotlib.pyplot as plt
from sympy import Matrix,eye,factor
from sympy.abc import lamda


def plot_arrow(vector, new_vector, theta):
    '''原始向量经过矩阵转换后的绘图'''
    plt.arrow(0, 0, vector[0], vector[1], width=0.01, color='blue')
    plt.arrow(0, 0, new_vector[0], new_vector[1], width=0.01, color='red')
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.title('theta={}'.format(theta))
    plt.grid()  # 添加网格
    plt.show()


def rotate_arrow():
    vector = np.array([1, 0])
    theta = 30
    mat = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    new_vector = np.dot(vector, mat)
    plot_arrow(vector, new_vector, theta)


lamda_E = lamda*eye(3)
A = Matrix([[0,1,0],[0,0,1],[-6,-11,-6]])
factor((lamda_E-A).det())

