from kernel_haar_phi import *
from matplotlib import pyplot
from wavedecs import *

def thres(K_dwt):
    L=[]
    K=[]
    n=K_dwt.cols
    K_dwt_thres=matrix(n,n)
    K=K_dwt.tolist()
    print n
    for i in range(n):
        L.extend(K[i][:])
    for i in range(len(L)):
        L[i]=abs(L[i])
    L.sort()
    L.reverse()
    print L
    return L

n_min,n_max=2,3

fname = 'm3_poly_all_error' + ".txt"
fo = open(fname, "w")

for n_log in range(n_min,n_max):
    n=pow(2,n_log)

    K=project_kernel_haar_phi(n)
    L=thres(K)
    pyplot.plot(L,label="Haar Scale")
    L=thres(dwt2(K))
    pyplot.plot(L,label="Haar Scale")
    plt.legend()
    pyplot.show()


    print "\n\n\n"