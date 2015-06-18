# # from kernel_haar_phi import *
# # from save_read import *
# # from s_error import *
# # from wavedecs import *
# # K_f,K_fp,K_p=smrt_error(8)
# # K=readit(8,"haar_scale_K_mat_dist_1")
# # K8_error_smt=matrix(8,8)
# # for i in range(K.cols):
# #     for j in range(K.cols):
# #         K8_error_smt[i,j]=K_f[i,j]-K[i,j]*K_fp[i,j]+K[i,j]*K[i,j]*K_p[i,j]
# # # K = project_kernel_haar_phi(n)
# # # K_error=smrt_error(n)saveit(n,K,"haar_scale_K_mat_dist_1")
# # # saveit(n,K_error,"haar_scale_K_error_mat_dist_1")
# # # K_rec=readit(n,"haar_scale_K_mat_dist_1")
# # K4_error=readit(4,"haar_scale_K_error_mat_dist_1")
# # K8_error=readit(8,"haar_scale_K_error_mat_dist_1")
# # num_k=0
# # for i in range(8):
# #     for j in range(8):
# #         num_k=num_k+abs(K8_error_smt[i,j])
# # print num_k
# # # K_4_8=matrix(8,8)
# # # K_4_8[0:4,0:4]=K4_error
# # # K4_idwt=idwt2_inside(K_4_8)

# from kernel_haar_phi import *
# from save_read import *
# from s_error import *
# from wavedecs import *
# dist=1
# # 256=256
# fname = 'haar_scale_all_error'+str(dist) + ".txt"
# fo = open(fname, "w")
# K_f,K_fp,K_p=readit(256,"haar_scale_K_f_mat_dist_"+str(dist)),readit(256,"haar_scale_K_fp_mat_dist_"+str(dist)),readit(256,"haar_scale_K_p_mat_dist_"+str(dist))

# # K_f,K_fp,K_p=smrt_error(256,1)
# for n in [4,8,16,32,64,128,256]:


#     # n=8
#     K4=readit(n,"haar_scale_K_mat_dist_"+str(dist))

#     K_4_8=matrix(256,256)
#     K_4_8[0:n,0:n]=K4
#     nc=256
#     K4_8_idwt=K_4_8
#     while nc!=n:
#         print "f"
#         K4_8_idwt=idwt2_inside(K4_8_idwt)
#         nc=nc/2
#         # K4_8_idwt=idwt2_inside(idwt2_inside(idwt2_inside(idwt2_inside(idwt2_inside(K_4_8)))))
#     # print K4_8_idwt


#     K8_error_smt=matrix(256,256)
#     for i in range(256):
#         for j in range(256):
#             K8_error_smt[i,j]=K_f[i,j]-K4_8_idwt[i,j]*K_fp[i,j]+K4_8_idwt[i,j]*K4_8_idwt[i,j]*K_p[i,j]
#     # K = project_kernel_haar_phi(n)
#     # K_error=smrt_error(n)saveit(n,K,"haar_scale_K_mat_dist_1")
#     # saveit(n,K_error,"haar_scale_K_error_mat_dist_1")
#     # K_rec=readit(n,"haar_scale_K_mat_dist_1")
#     # K4_error=readit(4,"haar_scale_K_error_mat_dist_1")
#     # K8_error=readit(8,"haar_scale_K_error_mat_dist_1")

#     num_k=0
#     for i in range(256):
#         for j in range(256):
#             num_k=num_k+K8_error_smt[i,j]
#     print num_k
#     print "n = ", n, "\n"
#     fo.write("n = "+str(n) + "\n")

#     print "error_k = ", num_k, "\n"
#     fo.write("error_k = "+str(num_k) + "\n")

# # from kernel_haar_phi import *
# # from save_read import *
# # from s_error import *
# # from wavedecs import *
# # K_f,K_fp,K_p=smrt_error(8)
# # K=readit(8,"haar_scale_K_mat_dist_1")
# # K8_error_smt=matrix(8,8)
# # for i in range(K.cols):
# #     for j in range(K.cols):
# #         K8_error_smt[i,j]=K_f[i,j]-K[i,j]*K_fp[i,j]+K[i,j]*K[i,j]*K_p[i,j]
# # # K = project_kernel_haar_phi(n)
# # # K_error=smrt_error(n)saveit(n,K,"haar_scale_K_mat_dist_1")
# # # saveit(n,K_error,"haar_scale_K_error_mat_dist_1")
# # # K_rec=readit(n,"haar_scale_K_mat_dist_1")
# # K4_error=readit(4,"haar_scale_K_error_mat_dist_1")
# # K8_error=readit(8,"haar_scale_K_error_mat_dist_1")
# # num_k=0
# # for i in range(8):
# #     for j in range(8):
# #         num_k=num_k+abs(K8_error_smt[i,j])
# # print num_k
# # # K_4_8=matrix(8,8)
# # # K_4_8[0:4,0:4]=K4_error
# # # K4_idwt=idwt2_inside(K_4_8)

# # # from kernel_haar_phi import *
# # # from save_read import *
# # # from s_error import *
# # # from wavedecs import *
# # # dist=0.5
# # # n1=256
# # # # K_f,K_fp,K_p=smrt_error(n1,1)

# # # K_f,K_fp,K_p=readit(n1,"haar_scale_K_f_mat_dist_"+str(dist)),readit(n1,"haar_scale_K_fp_mat_dist_"+str(dist)),readit(n1,"haar_scale_K_p_mat_dist_"+str(dist))


# # # n2=4
# # # K4=readit(n2,"haar_scale_K_mat_dist_"+str(dist))

# # K_4_8=matrix(n1,n1)
# # K_4_8[0:n2,0:n2]=K4
# # K4_8_idwt=idwt2_inside(idwt2_inside(idwt2_inside(idwt2_inside(idwt2_inside(K_4_8)))))
# # # print K4_8_idwt


# # K8_error_smt=matrix(n1,n1)
# # for i in range(n1):
# #     for j in range(n1):
# #         K8_error_smt[i,j]=K_f[i,j]-K4_8_idwt[i,j]*K_fp[i,j]+K4_8_idwt[i,j]*K4_8_idwt[i,j]*K_p[i,j]
# # # K = project_kernel_haar_phi(n)
# # # K_error=smrt_error(n)saveit(n,K,"haar_scale_K_mat_dist_1")
# # # saveit(n,K_error,"haar_scale_K_error_mat_dist_1")
# # # K_rec=readit(n,"haar_scale_K_mat_dist_1")
# # # K4_error=readit(4,"haar_scale_K_error_mat_dist_1")
# # # K8_error=readit(8,"haar_scale_K_error_mat_dist_1")

# # num_k=0
# # for i in range(n1):
# #     for j in range(n1):
# #         num_k=num_k+K8_error_smt[i,j]
# # print num_k

from save_read import *
from wavedecs import *

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


n2=16
dist = 0.25


fname = 'haar_scale_all_error' +str(dist)+ ".txt"
fo = open(fname, "w")
a_2_mat=readiterror(n2,"m3_scale_a_2_mat_dist_"+str(dist))
b_2_mat=readiterror(n2,"m3_scale_b_2_mat_dist_"+str(dist))
c_2_mat=readiterror(n2,"m3_scale_c_2_mat_dist_"+str(dist))
d_2_mat=readiterror(n2,"m3_scale_d_2_mat_dist_"+str(dist))
e_2_mat=readiterror(n2,"m3_scale_e_2_mat_dist_"+str(dist))
f_2_mat=readiterror(n2,"m3_scale_f_2_mat_dist_"+str(dist))
g_2_mat=readiterror(n2,"m3_scale_g_2_mat_dist_"+str(dist))
h_2_mat=readiterror(n2,"m3_scale_h_2_mat_dist_"+str(dist))
i_2_mat=readiterror(n2,"m3_scale_i_2_mat_dist_"+str(dist))
j_2_mat=readiterror(n2,"m3_scale_j_2_mat_dist_"+str(dist))
ab2_mat=readiterror(n2,"m3_scale_ab2_mat_dist_"+str(dist))
ac2_mat=readiterror(n2,"m3_scale_ac2_mat_dist_"+str(dist))
ad2_mat=readiterror(n2,"m3_scale_ad2_mat_dist_"+str(dist))
ae2_mat=readiterror(n2,"m3_scale_ae2_mat_dist_"+str(dist))
af2_mat=readiterror(n2,"m3_scale_af2_mat_dist_"+str(dist))
ag2_mat=readiterror(n2,"m3_scale_ag2_mat_dist_"+str(dist))
ah2_mat=readiterror(n2,"m3_scale_ah2_mat_dist_"+str(dist))
ai2_mat=readiterror(n2,"m3_scale_ai2_mat_dist_"+str(dist))
aj2_mat=readiterror(n2,"m3_scale_aj2_mat_dist_"+str(dist))
bc2_mat=readiterror(n2,"m3_scale_bc2_mat_dist_"+str(dist))
bd2_mat=readiterror(n2,"m3_scale_bd2_mat_dist_"+str(dist))
be2_mat=readiterror(n2,"m3_scale_be2_mat_dist_"+str(dist))
bf2_mat=readiterror(n2,"m3_scale_bf2_mat_dist_"+str(dist))
bg2_mat=readiterror(n2,"m3_scale_bg2_mat_dist_"+str(dist))
bh2_mat=readiterror(n2,"m3_scale_bh2_mat_dist_"+str(dist))
bi2_mat=readiterror(n2,"m3_scale_bi2_mat_dist_"+str(dist))
bj2_mat=readiterror(n2,"m3_scale_bj2_mat_dist_"+str(dist))
cd2_mat=readiterror(n2,"m3_scale_cd2_mat_dist_"+str(dist))
ce2_mat=readiterror(n2,"m3_scale_ce2_mat_dist_"+str(dist))
cf2_mat=readiterror(n2,"m3_scale_cf2_mat_dist_"+str(dist))
cg2_mat=readiterror(n2,"m3_scale_cg2_mat_dist_"+str(dist))
ch2_mat=readiterror(n2,"m3_scale_ch2_mat_dist_"+str(dist))
ci2_mat=readiterror(n2,"m3_scale_ci2_mat_dist_"+str(dist))
cj2_mat=readiterror(n2,"m3_scale_cj2_mat_dist_"+str(dist))
de2_mat=readiterror(n2,"m3_scale_de2_mat_dist_"+str(dist))
df2_mat=readiterror(n2,"m3_scale_df2_mat_dist_"+str(dist))
dg2_mat=readiterror(n2,"m3_scale_dg2_mat_dist_"+str(dist))
dh2_mat=readiterror(n2,"m3_scale_dh2_mat_dist_"+str(dist))
di2_mat=readiterror(n2,"m3_scale_di2_mat_dist_"+str(dist))
dj2_mat=readiterror(n2,"m3_scale_dj2_mat_dist_"+str(dist))
ef2_mat=readiterror(n2,"m3_scale_ef2_mat_dist_"+str(dist))
eg2_mat=readiterror(n2,"m3_scale_eg2_mat_dist_"+str(dist))
eh2_mat=readiterror(n2,"m3_scale_eh2_mat_dist_"+str(dist))
ei2_mat=readiterror(n2,"m3_scale_ei2_mat_dist_"+str(dist))
ej2_mat=readiterror(n2,"m3_scale_ej2_mat_dist_"+str(dist))
fg2_mat=readiterror(n2,"m3_scale_fg2_mat_dist_"+str(dist))
fh2_mat=readiterror(n2,"m3_scale_fh2_mat_dist_"+str(dist))
fi2_mat=readiterror(n2,"m3_scale_fi2_mat_dist_"+str(dist))
fj2_mat=readiterror(n2,"m3_scale_fj2_mat_dist_"+str(dist))
gh2_mat=readiterror(n2,"m3_scale_gh2_mat_dist_"+str(dist))
gi2_mat=readiterror(n2,"m3_scale_gi2_mat_dist_"+str(dist))
gj2_mat=readiterror(n2,"m3_scale_gj2_mat_dist_"+str(dist))
hi2_mat=readiterror(n2,"m3_scale_hi2_mat_dist_"+str(dist))
hj2_mat=readiterror(n2,"m3_scale_hj2_mat_dist_"+str(dist))
ij2_mat=readiterror(n2,"m3_scale_ij2_mat_dist_"+str(dist))


for n in [16]:
    # n=4
    
    K=readit(n,"qlmw_K_mat_dist_"+str(dist))
    # K=idwt2(dwt2(K))

    # print K.cols, K.rows




    # n2=8

    K_4_8=matrix(n2*3,n2*3)
    K_4_8[0:n*3,0:n*3]=K
    # K4_8_idwt=idwt2_inside(K_4_8)
    # nc=n2
    # while nc!=n:
    #     K4_8_idwt=idwt2_inside(K4_8_idwt)
    #     nc=nc/2
    # print K4_8_idwt.cols, K4_8_idwt.rows
    # print ce2_mat.cols, ce2_mat.rows
    # de2_mat=readiterror(n2,"m2_scale_de2_mat_dist_"+str(dist))
    # print K
    K_error=matrix(n2,n2)
    num_k=0
    for i in range(n2):
        for j in range(n2):
            K_error[i,j]=a_2_mat[i,j]+\
            +b_2_mat[i,j]*K_4_8[3*i+0,3*j+0]*K_4_8[3*i+0,3*j+0]+\
            +c_2_mat[i,j]*K_4_8[3*i+0,3*j+1]*K_4_8[3*i+0,3*j+1]+\
            +d_2_mat[i,j]*K_4_8[3*i+0,3*j+2]*K_4_8[3*i+0,3*j+2]+\
            +e_2_mat[i,j]*K_4_8[3*i+1,3*j+0]*K_4_8[3*i+1,3*j+0]+\
            +f_2_mat[i,j]*K_4_8[3*i+1,3*j+1]*K_4_8[3*i+1,3*j+1]+\
            +g_2_mat[i,j]*K_4_8[3*i+1,3*j+2]*K_4_8[3*i+1,3*j+2]+\
            +h_2_mat[i,j]*K_4_8[3*i+2,3*j+0]*K_4_8[3*i+2,3*j+0]+\
            +i_2_mat[i,j]*K_4_8[3*i+2,3*j+1]*K_4_8[3*i+2,3*j+1]+\
            +j_2_mat[i,j]*K_4_8[3*i+2,3*j+2]*K_4_8[3*i+2,3*j+2]+\
            -ab2_mat[i,j]*K_4_8[3*i+0,3*j+0]+\
            -ac2_mat[i,j]*K_4_8[3*i+0,3*j+1]+\
            -ad2_mat[i,j]*K_4_8[3*i+0,3*j+2]+\
            -ae2_mat[i,j]*K_4_8[3*i+1,3*j+0]+\
            -af2_mat[i,j]*K_4_8[3*i+1,3*j+1]+\
            -ag2_mat[i,j]*K_4_8[3*i+1,3*j+2]+\
            -ah2_mat[i,j]*K_4_8[3*i+2,3*j+0]+\
            -ai2_mat[i,j]*K_4_8[3*i+2,3*j+1]+\
            -aj2_mat[i,j]*K_4_8[3*i+2,3*j+2]+\
            +bc2_mat[i,j]*K_4_8[3*i+0,3*j+0]*K_4_8[3*i+0,3*j+1]+\
            +bd2_mat[i,j]*K_4_8[3*i+0,3*j+0]*K_4_8[3*i+0,3*j+2]+\
            +be2_mat[i,j]*K_4_8[3*i+0,3*j+0]*K_4_8[3*i+1,3*j+0]+\
            +bf2_mat[i,j]*K_4_8[3*i+0,3*j+0]*K_4_8[3*i+1,3*j+1]+\
            +bg2_mat[i,j]*K_4_8[3*i+0,3*j+0]*K_4_8[3*i+1,3*j+2]+\
            +bh2_mat[i,j]*K_4_8[3*i+0,3*j+0]*K_4_8[3*i+2,3*j+0]+\
            +bi2_mat[i,j]*K_4_8[3*i+0,3*j+0]*K_4_8[3*i+2,3*j+1]+\
            +bj2_mat[i,j]*K_4_8[3*i+0,3*j+0]*K_4_8[3*i+2,3*j+2]+\
            +cd2_mat[i,j]*K_4_8[3*i+0,3*j+1]*K_4_8[3*i+0,3*j+2]+\
            +ce2_mat[i,j]*K_4_8[3*i+0,3*j+1]*K_4_8[3*i+1,3*j+0]+\
            +cf2_mat[i,j]*K_4_8[3*i+0,3*j+1]*K_4_8[3*i+1,3*j+1]+\
            +cg2_mat[i,j]*K_4_8[3*i+0,3*j+1]*K_4_8[3*i+1,3*j+2]+\
            +ch2_mat[i,j]*K_4_8[3*i+0,3*j+1]*K_4_8[3*i+2,3*j+0]+\
            +ci2_mat[i,j]*K_4_8[3*i+0,3*j+1]*K_4_8[3*i+2,3*j+1]+\
            +cj2_mat[i,j]*K_4_8[3*i+0,3*j+1]*K_4_8[3*i+2,3*j+2]+\
            +de2_mat[i,j]*K_4_8[3*i+0,3*j+2]*K_4_8[3*i+1,3*j+0]+\
            +df2_mat[i,j]*K_4_8[3*i+0,3*j+2]*K_4_8[3*i+1,3*j+1]+\
            +dg2_mat[i,j]*K_4_8[3*i+0,3*j+2]*K_4_8[3*i+1,3*j+2]+\
            +dh2_mat[i,j]*K_4_8[3*i+0,3*j+2]*K_4_8[3*i+2,3*j+0]+\
            +di2_mat[i,j]*K_4_8[3*i+0,3*j+2]*K_4_8[3*i+2,3*j+1]+\
            +dj2_mat[i,j]*K_4_8[3*i+0,3*j+2]*K_4_8[3*i+2,3*j+2]+\
            +ef2_mat[i,j]*K_4_8[3*i+1,3*j+0]*K_4_8[3*i+1,3*j+1]+\
            +eg2_mat[i,j]*K_4_8[3*i+1,3*j+0]*K_4_8[3*i+1,3*j+2]+\
            +eh2_mat[i,j]*K_4_8[3*i+1,3*j+0]*K_4_8[3*i+2,3*j+0]+\
            +ei2_mat[i,j]*K_4_8[3*i+1,3*j+0]*K_4_8[3*i+2,3*j+1]+\
            +ej2_mat[i,j]*K_4_8[3*i+1,3*j+0]*K_4_8[3*i+2,3*j+2]+\
            +fg2_mat[i,j]*K_4_8[3*i+1,3*j+1]*K_4_8[3*i+1,3*j+2]+\
            +fh2_mat[i,j]*K_4_8[3*i+1,3*j+1]*K_4_8[3*i+2,3*j+0]+\
            +fi2_mat[i,j]*K_4_8[3*i+1,3*j+1]*K_4_8[3*i+2,3*j+1]+\
            +fj2_mat[i,j]*K_4_8[3*i+1,3*j+1]*K_4_8[3*i+2,3*j+2]+\
            +gh2_mat[i,j]*K_4_8[3*i+1,3*j+2]*K_4_8[3*i+2,3*j+0]+\
            +gi2_mat[i,j]*K_4_8[3*i+1,3*j+2]*K_4_8[3*i+2,3*j+1]+\
            +gj2_mat[i,j]*K_4_8[3*i+1,3*j+2]*K_4_8[3*i+2,3*j+2]+\
            +hi2_mat[i,j]*K_4_8[3*i+2,3*j+0]*K_4_8[3*i+2,3*j+1]+\
            +hj2_mat[i,j]*K_4_8[3*i+2,3*j+0]*K_4_8[3*i+2,3*j+2]+\
            +ij2_mat[i,j]*K_4_8[3*i+2,3*j+2]*K_4_8[3*i+2,3*j+2]
    # print num_k
    print K_error
    num_k=0
    for i in range(n2):
        for j in range(n2):
            num_k=num_k+K_error[i,j]
    print num_k

    print "n = ", n, "\n"
    fo.write("n = "+str(n) + "\n")

    print "error_k = ", num_k, "\n"
    fo.write("error_k = "+str(num_k) + "\n")
