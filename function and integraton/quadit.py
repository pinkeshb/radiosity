from mpmath import *
import numpy
def fun(x1,y1,x2,y2):
    # return x1*y1*x2*y2
    return 1/((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+1)
def quadit(f,(a1,b1),(a2,b2),(a3,b3),(a4,b4),deg):

    x,w=numpy.polynomial.legendre.leggauss(deg)
    bma1=(b1-a1)/2.0
    bpa1=(b1+a1)/2.0
    bma2=(b2-a2)/2.0
    bpa2=(b2+a2)/2.0
    bma3=(b3-a3)/2.0
    bpa3=(b3+a3)/2.0
    bma4=(b4-a4)/2.0
    bpa4=(b4+a4)/2.0

    # points=[) for i in range(len(x))]
    sum=0
    for i in range(len(x)):
        for j in range(len(x)):
            for k in range(len(x)):
                for l in range(len(x)):
                    sum=sum+w[i]*w[j]*w[k]*w[l]*f(  bma1*x[i]+bpa1,
                                                    bma2*x[j]+bpa2,
                                                    bma3*x[k]+bpa3,
                                                    bma4*x[l]+bpa4)
    return sum*bma1*bma2*bma3*bma4
print quadit(fun,(0,1),(0,1),(0,1),(0,1),10)
# print quad(fun,[,1])
