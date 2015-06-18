from mpmath import *
from kernel_haar_phi import *
n=8
dist=0.125
fname = str(n) + 'haar_scale_K_mat_dist_'+str(dist) + ".txt"
fo = open(fname, "r")
n=fo.readline()
n=int(n)
K = matrix(n,n)
for i in range(n):
    line=fo.readline()
    # print line
    line = line.split()
    # print line[0]
    print i
    for j in range(n):

        K[i,j]=float(line[j])
K_o=project_kernel_haar_phi(n)
for i in range(n):
    for j in range(n):
        if (K[i,j]-K_o[i,j])>0.0000001:
            print "diff"
        else: 
            print "s",