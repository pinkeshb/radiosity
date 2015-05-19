from kernel_m2_phi import *
from matplotlib import pyplot
from wavedecs import *

def thres(K_dwt):
    L=[]
    K=[]
    n=K_dwt.cols
    # K_dwt_thres=matrix(n,n)
    K=K_dwt.tolist()
    print n
    for i in range(n):
        L.extend(K[i][:])
    for i in range(len(L)):
        L[i]=abs(L[i])
    L.sort()
    L.reverse()
    print L
    pyplot.plot(L)
    pyplot.show()

n_min,n_max=2,3

fname = 'haar_scale_all_error' + ".txt"
fo = open(fname, "w")

for n_log in range(n_min,n_max):
    n=pow(2,n_log)

    K=project_kernel_m2_phi(n,n*n*4)
    thres(K)
    thres(dwt2(K))


    print "\n\n\n"