from kernel_m2_phi import *
from mpmath import *
from m2_phi import *
import sys
def B_Error(B,n):
	b = lambda s:66.0/23.0*s*s+42.0/23.0*s+1
	print n
	B_error=zeros(n,1)
	a=1.0/n
	for i in range(n):
		print i,"afdjahdf"
		b_error=lambda s:(b(s)-B[2*i]*dia_trans(s, a, i  / float(n), phi_1_m2)-B[2*i+1]*dia_trans(s, a, i  / float(n), phi_2_m2))*\
						(b(s)-B[2*i]*dia_trans(s, a, i/ float(n), phi_1_m2)-B[2*i+1]*dia_trans(s, a, i/ float(n), phi_2_m2))
		B_error[i]=quad(b_error,[i / float(n), (i + 1) / float(n)])
		print B_error[i]

		print i,"afdjahdf"
	return B_error
def main_fn(n, thres):
    fname=str(n)+'haar_scale'+".txt"
    fo = open(fname, "w")
    K,K_error=project_kernel_m2_phi(n)
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
    B_error=B_Error(B,n)
    print "B_error",B_error
    fo.write("\n\n\nB_error"+str(iter)+"="+str(B_error))
    return B,B_error,K,K_error
if __name__ == "__main__":
    thres = 0.001
    print main_fn(4, thres)
