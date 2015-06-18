from kernel_m3_phi import *

n_min,n_max=2,3

fname = 'wavelet_all_error_div_2*n' + ".txt"
fo = open(fname, "w")
dist=0.25
for n_log in range(n_min,n_max):
    n=pow(2,n_log)
    top_n=3*n*3*n
    K,K_error = project_kernel_m3_phi(n,dist)
    # print "K_thres_error = ", K_thres_error, "\n"
    # fo.write("K_thres_error = "+str(K_thres_error) + "\n")

    num_k=0
    for i in range(n):
        for j in range(n):
            num_k=num_k+K_error[i,j]



    print "n = ", n, "\n"
    fo.write("n = "+str(n) + "\n")
    print "top_n = ", top_n, "\n"
    fo.write("top_n = "+str(top_n) + "\n")

    print "error_k = ", num_k, "\n"
    fo.write("error_k = "+str(num_k) + "\n")


    print "\n\n\n"
