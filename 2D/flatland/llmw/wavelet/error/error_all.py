from kernel_m2_phi import *

n_min,n_max=3,4
dist=0.25
fname = 'wavelet_all_error_dist'+str(dist) + ".txt"
fo = open(fname, "w")

for n_log in range(n_min,n_max):
    n=pow(2,n_log)
    top_n=2*n*2*n
    K,K_dwt,K_dwt_thres,K_thres,K_thres_error = project_kernel_m2_phi(n,top_n,dist)
    # print "K_thres_error = ", K_thres_error, "\n"
    # fo.write("K_thres_error = "+str(K_thres_error) + "\n")
    print K_thres_error
    num_k=0
    for i in range(n):
        for j in range(n):
            num_k=num_k+K_thres_error[i,j]



    print "n = ", n, "\n"
    fo.write("n = "+str(n) + "\n")
    print "top_n = ", top_n, "\n"
    fo.write("top_n = "+str(top_n) + "\n")

    print "error_k = ", num_k, "\n"
    fo.write("error_k = "+str(num_k) + "\n")

    print K
    print "\n\n\n"
