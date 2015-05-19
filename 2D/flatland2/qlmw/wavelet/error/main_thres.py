from kernel_m2_phi import *
from mpmath import *
import sys
from wavedecs import *
def thres_it(K_dwt,top_n):
    print "K_dwt",K_dwt
    L=[]
    K=[]
    n=K_dwt.cols/2
    K_dwt_thres=matrix(n*2,n*2)
    K=K_dwt.tolist()
    print "n",n
    for i in range(n*2):
        L.extend(K[i][:])
    for i in range(len(L)):
        L[i]=abs(L[i])
    L.sort()
    L.reverse()
    print "L",L
    # print top_n
    thresh=L[top_n-1]
    print "thresh",thresh
    start=L.index(thresh)
    alowed=top_n-start
    print "start", start 
    for i in range(0,n*2):
        for j in range(0,n*2):
            if abs(K_dwt[i,j])>thresh:
                K_dwt_thres[i,j]=K_dwt[i,j]
            elif abs(K_dwt[i,j])==thresh and alowed>0:
                alowed=alowed-1
                K_dwt_thres[i,j]=K_dwt[i,j]
            else:
                K_dwt_thres[i,j]=0
    print "K_dwt_thres",K_dwt_thres
    return K_dwt_thres
def main_fn(n,top_n):
    fname=str(n)+'haar_scale'+".txt"
    fo = open(fname, "w")

    K=project_kernel_m2_phi(n)
    K_dwt=dwt2(K)

    K_dwt_thres=thres_it(K_dwt,top_n)
    
    return K,K_dwt,K_dwt_thres
if __name__ == "__main__":
    thres = 0.001
    print main_fn(4, thres)
