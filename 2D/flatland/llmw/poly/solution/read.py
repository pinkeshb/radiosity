from kernel_m2_phi import *
from mpmath import *
from wavedecs import *
n=4
K_original = project_kernel_m2_phi(n)
n=n*2
fname = str(n) + 'haar_scale_K_mat' + ".txt"
fo = open(fname, "r")
# fo.write(str(n) + "\n")
n=fo.readline()
n=int(n)
# print n
K = matrix(n*2,n*2)
for i in range(n):
    line=fo.readline()
    line = line.split()
    for j in range(n):
        K[i,j]=float(line[j])
        # print float(line[j])
    # fo.write("\n")
K=dwt2_inside(K)
print "K",K
print "K_original",K_original
n=n/2
num_k=0
for i in range(n*2):
    for j in range(n*2):
        num_k=num_k+abs(K[i,j]-K_original[i,j])
print num_k