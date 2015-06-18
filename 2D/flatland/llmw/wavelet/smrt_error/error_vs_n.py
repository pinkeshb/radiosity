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


n2=64
dist = 0.0625


fname = 'haar_scale_all_error' +str(dist)+ ".txt"
fo = open(fname, "w")


for n in [4,8,16,32,64]:
    # n=4
    
    K=readit(n,"haar_scale_K_mat_dist_"+str(dist))

    # print K.cols, K.rows




    # n2=8

    K_4_8=matrix(n2*2,n2*2)
    K_4_8[0:n*2,0:n*2]=K
    K4_8_idwt=K_4_8
    nc=n2
    while nc!=n:
        K4_8_idwt=idwt2_inside(K4_8_idwt)
        nc=nc/2
    # print K4_8_idwt.cols, K4_8_idwt.rows
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

    print "n = ", n, "\n"
    fo.write("n = "+str(n) + "\n")

    print "error_k = ", num_k, "\n"
    fo.write("error_k = "+str(num_k) + "\n")
