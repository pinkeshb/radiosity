from kernel_haar_phi import *
from mpmath import *
from wavedecs import *
n=4
K_original = project_kernel_haar_phi(n)
n=256
fname = str(n) + 'haar_scale_K_mat_dist_0.25' + ".txt"
fo = open(fname, "r")
# fo.write(str(n) + "\n")
n=fo.readline()
n=int(n)
# print n
K = matrix(n,n)
for i in range(n):
    line=fo.readline()
    # print line
    line = line.split()
    # print line[0]
    print i
    for j in range(n):

        K[i,j]=float(line[j])
        # print float(line[j])
    # fo.write("\n")
K1=dwt2_inside(K)
K2=dwt2_inside(K1[0:128,0:128])
K3=dwt2_inside(K2[0:64,0:64])
K4=dwt2_inside(K3[0:32,0:32])
K5=dwt2_inside(K4[0:16,0:16])
K6=dwt2_inside(K5[0:16,0:16])
print "K",K6
print "K_original",K_original
n=4
num_k=0
for i in range(n):
    for j in range(n):
        num_k=num_k+abs(K6[i,j]-K_original[i,j])
print num_k