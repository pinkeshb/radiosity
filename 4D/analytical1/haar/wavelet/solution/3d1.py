from matplotlib.mlab import  bivariate_normal
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from main import *
import numpy as np
import copy
from haarphi import *
def get_pix(x,y,B,n):
    i=int((x)*n)
    if i==n:
        i=n-1
    j=int((y)*n)
    if j==n:
        j=n-1
    a=1.0/n
    b=lambda s,t:   B[i+0][j+0]*dia_trans(s, a, i  / float(n), phi_haar)*dia_trans(t, a, j  / float(n), phi_haar)
                    
    return b(x,y)
def get_test_data(n,delta=0.005,str="numerical"):
    if str=="numerical":
        B1,B2=main_fn(n,0.001,0.25) 

        # f1 = lambda s, t: s*s*s*s+t*t
        f1 = lambda s, t: get_pix(s,t,B1,n)
        # dist=1
        # f2 = lambda s, t: dist*dist/ (3*pow(((s - t) * (s - t) + dist*dist), 1.5))
        # f3 = lambda s, t: s - t
    else:
        f1 = lambda s, t: 1+9.0/32.0*s*t

    x = y = np.arange(0, 1.0, delta)
    X, Y = np.meshgrid(x, y)
    Z=copy.deepcopy(X)
    for i in range(len(x)):
        for j in range(len(y)):
            # print X[i][j]
            # X[i][j]=1
            Z[i][j]=f1(X[i][j],Y[i][j])

    return X, Y, Z


n=4
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x, y, z = get_test_data(n,0.005,"numerical")
ax.plot_wireframe(x,y,z, rstride=2, cstride=2)
x, y, z = get_test_data(n,0.005,"original")
ax.plot_wireframe(x,y,z, rstride=2, cstride=2,color="red")

plt.show()