from kernel_haar_phi import *
from mpmath import *
def readit(n):
    fname = str(n) + 'haar_scale_K_mat' + ".txt"
    K_rec=[[[[1 for x in range(n)] for x in range(n)] for x in range(n)] for x in range(n)] 
    fo = open(fname,'r')
    n=int(fo.readline().split()[0])
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    line=fo.readline()
                    # print line,"line"
                    line=line.split()
                    # print line
                    num=float(line[0])
                    K_rec[i][j][k][l]=num
                    # print i*n*n*n+j*n*n+k*n+l
    return K_rec
def saveit(n):
    K = project_kernel_haar_phi(n)

    fname = str(n) + 'haar_scale_K_mat' + ".txt"
    fo = open(fname, "w")
    fo.write(str(n) + "\n")
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    fo.write(str(K[i][j][k][l]) + "\n")
                    # print K[i][j][k][l]
    fo.write("end" + "\n")
    fo.close()
    return K
if __name__=="__main__":

    n=8
    K=saveit(n)
    K_rec=readit(n)
    # print K_rec

    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if (abs(K[i][j][k][l] - K_rec[i][j][k][l]) > 0.000000001):
                        print i*n*n*n+j*n*n+k*n+l
                        print K[i][j][k][l] - K_rec[i][j][k][l]