from kernel_m3_phi import *
from matplotlib import pyplot

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
    pyplot.plot(L)
    pyplot.show()

n_min,n_max=2,4

# fname = 'm3_poly_all_error' + ".txt"
# fo = open(fname, "w")

for n_log in range(n_min,n_max):
    n=pow(2,n_log)

    K,K_error=project_kernel_m3_phi(n)
    thres(K)


    print "\n\n\n"