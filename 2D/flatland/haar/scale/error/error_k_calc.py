from kernel_haar_phi import *
from wavedecs import *
fname = 'haar_scale_all_error' + ".txt"
fo = open(fname, "w")
K_4_8=matrix(8,8)
# print K_4_8
K4,K4_error=project_kernel_haar_phi(4)
K8,K8_error=project_kernel_haar_phi(8)
K_4_8[0:4,0:4]=K4_error
# print K_4_8
K4_idwt=idwt2_inside(K_4_8)
print K4_idwt
print K8_error
# print "K4_error",K4
# print "K4_dwt_error",K4_dwt


