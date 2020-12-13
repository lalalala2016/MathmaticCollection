# ===================================
# @Time : 2020/11/30 22:55
# 求积分
# https://zhuanlan.zhihu.com/p/102413094
# ===================================

import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0,6,1000)
y = np.cos(2*np.pi*x)*np.exp(-x)+1.2

plt.axis([np.min(x),np.max(x),0,np.max(y)])           #坐标范围
plt.plot(x,y,label="$cos(2πx)e^{-x}+1.2$")            #画曲线，带图示
plt.fill_between(x,y1=y,y2=0,where=(x>=0.7)&(x<=4),   #填充积分区域
                 facecolor='blue',alpha=0.2)
plt.text(0.5*(0.7+4),0.4,r"$\int_{0.7}^4(cos(2πx)e^{-x}+1.2)\mathrm{d}x$",
         horizontalalignment='center',fontsize=14)    #增加说明文本
plt.legend()                                          #显示图示
plt.show()


def sum_bar_area():
    '''划分小矩形求和
    '''
    import numpy as np

    x = np.linspace(0.7, 4.0, 1000)
    y = np.cos(2 * np.pi * x) * np.exp(-x) + 1.2
    dx = x[1] - x[0]  # 每个矩形的宽度
    fArea = np.sum(y * dx)  # 矩形宽*高，再求和
    print("Integral area:", fArea)


def use_quad():
    import math
    from scipy import integrate

    def func(x):
        print("x=", x)  # 用于展示quad()函数对func的多次调用
        return math.cos(2 * math.pi * x) * math.exp(-x) + 1.2

    fArea, err = integrate.quad(func, 0.7, 4)
    print("Integral area:", fArea)

if __name__ == '__main__':
    print()