from mpmath import *
import numpy
def fun(x1,x2):
    # return x*y*z*w*x*y*z*w
    return 1/((x1-x2)*(x1-x2)+1)
def quadit(f,deg):

    x,w=numpy.polynomial.legendre.leggauss(deg)
    # points=[) for i in range(len(x))]
    sum=0
    for i in range(len(x)):
        for j in range(len(x)):
                    sum=sum+w[i]*w[j]*f(x[i],x[j])
    return sum
print quadit(fun,10)
print quad(fun,[-1,1],[-1,1])
