import math
from mpmath import *
from matplotlib import pyplot
root3=pow(3,0.5)
root5=pow(5,0.5)

def phi_0_m3(x):
    if 0<=x<1:
        return 1.0
    else:
        return 0.0
def phi_1_m3(x):
    if 0<=x<1:
        return (2*float(x)-1)*root3
    else:
        return 0.0
def phi_2_m3(x):
    if 0<=x<1:
        return (2*float(x)-1)*(2*float(x)-1)*root5*3/2.0-root5/2.0
    else:
        return 0.0
def psi_0_m3(x):
    if 0<=x<0.5:
        return -(120*x*x-72*x+7)/3.0
    elif 0.5<=x<1:
        return (120*x*x-168*x+55)/3.0
    else:
        return 0.0
def psi_1_m3(x):
    if 0<=x<0.5:
        return (30*x*x-14*x+1)*root3
    elif 0.5<=x<1:
        return (30*x*x-46*x+17)*root3
    else:
        return 0.0
def psi_2_m3(x):
    if 0<=x<0.5:
        return -(48*x*x-18*x+1)*root5/3
    elif 0.5<=x<1:
        return (48*x*x-78*x+31)*root5/3
    else:
        return 0.0
# def phi_0_m3(x):
#   if 0<=x<1:
#       return -(120*x*x-72*x+7)/3.0
#   else:
#       return 0.0
# def phi_0_m3(x):
#   if 0<=x<1:
#       return -(120*x*x-72*x+7)/3.0
#   else:
#       return 0.0
def dia_trans(x,a,s,f):
    return f((x-s)/float(a))/pow(a,0.5)
if __name__=="__main__":
    m=linspace(0,1,250)
    # y=[-root3*dia_trans(z,0.5,0,phi_0_m3)+root3*dia_trans(z,0.5,0.5,phi_0_m3)+dia_trans(z,0.5,0,phi_1_m3)+dia_trans(z,0.5,0.5,phi_1_m3) for z in m]
    # y=[(-root5*root3*dia_trans(z,0.5,0,phi_1_m3)/4/pow(2,0.5)+dia_trans(z,0.5,0,phi_2_m3)/4/pow(2,0.5)+root5*root3*dia_trans(z,0.5,0.5,phi_1_m3)/4/pow(2,0.5)+dia_trans(z,0.5,0.5,phi_2_m3)/4/pow(2,0.5)) for z in m]
    # y=[(+root5*root3*dia_trans(z,0.5,0,phi_1_m3)/4/pow(2,0.5)-dia_trans(z,0.5,0,phi_0_m3)/4/pow(2,0.5)+root5*root3*dia_trans(z,0.5,0.5,phi_1_m3)/4/pow(2,0.5)-dia_trans(z,0.5,0.5,phi_0_m3)/4/pow(2,0.5)) for z in m]
    # y=[(-dia_trans(z,0.5,0,phi_2_m3)/pow(2,0.5)+dia_trans(z,0.5,0.5,phi_2_m3)/pow(2,0.5)) for z in m]
    # y=[(dia_trans(z,0.5,0,phi_2_m3)/pow(2,0.5)) for z in m]
    # y=[(-dia_trans(z,0.5,0,phi_2_m3)/pow(2,0.5)
        # +dia_trans(z,0.5,0.5,phi_2_m3)/pow(2,0.5))
         # for z in m]
    # pyplot.plot(m,y)
    # pyplot.show()
    # f=lambda s: dia_trans(s,1,0,psi_2_m3)*dia_trans(s,1,0,psi_2_m3)
    # print quad(f,[0,1])
    print dia_trans(0,1,0,psi_2_m3)
# print dia_trans(0.49,0.25,0.25,phi_2_m2)
# print pow(1.732050808,math.log(2,2))