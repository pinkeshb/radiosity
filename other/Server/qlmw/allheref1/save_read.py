from kernel_m3_phi import *
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
    n=int(n)*3
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
    n=8
    dist = 0.5
    # K=readit(n,"qlmw_K_mat_dist_"+str(dist))
    K,K_error_original=project_kernel_m3_phi(n,dist)
    a_2_mat,b_2_mat,c_2_mat,d_2_mat,e_2_mat,f_2_mat,g_2_mat,h_2_mat,i_2_mat,j_2_mat,ab2_mat,ac2_mat,ad2_mat,ae2_mat,af2_mat,ag2_mat,ah2_mat,ai2_mat,aj2_mat,bc2_mat,bd2_mat,be2_mat,bf2_mat,bg2_mat,bh2_mat,bi2_mat,bj2_mat,cd2_mat,ce2_mat,cf2_mat,cg2_mat,ch2_mat,ci2_mat,cj2_mat,de2_mat,df2_mat,dg2_mat,dh2_mat,di2_mat,dj2_mat,ef2_mat,eg2_mat,eh2_mat,ei2_mat,ej2_mat,fg2_mat,fh2_mat,fi2_mat,fj2_mat,gh2_mat,gi2_mat,gj2_mat,hi2_mat,hj2_mat,ij2_mat=smrt_error(n,dist)
    # saveit(n,a_2_mat,"m3_scale_a_2_mat_dist_"+str(dist))
    # saveit(n,b_2_mat,"m3_scale_b_2_mat_dist_"+str(dist))
    # saveit(n,c_2_mat,"m3_scale_c_2_mat_dist_"+str(dist))
    # saveit(n,d_2_mat,"m3_scale_d_2_mat_dist_"+str(dist))
    # saveit(n,e_2_mat,"m3_scale_e_2_mat_dist_"+str(dist))
    # saveit(n,f_2_mat,"m3_scale_f_2_mat_dist_"+str(dist))
    # saveit(n,g_2_mat,"m3_scale_g_2_mat_dist_"+str(dist))
    # saveit(n,h_2_mat,"m3_scale_h_2_mat_dist_"+str(dist))
    # saveit(n,i_2_mat,"m3_scale_i_2_mat_dist_"+str(dist))
    # saveit(n,j_2_mat,"m3_scale_j_2_mat_dist_"+str(dist))
    # saveit(n,ab2_mat,"m3_scale_ab2_mat_dist_"+str(dist))
    # saveit(n,ac2_mat,"m3_scale_ac2_mat_dist_"+str(dist))
    # saveit(n,ad2_mat,"m3_scale_ad2_mat_dist_"+str(dist))
    # saveit(n,ae2_mat,"m3_scale_ae2_mat_dist_"+str(dist))
    # saveit(n,af2_mat,"m3_scale_af2_mat_dist_"+str(dist))
    # saveit(n,ag2_mat,"m3_scale_ag2_mat_dist_"+str(dist))
    # saveit(n,ah2_mat,"m3_scale_ah2_mat_dist_"+str(dist))
    # saveit(n,ai2_mat,"m3_scale_ai2_mat_dist_"+str(dist))
    # saveit(n,aj2_mat,"m3_scale_aj2_mat_dist_"+str(dist))
    # saveit(n,bc2_mat,"m3_scale_bc2_mat_dist_"+str(dist))
    # saveit(n,bd2_mat,"m3_scale_bd2_mat_dist_"+str(dist))
    # saveit(n,be2_mat,"m3_scale_be2_mat_dist_"+str(dist))
    # saveit(n,bf2_mat,"m3_scale_bf2_mat_dist_"+str(dist))
    # saveit(n,bg2_mat,"m3_scale_bg2_mat_dist_"+str(dist))
    # saveit(n,bh2_mat,"m3_scale_bh2_mat_dist_"+str(dist))
    # saveit(n,bi2_mat,"m3_scale_bi2_mat_dist_"+str(dist))
    # saveit(n,bj2_mat,"m3_scale_bj2_mat_dist_"+str(dist))
    # saveit(n,cd2_mat,"m3_scale_cd2_mat_dist_"+str(dist))
    # saveit(n,ce2_mat,"m3_scale_ce2_mat_dist_"+str(dist))
    # saveit(n,cf2_mat,"m3_scale_cf2_mat_dist_"+str(dist))
    # saveit(n,cg2_mat,"m3_scale_cg2_mat_dist_"+str(dist))
    # saveit(n,ch2_mat,"m3_scale_ch2_mat_dist_"+str(dist))
    # saveit(n,ci2_mat,"m3_scale_ci2_mat_dist_"+str(dist))
    # saveit(n,cj2_mat,"m3_scale_cj2_mat_dist_"+str(dist))
    # saveit(n,de2_mat,"m3_scale_de2_mat_dist_"+str(dist))
    # saveit(n,df2_mat,"m3_scale_df2_mat_dist_"+str(dist))
    # saveit(n,dg2_mat,"m3_scale_dg2_mat_dist_"+str(dist))
    # saveit(n,dh2_mat,"m3_scale_dh2_mat_dist_"+str(dist))
    # saveit(n,di2_mat,"m3_scale_di2_mat_dist_"+str(dist))
    # saveit(n,dj2_mat,"m3_scale_dj2_mat_dist_"+str(dist))
    # saveit(n,ef2_mat,"m3_scale_ef2_mat_dist_"+str(dist))
    # saveit(n,eg2_mat,"m3_scale_eg2_mat_dist_"+str(dist))
    # saveit(n,eh2_mat,"m3_scale_eh2_mat_dist_"+str(dist))
    # saveit(n,ei2_mat,"m3_scale_ei2_mat_dist_"+str(dist))
    # saveit(n,ej2_mat,"m3_scale_ej2_mat_dist_"+str(dist))
    # saveit(n,fg2_mat,"m3_scale_fg2_mat_dist_"+str(dist))
    # saveit(n,fh2_mat,"m3_scale_fh2_mat_dist_"+str(dist))
    # saveit(n,fi2_mat,"m3_scale_fi2_mat_dist_"+str(dist))
    # saveit(n,fj2_mat,"m3_scale_fj2_mat_dist_"+str(dist))
    # saveit(n,gh2_mat,"m3_scale_gh2_mat_dist_"+str(dist))
    # saveit(n,gi2_mat,"m3_scale_gi2_mat_dist_"+str(dist))
    # saveit(n,gj2_mat,"m3_scale_gj2_mat_dist_"+str(dist))
    # saveit(n,hi2_mat,"m3_scale_hi2_mat_dist_"+str(dist))
    # saveit(n,hj2_mat,"m3_scale_hj2_mat_dist_"+str(dist))
    # saveit(n,ij2_mat,"m3_scale_ij2_mat_dist_"+str(dist))
    # # K=
    print K
    K_error=matrix(n,n)
    num_k=0
    for i in range(n):
        for j in range(n):
            K_error[i,j]=a_2_mat[i,j]+\
            +b_2_mat[i,j]*K[3*i+0,3*j+0]*K[3*i+0,3*j+0]+\
            +c_2_mat[i,j]*K[3*i+0,3*j+1]*K[3*i+0,3*j+1]+\
            +d_2_mat[i,j]*K[3*i+0,3*j+2]*K[3*i+0,3*j+2]+\
            +e_2_mat[i,j]*K[3*i+1,3*j+0]*K[3*i+1,3*j+0]+\
            +f_2_mat[i,j]*K[3*i+1,3*j+1]*K[3*i+1,3*j+1]+\
            +g_2_mat[i,j]*K[3*i+1,3*j+2]*K[3*i+1,3*j+2]+\
            +h_2_mat[i,j]*K[3*i+2,3*j+0]*K[3*i+2,3*j+0]+\
            +i_2_mat[i,j]*K[3*i+2,3*j+1]*K[3*i+2,3*j+1]+\
            +j_2_mat[i,j]*K[3*i+2,3*j+2]*K[3*i+2,3*j+2]+\
            -ab2_mat[i,j]*K[3*i+0,3*j+0]+\
            -ac2_mat[i,j]*K[3*i+0,3*j+1]+\
            -ad2_mat[i,j]*K[3*i+0,3*j+2]+\
            -ae2_mat[i,j]*K[3*i+1,3*j+0]+\
            -af2_mat[i,j]*K[3*i+1,3*j+1]+\
            -ag2_mat[i,j]*K[3*i+1,3*j+2]+\
            -ah2_mat[i,j]*K[3*i+2,3*j+0]+\
            -ai2_mat[i,j]*K[3*i+2,3*j+1]+\
            -aj2_mat[i,j]*K[3*i+2,3*j+2]+\
            +bc2_mat[i,j]*K[3*i+0,3*j+0]*K[3*i+0,3*j+1]+\
            +bd2_mat[i,j]*K[3*i+0,3*j+0]*K[3*i+0,3*j+2]+\
            +be2_mat[i,j]*K[3*i+0,3*j+0]*K[3*i+1,3*j+0]+\
            +bf2_mat[i,j]*K[3*i+0,3*j+0]*K[3*i+1,3*j+1]+\
            +bg2_mat[i,j]*K[3*i+0,3*j+0]*K[3*i+1,3*j+2]+\
            +bh2_mat[i,j]*K[3*i+0,3*j+0]*K[3*i+2,3*j+0]+\
            +bi2_mat[i,j]*K[3*i+0,3*j+0]*K[3*i+2,3*j+1]+\
            +bj2_mat[i,j]*K[3*i+0,3*j+0]*K[3*i+2,3*j+2]+\
            +cd2_mat[i,j]*K[3*i+0,3*j+1]*K[3*i+0,3*j+2]+\
            +ce2_mat[i,j]*K[3*i+0,3*j+1]*K[3*i+1,3*j+0]+\
            +cf2_mat[i,j]*K[3*i+0,3*j+1]*K[3*i+1,3*j+1]+\
            +cg2_mat[i,j]*K[3*i+0,3*j+1]*K[3*i+1,3*j+2]+\
            +ch2_mat[i,j]*K[3*i+0,3*j+1]*K[3*i+2,3*j+0]+\
            +ci2_mat[i,j]*K[3*i+0,3*j+1]*K[3*i+2,3*j+1]+\
            +cj2_mat[i,j]*K[3*i+0,3*j+1]*K[3*i+2,3*j+2]+\
            +de2_mat[i,j]*K[3*i+0,3*j+2]*K[3*i+1,3*j+0]+\
            +df2_mat[i,j]*K[3*i+0,3*j+2]*K[3*i+1,3*j+1]+\
            +dg2_mat[i,j]*K[3*i+0,3*j+2]*K[3*i+1,3*j+2]+\
            +dh2_mat[i,j]*K[3*i+0,3*j+2]*K[3*i+2,3*j+0]+\
            +di2_mat[i,j]*K[3*i+0,3*j+2]*K[3*i+2,3*j+1]+\
            +dj2_mat[i,j]*K[3*i+0,3*j+2]*K[3*i+2,3*j+2]+\
            +ef2_mat[i,j]*K[3*i+1,3*j+0]*K[3*i+1,3*j+1]+\
            +eg2_mat[i,j]*K[3*i+1,3*j+0]*K[3*i+1,3*j+2]+\
            +eh2_mat[i,j]*K[3*i+1,3*j+0]*K[3*i+2,3*j+0]+\
            +ei2_mat[i,j]*K[3*i+1,3*j+0]*K[3*i+2,3*j+1]+\
            +ej2_mat[i,j]*K[3*i+1,3*j+0]*K[3*i+2,3*j+2]+\
            +fg2_mat[i,j]*K[3*i+1,3*j+1]*K[3*i+1,3*j+2]+\
            +fh2_mat[i,j]*K[3*i+1,3*j+1]*K[3*i+2,3*j+0]+\
            +fi2_mat[i,j]*K[3*i+1,3*j+1]*K[3*i+2,3*j+1]+\
            +fj2_mat[i,j]*K[3*i+1,3*j+1]*K[3*i+2,3*j+2]+\
            +gh2_mat[i,j]*K[3*i+1,3*j+2]*K[3*i+2,3*j+0]+\
            +gi2_mat[i,j]*K[3*i+1,3*j+2]*K[3*i+2,3*j+1]+\
            +gj2_mat[i,j]*K[3*i+1,3*j+2]*K[3*i+2,3*j+2]+\
            +hi2_mat[i,j]*K[3*i+2,3*j+0]*K[3*i+2,3*j+1]+\
            +hj2_mat[i,j]*K[3*i+2,3*j+0]*K[3*i+2,3*j+2]+\
            +ij2_mat[i,j]*K[3*i+2,3*j+2]*K[3*i+2,3*j+2]
            num_k=num_k+K_error[i,j]
    print "error",num_k
    print "K_errorsmt",K_error
    print "K_error_original",K_error_original
    sum_a=0
    for i in range(n):
        for j in range(n):
            sum_a=sum_a+a_2_mat[i,j]
    print "rel=",sum_a

    # K = project_kernel_haar_phi(n)
    # K_error=smrt_error(n)
    # saveit(n,K,"haar_scale_K_mat_dist_1")
    # saveit(n,K_error,"haar_scale_K_error_mat_dist_1")
    # K_rec=readit(n,"haar_scale_K_mat_dist_1")
    # K_error_rec=readit(n,"haar_scale_K_error_mat_dist_1")

    num_k=0
    for i in range(n):
        for j in range(n):
            num_k=num_k+abs(K_error[i,j]-K_error_original[i,j])
    print num_k

