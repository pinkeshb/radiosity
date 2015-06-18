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
    # print i,j
    b=lambda s,t:B[2*i][2*j]*dia_trans(s, a, i  / float(n), phi_1_m2)*dia_trans(t, a, j  / float(n), phi_1_m2)+\
                    B[2*i+1][2*j+1]*dia_trans(s, a, i  / float(n), phi_2_m2)*dia_trans(t, a, j  / float(n), phi_2_m2)+\
                    B[2*i][2*j+1]*dia_trans(s, a, i  / float(n), phi_1_m2)*dia_trans(t, a, j  / float(n), phi_2_m2)+\
                    B[2*i+1][2*j]*dia_trans(s, a, i  / float(n), phi_2_m2)*dia_trans(t, a, j  / float(n), phi_1_m2)
    return b(x,y)
# def get_test_data(n,delta=0.005):
#     B1=main_fn(n,0.001,0.25) 

#     # f1 = lambda s, t: s*s*s*s+t*t
#     f1 = lambda s, t: get_pix(s,t,B1,n)
#     # dist=1
#     # f2 = lambda s, t: dist*dist/ (2*pow(((s - t) * (s - t) + dist*dist), 1.5))
#     # f3 = lambda s, t: s - t
#     from matplotlib.mlab import  bivariate_normal
#     x = y = np.arange(0, 1.0, delta)
#     X, Y = np.meshgrid(x, y)
#     Z=copy.deepcopy(X)
#     for i in range(len(x)):
#         for j in range(len(y)):
#             # print X[i][j]
#             # X[i][j]=1
#             Z[i][j]=f1(X[i][j],Y[i][j])

#     return X, Y, Z

def get_test_data(n,f1,delta=0.005):


    x = y = np.arange(0, 1.0, delta)
    X, Y = np.meshgrid(x, y)
    Z=copy.deepcopy(X)
    for i in range(len(x)):
        for j in range(len(y)):
            # print X[i][j]
            # X[i][j]=1
            Z[i][j]=f1(X[i][j],Y[i][j])

    return X, Y, Z

n=2
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
B1=main_fn(n,0.001,0.25) 

# f1 = lambda s, t: s*s*s*s+t*t
f1 = lambda s, t: get_pix(s,t,B1,n)
x, y, z = get_test_data(n,f1,0.005)
ax.plot_wireframe(x,y,z, rstride=2, cstride=2)
f1 = lambda s, t: 1+9.0/32.0*s*t

x, y, z = get_test_data(n,f1,0.005)
ax.plot_wireframe(x,y,z, rstride=2, cstride=2,color="green")

f1 = lambda s, t:1+9.0/32.0*s*t- get_pix(s,t,B1,n)

x, y, z = get_test_data(n,f1,0.005)
ax.plot_wireframe(x,y,z, rstride=2, cstride=2,color="red")

plt.show()
# n=1
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# x, y, z = get_test_data(n,0.005)
# ax.plot_wireframe(x,y,z, rstride=2, cstride=2)

# plt.show()