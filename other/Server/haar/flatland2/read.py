# from kernel_haar_phi import *
from mpmath import *
n=8
fname = str(n) + 'haar_scale_K_mat' + ".txt"
fo = open(fname, "r")
# fo.write(str(n) + "\n")
n=fo.readline()
n=int(n)
print n
K = matrix(n,n)
for i in range(n):
    line=fo.readline()
    line = line.split()
    for j in range(n):
        K[i,j]=float(line[j])
        # print float(line[j])
    # fo.write("\n")
print K