
from kernel_haar_phi import *
from save_read import *
from s_error import *
from wavedecs import *


def thres(K_dwt, top_n):
    L = []
    K = []
    n = K_dwt.cols
    K_dwt_thres = matrix(n, n)
    K = K_dwt.tolist()
    print n
    for i in range(n):
        L.extend(K[i][:])
    for i in range(len(L)):
        L[i] = abs(L[i])
    L.sort()
    L.reverse()
    # print L
    # print top_n
    thresh = L[top_n - 1]
    print thresh
    start = L.index(thresh)
    alowed = top_n - start
    print start
    for i in range(0, n):
        for j in range(0, n):
            if abs(K_dwt[i, j]) > thresh:
                K_dwt_thres[i, j] = K_dwt[i, j]
            elif abs(K_dwt[i, j]) == thresh and alowed > 0:
                alowed = alowed - 1
                K_dwt_thres[i, j] = K_dwt[i, j]
            else:
                K_dwt_thres[i, j] = 0
    return K_dwt_thres
dist=1
K_f,K_fp,K_p=readit(256,"haar_scale_K_f_mat_dist_"+str(dist)),readit(256,"haar_scale_K_fp_mat_dist_"+str(dist)),readit(256,"haar_scale_K_p_mat_dist_"+str(dist))

# 256=256
fname = str(256)+'haar_scale_topn_all_error'+str(dist) + ".txt"
fo = open(fname, "w")

print "n = ", 256, "\n"
fo.write("n = "+str(256) + "\n")

# K_f,K_fp,K_p=smrt_error(256,1)
# for n in [4,8,16,32,64,128,256]:

def error_it_topn(n,K4):

    # n=8

    K_4_8=matrix(256,256)
    K_4_8[0:n,0:n]=K4
    nc=256
    K4_8_idwt=K_4_8
    while nc!=n:
        print "f"
        K4_8_idwt=idwt2_inside(K4_8_idwt)
        nc=nc/2
        # K4_8_idwt=idwt2_inside(idwt2_inside(idwt2_inside(idwt2_inside(idwt2_inside(K_4_8)))))
    # print K4_8_idwt


    K8_error_smt=matrix(256,256)
    for i in range(256):
        for j in range(256):
            K8_error_smt[i,j]=K_f[i,j]-K4_8_idwt[i,j]*K_fp[i,j]+K4_8_idwt[i,j]*K4_8_idwt[i,j]*K_p[i,j]
    # K = project_kernel_haar_phi(n)
    # K_error=smrt_error(n)saveit(n,K,"haar_scale_K_mat_dist_1")
    # saveit(n,K_error,"haar_scale_K_error_mat_dist_1")
    # K_rec=readit(n,"haar_scale_K_mat_dist_1")
    # K4_error=readit(4,"haar_scale_K_error_mat_dist_1")
    # K8_error=readit(8,"haar_scale_K_error_mat_dist_1")

    num_k=0
    for i in range(256):
        for j in range(256):
            num_k=num_k+K8_error_smt[i,j]
    print num_k
    return num_k





K=readit(256,"haar_scale_K_mat_dist_"+str(dist))
#K_dwt=dwt2(K)
for topn in [256*256,256*256/2,256*256/4,256*256/8,256*256/16,256*256/32,256*256/64,256*256/128,256,256/2,256/4,256/8]:
    K_thres=thres(K,topn)
    #K_thres=idwt2(K_dwt_thres)
    num_k= error_it_topn(256,K_thres)
    print "topn = ", topn, "\n"
    fo.write("topn = "+str(topn) + "\n")

    print "error_k = ", num_k, "\n"
    fo.write("error_k = "+str(num_k) + "\n")