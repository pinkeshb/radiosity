from main import *
from mpmath import *
# from matplotlib 
def get_pix(x,B,n):
    i=int((x)*n)
    if i==n:
        i=n-1
    # print i
    a=1.0/n
    b_error=lambda s:B[3*i]*dia_trans(s, a, i  / float(n), phi_0_m3)+\
                    B[3*i+1]*dia_trans(s, a, i  / float(n), phi_1_m3)+\
                    B[3*i+2]*dia_trans(s, a, i  / float(n), phi_2_m3)
    return b_error(x)

def plotit(n):
    # B=[   0.3550636358244,0.0003958436200413, 0.365347954748293,0.0071251851607434,  0.42705386829165, 0.031667489603304, 0.622455927845617,0.0858980655489621]
    # B=[ 0.288461538461538,0.0333086693763246,               0.0, 0.403846153846154,
    # 0.0333086693763246,               0.0, 0.519230769230769,0.0333086693763246, 
    #               0.0, 0.634615384615385,0.0333086693763246,               0.0]

    b = lambda s:66.0/23.0*s*s+42.0/23.0*s+1
    m = linspace(0, 1-0.00000000001, 250)
    B=main_fn(n,0.00000001)

    y=[get_pix(x,B,n) for x in m]
    # b = lambda s:66.0/23.0*s*s+42.0/23.0*s+1
    y_ideal=[b(x) for x in m]
    y_error=[y_ideal[i]-y[i] for i in range(250)]
    pyplot.plot(m,y,label="Numerically calculated")

    # pyplot.ylabel('Element value')
    pyplot.plot(m,y_ideal,label="Ideal")
    pyplot.plot(m,y_error,label="Error")
    pyplot.xlabel('x')
    pyplot.legend( loc=2)
    pyplot.show()
plotit(4)