# from kernel_haar_phi import *
# from save_read import *
# from s_error import *
# from wavedecs import *
# K_f,K_fp,K_p=smrt_error(8)
# K=readit(8,"haar_scale_K_mat_dist_1")
# K8_error_smt=matrix(8,8)
# for i in range(K.cols):
#     for j in range(K.cols):
#         K8_error_smt[i,j]=K_f[i,j]-K[i,j]*K_fp[i,j]+K[i,j]*K[i,j]*K_p[i,j]
# # K = project_kernel_haar_phi(n)
# # K_error=smrt_error(n)saveit(n,K,"haar_scale_K_mat_dist_1")
# # saveit(n,K_error,"haar_scale_K_error_mat_dist_1")
# # K_rec=readit(n,"haar_scale_K_mat_dist_1")
# K4_error=readit(4,"haar_scale_K_error_mat_dist_1")
# K8_error=readit(8,"haar_scale_K_error_mat_dist_1")
# num_k=0
# for i in range(8):
#     for j in range(8):
#         num_k=num_k+abs(K8_error_smt[i,j])
# print num_k
# # K_4_8=matrix(8,8)
# # K_4_8[0:4,0:4]=K4_error
# # K4_idwt=idwt2_inside(K_4_8)

from kernel_haar_phi import *
from save_read import *
from s_error import *
from wavedecs import *
dist=1
K_f,K_fp,K_p=readit(256,"haar_scale_K_f_mat_dist_"+str(dist)),readit(256,"haar_scale_K_fp_mat_dist_"+str(dist)),readit(256,"haar_scale_K_p_mat_dist_"+str(dist))

# 256=256
fname = 'haar_scale_all_error'+str(dist) + ".txt"
fo = open(fname, "w")

# K_f,K_fp,K_p=smrt_error(256,1)
for n in [4,8,16,32,64,128,256]:


    # n=8
    K4=readit(n,"haar_scale_K_mat_dist_"+str(dist))

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
    print "n = ", n, "\n"
    fo.write("n = "+str(n) + "\n")

    print "error_k = ", num_k, "\n"
    fo.write("error_k = "+str(num_k) + "\n")

# from kernel_haar_phi import *
# from save_read import *
# from s_error import *
# from wavedecs import *
# K_f,K_fp,K_p=smrt_error(8)
# K=readit(8,"haar_scale_K_mat_dist_1")
# K8_error_smt=matrix(8,8)
# for i in range(K.cols):
#     for j in range(K.cols):
#         K8_error_smt[i,j]=K_f[i,j]-K[i,j]*K_fp[i,j]+K[i,j]*K[i,j]*K_p[i,j]
# # K = project_kernel_haar_phi(n)
# # K_error=smrt_error(n)saveit(n,K,"haar_scale_K_mat_dist_1")
# # saveit(n,K_error,"haar_scale_K_error_mat_dist_1")
# # K_rec=readit(n,"haar_scale_K_mat_dist_1")
# K4_error=readit(4,"haar_scale_K_error_mat_dist_1")
# K8_error=readit(8,"haar_scale_K_error_mat_dist_1")
# num_k=0
# for i in range(8):
#     for j in range(8):
#         num_k=num_k+abs(K8_error_smt[i,j])
# print num_k
# # K_4_8=matrix(8,8)
# # K_4_8[0:4,0:4]=K4_error
# # K4_idwt=idwt2_inside(K_4_8)

# # from kernel_haar_phi import *
# # from save_read import *
# # from s_error import *
# # from wavedecs import *
# # dist=0.5
# # n1=256
# # # K_f,K_fp,K_p=smrt_error(n1,1)

# # K_f,K_fp,K_p=readit(n1,"haar_scale_K_f_mat_dist_"+str(dist)),readit(n1,"haar_scale_K_fp_mat_dist_"+str(dist)),readit(n1,"haar_scale_K_p_mat_dist_"+str(dist))


# # n2=4
# # K4=readit(n2,"haar_scale_K_mat_dist_"+str(dist))

# K_4_8=matrix(n1,n1)
# K_4_8[0:n2,0:n2]=K4
# K4_8_idwt=idwt2_inside(idwt2_inside(idwt2_inside(idwt2_inside(idwt2_inside(K_4_8)))))
# # print K4_8_idwt


# K8_error_smt=matrix(n1,n1)
# for i in range(n1):
#     for j in range(n1):
#         K8_error_smt[i,j]=K_f[i,j]-K4_8_idwt[i,j]*K_fp[i,j]+K4_8_idwt[i,j]*K4_8_idwt[i,j]*K_p[i,j]
# # K = project_kernel_haar_phi(n)
# # K_error=smrt_error(n)saveit(n,K,"haar_scale_K_mat_dist_1")
# # saveit(n,K_error,"haar_scale_K_error_mat_dist_1")
# # K_rec=readit(n,"haar_scale_K_mat_dist_1")
# # K4_error=readit(4,"haar_scale_K_error_mat_dist_1")
# # K8_error=readit(8,"haar_scale_K_error_mat_dist_1")

# num_k=0
# for i in range(n1):
#     for j in range(n1):
#         num_k=num_k+K8_error_smt[i,j]
# print num_k