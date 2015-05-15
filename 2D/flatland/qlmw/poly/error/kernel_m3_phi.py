from mpmath import *
from m3_phi import *
from matplotlib import pyplot
def project_kernel_m3_phi(n):
  # kernel
  dist=0.25
  f1 = lambda s, t: dist*dist/ (2*pow(((s - t) * (s - t) + dist*dist), 1.5))
  # basis
  # amplitude=pow(n,0.5)
  # f2 = lambda s: amplitude
  # f3 = lambda s: amplitude
  # integrand
  # f = lambda s,t: f1(s,t)*f2(s)*f3(t)
  # f = lambda s,t: f1(s,t)*f3(t)*f2(s)
  # m=linspace(0,1,250)
  a=1.0/n
  K=matrix(n*3,n*3)
  for i in range(0,n*3):
    for j in range(0,n*3):
      if i%3==0 and j%3==0:
        print 00
        f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/3)/float(n),phi_0_m3)*dia_trans(t,a,(j/3)/float(n),phi_0_m3)
      if i%3==0 and j%3==1:
        print 01
        f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/3)/float(n),phi_0_m3)*dia_trans(t,a,(j/3)/float(n),phi_1_m3)
      if i%3==0 and j%3==2:
        print 02
        f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/3)/float(n),phi_0_m3)*dia_trans(t,a,(j/3)/float(n),phi_2_m3)
      if i%3==1 and j%3==0:
        print 10
        f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/3)/float(n),phi_1_m3)*dia_trans(t,a,(j/3)/float(n),phi_0_m3)
      if i%3==1 and j%3==1:
        print 11
        f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/3)/float(n),phi_1_m3)*dia_trans(t,a,(j/3)/float(n),phi_1_m3)
      if i%3==1 and j%3==2:
        print 12
        f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/3)/float(n),phi_1_m3)*dia_trans(t,a,(j/3)/float(n),phi_2_m3)
      if i%3==2 and j%3==0:
        print 20
        f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/3)/float(n),phi_2_m3)*dia_trans(t,a,(j/3)/float(n),phi_0_m3)
      if i%3==2 and j%3==1:
        print 21
        f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/3)/float(n),phi_2_m3)*dia_trans(t,a,(j/3)/float(n),phi_1_m3)
      if i%3==2 and j%3==2:
        print 22
        f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/3)/float(n),phi_2_m3)*dia_trans(t,a,(j/3)/float(n),phi_2_m3)
        # y=[dia_trans(z,a,(i/3)/float(n),phi_1_m3) for z in m]
        # pyplot.plot(m,y)
        # # print y ,"y"
        # pyplot.show()

      # print f
      K[i,j]=quad(f,[(i/3)/float(n),((i/3)+1)/float(n)],[(j/3)/float(n),((j/3)+1)/float(n)],method='gauss-legendre')
      print [(i/3)/float(n),((i/3)+1)/float(n)],[(j/3)/float(n),((j/3)+1)/float(n)]
      # if abs(K[i,j])<=0.0000000001:
      #   K[i,j]=0
      # K[i,j]=i*j
  K_error =matrix(n,n)
  for i in range(0, n):
      for j in range(0, n):
          f_error = lambda s, t: (f1(s, t) - K[3*i, 3*j] * dia_trans(s, a, (i) / float(n),
                                            phi_0_m3) * dia_trans(t, a, (j) / float(n), phi_0_m3)
                                              - K[3*i, 3*j+1] * dia_trans(s, a, (i) / float(n),
                                            phi_0_m3) * dia_trans(t, a, (j) / float(n), phi_1_m3)
                                              - K[3*i, 3*j+2] * dia_trans(s, a, (i) / float(n),
                                            phi_0_m3) * dia_trans(t, a, (j) / float(n), phi_2_m3)
                                              - K[3*i+1, 3*j+0] * dia_trans(s, a, (i) / float(n),
                                            phi_1_m3) * dia_trans(t, a, (j) / float(n), phi_0_m3)
                                              - K[3*i+1, 3*j+1] * dia_trans(s, a, (i) / float(n),
                                            phi_1_m3) * dia_trans(t, a, (j) / float(n), phi_1_m3)
                                              - K[3*i+1, 3*j+2] * dia_trans(s, a, (i) / float(n),
                                            phi_1_m3) * dia_trans(t, a, (j) / float(n), phi_2_m3)
                                              - K[3*i+2, 3*j] * dia_trans(s, a, (i) / float(n),
                                            phi_2_m3) * dia_trans(t, a, (j) / float(n), phi_0_m3)
                                              - K[3*i+2, 3*j+1] * dia_trans(s, a, (i) / float(n),
                                            phi_2_m3) * dia_trans(t, a, (j) / float(n), phi_1_m3)
                                              - K[3*i+2, 3*j+2] * dia_trans(s, a, (i) / float(n),
                                            phi_2_m3) * dia_trans(t, a, (j) / float(n), phi_2_m3))*\
                                  (f1(s, t) - K[3*i, 3*j] * dia_trans(s, a, (i) / float(n),
                                            phi_0_m3) * dia_trans(t, a, (j) / float(n), phi_0_m3)
                                              - K[3*i, 3*j+1] * dia_trans(s, a, (i) / float(n),
                                            phi_0_m3) * dia_trans(t, a, (j) / float(n), phi_1_m3)
                                              - K[3*i, 3*j+2] * dia_trans(s, a, (i) / float(n),
                                            phi_0_m3) * dia_trans(t, a, (j) / float(n), phi_2_m3)
                                              - K[3*i+1, 3*j+0] * dia_trans(s, a, (i) / float(n),
                                            phi_1_m3) * dia_trans(t, a, (j) / float(n), phi_0_m3)
                                              - K[3*i+1, 3*j+1] * dia_trans(s, a, (i) / float(n),
                                            phi_1_m3) * dia_trans(t, a, (j) / float(n), phi_1_m3)
                                              - K[3*i+1, 3*j+2] * dia_trans(s, a, (i) / float(n),
                                            phi_1_m3) * dia_trans(t, a, (j) / float(n), phi_2_m3)
                                              - K[3*i+2, 3*j] * dia_trans(s, a, (i) / float(n),
                                            phi_2_m3) * dia_trans(t, a, (j) / float(n), phi_0_m3)
                                              - K[3*i+2, 3*j+1] * dia_trans(s, a, (i) / float(n),
                                            phi_2_m3) * dia_trans(t, a, (j) / float(n), phi_1_m3)
                                              - K[3*i+2, 3*j+2] * dia_trans(s, a, (i) / float(n),
                                            phi_2_m3) * dia_trans(t, a, (j) / float(n), phi_2_m3))

          K_error[i, j] = quad(f_error, [i / float(n), (i + 1) / float(n)],[j / float(n), (j + 1) / float(n)],method='gauss-legendre')
          print [i / float(n), (i + 1) / float(n)]
          print [j / float(n), (j + 1) / float(n)]

  return K,K_error

# print project_kernel_m3_phi(4)
# m=linspace(0,1,250)
# i=0
# j=1
# f1 = lambda s, t: s-t
# f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/3)/float(n),phi_1_m3)*dia_trans(t,a,(j/3)/float(n),phi_2_m3)
# n=4
# print [(i/3)/float(n),((i/3)+1)/float(n)],[(j/3)/float(n),((j/3)+1)/float(n)]
# print quad(f,[(i/3)/float(n),((i/3)+1)/float(n)],[(j/3)/float(n),((j/3)+1)/float(n)])
# y=[dia_trans(z,a,(i/3)/float(n),phi_1_m3) for z in m]
# pyplot.plot(m,y)
# # print y ,"y"
# pyplot.show()