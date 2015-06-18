from kernel_m3_phi import *
from mpmath import *
import sys



def main_fn(n, thres):
    fname=str(n)+'haar_scale'+".txt"
    fo = open(fname, "w")


    K=project_kernel_m3_phi(n)
    E=matrix([[0]*n*3]).transpose()
    for i in range(n*3):
        if i%3==0:
            E[i]=1.0/pow(n,0.5)
    B=zeros(3*n,1)
    B_pre=zeros(3*n,1)


    print "K=", K
    print "E=", E
    fo.write("n="+str(n)+"\n")
    fo.write("K="+str(K)+"\n")
    fo.write("E="+str(E)+"\n")
    B_pre=B+1

    iter = 0
    converged = False

    while(not converged):
        iter+=1
        # print diag(B)*B-diag(B_pre)*B_pre
        # print "B"+str(iter)+"=", B        
        print "B  " + str(iter) + "=", B
        fo.write("B  " + str(iter) + "=" + str(B) + "\n\n")
        B_pre=B
        B=E+K*B_pre

        # if int(input("Please enter an integer: "))==1:
        #     check=True
        # else:
        #     check=False
        change_energy = 0
        for i in range(3*n):
          change_energy = change_energy + \
              (B[i] - B_pre[i]) * (B[i] - B_pre[i])
        if change_energy < thres:
          converged = True
    print "final"

    print "\n\n\nB"+str(iter)+"=", B
    fo.write("\n\n\nB"+str(iter)+"="+str(B))
    return B
if __name__ == "__main__":
    thres = 0.001
    print main_fn(4, thres)
