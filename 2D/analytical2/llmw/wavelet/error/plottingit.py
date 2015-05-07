from main_thres import *
from mpmath import *

def get_pix(x,B,n):
    i=int((x)*n)
    if i==n:
        i=n-1
    # print i
    a=1.0/n
    b_error=lambda s:B[2*i]*dia_trans(s, a, i  / float(n), phi_1_m2)+\
                    B[2*i+1]*dia_trans(s, a, i  / float(n), phi_2_m2)
    return b_error(x)
def plot_it(B,n):
    # from matplotlib
    m = linspace(0, 1, 250)
    # B=[   0.3550636358244,0.0003958436200413, 0.365347954748293,0.0071251851607434,  0.42705386829165, 0.031667489603304, 0.622455927845617,0.0858980655489621]
    y=[get_pix(x,B,n) for x in m]
    b = lambda s:8.0/9.0*s*s*s*s+32.0/45.0
    y_ideal=[b(x) for x in m]
    y_error=[y_ideal[i]-y[i] for i in range(250)]
    pyplot.plot(y)
    pyplot.plot(y_ideal)
    pyplot.plot(y_error)
    # print y ,"y"
    pyplot.show() 
if __name__=="__main__":
    n=8
    B,B_error,K,K_error=main_fn(n,0.001,n*n*4)
    plot_it(B,n)