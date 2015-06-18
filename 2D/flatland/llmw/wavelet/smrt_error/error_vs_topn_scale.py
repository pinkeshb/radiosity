
# from kernel_haar_phi import *
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
n2=64
# K_f,K_fp,K_p=readit(64,"m2_scale_K_f_mat_dist_"+str(dist)),readit(64,"m2_scale_K_fp_mat_dist_"+str(dist)),readit(64,"m2_scale_K_p_mat_dist_"+str(dist))
a_2_mat=readiterror(n2,"m2_scale_a_2_mat_dist_"+str(dist))
b_2_mat=readiterror(n2,"m2_scale_b_2_mat_dist_"+str(dist))
c_2_mat=readiterror(n2,"m2_scale_c_2_mat_dist_"+str(dist))
d_2_mat=readiterror(n2,"m2_scale_d_2_mat_dist_"+str(dist))
e_2_mat=readiterror(n2,"m2_scale_e_2_mat_dist_"+str(dist))
ab2_mat=readiterror(n2,"m2_scale_ab2_mat_dist_"+str(dist))
cd2_mat=readiterror(n2,"m2_scale_cd2_mat_dist_"+str(dist))
ac2_mat=readiterror(n2,"m2_scale_ac2_mat_dist_"+str(dist))
ad2_mat=readiterror(n2,"m2_scale_ad2_mat_dist_"+str(dist))
bc2_mat=readiterror(n2,"m2_scale_bc2_mat_dist_"+str(dist))
bd2_mat=readiterror(n2,"m2_scale_bd2_mat_dist_"+str(dist))
ae2_mat=readiterror(n2,"m2_scale_ae2_mat_dist_"+str(dist))
be2_mat=readiterror(n2,"m2_scale_be2_mat_dist_"+str(dist))
ce2_mat=readiterror(n2,"m2_scale_ce2_mat_dist_"+str(dist))
# 64=64
fname = str(64)+'haar_topn_all_error'+str(dist) + ".txt"
fo = open(fname, "w")

print "n = ", 64, "\n"
fo.write("n = "+str(64) + "\n")

# K_f,K_fp,K_p=smrt_error(64,1)
# for n in [4,8,16,32,64,128,64]:

def error_it_topn(n,K4):

    # n=8

   
    K_4_8=matrix(n2*2,n2*2)
    K_4_8[0:n*2,0:n*2]=K4
    K4_8_idwt=K_4_8
    nc=n2
    while nc!=n:
        K4_8_idwt=idwt2_inside(K4_8_idwt)
        nc=nc/2
    # print K4_8_idwt.cols, K4_8_idwt.rows

    print ce2_mat.cols, ce2_mat.rows
    de2_mat=readiterror(n2,"m2_scale_de2_mat_dist_"+str(dist))
    # print K
    K_error=matrix(n2,n2)
    num_k=0
    for i in range(n2):
        for j in range(n2):
            K_error[i,j]=a_2_mat[i,j]+\
            +b_2_mat[i,j]*K4_8_idwt[2*i+0,2*j+0]*K4_8_idwt[2*i+0,2*j+0]+\
            +c_2_mat[i,j]*K4_8_idwt[2*i+0,2*j+1]*K4_8_idwt[2*i+0,2*j+1]+\
            +d_2_mat[i,j]*K4_8_idwt[2*i+1,2*j+0]*K4_8_idwt[2*i+1,2*j+0]+\
            +e_2_mat[i,j]*K4_8_idwt[2*i+1,2*j+1]*K4_8_idwt[2*i+1,2*j+1]+\
            -ab2_mat[i,j]*K4_8_idwt[2*i+0,2*j+0]+\
            +cd2_mat[i,j]*K4_8_idwt[2*i+0,2*j+1]*K4_8_idwt[2*i+1,2*j+0]+\
            -ac2_mat[i,j]*K4_8_idwt[2*i+0,2*j+1]+\
            -ad2_mat[i,j]*K4_8_idwt[2*i+1,2*j+0]+\
            +bc2_mat[i,j]*K4_8_idwt[2*i+0,2*j+0]*K4_8_idwt[2*i+0,2*j+1]+\
            +bd2_mat[i,j]*K4_8_idwt[2*i+0,2*j+0]*K4_8_idwt[2*i+1,2*j+0]+\
            -ae2_mat[i,j]*K4_8_idwt[2*i+1,2*j+1]+\
            +be2_mat[i,j]*K4_8_idwt[2*i+0,2*j+0]*K4_8_idwt[2*i+1,2*j+1]+\
            +ce2_mat[i,j]*K4_8_idwt[2*i+0,2*j+1]*K4_8_idwt[2*i+1,2*j+1]+\
            +de2_mat[i,j]*K4_8_idwt[2*i+1,2*j+0]*K4_8_idwt[2*i+1,2*j+1]
    # print num_k
    print K_error
    num_k=0
    for i in range(n2):
        for j in range(n2):
            num_k=num_k+K_error[i,j]
    print num_k
    return num_k




K=readit(64,"haar_scale_K_mat_dist_"+str(dist))
# K_dwt=dwt2(K)

for topn in [64*64*4,64*64*4/2,64*64*4/4,64*64*4/8,64*64*4/16,64*64*4/32,64*64*4/64,64*64*4/128,64,64/2,64/4,64/8]:
    
    K_thres=thres(K,topn)
    num_k= error_it_topn(64,K_thres)
    print "topn = ", topn, "\n"
    fo.write("topn = "+str(topn) + "\n")

    print "error_k = ", num_k, "\n"
    fo.write("error_k = "+str(num_k) + "\n")