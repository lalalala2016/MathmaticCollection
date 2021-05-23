create_time: 2021年5月20日

[toc]

## 一、课本例题

### 1、$\lambda$矩阵化为标准型

$\left[\begin{matrix}\lambda^3-\lambda&2\lambda^2\\\lambda^2+5\lambda&3\lambda\end{matrix}\right]$

> 互换两行，互换两列：$=\left[\begin{matrix}3 \lambda & \lambda^{2} + 5 \lambda\\2 \lambda^{2} & \lambda^{3} - \lambda\end{matrix}\right]$
> 第二行+-$\frac{2 \lambda}{3}$第一行：$=\left[\begin{matrix}3 \lambda & \lambda^{2} + 5 \lambda\\0 & \lambda^{3} - \frac{2 \lambda \left(\lambda^{2} + 5 \lambda\right)}{3} - \lambda\end{matrix}\right]$
> 第二列+-$\frac{5}{3}$第一列：$=\left[\begin{matrix}3 \lambda & \lambda^{2}\\0 & \lambda^{3} - \frac{2 \lambda \left(\lambda^{2} + 5 \lambda\right)}{3} - \lambda\end{matrix}\right]$
> 第二列+$-\frac{1}{3} \lambda$第一列：$=\left[\begin{matrix}3 \lambda & 0\\0 & \lambda^{3} - \frac{2 \lambda \left(\lambda^{2} + 5 \lambda\right)}{3} - \lambda\end{matrix}\right]$
> 对角线值系数为1：$\left[\begin{matrix}1.0 \lambda & 0\\0 & \lambda \left(\lambda^{2} - 10 \lambda - 3\right)\end{matrix}\right]$



### 2、$\lambda$矩阵化为标准型

计算$\left[\begin{matrix}1 - \lambda & \lambda^{2} & \lambda\\\lambda & \lambda & - \lambda\\\lambda^{2} + 1 & \lambda^{2} & - \lambda^{2}\end{matrix}\right]$的标准型

> 第一列+$1$第三列：$=\left[\begin{matrix}1 & \lambda^{2} & \lambda\\0 & \lambda & - \lambda\\1 & \lambda^{2} & - \lambda^{2}\end{matrix}\right]$
>
> 第三行+$-1$第一行：$=\left[\begin{matrix}1 & \lambda^{2} & \lambda\\0 & \lambda & - \lambda\\0 & 0 & - \lambda^{2} - \lambda\end{matrix}\right]$
>
> 第一行+$- \lambda$第二行：$=\left[\begin{matrix}1 & 0 & \lambda^{2} + \lambda\\0 & \lambda & - \lambda\\0 & 0 & - \lambda^{2} - \lambda\end{matrix}\right]$
>
> 第一行+$1$第三行：$=\left[\begin{matrix}1 & 0 & 0\\0 & \lambda & - \lambda\\0 & 0 & - \lambda^{2} - \lambda\end{matrix}\right]$
>
> 第三列+$1$第二列：$=\left[\begin{matrix}1 & 0 & 0\\0 & \lambda & 0\\0 & 0 & - \lambda^{2} - \lambda\end{matrix}\right]$
>
> 系数为1：$=\left[\begin{matrix}1 & 0 & 0\\0 & \lambda & 0\\0 & 0 & \lambda^{2} + \lambda\end{matrix}\right]$



### 3、$\lambda$矩阵化为标准型

计算$\left[\begin{matrix}\lambda^{2} + \lambda & 0 & 0\\0 & \lambda & 0\\0 & 0 & \left(\lambda + 1\right)^{2}\end{matrix}\right]$的标准型

> 1级子式: $\lambda^{2} + \lambda,\lambda,\left(\lambda + 1\right)^{2}$，首项系数为1的最大公因式$D_1(\lambda)=1$
>
> 2级子式: $\lambda^{2} \left(\lambda + 1\right),\lambda \left(\lambda + 1\right)^{3},\lambda \left(\lambda + 1\right)^{2}$，首项系数为1的最大公因式$D_2(\lambda)=\lambda*(\lambda + 1)$
>
> 3级子式: $\lambda^{2} \left(\lambda + 1\right)^{3}$，首项系数为1的最大公因式$D_3(\lambda)=\lambda^{2} \left(\lambda + 1\right)^{3}$
>
> 矩阵的行列式因子为：$D_1=1,D_2=\lambda(\lambda + 1),D_3=\lambda^{2} \left(\lambda + 1\right)^{3}$
>
> 则对应的不变因子为：$d_1=1,d_2=\lambda \left(\lambda + 1\right),d_3=\lambda \left(\lambda + 1\right)^{2}$
>
> 矩阵的标准型为：$\left[\begin{matrix}1 & 0 & 0\\0 & \lambda \left(\lambda + 1\right) & 0\\0 & 0 & \lambda \left(\lambda + 1\right)^{2}\end{matrix}\right]$



### 4、$\lambda$矩阵化为标准型

计算$\left[\begin{matrix}0 & 0 & 0 & \lambda^{2}\\0 & 0 & \lambda^{2} - \lambda & 0\\0 & \left(\lambda - 1\right)^{2} & 0 & 0\\\lambda^{2} - \lambda & 0 & 0 & 0\end{matrix}\right]$的标准型

> 1级子式: $\lambda^{2},\lambda \left(\lambda - 1\right),\left(\lambda - 1\right)^{2},\lambda \left(\lambda - 1\right)$，首项系数为1的最大公因式$D_1(\lambda)=1$
>
> 2级子式: $\lambda^{3} \left(\lambda - 1\right),\lambda^{2} \left(\lambda - 1\right)^{2},\lambda^{3} \left(\lambda - 1\right),\lambda \left(\lambda - 1\right)^{3},\lambda^{2} \left(\lambda - 1\right)^{2},\lambda \left(\lambda - 1\right)^{3}$
>
> 首项系数为1的最大公因式$D_2(\lambda)=\lambda \left(\lambda - 1\right)$
>
> 3级子式: $\lambda^{3} \left(\lambda - 1\right)^{3},\lambda^{4} \left(\lambda - 1\right)^{2},\lambda^{3} \left(\lambda - 1\right)^{3},\lambda^{2} \left(\lambda - 1\right)^{4}$
>
> 首项系数为1的最大公因式$D_3(\lambda)=\lambda^{2} \left(1 - \lambda\right)^{2}$
>
> 四阶子式为|A|，最大公因式为本身，$D_4(\lambda)=\lambda^{4} \left(\lambda - 1\right)^{4}$

矩阵的行列式因子为：$D_1=1,D_2=\lambda \left(\lambda - 1\right),D_3=\lambda^{2} \left(1 - \lambda\right)^{2}，D_4=\lambda^{4} \left(\lambda - 1\right)^{4}$
则对应的不变因子为：$d_1=1,d_2=\lambda \left(\lambda - 1\right),d_3=\frac{\lambda \left(1 - \lambda\right)^{2}}{\lambda - 1},d_4=\frac{\lambda^{2} \left(\lambda - 1\right)^{4}}{\left(1 - \lambda\right)^{2}}$

矩阵的标准型为：$\left[\begin{matrix}1 & 0 & 0 & 0\\0 & \lambda \left(\lambda - 1\right) & 0 & 0\\0 & 0 & \frac{\lambda \left(1 - \lambda\right)^{2}}{\lambda - 1} & 0\\0 & 0 & 0 & \frac{\lambda^{2} \left(\lambda - 1\right)^{4}}{\left(1 - \lambda\right)^{2}}\end{matrix}\right]$



### 5、$\lambda$矩阵化为标准型

计算$\left[\begin{matrix}3 \lambda^{2} + 2 \lambda - 3 & 2 \lambda - 1 & \lambda^{2} + 2 \lambda - 3\\4 \lambda^{2} + 3 \lambda - 5 & 3 \lambda - 2 & \lambda^{2} + 3 \lambda - 4\\\lambda^{2} + \lambda - 4 & \lambda - 2 & \lambda - 1\end{matrix}\right]$的标准型

> 第三列+$-1*$第二列：$=\left[\begin{matrix}3 \lambda^{2} + 2 \lambda - 3 & 2 \lambda - 1 & \lambda^{2} - 2\\4 \lambda^{2} + 3 \lambda - 5 & 3 \lambda - 2 & \lambda^{2} - 2\\\lambda^{2} + \lambda - 4 & \lambda - 2 & 1\end{matrix}\right]$
>
> 第一列+$-1$第二列：$=\left[\begin{matrix}3 \lambda^{2} - 2 & 2 \lambda - 1 & \lambda^{2} - 2\\4 \lambda^{2} - 3 & 3 \lambda - 2 & \lambda^{2} - 2\\\lambda^{2} - 2 & \lambda - 2 & 1\end{matrix}\right]$
>
> 第二行+$-1$第一行：$=\left[\begin{matrix}3 \lambda^{2} - 2 & 2 \lambda - 1 & \lambda^{2} - 2\\\lambda^{2} - 1 & \lambda - 1 & 0\\\lambda^{2} - 2 & \lambda - 2 & 1\end{matrix}\right]$
>
> 第三行+$-1$第二行：$=\left[\begin{matrix}3 \lambda^{2} - 2 & 2 \lambda - 1 & \lambda^{2} - 2\\\lambda^{2} - 1 & \lambda - 1 & 0\\-1 & -1 & 1\end{matrix}\right]$
>
> 第二列+$1$第三列：$=\left[\begin{matrix}3 \lambda^{2} - 2 & \lambda^{2} + 2 \lambda - 3 & \lambda^{2} - 2\\\lambda^{2} - 1 & \lambda - 1 & 0\\-1 & 0 & 1\end{matrix}\right]$
>
> 第一列+$1$第三列：$=\left[\begin{matrix}4 \lambda^{2} - 4 & \lambda^{2} + 2 \lambda - 3 & \lambda^{2} - 2\\\lambda^{2} - 1 & \lambda - 1 & 0\\0 & 0 & 1\end{matrix}\right]$
>
> 第一列+$-(\lambda + 1)$第二列：$=\left[\begin{matrix}- \lambda^{3} + \lambda^{2} + \lambda - 1 & \lambda^{2} + 2 \lambda - 3 & \lambda^{2} - 2\\0 & \lambda - 1 & 0\\0 & 0 & 1\end{matrix}\right]$
>
> 然后把第一行的2，3弄成0：$=\left[\begin{matrix}- \lambda^{3} + \lambda^{2} + \lambda - 1 & 0 & 0\\0 & \lambda - 1 & 0\\0 & 0 & 1\end{matrix}\right]$
>
> 转换成标准型: $=\left[\begin{matrix}1 & 0 & 0\\0 & \lambda - 1 & 0\\0 & 0 & - \lambda^{3} + \lambda^{2} + \lambda - 1\end{matrix}\right]$



### 6、$\lambda$矩阵化为标准型

计算$\left[\begin{matrix}2 \lambda & 3 & 0 & 1 & \lambda\\4 \lambda & 3 \lambda + 6 & 0 & \lambda + 2 & 2 \lambda\\0 & 6 \lambda & \lambda & 2 \lambda & 0\\\lambda - 1 & 0 & \lambda - 1 & 0 & 0\\3 \lambda - 3 & 1 - \lambda & 2 \lambda - 2 & 0 & 0\end{matrix}\right]$的标准型

> 第一列+$-2$第五列，第二列+$-3$第四列：$=\left[\begin{matrix}0 & 0 & 0 & 1 & \lambda\\0 & 0 & 0 & \lambda + 2 & 2 \lambda\\0 & 0 & \lambda & 2 \lambda & 0\\\lambda - 1 & 0 & \lambda - 1 & 0 & 0\\3 \lambda - 3 & 1 - \lambda & 2 \lambda - 2 & 0 & 0\end{matrix}\right]$
>
> 第一列+$3$第二列，第三列+$2$第二列：$=\left[\begin{matrix}0 & 0 & 0 & 1 & \lambda\\0 & 0 & 0 & \lambda + 2 & 2 \lambda\\0 & 0 & \lambda & 2 \lambda & 0\\\lambda - 1 & 0 & \lambda - 1 & 0 & 0\\0 & 1 - \lambda & 0 & 0 & 0\end{matrix}\right]$
>
> 第二行+-2第一行：$=\left[\begin{matrix}0 & 0 & 0 & 1 & \lambda\\0 & 0 & 0 & \lambda & 0\\0 & 0 & \lambda & 2 \lambda & 0\\\lambda - 1 & 0 & \lambda - 1 & 0 & 0\\0 & 1 - \lambda & 0 & 0 & 0\end{matrix}\right]$
>
> 第三列+-1第一列：$=\left[\begin{matrix}0 & 0 & 0 & 1 & \lambda\\0 & 0 & 0 & \lambda & 0\\0 & 0 & \lambda & 2 \lambda & 0\\\lambda - 1 & 0 & 0 & 0 & 0\\0 & 1 - \lambda & 0 & 0 & 0\end{matrix}\right]$
>
> `分水岭`
>
> 第二行+$3$第一行：$=\left[\begin{matrix}0 & 0 & 0 & 1 & \lambda\\0 & 0 & 0 & 0 & - \lambda^{2}\\0 & 0 & \lambda & 2 \lambda & 0\\\lambda - 1 & 0 & 0 & 0 & 0\\0 & 1 - \lambda & 0 & 0 & 0\end{matrix}\right]$
>
> 第四列+-2第三列：$=\left[\begin{matrix}0 & 0 & 0 & 1 & \lambda\\0 & 0 & 0 & 0 & - \lambda^{2}\\0 & 0 & \lambda & 0 & 0\\\lambda - 1 & 0 & 0 & 0 & 0\\0 & 1 - \lambda & 0 & 0 & 0\end{matrix}\right]$
>
> 第五列+- $\lambda$第四列：$=\left[\begin{matrix}0 & 0 & 0 & 1 & 0\\0 & 0 & 0 & 0 & - \lambda^{2}\\0 & 0 & \lambda & 0 & 0\\\lambda - 1 & 0 & 0 & 0 & 0\\0 & 1 - \lambda & 0 & 0 & 0\end{matrix}\right]$

第1列第4列互换，2、5列互换，转换为对角矩阵：$=\left[\begin{matrix}1 & 0 & 0 & 0 & 0\\0 & - \lambda^{2} & 0 & 0 & 0\\0 & 0 & \lambda & 0 & 0\\0 & 0 & 0 & \lambda - 1 & 0\\0 & 0 & 0 & 0 & 1 - \lambda\end{matrix}\right]$

1级子式: $1,- \lambda^{2},\lambda,\lambda - 1,1 - \lambda$，首项系数为1的最大公因式$D_1(\lambda)=1$

2级子式: $\lambda^{2} \left(\lambda - 1\right),1 - \lambda,- \left(\lambda - 1\right)^{2},- \lambda^{2},- \lambda^{3},\lambda - 1,\lambda,- \lambda^{2} \left(\lambda - 1\right),- \lambda \left(\lambda - 1\right),\lambda \left(\lambda - 1\right)$,首项系数为1的最大公因式$D_2(\lambda)=1$

3级子式: $\lambda^{2} \left(\lambda - 1\right)^{2},\lambda^{2} \left(\lambda - 1\right),- \lambda^{3} \left(\lambda - 1\right),- \left(\lambda - 1\right)^{2},- \lambda \left(\lambda - 1\right)^{2},\lambda^{3} \left(\lambda - 1\right),- \lambda^{3},- \lambda \left(\lambda - 1\right),- \lambda^{2} \left(\lambda - 1\right),\lambda \left(\lambda - 1\right)$,首项系数为1的最大公因式$D_3(\lambda)=1$

4级子式: $\lambda^{3} \left(\lambda - 1\right)^{2},- \lambda \left(\lambda - 1\right)^{2},- \lambda^{3} \left(\lambda - 1\right),\lambda^{2} \left(\lambda - 1\right)^{2},\lambda^{3} \left(\lambda - 1\right)$，首项系数为1的最大公因式$D_4(\lambda)=\lambda \left(1 - \lambda\right)$

五阶子式为|A|，最大公因式为本身，$D_5(\lambda)=\lambda^{3} \left(\lambda - 1\right)^{2}$

矩阵的行列式因子为：$1,1,1,\lambda \left(1 - \lambda\right),\lambda^{3} \left(\lambda - 1\right)^{2}$
则对应的不变因子为：$1,1,1,\lambda \left(1 - \lambda\right),\lambda^{2} \left(\lambda - 1\right)$

矩阵的标准型为：$\left[\begin{matrix}1 & 0 & 0 & 0 & 0\\0 & 1 & 0 & 0 & 0\\0 & 0 & 1 & 0 & 0\\0 & 0 & 0 & \lambda \left(1 - \lambda\right) & 0\\0 & 0 & 0 & 0 & - \lambda^{2} \left(\lambda - 1\right)\end{matrix}\right]$





### 7、求不变因子

计算$\left[\begin{matrix}\lambda - 2 & -1 & 0\\0 & \lambda - 2 & -1\\0 & 0 & \lambda - 2\end{matrix}\right]$的不变因子

1级子式:$-1,\lambda - 2$,首项系数为1的最大公因式$D_1=1$

> 2阶子式12：$\left[\begin{matrix}\lambda - 2 & -1\\0 & \lambda - 2\end{matrix}\right]=\left(\lambda - 2\right)^{2}$
> 2阶子式13：$\left[\begin{matrix}\lambda - 2 & 0\\0 & -1\end{matrix}\right]=2 - \lambda$
>
> ...

首项系数为1的最大公因式$D_2=1$

三阶子式为|A|，最大公因式为本身，$D_3 = \left(\lambda - 2\right)^{3}$

矩阵的行列式因子为：$1,1,\left(\lambda - 2\right)^{3}$
矩阵的不变因子为：$1,1,\left(\lambda - 2\right)^{3}$









