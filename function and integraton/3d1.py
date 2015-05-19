from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

def get_test_data(delta=0.05):
    f1 = lambda s, t: s*s*s*s+t*t
    dist=1
    f2 = lambda s, t: dist*dist/ (2*pow(((s - t) * (s - t) + dist*dist), 1.5))
    f3 = lambda s, t: s - t
    from matplotlib.mlab import  bivariate_normal
    x = y = np.arange(0, 1.0, delta)
    X, Y = np.meshgrid(x, y)

    Z=f1(X,Y)

    return X, Y, Z



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x, y, z = get_test_data(0.05)
ax.plot_wireframe(x,y,z, rstride=2, cstride=2)

plt.show()