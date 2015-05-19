from kernel_m3_phi import *
from mpmath import *
n=4
fname = str(n) + 'qlmw_K_mat_dist_1' + ".txt"
fo = open(fname, "w")
fo.write(str(n) + "\n")
K = project_kernel_m3_phi(n)
for i in range(K.cols):
    for j in range(K.cols):
        fo.write(str(float(K[i,j]))+"\t\t")
    fo.write("\n")
