from mpmath import *


def project_kernel_haar_phi(n):
    # kernel
    f1 = lambda s, t: s - t
    f = lambda s, t: f1(s, t) * pow(n, 0.5) * pow(n, 0.5)

    K = matrix(n, n)
    for i in range(0, n):
        for j in range(0, n):
            K[i, j] = quad(
                f, [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)])
            print[
                i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)]

    K_error = matrix(n, n)
    for i in range(0, n):
        for j in range(0, n):
        	f_error = lambda s, t: (f1(s, t) - K[i, j] * pow(n, 0.5) * pow(n, 0.5))*\
        							(f1(s, t) - K[i, j] * pow(n, 0.5) * pow(n, 0.5))
        	K_error[i, j] = quad(f_error, [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)])

    return K,K_error
