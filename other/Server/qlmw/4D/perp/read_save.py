from kernel_m3_phi import *
from mpmath import *
def readit(n,dist):
    fname = str(n) + 'm3_scale_K_mat_dist_'+str(dist) + ".txt"
    K_rec=[[[[1 for x in range(3*n)] for x in range(3*n)] for x in range(3*n)] for x in range(3*n)] 
    fo = open(fname,'r')
    n=int(fo.readline().split()[0])
    # print n
    for i in range(3*n):
        for j in range(3*n):
            for k in range(3*n):
                for l in range(3*n):
                    line=fo.readline()
                    # print line,"line"
                    line=line.split()
                    # print line
                    # print i*3*n*3*n*3*n+j*3*n*3*n+k*3*n+l
                    # print i
                    # print i
                    num=float(line[0])
                    K_rec[i][j][k][l]=num
    return K_rec
def saveit(n,dist):
    K = project_kernel_m3_phi(n,dist)

    fname = str(n) + 'm3_scale_K_mat_dist_'+str(dist) + ".txt"
    fo = open(fname, "w")
    fo.write(str(n) + "\n")
    for i in range(3*n):
        for j in range(3*n):
            for k in range(3*n):
                for l in range(3*n):
                    fo.write(str(K[i][j][k][l]) + "\n")
                    # print K[i][j][k][l]
    # fo.write("end" + "\n")
    fo.close()
    return K
if __name__=="__main__":

    n=4
    dist=1
    K=saveit(n,dist)
    K_rec=readit(n,dist)
    # print K_rec
    # print len(K_rec)
    n=n*3
    for i in range(n):
        print i
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if (abs(K[i][j][k][l] - K_rec[i][j][k][l]) > 0.000000001):

                        print i*n*n*n+j*n*n+k*n+l
                        print K[i][j][k][l] - K_rec[i][j][k][l]