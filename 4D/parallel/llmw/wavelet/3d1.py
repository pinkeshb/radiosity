from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from main import *
import numpy as np
import copy
def get_pix(x,y,B,n):
    i=int((x)*n)
    if i==n:
        i=n-1
    j=int((y)*n)
    if j==n:
        j=n-1
    a=1.0/n
    b=lambda s,t:B[2*i][2*j]*dia_trans(s, a, i  / float(n), phi_1_m2)*dia_trans(t, a, j  / float(n), phi_1_m2)+\
                    B[2*i+1][2*j+1]*dia_trans(s, a, i  / float(n), phi_2_m2)*dia_trans(t, a, j  / float(n), phi_2_m2)+\
                    B[2*i][2*j+1]*dia_trans(s, a, i  / float(n), phi_1_m2)*dia_trans(t, a, j  / float(n), phi_2_m2)+\
                    B[2*i+1][2*j]*dia_trans(s, a, i  / float(n), phi_2_m2)*dia_trans(t, a, j  / float(n), phi_1_m2)
    return b(x,y)
def get_test_data(delta=0.005):
    B1,B2=main_fn(16,0.001,0.25) 

    # f1 = lambda s, t: s*s*s*s+t*t
    f1 = lambda s, t: get_pix(s,t,B1,4)
    dist=1
    f2 = lambda s, t: dist*dist/ (2*pow(((s - t) * (s - t) + dist*dist), 1.5))
    f3 = lambda s, t: s - t
    from matplotlib.mlab import  bivariate_normal
    x = y = np.arange(0, 1.0, delta)
    X, Y = np.meshgrid(x, y)
    Z=copy.deepcopy(X)
    for i in range(len(x)):
        for j in range(len(y)):
            # print X[i][j]
            # X[i][j]=1
            Z[i][j]=f1(X[i][j],Y[i][j])

    return X, Y, Z



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x, y, z = get_test_data(0.005)
ax.plot_wireframe(x,y,z, rstride=2, cstride=2)

plt.show()