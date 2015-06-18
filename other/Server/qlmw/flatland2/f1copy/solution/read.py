from kernel_m3_phi import *
from mpmath import *
n=4
K_original = project_kernel_m3_phi(n)

fname = str(n) + 'qlmw_K_mat_dist_1' + ".txt"
fo = open(fname, "r")
# fo.write(str(n) + "\n")
n=fo.readline()
n=int(n)
print n
K = matrix(n*3,n*3)
for i in range(n*3):
    line=fo.readline()
    line = line.split()
    for j in range(n*3):
        K[i,j]=float(line[j])
        # print float(line[j])
    # fo.write("\n")
print K
numk=0
for i in  range(n*3):
    for j in range(n*3):
        numk=numk+abs(K[i,j]-K_original[i,j])
print numk