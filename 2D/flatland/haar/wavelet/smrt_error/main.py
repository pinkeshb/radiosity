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
K_f,K_fp,K_p=smrt_error(16)
K4=project_kernel_haar_phi(4)

K_4_8=matrix(16,16)
K_4_8[0:4,0:4]=K4
K4_8_idwt=idwt2_inside(idwt2_inside(K_4_8))
print K4_8_idwt


K8_error_smt=matrix(16,16)
for i in range(16):
    for j in range(16):
        K8_error_smt[i,j]=K_f[i,j]-K4_8_idwt[i,j]*K_fp[i,j]+K4_8_idwt[i,j]*K4_8_idwt[i,j]*K_p[i,j]
# K = project_kernel_haar_phi(n)
# K_error=smrt_error(n)saveit(n,K,"haar_scale_K_mat_dist_1")
# saveit(n,K_error,"haar_scale_K_error_mat_dist_1")
# K_rec=readit(n,"haar_scale_K_mat_dist_1")
# K4_error=readit(4,"haar_scale_K_error_mat_dist_1")
# K8_error=readit(8,"haar_scale_K_error_mat_dist_1")

num_k=0
for i in range(16):
    for j in range(16):
        num_k=num_k+K8_error_smt[i,j]
print num_k