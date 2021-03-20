# ===================================
# @Time : 2020/11/30 22:55
# 求积分
# ===================================

from sympy import integrate,Integral,simplify,latex
from sympy.abc import x,y,u,v,a,b,c,d,n,m
from sympy.integrals.manualintegrate import integral_steps
from sympy import atan


def analysis_steps(steps):
    try:
        # 目标函数
        context = steps.context
        field = steps._fields
    except:
        for line in steps:
            analysis_steps(line)
    else:
        if 'alternatives' in field:
            print('函数变更：$'+latex(Integral(context,x))+'$')
            new_steps = steps.alternatives[0]
            f1 = '$'+latex(Integral(new_steps.rewritten,x))+'$'
            print('='+f1+'\n')
            analysis_steps(new_steps)
        if 'rewritten' in field:
            new_f = '$'+latex(Integral(steps.rewritten,x))+'$'
            print('函数Rewritten：$' + latex(Integral(context,x)) + '$ ='+new_f+'\n')
            new_steps = steps.substep.substeps
            analysis_steps(new_steps)
        if 'substeps' in field:
            new_steps = steps.substeps
            analysis_steps(new_steps)
        if 'other' in field:
            result = simplify(integrate(context,x))
            out4 = '$'+latex(Integral(context,x))+'='+latex(result)+'$'
            print('分项积分：'+out4+'\n')



f_x = atan(x)
out_f = '$'+latex(Integral(f_x,x))+'$'
steps = integral_steps(f_x,x)
analysis_steps(steps)
f_x_result = '$'+latex(simplify(integrate(f_x,x)))+'$'
print('结果为：'+out_f+'='+f_x_result)
