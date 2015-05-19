from kernel_m2_phi import *
from mpmath import *
n=4
dist=0.25
fname = str(n) + 'haar_scale_K_mat_dist_'+str(dist) + ".txt"
fo = open(fname, "w")
fo.write(str(n) + "\n")
K = project_kernel_m2_phi(n,dist)
for i in range(K.cols):
    for j in range(K.cols):
        fo.write(str(float(K[i,j]))+"\t\t")
    fo.write("\n")
