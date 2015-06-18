from kernel_haar_phi import *
from mpmath import *
import sys
from read_save import *
# from wavedecs import *
def copyit(B_pre,B,n):
    # print "inside copyit"
    # print B_pre
    # print B
    for i in range(n):
        for j in range(n):
            B_pre[i][j]=B[i][j]
    # print B_pre
    # print B
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
def main_fn(n, thres,dist):
    fname = str(n) + 'haar_scale' + ".txt"
    fo = open(fname, "w")

    K = project_kernel_haar_phi(n,dist)
    # K=readit(n,dist)
    # print "K",K
    E = [[1.0 / n for x in range(n)] for x in range(n)] 
    # for i in range(n):
        # for j in range(n):
            # if i>=3*n/4 or j>=3*n/4 or i<n/4 or j<n/4:
            # if i>=3*n/4 or j>=3*n/4 or i<n/4 or j<n/4:
                # E[i][j]=0
    # E[3 * n / 4:n][3 * n / 4:n] =(([[1]*n/4]*n/4)/ pow(n, 0.5)
    # E2 = matrix([[0] * n]).transpose()
    # E2 = [[0 for x in range(n)] for x in range(n)] 

    B = [[0 for x in range(n)] for x in range(n)] 
    # B2 = [[0 for x in range(n)] for x in range(n)] 
    B_pre = [[1 for x in range(n)] for x in range(n)] 
    # B2_pre = [[1 for x in range(n)] for x in range(n)] 

    # print "K=", K
    # print "E=", E
    # print "E2=", E2
    fo.write("n=" + str(n) + "\n")
    fo.write("K=" + str(K) + "\n")
    fo.write("E=" + str(E) + "\n")
    # fo.write("E2=" + str(E2) + "\n")
    fo.write("interation begines\n\n")
    # B_pre = B + 1
    # B2_pre = B2 + 1

    iter = 0
    converged = False

    # print "B  " + str(iter) + "=", B
    fo.write("B  " + str(iter) + "=" + str(B) + "\n\n")
    # print "B2  " + str(iter) + "=", B2
    # fo.write("B2  " + str(iter) + "=" + str(B2) + "\n\n")
    # while(not (diag(B)*B-diag(B_pre)*B_pre == zeros(n,1) or
    # diag(B2)*B2-diag(B2_pre)*B2_pre == zeros(n,1))):
    while (not converged):
        # solve
        iter += 1

        copyit(B_pre,B,n)
        # copyit(B2_pre,B2,n)
        # B = E + K * B_pre
        # iterit(B,E,K,B2_pre,n)
        # B2 = E2 + K * B_pre
        iterit(B,E,K,B_pre,n)
        # print "B  " + str(iter) + "=", B
        fo.write("B  " + str(iter) + "=" + str(B) + "\n\n")
        # print "B2  " + str(iter) + "=", B2
        # fo.write("B2  " + str(iter) + "=" + str(B2) + "\n\n")
        # if int(input("Please enter an integer: "))==1:
        if iter==50:
          converged=True
        else:
          converged=False
        # print diag(B)*B-diag(B_pre)*B_pre
        # print diag(B2)*B2-diag(B2_pre)*B2_pre
        # change_energy = 0
        # for i in range(n):
        #     change_energy = change_energy + \
        #         (B[i] - B_pre[i]) * (B[i] - B_pre[i]) + \
                # (B2[i] - B2_pre[i]) * (B2[i] - B2_pre[i])
        # if change_energy < thres:
        #     converged = True
    # print "final"
    # print "\n\n\nB  " + str(iter) + "=", B * pow(n, 0.5)
    # # fo.write("\n\n\nB  " + str(iter) + "=" + str(B * pow(n, 0.5)))
    # print "\n\n\nB2  " + str(iter) + "=", B2 * pow(n, 0.5)
    # fo.write("\n\n\nB2  " + str(iter) + "=" + str(B2 * pow(n, 0.5)))
    # B_proj = B * pow(n, 0.5)
    # B2_proj = B2 * pow(n, 0.5)
    return B, K
    # return B, B2
if __name__ == "__main__":
    thres = 0.001
    n=4
    B,K= main_fn(n, thres,1)
    for i in range(n):
        for j in range(n):
            print B[i][j],"\t",
        print "\n"
    # for i in range(n):
        # for j in range(n):
            # print B2[i][j],"\t",
        # print "\n"
    # E = [[0]*n]*n
    # E = [[0 for x in range(2)] for x in range(2)] 
    # E2 = [[0 for x in range(2)] for x in range(2)] 
    # copyit(E2,E)
    # E2[0][0]=10
    # print E
    # # c=0
    # print E
    # for i in range(n):
    #     for j in range(n):
    #         # E[i][j]=c
            # print (i,j)
    #         # c+=1
    #         if i>=3*n/4 and j>=3*n/4:
    #             E[i][j]=1.0/n
    # # E[0][0]=1
    # # E[0][1]=2
    # # E[1][0]=3
    # # E[1][1]=4
    # print E
    # E[3 * n / 4:n][3 * n / 4:n] =([[1]*(n/4)]*(n/4))
