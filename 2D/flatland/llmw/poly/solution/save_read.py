from kernel_m2_phi import *
from mpmath import *
n=8
fname = str(n) + 'haar_scale_K_mat' + ".txt"
fo = open(fname, "w")
fo.write(str(n) + "\n")
K = project_kernel_m2_phi(n)
for i in range(K.cols):
    for j in range(K.cols):
        fo.write(str(float(K[i,j]))+"\t\t")
    fo.write("\n")
