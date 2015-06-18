from kernel_haar_phi import *
from mpmath import *
import sys
from read_save import *
from wavedecs import *
def thres_it(K, top_n):
    L = []
    # K = []
    n = len(K)
    if top_n==n*n*n*n:
        return K
    print "n",n
    # K_dwt_thres = matrix(n, n)
    K_thres=[[[[1 for x in range(n)] for x in range(n)] for x in range(n)] for x in range(n)] 
    # K = K_dwt.tolist()
    print n
    for i in range(n):
        for j in range(n):
            for k in range(n):
                L.extend(K[i][j][k][:])
    print len(L)
    for i in range(len(L)):
        L[i] = abs(L[i])
    L.sort()
    L.reverse()
    # print L
    # print top_n
    thresh = L[top_n - 1]
    print thresh
    start = L.index(thresh)
    alowed = top_n - start
    print start
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if abs(K[i][j][k][l]) > thresh:
                        K_thres[i][j][k][l] = K[i][j][k][l]
                    elif abs(K[i][j][k][l]) == thresh and alowed > 0:
                        alowed = alowed - 1
                        K_thres[i][j][k][l]= K[i][j][k][l]
                    else:
                        K_thres[i][j][k][l] = 0
    return K_thres
def copyit(B1_pre,B1,n):
    # print "inside copyit"
    # print B1_pre
    # print B1
    for i in range(n):
        for j in range(n):
            B1_pre[i][j]=B1[i][j]
    # print B1_pre
    # print B1
    # print "inside copyit"
def iterit(B,E,K,B_pre,n):
    # print "E",E
    # print "B",B
    # print "K",K
    # print "B_pre",B_pre
    for i in range(n):
        for j in range(n):
            sum=0
            for i1 in range(n):
                for j1 in range(n):
                    # print "sum",sum
                    sum=sum+B_pre[i1][j1]*K[i][j][i1][j1]
            # print "B[i][j]",B[i][j]
            # print "E[i][j]",E[i][j]
            B[i][j]=E[i][j]+sum
    # print "E",E
    # print "B",B
    # print "K",K
    # print "B_pre",B_pre
def main_fn(n, thres,dist,top_n):
    fname = str(n) + 'haar_scale' + ".txt"
    fo = open(fname, "w")

    # K = project_kernel_haar_phi(n)
    # K=readit(n,dist)
    K_1=readit(n,dist)
    K_dwt_thres=thres_it(dwt4(K_1,n), top_n)

    K=idwt4(K_dwt_thres,n)
    # K=K_1
    # print "K",K
    E1 = [[1 for x in range(n)] for x in range(n)] 
    for i in range(n):
        for j in range(n):
            if i>=3*n/4 or j>=3*n/4 or i<n/4 or j<n/4:
                E1[i][j]=0
    # E1[3 * n / 4:n][3 * n / 4:n] =(([[1]*n/4]*n/4)/ pow(n, 0.5)
    # E2 = matrix([[0] * n]).transpose()
    E2 = [[0 for x in range(n)] for x in range(n)] 

    B1 = [[0 for x in range(n)] for x in range(n)] 
    B2 = [[0 for x in range(n)] for x in range(n)] 
    B1_pre = [[1 for x in range(n)] for x in range(n)] 
    B2_pre = [[1 for x in range(n)] for x in range(n)] 

    # print "K=", K
    # print "E1=", E1
    # print "E2=", E2
    fo.write("n=" + str(n) + "\n")
    fo.write("K=" + str(K) + "\n")
    fo.write("E1=" + str(E1) + "\n")
    fo.write("E2=" + str(E2) + "\n")
    fo.write("interation begines\n\n")
    # B1_pre = B1 + 1
    # B2_pre = B2 + 1

    iter = 0
    converged = False

    # print "B1  " + str(iter) + "=", B1
    fo.write("B1  " + str(iter) + "=" + str(B1) + "\n\n")
    # print "B2  " + str(iter) + "=", B2
    fo.write("B2  " + str(iter) + "=" + str(B2) + "\n\n")
    # while(not (diag(B1)*B1-diag(B1_pre)*B1_pre == zeros(n,1) or
    # diag(B2)*B2-diag(B2_pre)*B2_pre == zeros(n,1))):
    while (not converged):
        # solve
        iter += 1

        copyit(B1_pre,B1,n)
        copyit(B2_pre,B2,n)
        # B1 = E1 + K * B2_pre
        iterit(B1,E1,K,B2_pre,n)
        # B2 = E2 + K * B1_pre
        iterit(B2,E2,K,B1_pre,n)
        # print "B1  " + str(iter) + "=", B1
        fo.write("B1  " + str(iter) + "=" + str(B1) + "\n\n")
        # print "B2  " + str(iter) + "=", B2
        fo.write("B2  " + str(iter) + "=" + str(B2) + "\n\n")
        # if int(input("Please enter an integer: "))==1:
        if iter==10:
          converged=True
        else:
          converged=False
        # print diag(B1)*B1-diag(B1_pre)*B1_pre
        # print diag(B2)*B2-diag(B2_pre)*B2_pre
        # change_energy = 0
        # for i in range(n):
        #     change_energy = change_energy + \
        #         (B1[i] - B1_pre[i]) * (B1[i] - B1_pre[i]) + \
        #         (B2[i] - B2_pre[i]) * (B2[i] - B2_pre[i])
        # if change_energy < thres:
        #     converged = True
    # print "final"
    # print "\n\n\nB1  " + str(iter) + "=", B1 * pow(n, 0.5)
    # # fo.write("\n\n\nB1  " + str(iter) + "=" + str(B1 * pow(n, 0.5)))
    # print "\n\n\nB2  " + str(iter) + "=", B2 * pow(n, 0.5)
    # fo.write("\n\n\nB2  " + str(iter) + "=" + str(B2 * pow(n, 0.5)))
    # B1_proj = B1 * pow(n, 0.5)
    # B2_proj = B2 * pow(n, 0.5)
    # return B1_proj, B2_proj, K
    return B1, B2
if __name__ == "__main__":
    n=2
    dist=0.25
    top_n=n*n*n
    K_1=readit(n,dist)
    # print len(K_1)
    K=idwt4(dwt4(K_1,n),n)
    # K=idwt4(thres(dwt4(K_1,n), top_n),n)
    print len(K)
    K=thres(K, top_n)
    print K
    print K_1

    # thres = 0.001
    # n=4
    # B1, B2= main_fn(n, thres,0.25)
    # for i in range(n):
    #     for j in range(n):
    #         print B1[i][j],"\t",
    #     print "\n"
    # for i in range(n):
    #     for j in range(n):
    #         print B2[i][j],"\t",
    #     print "\n"
    # E1 = [[0]*n]*n
    # E1 = [[0 for x in range(2)] for x in range(2)] 
    # E2 = [[0 for x in range(2)] for x in range(2)] 
    # copyit(E2,E1)
    # E2[0][0]=10
    # print E1
    # # c=0
    # print E1
    # for i in range(n):
    #     for j in range(n):
    #         # E1[i][j]=c
            # print (i,j)
    #         # c+=1
    #         if i>=3*n/4 and j>=3*n/4:
    #             E1[i][j]=1.0/n
    # # E1[0][0]=1
    # # E1[0][1]=2
    # # E1[1][0]=3
    # # E1[1][1]=4
    # print E1
    # E1[3 * n / 4:n][3 * n / 4:n] =([[1]*(n/4)]*(n/4))
