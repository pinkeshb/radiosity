from kernel_m2_phi import *
from mpmath import *
import sys

def main_fn(n, thres):
    fname=str(n)+'haar_scale'+".txt"
    fo = open(fname, "w")

    K=project_kernel_m2_phi(n)
    E=matrix([[1.0/pow(n,0.5)]*n*2]).transpose()
    for i in range(n*2):
        if i%2==1:
            E[i]=0
    B=zeros(2*n,1)
    B_pre=zeros(2*n,1)

    
    print "K=", K
    print "E=", E
    fo.write("n="+str(n)+"\n")
    fo.write("K="+str(K)+"\n")
    fo.write("E="+str(E)+"\n")
    B_pre=B+1
    iter = 0
    converged = False

    print "B  " + str(iter) + "=", B
    fo.write("B  " + str(iter) + "=" + str(B) + "\n\n")

    while(not converged):
        iter+=1
        B_pre=B
        B=E+K*B_pre
        print "B  " + str(iter) + "=", B
        fo.write("B  " + str(iter) + "=" + str(B) + "\n\n")
        # if int(input("Please enter an integer: "))==1:
        #     check=True
        # else:
        #     check=False
        change_energy = 0
        for i in range(2*n):
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
