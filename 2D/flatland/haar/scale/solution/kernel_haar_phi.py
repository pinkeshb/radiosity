from mpmath import *


def project_kernel_haar_phi(n):
    # kernel
    f1 = lambda s, t: 0.25 / (4*pow(((s - t) * (s - t) + 0.25), 1.5))
    f = lambda s, t: f1(s, t) * pow(n, 0.5) * pow(n, 0.5)

    K = matrix(n, n)
    for i in range(0, n):
        for j in range(0, n):
            K[i, j] = quad(
                f, [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)])
            print[
                i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)]

    return K