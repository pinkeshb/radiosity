# from kernel_m2_phi import *
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

if __name__=="__main__":
    n=128
    # K=readit(n,"haar_scale_K_mat")
    # K=project_kernel_m2_phi(n)
    a_2_mat,b_2_mat,c_2_mat,d_2_mat,e_2_mat,ab2_mat,cd2_mat,ac2_mat,ad2_mat,bc2_mat,bd2_mat,ae2_mat,be2_mat,ce2_mat,de2_mat=smrt_error(n)
    saveit(n,a_2_mat,"haar_scale_a_2_mat")
    saveit(n,a_2_mat,"m2_scale_a_2_mat")
    saveit(n,b_2_mat,"m2_scale_b_2_mat")
    saveit(n,c_2_mat,"m2_scale_c_2_mat")
    saveit(n,d_2_mat,"m2_scale_d_2_mat")
    saveit(n,e_2_mat,"m2_scale_e_2_mat")
    saveit(n,ab2_mat,"m2_scale_ab2_mat")
    saveit(n,cd2_mat,"m2_scale_cd2_mat")
    saveit(n,ac2_mat,"m2_scale_ac2_mat")
    saveit(n,ad2_mat,"m2_scale_ad2_mat")
    saveit(n,bc2_mat,"m2_scale_bc2_mat")
    saveit(n,bd2_mat,"m2_scale_bd2_mat")
    saveit(n,ae2_mat,"m2_scale_ae2_mat")
    saveit(n,be2_mat,"m2_scale_be2_mat")
    saveit(n,ce2_mat,"m2_scale_ce2_mat")
    saveit(n,de2_mat,"m2_scale_de2_mat")
    # # K=
    # print K
    K_error=matrix(n,n)
    # num_k=0
    # for i in range(n):
    #     for j in range(n):
    #         K_error[i,j]=a_2_mat[i,j]+\
    #         +b_2_mat[i,j]*K[2*i+0,2*j+0]*K[2*i+0,2*j+0]+\
    #         +c_2_mat[i,j]*K[2*i+0,2*j+1]*K[2*i+0,2*j+1]+\
    #         +d_2_mat[i,j]*K[2*i+1,2*j+0]*K[2*i+1,2*j+0]+\
    #         +e_2_mat[i,j]*K[2*i+1,2*j+1]*K[2*i+1,2*j+1]+\
    #         -ab2_mat[i,j]*K[2*i+0,2*j+0]+\
    #         +cd2_mat[i,j]*K[2*i+0,2*j+1]*K[2*i+1,2*j+0]+\
    #         -ac2_mat[i,j]*K[2*i+0,2*j+1]+\
    #         -ad2_mat[i,j]*K[2*i+1,2*j+0]+\
    #         +bc2_mat[i,j]*K[2*i+0,2*j+0]*K[2*i+0,2*j+1]+\
    #         +bd2_mat[i,j]*K[2*i+0,2*j+0]*K[2*i+1,2*j+0]+\
    #         -ae2_mat[i,j]*K[2*i+1,2*j+1]+\
    #         +be2_mat[i,j]*K[2*i+0,2*j+0]*K[2*i+1,2*j+1]+\
    #         +ce2_mat[i,j]*K[2*i+0,2*j+1]*K[2*i+1,2*j+1]+\
    #         +de2_mat[i,j]*K[2*i+1,2*j+0]*K[2*i+1,2*j+1]
    # print num_k
    # print K_error
    sum_a=0
    for i in range(n):
        for j in range(n):
            sum_a=sum_a+a_2_mat[i,j]
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
