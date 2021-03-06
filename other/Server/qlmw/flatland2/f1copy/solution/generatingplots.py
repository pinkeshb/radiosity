from mpmath import *
from m3_phi import *
from matplotlib import pyplot
def plotphi(f):
    x=linspace(-0.25,1.25,1000)
    y=[dia_trans(m,1,0,f) for m in x]
    pyplot.axis([-0.25, 1.25, -3, +3])
    pyplot.grid(True)
    pyplot.xlabel('x')
    pyplot.plot(x,y)
    pyplot.show()
plotphi(psi_2_m3)
plotphi(psi_1_m3)
plotphi(psi_0_m3)
plotphi(phi_0_m3)
plotphi(phi_1_m3)
plotphi(phi_2_m3)
