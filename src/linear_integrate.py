# ===================================
# @Time : 2020/11/30 22:55
# 曲线积分：第一型曲线积分，第二型曲线积分
# ===================================
from sympy.abc import x, y, z, u, v, s, t, theta
from sympy.integrals.manualintegrate import integral_steps
from sympy import sin, cos, atan, pi, sqrt, diff
from sympy.plotting import plot, plot3d, PlotGrid, plot_parametric, plot3d_parametric_surface, plot3d_parametric_line
from sympy import S
from sympy.abc import x, y, z, s, u, v
from sympy.abc import pi, theta
from sympy.functions import beta, gamma, exp, sqrt
from sympy import integrate, latex, Integral, symbols, expand, Eq, diff, simplify
from sympy.solvers.solveset import solveset, solveset_real
from sympy.plotting import plot, plot3d, PlotGrid, plot_parametric
from sympy import sin, cos, tan, cot, sec, csc, atan

a, b, L, k, r, R = symbols('a,b,L,k,r,R', constant=True)


class Symmetric:
    # 对称法：奇偶对称法、轮循对称法
    # 博客： https://blog.csdn.net/weixin_39622562/article/details/112151532#t2
    def L_symmetric_explore(self, L_func):
        '''判断曲线L的奇偶
        优先判断上下型（关于x轴对称）
        '''
        negtive_x_L_func = L_func.subs(x, -x)
        negtive_y_L_func = L_func.subs(y, -y)
        if negtive_y_L_func == L_func:
            # upper and down(priority)
            symmetric_type = 'x_axis_symmetric'
        elif negtive_x_L_func == L_func:
            # left and right
            symmetric_type = 'y_axis_symmetric'  # x_axis_symmetric
        else:
            symmetric_type = False
        return symmetric_type

    def PQ_symmetric_explore(self, symmetric_type, F_func, func_type='P'):
        '''
        https://wenku.baidu.com/view/490908650b1c59eef8c7b42e.html
        '''
        # 奇偶对称性(base pei deduce, html seems not true)
        analysis_result = ''
        cal_type = ''
        if symmetric_type == 'x_axis_symmetric':
            down_F_func = F_func.subs(y, -y)
            if func_type == 'P':
                # 偶0奇倍
                if down_F_func == F_func:
                    symmetric = True
                    analysis_result = 'P偶0奇倍,这里P(x,-y)=Q(x,y)为偶函数，$\int_L Pdx = 0$'
                    cal_type = '0'
                elif down_F_func == -F_func:
                    analysis_result = 'P偶0奇倍,这里P(x,-y)=-P(x,y)为奇函数，$\int_L Pdx = 2\int_{L,y>0}Pdx$'
                    symmetric = True
                    cal_type = '2multiple'
                else:
                    symmetric = False
            elif func_type == 'Q':
                # 偶倍奇0
                if down_F_func == F_func:
                    analysis_result = 'Q偶倍奇0,这里Q(x,-y)=Q(x,y)为偶函数，$\int_L Qdy = 2\int_{L,y>0}Qdy$'
                    cal_type = '2multiple'
                    symmetric = True
                if down_F_func == -F_func:
                    analysis_result = 'Q偶倍奇0,这里Q(x,-y)=-Q(x,y)为奇函数，$\int_L Qdy= 0$'
                    cal_type = '0'
                    symmetric = True
                else:
                    symmetric = False
            else:
                symmetric = False
        else:
            symmetric = False
        return analysis_result, symmetric, cal_type

    def even_odd_symmetric_way(self, L_func, L_value, P_func, Q_func):
        symmetric_type = self.L_symmetric_explore(L_func)
        symmetric_way = False
        result = None
        if symmetric_type:
            print('L is {} line'.format(symmetric_type))
            P_analysis, P_symmetric, P_cal_type = self.PQ_symmetric_explore(symmetric_type, P_func, func_type='P')
            Q_analysis, Q_symmetric, Q_cal_type = self.PQ_symmetric_explore(symmetric_type, Q_func, func_type='Q')
            if P_symmetric and Q_symmetric:
                # PQ both in [odd func.even func]
                if P_cal_type == '0' and Q_cal_type == '0':
                    print(P_analysis)
                    print(Q_analysis)
                    result = 0
                symmetric_way = True
        return symmetric_way, result

    def lunhuan_symmetric_way(self):
        # transform xyz to yzx,L still original,no change
        # judge_if have turn property
        trun_symmetric = True
        if trun_symmetric:
            print('transform xyz to yzx,L still no change,so we can use trun approach')
            # first
            step1 = '$\int_Lf(x)ds = \int_Lf(y)ds = \int_Lf(z)ds$'
            print('有属性：{}'.format(step1))
            # second
            # ??
        return trun_symmetric


class Substitution:
    def __init__(self, P_func, Q_func, x_subs, y_subs, t_min, t_max, t):
        self.analysis_result(P_func, Q_func, x_subs, y_subs, t_min, t_max, t)

    def create_new_L_func(self, L1_func, L1_value, L2_func, L2_value, L3_func, L3_value):
        '''更新L的函数'''
        new_x = (u - v) / sqrt(2)
        new_y = y
        new_z = (u + v) / sqrt(2)
        # new_x_z = simplify(new_x ** 2 + new_z ** 2)

        step1 = '已知${}^2 + {}^2 = u^2+v^2$，引入该属性'.format(latex(new_x), latex(new_z))
        step2 = r'$set L: \begin{cases}x=\frac{(u - v)}{\sqrt{2}}\\y=y\\z=\frac{(u + v)}{\sqrt{2}}\end{cases}$'
        print(step1 + step2)

        new_L3_func = L3_func.subs({x: new_x, y: new_y, z: new_z})
        new_L3_value = L3_value.subs({x: new_x, y: new_y, z: new_z})

    def second_integrate_use_theta(self, P_func, Q_func, new_x, new_y, theta_min, theta_max):
        '''x,y transfor to theta, change coordinates system'''
        new_P_func = P_func.subs({x: new_x, y: new_y})
        new_Q_func = Q_func.subs({x: new_x, y: new_y})
        diff_new_x = diff(new_x, theta)
        diff_new_y = diff(new_y, theta)
        step1 = r'$\int_L Pdx+Qdy = \int_{}^{} {}*{}d_{}+{}*{}d_{}$'.format(theta_min, theta_max,
                                                                            latex(new_P_func), latex(diff_new_x),
                                                                            latex(theta),
                                                                            latex(new_Q_func), latex(diff_new_y),
                                                                            latex(theta)
                                                                            )
        # print(step1)
        cal_func = simplify(new_P_func * diff_new_x) + simplify(new_Q_func * diff_new_y)
        step2 = r'$=\int_{}^{} {}d_{}$'.format(theta_min, theta_max, latex(cal_func), latex(theta))

        result = integrate(cal_func, (theta, theta_min, theta_max))
        step3 = r'$={}$'.format(latex(result))
        print(step3)

    def analysis_result(self, P_func, Q_func, x_subs, y_subs, t_min, t_max, t):
        # 曲线L在x的坐标系上
        L_trans = r'解：$set L: \begin{cases} ' + \
                  r'x={}\\y={} & t \in [{},{}]'.format(latex(x_subs), latex(y_subs), t_min, t_max) + \
                  r'\end{cases}$'
        print(L_trans)

        print('$\int_L {}dx + ({})dy$'.format(latex(P_func), latex(Q_func)))
        # 第一型曲线积分求解
        try:
            # 'int' object has no attribute 'subs'
            new_P_func = P_func.subs({x: x_subs, y: y_subs})
        except:
            new_P_func = P_func

        try:
            new_Q_func = Q_func.subs({x: x_subs, y: y_subs})
        except:
            new_Q_func = Q_func
        diff1 = diff(x_subs, t)
        diff2 = diff(y_subs, t)

        cal_func = simplify(new_P_func * diff1 + new_Q_func * diff2)
        simpy_submit = latex(Integral(cal_func, (t, t_min, t_max)))
        print(r'变量替换法: $= \int_{}^{} {}*{}d{}+{}*{}d{} = {}$'.format(t_min, t_max,
                                                                     latex(new_P_func), latex(diff1), t,
                                                                     latex(new_Q_func), latex(diff2), t, simpy_submit))
        # 不定积分求原函数F(x)
        result = simplify(integrate(cal_func, (t, t_min, t_max)))
        latex_result = latex(result)
        print('= $F(x)|_a^b={}|_{}^{} = {}$'.format(latex(integrate(cal_func, t)), t_min, t_max, latex_result))

    def three_dim_analysis_result(self, P_func, Q_func, R_func, x_subs, y_subs, z_subs, t_min, t_max, t):
        # 曲线L在x的坐标系上
        L_trans = r'解：$set L: \begin{cases} ' + \
                  r'x={}\\y={}\\z={} & t \in [{},{}]'.format(latex(x_subs),
                                                             latex(y_subs),
                                                             latex(z_subs),
                                                             t_min,
                                                             t_max) + r'\end{cases}$'
        print(L_trans)

        print('$\int_L {}dx + ({})dy + ({})dz$'.format(latex(P_func), latex(Q_func), latex(R_func)))
        # 第一型曲线积分求解
        new_P_func = P_func.subs({x: x_subs, y: y_subs, z: z_subs})
        new_Q_func = Q_func.subs({x: x_subs, y: y_subs, z: z_subs})
        new_R_func = R_func.subs({x: x_subs, y: y_subs, z: z_subs})
        diff1 = diff(x_subs, t)
        diff2 = diff(y_subs, t)
        diff3 = diff(z_subs, t)

        # cal_func = simplify(new_P_func * diff1 + new_Q_func * diff2 + new_R_func * diff3)
        # 有时候简化了反而加深计算复杂度
        cal_func = new_P_func * diff1 + new_Q_func * diff2 + new_R_func * diff3
        simpy_submit = latex(Integral(cal_func, (t, t_min, t_max)))
        print(r'$= \int_{}^{} ({}*{})d{}+({}*{})d{}+({}*{})d{} = {}$'.format(t_min, t_max,
                                                                             latex(new_P_func), latex(diff1), t,
                                                                             latex(new_Q_func), latex(diff2), t,
                                                                             latex(new_R_func), latex(diff3), t,
                                                                             simpy_submit))
        # 不定积分求原函数F(x)
        result = simplify(integrate(cal_func, (t, t_min, t_max)))
        latex_result = latex(result)
        print('= $F(x)|_a^b={}|_{}^{} = {}$'.format(latex(integrate(cal_func, t)), t_min, t_max, latex_result))


class GreenFormula:
    def __init__(self, P_func, Q_func):
        # self.green_diminish_useless_line(P_func, Q_func)
        self.calculate_oint(P_func, Q_func)

    # 处理第二型曲线积分
    def special_green_property(self, P_func, Q_func):
        '''格林公式等于0的时候，四个公式是等价的
        \oint_L Pdx + Qdy = \iint_D \frac{dQ}{dx} - \frac{dP}{dy}d\delta = 0
        '''
        # 条件： D是单连通区域
        simply_connected = True
        if simply_connected:
            P_diff_y = diff(P_func, y)
            Q_diff_x = diff(Q_func, x)
            if P_diff_y == Q_diff_x:
                step1 = r'由于$\frac{dP(x,y)}{dy} = \frac{dQ(x,y)}{dx}' \
                        + '={}$'.format(latex(P_diff_y)) \
                        + '具有$\oint_LPdx+Qdy=0$,且积分值与起点和终点有关，与路径无关'

    def calculate_oint(self, P_func, Q_func):
        '''应用格林公式求解封闭曲线的第二积分
        当然也可以把L拆成很多段累加，例如课本例1，例2
        \oint_L Pdx + Qdy = \iint_D \frac{dQ}{dx} - \frac{dP}{dy}d\delta
        '''
        print('要求L围成的D是单连通区域')
        # 条件：求解\oint（L形成的D是闭区域）
        P_diff_y = diff(P_func, y)
        Q_diff_x = diff(Q_func, x)
        cal_func = Q_diff_x - P_diff_y
        step1 = r'由格林公式：$\oint_L Pdx + Qdy = \iint_D \frac{dQ}{dx} - \frac{dP}{dy}dxdy$'
        step2 = r'$\iint_D ({})- ({})dxdy$'.format(latex(Q_diff_x), latex(P_diff_y))
        step3 = r'得二重积分：$\oint_L {}dx + {}dy =\iint{}dxdx$'.format(latex(P_func), latex(Q_func),
                                                                   latex(simplify(cal_func)))
        print(step1)
        print(step2)
        print(step3)

    def green_diminish_useless_line(self, P_func, Q_func):
        '''优先处理封闭曲线，然后减去非目标曲线后得到目的结果
        要求（1）PQ的函数比较简单，容易求导；（2）非目标曲线的结果比较容易计算
        L是正方向的，D永远保持在左侧
        '''
        step1 = r'$\oint_L {}dx + {}dy'.format(latex(P_func),
                                               latex(Q_func)) \
                + r' = \iint_D \frac{dQ}{dx} - \frac{dP}{dy}dxdy$'
        P_diff_y = diff(P_func, y)
        Q_diff_x = diff(Q_func, x)
        cal_func = Q_diff_x - P_diff_y
        step2 = '$\iint_D {}-{}dxdy$'.format(latex(Q_diff_x), latex(P_diff_y))
        print('容易由格林公式得到封闭曲线的积分： {} = {}'.format(step1, step2))


class Database(Substitution, Symmetric):
    '''第二型曲线积分
    典型例题'''

    def __init__(self):
        self.second_test4()

    def first_test1(self):
        '''第一型曲线积分：曲线质量
        '''
        x_subs = a * cos(t)  # 控制半圆半径
        y_subs = a * sin(t)
        t_min = -pi / 2
        t_max = pi / 2
        func = (x ** 2 + y ** 2) ** (1 / 2)
        # plot_parametric((x_subs.subs(a, 1), y_subs.subs(a, 1)), (t, t_min, t_max), title='curvi linear: L')

        # 曲线L在t的坐标系上
        L_trans = r'$set L: \begin{cases} ' + \
                  r'x={}\\y={} & t \in [{},{}]'.format(latex(x_subs), latex(y_subs), t_min, t_max) + \
                  r'\end{cases}$'
        print(L_trans)

        # 密度函数
        print('$' + latex(Integral(func, (s, L,))) + '$')

        # 第一型曲线积分求解
        new_func = func.subs({x: x_subs, y: y_subs})
        diff1 = diff(x_subs, t)
        diff2 = diff(y_subs, t)
        new_ds = sqrt(diff1 ** 2 + diff2 ** 2)
        cal_func = simplify(new_func) * simplify(new_ds)
        print(r'$= \int_{}^{} {}'.format(t_min, t_max, latex(new_func)) + latex(new_ds) + 'd{}$'.format(t))
        print('$=' + latex(Integral(cal_func, (t, t_min, t_max))) + '$')
        result = integrate(cal_func, (t, t_min, t_max))
        print('$={}$'.format(latex(result)))

    def second_test1(self):
        '''y是关于x的显函数
        PQ的操作比较稳定的，就是替换掉就好
        '''
        # y是关于x的显函数
        # PQ的操作比较稳定的，就是替换掉就好
        P_func = y
        Q_func = x
        # 基于L得到x_subs，y_subs
        x_subs = x
        y_subs = 2 * x
        x_min = 0
        x_max = 1
        self.analysis_result(P_func, Q_func, x_subs, y_subs, x_min, x_max, x)

    def second_test2(self):
        '''x关于y的显函数'''
        P_func = y
        Q_func = x
        # 基于L得到x_subs，y_subs
        x_subs = 1
        y_subs = y
        y_min = 0
        y_max = 2
        self.analysis_result(P_func, Q_func, x_subs, y_subs, y_min, y_max, y)

    def second_test3(self):
        '''关于t的三维曲线积分'''
        P_func = x * y
        Q_func = x - y
        R_func = x ** 2
        # L:
        x_subs = a * cos(t)
        y_subs = a * sin(t)
        z_subs = b * t
        t_min = 0
        t_max = pi
        self.three_dim_analysis_result(P_func, Q_func, R_func, x_subs, y_subs, z_subs, t_min, t_max, t)

    def second_test4(self):
        '''奇偶对称性的使用'''
        P_func = exp(-(x ** 2 + y ** 2)) * cos(2 * x * y)
        Q_func = exp(-(x ** 2 + y ** 2)) * sin(2 * x * y)
        # L: x^2+y^2=1,inverse
        L_func = x ** 2 + y ** 2
        L_value = 1
        print('求解$\int_L{}dx+{}dy$，其中L为${}={}$'.format(latex(P_func), latex(Q_func), L_func, L_value))

        symmetric_way, result = self.even_odd_symmetric_way(L_func, L_value, P_func, Q_func)
        if symmetric_way:
            print('$\int_L {}dx+{}dy={}$'.format(latex(P_func), latex(Q_func), result))
        # # 不能用这种方法，电脑卡死
        # new_x = sqrt(L_value) * cos(theta)
        # new_y = sqrt(L_value) * sin(theta)
        # theta_min = 0
        # theta_max = 2 * pi
        # # self.second_integrate_use_theta(P_func, Q_func, new_x, new_y, theta_min, theta_max)

    def second_test5(self):
        func = x ** 2
        L1_func = x ** 2 + y ** 2 + z ** 2
        L1_value = R ** 2
        L2_func = x + y + z
        L2_value = 0

        print('求解$\int_L{}ds$，其中L：${}={}，{}={}$'.format(latex(func),
                                                        latex(L1_func), latex(L1_value),
                                                        latex(L2_func), latex(L2_value)))
        trun_symmetric = self.lunhuan_symmetric_way()
        if trun_symmetric:
            func_x = func.subs(x, x)
            func_y = func.subs(x, y)
            func_z = func.subs(x, z)
            step1 = r'$\int_L{}ds = '.format(latex(func))
            step2 = r'\frac{1}{3}' + '\int_L{}ds+\int_L{}ds+\int_L{}ds$'.format(latex(func_x),
                                                                                latex(func_y),
                                                                                latex(func_z))
            print(step1 + step2)
            # cal_func = func_x + func_y + func_z
            cal_func = L1_value
            result = integrate(cal_func, (theta, 2 * pi))
            print('$= 1/3 * {}$'.format(latex(result)))

    def second_test6(self):
        '''【待定】'''
        # PQR,Q(-y)=-Q(y)
        L1_func = x ** 2 + y ** 2 + z ** 2
        L1_value = 1
        L2_func = sqrt(x ** 2 + y ** 2)
        L2_value = k * z  # <
        L3_func = y ** 2
        L3_value = 2 * x * z  # <=
        print(
            '计算$\oint_L P(z)dx+Q(y)dy+R(x)dx$，其中$L：{}={}，{}<{}，{} \leq {}$'.format(latex(L1_func), latex(L1_value),
                                                                                   latex(L2_func), latex(L2_value),
                                                                                   latex(L3_func), latex(L3_value)))
        self.create_new_L_func(L1_func, L1_value, L2_func, L2_value, L3_func, L3_value)


def first_form_integrate(func, L):
    # 习题描述
    desc_str = '计算$\int_L {}ds$'.format(latex(func))
    L_str = []
    for line in L:
        L_str.append('{} {} {}'.format(latex(line[0]), line[1], latex(line[2])))
    L_desc = '其中L：$' + ', '.join(L_str) + '$'
    print(desc_str + L_desc)


# def second_form_integrate()
if __name__ == '__main__':
    P_func = 2*x+sin(y)
    Q_func = x*cos(y)
    GreenFormula(P_func, Q_func)

    # L :x 0-1上，y=0
    #x_subs, y_subs, t_min, t_max, t = a*cos(theta),a*sin(theta),0,2*pi,theta
    # L: x=0,y \in [0,1]
    # x_subs, y_subs, t_min, t_max, t = 0, y, 0, 1, y

    #Substitution(P_func, Q_func, x_subs, y_subs, t_min, t_max, t)
