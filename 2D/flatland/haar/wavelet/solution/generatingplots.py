from mpmath import *
from haarphi import *
from matplotlib import pyplot
def plotphi(f):
    x=linspace(-0.25,1.25,1000)
    y=[dia_trans(m,1,0,f) for m in x]
    pyplot.axis([-0.25, 1.25, -2, +2])
    pyplot.grid(True)
    pyplot.xlabel('x')
    pyplot.plot(x,y)
    pyplot.show()
plotphi(psi_haar)
plotphi(phi_haar)

