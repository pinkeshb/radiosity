from mpmath import *


def project_kernel_haar_phi(n):
    # kernel
    f1 = lambda s, t: (s+0.1)*(t+0.1)/ (2*pow(((s+0.1)*(s+0.1) +(t+0.1)*(t+0.1)), 1.5))
    f = lambda s, t: f1(s, t) * pow(n, 0.5) * pow(n, 0.5)

    K = matrix(n, n)
    for i in range(0, n):
	print i/float(n)*100, "percent"
        for j in range(0, n):
            K[i, j] = quad(
                f, [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)],method='gauss-legendre')
            print[
                i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)]

    return K

print project_kernel_haar_phi(8)
