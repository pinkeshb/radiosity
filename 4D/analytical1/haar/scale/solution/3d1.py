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

n=8
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
B1,B2=main_fn(n,0.001,0.25) 

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

# n=8
# top_n=n*n*n*n
# B1,B2=main_fn(n,0.001,0.25,top_n) 

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# # n=4
# x, y, z = get_test_data(n,0.005,B2)
# ax.plot_wireframe(x,y,z, rstride=2, cstride=2)
# # plt.show()

# top_n=n*n*n*n/2
# B1_top,B2_top=main_fn(n,0.001,0.25,top_n) 

# x, y, z = get_test_data(n,0.005,B2_top)
# ax.plot_wireframe(x,y,z, rstride=2, cstride=2,color="green")


# error = [[0 for x in range(n)] for x in range(n)] 
# for i in range(n):
#     for j in range(n):
#         error[i][j]=B2_top[i][j]-B2[i][j]
# x, y, z = get_test_data(n,0.005,error)
# ax.plot_wireframe(x,y,z, rstride=2, cstride=2,color="red")

# plt.show()