# from kernel_m2_phi import *
from matplotlib import pyplot
from wavedecs import *
from save_read import *

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

n_min,n_max=4,5

# fname = 'm3_poly_all_error' + ".txt"
# fo = open(fname, "w")
dist=0.25
for n_log in range(n_min,n_max):
    n=pow(2,n_log)

    K=readit(n,"qlmw_K_mat_dist_"+str(dist))
    L=thres(K)
    pyplot.plot(L,label="LLMW Scale")
    pyplot.xlabel('sorted elements')




    pyplot.grid(True)

    L=thres(dwt2(K))
    pyplot.plot(L,label="LLMW Wavelet")
    pyplot.xlabel('sorted elements')

    pyplot.legend()

    pyplot.yscale('log')
    pyplot.xscale('log')
    pyplot.show()


    print "\n\n\n"