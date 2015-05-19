import Image
from mpmath import *
from main import *
from matplotlib import pyplot
def get_pix(x,y,B,n):
    i=int((x)*n)
    if i==n:
        i=n-1
    j=int((y)*n)
    if j==n:
        j=n-1
    a=1.0/n
    b=lambda s,t: B[3*i+0][3*j+0]*dia_trans(s, a, i  / float(n), phi_0_m3)*dia_trans(t, a, j  / float(n), phi_0_m3)+\
                    B[3*i+0][3*j+1]*dia_trans(s, a, i  / float(n), phi_0_m3)*dia_trans(t, a, j  / float(n), phi_1_m3)+\
                    B[3*i+0][3*j+2]*dia_trans(s, a, i  / float(n), phi_0_m3)*dia_trans(t, a, j  / float(n), phi_2_m3)+\
                    B[3*i+1][3*j+0]*dia_trans(s, a, i  / float(n), phi_1_m3)*dia_trans(t, a, j  / float(n), phi_0_m3)+\
                    B[3*i+1][3*j+1]*dia_trans(s, a, i  / float(n), phi_1_m3)*dia_trans(t, a, j  / float(n), phi_1_m3)+\
                    B[3*i+1][3*j+2]*dia_trans(s, a, i  / float(n), phi_1_m3)*dia_trans(t, a, j  / float(n), phi_2_m3)+\
                    B[3*i+2][3*j+0]*dia_trans(s, a, i  / float(n), phi_2_m3)*dia_trans(t, a, j  / float(n), phi_0_m3)+\
                    B[3*i+2][3*j+1]*dia_trans(s, a, i  / float(n), phi_2_m3)*dia_trans(t, a, j  / float(n), phi_1_m3)+\
                    B[3*i+2][3*j+2]*dia_trans(s, a, i  / float(n), phi_2_m3)*dia_trans(t, a, j  / float(n), phi_2_m3)
    return b(x,y)
def plot_it():

    n=4
    dist=0.125
    B1,B2=main_fn(n,0.001,dist) 
    # print B1
    x=1024/2
    y=1024/2
    th=x/n
    pix1=[[1 for l in range(x)] for m in range(y)] 
    max=-10
    for i in range(x):
        for j in range(x):
            # print i/float(x)
            pix1[i][j]=get_pix(i/float(x),j/float(x),B1,n)
            if pix1[i][j]>max:
                max = pix1[i][j]
    pix2=[[1 for l in range(x)] for m in range(y)] 
    # print "max",max
    for i in range(x):
        for j in range(x):
            # print i/float(x)
            pix2[i][j]=get_pix(i/float(x),j/float(x),B2,n)
            if pix2[i][j]>max:
                max = pix2[i][j]
    print "max",max
    for i in range(x):
        for j in range(x):
            # print i/float(x)
            pix1[i][j]=pix1[i][j]/max
    # print "max",max
    for i in range(x):
        for j in range(x):
            # print i/float(x)
            pix2[i][j]=pix2[i][j]/max

    # pyplot.plot(pix2)
    # # print y ,"y"
    # pyplot.show()
    # pyplot.plot(pix1)
    # # print y ,"y"
    # pyplot.show()
    # for i in range(x-1):
    #     diff[i]=pix[i+1]-pix[i]
    #     if diff[i]<0:
    #         diff[i]=-1
    #     elif diff[i]>0:
    #         diff[i]=+1
    #     else:
    #         diff[i]=0
    # print "pix",pix
    # print diff
    # pix2=[0]*x
    # # print pix[x-1][y-1]
    # for i in range(x):
    #     pix2[i]=get_pix(i/float(x),B2,n)
    # print "pix2",pix2
    img2 = Image.new( 'RGB', (x,y), "black") # create a new black image
    pixels = img2.load() # create the pixel map
     
    for i in range(img2.size[0]):    # for every pixel:
        for j in range(img2.size[1]):
            # pixels[i,j] = (i, i,j) # set the colour accordingly
            val=int(pix2[i][j]*255)
            pixels[i,j]=(val,val,val)
            # print pixels[i,j]
     
    img2.show()
    img1 = Image.new( 'RGB', (x,y), "black") # create a new black image
    pixels1 = img1.load() # create the pixel map
     
    for i in range(img1.size[0]):    # for every pixel:
        for j in range(img1.size[1]):
            # pixels[i,j] = (i, i,j) # set the colour accordingly
            val1=int(pix1[i][j]*255.0)
            # print val1
            pixels1[i,j]=(val1,val1,val1)
            # print pixels[i,j]
     
    img1.show()
plot_it()
