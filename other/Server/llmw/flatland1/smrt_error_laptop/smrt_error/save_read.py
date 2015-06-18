# from kernel_haar_phi import *
from mpmath import *
from s_error import *
def saveit(n,K,name):
    fname = str(n) + name + ".txt"
    fo = open(fname, "w")
    fo.write(str(n) + "\n")
    # K = project_kernel_haar_phi(n)
    for i in range(K.cols):
        for j in range(K.cols):
            fo.write(str(float(K[i,j]))+"\t\t")
        fo.write("\n")
    fo.close()
def readit(n,name):
    fname = str(n) + name+ ".txt"
    fo = open(fname, "r")
    # fo.write(str(n) + "\n")
    n=fo.readline()
    n=int(n)*2
    K = matrix(n,n)
    for i in range(n):
        line=fo.readline()
        # print line
        line = line.split()
        # print line[0]
        print i
        for j in range(n):

            K[i,j]=float(line[j])
    fo.close()
    return K
def readiterror(n,name):
    fname = str(n) + name+ ".txt"
    fo = open(fname, "r")
    # fo.write(str(n) + "\n")
    n=fo.readline()
    n=int(n)
    K = matrix(n,n)
    for i in range(n):
        line=fo.readline()
        # print line
        line = line.split()
        # print line[0]
        print i
        for j in range(n):

            K[i,j]=float(line[j])
    fo.close()
    return K

if __name__=="__main__":
    n=4
    dist = 0.25
    K=readit(n,"haar_scale_K_mat_dist_"+str(dist))
    # a_2_mat,b_2_mat,c_2_mat,d_2_mat,e_2_mat,ab2_mat,cd2_mat,ac2_mat,ad2_mat,bc2_mat,bd2_mat,ae2_mat,be2_mat,ce2_mat,de2_mat=smrt_error(n,dist)
    # saveit(n,a_2_mat,"haar_scale_a_2_mat_dist_"+str(dist))
    # saveit(n,a_2_mat,"m2_scale_a_2_mat_dist_"+str(dist))
    # saveit(n,b_2_mat,"m2_scale_b_2_mat_dist_"+str(dist))
    # saveit(n,c_2_mat,"m2_scale_c_2_mat_dist_"+str(dist))
    # saveit(n,d_2_mat,"m2_scale_d_2_mat_dist_"+str(dist))
    # saveit(n,e_2_mat,"m2_scale_e_2_mat_dist_"+str(dist))
    # saveit(n,ab2_mat,"m2_scale_ab2_mat_dist_"+str(dist))
    # saveit(n,cd2_mat,"m2_scale_cd2_mat_dist_"+str(dist))
    # saveit(n,ac2_mat,"m2_scale_ac2_mat_dist_"+str(dist))
    # saveit(n,ad2_mat,"m2_scale_ad2_mat_dist_"+str(dist))
    # saveit(n,bc2_mat,"m2_scale_bc2_mat_dist_"+str(dist))
    # saveit(n,bd2_mat,"m2_scale_bd2_mat_dist_"+str(dist))
    # saveit(n,ae2_mat,"m2_scale_ae2_mat_dist_"+str(dist))
    # saveit(n,be2_mat,"m2_scale_be2_mat_dist_"+str(dist))
    # saveit(n,ce2_mat,"m2_scale_ce2_mat_dist_"+str(dist))
    # saveit(n,de2_mat,"m2_scale_de2_mat_dist_"+str(dist))
    # # K=
    a_2_mat=readiterror(n,"m2_scale_a_2_mat_dist_"+str(dist))
    b_2_mat=readiterror(n,"m2_scale_b_2_mat_dist_"+str(dist))
    c_2_mat=readiterror(n,"m2_scale_c_2_mat_dist_"+str(dist))
    d_2_mat=readiterror(n,"m2_scale_d_2_mat_dist_"+str(dist))
    e_2_mat=readiterror(n,"m2_scale_e_2_mat_dist_"+str(dist))
    ab2_mat=readiterror(n,"m2_scale_ab2_mat_dist_"+str(dist))
    cd2_mat=readiterror(n,"m2_scale_cd2_mat_dist_"+str(dist))
    ac2_mat=readiterror(n,"m2_scale_ac2_mat_dist_"+str(dist))
    ad2_mat=readiterror(n,"m2_scale_ad2_mat_dist_"+str(dist))
    bc2_mat=readiterror(n,"m2_scale_bc2_mat_dist_"+str(dist))
    bd2_mat=readiterror(n,"m2_scale_bd2_mat_dist_"+str(dist))
    ae2_mat=readiterror(n,"m2_scale_ae2_mat_dist_"+str(dist))
    be2_mat=readiterror(n,"m2_scale_be2_mat_dist_"+str(dist))
    ce2_mat=readiterror(n,"m2_scale_ce2_mat_dist_"+str(dist))
    de2_mat=readiterror(n,"m2_scale_de2_mat_dist_"+str(dist))
    print K
    K_error=matrix(n,n)
    num_k=0
    for i in range(n):
        for j in range(n):
            K_error[i,j]=a_2_mat[i,j]+\
            +b_2_mat[i,j]*K[2*i+0,2*j+0]*K[2*i+0,2*j+0]+\
            +c_2_mat[i,j]*K[2*i+0,2*j+1]*K[2*i+0,2*j+1]+\
            +d_2_mat[i,j]*K[2*i+1,2*j+0]*K[2*i+1,2*j+0]+\
            +e_2_mat[i,j]*K[2*i+1,2*j+1]*K[2*i+1,2*j+1]+\
            -ab2_mat[i,j]*K[2*i+0,2*j+0]+\
            +cd2_mat[i,j]*K[2*i+0,2*j+1]*K[2*i+1,2*j+0]+\
            -ac2_mat[i,j]*K[2*i+0,2*j+1]+\
            -ad2_mat[i,j]*K[2*i+1,2*j+0]+\
            +bc2_mat[i,j]*K[2*i+0,2*j+0]*K[2*i+0,2*j+1]+\
            +bd2_mat[i,j]*K[2*i+0,2*j+0]*K[2*i+1,2*j+0]+\
            -ae2_mat[i,j]*K[2*i+1,2*j+1]+\
            +be2_mat[i,j]*K[2*i+0,2*j+0]*K[2*i+1,2*j+1]+\
            +ce2_mat[i,j]*K[2*i+0,2*j+1]*K[2*i+1,2*j+1]+\
            +de2_mat[i,j]*K[2*i+1,2*j+0]*K[2*i+1,2*j+1]
    print num_k
    print K_error
    sum_a=0
    for i in range(n):
        for j in range(n):
            sum_a=sum_a+K_error[i,j]
    print sum_a

    # K = project_kernel_haar_phi(n)
    # K_error=smrt_error(n)
    # saveit(n,K,"haar_scale_K_mat_dist_1")
    # saveit(n,K_error,"haar_scale_K_error_mat_dist_1")
    # K_rec=readit(n,"haar_scale_K_mat_dist_1")
    # K_error_rec=readit(n,"haar_scale_K_error_mat_dist_1")

    # num_k=0
    # for i in range(n):
    #     for j in range(n):
    #         num_k=num_k+abs(K_error[i,j]-K_error_rec[i,j])
    # print num_k

