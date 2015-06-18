from kernel_m2_phi import *
from mpmath import *


def saveit(n,K,name):
    fname = str(n) + name + ".txt"
    fo = open(fname, "w")
    fo.write(str(n) + "\n")
    # K = project_kernel_haar_phi(n)
    for i in range(K.cols):
        for j in range(K.cols):
            fo.write(str(float(K[i,j]))+"\t\t")
        fo.write("\n")
    fo.close()
def readit(n,name):
    fname = str(n) + name+ ".txt"
    fo = open(fname, "r")
    # fo.write(str(n) + "\n")
    n=fo.readline()
    n=int(n)*2
    K = matrix(n,n)
    for i in range(n):
        line=fo.readline()
        # print line
        line = line.split()
        # print line[0]
        print i
        for j in range(n):

            K[i,j]=float(line[j])
    fo.close()
    return K

if __name__=="__main__":
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
