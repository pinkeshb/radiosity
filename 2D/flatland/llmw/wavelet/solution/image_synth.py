import Image
import m2_phi
from mpmath import *
from main_thres import *

from matplotlib import pyplot
def get_pix(x,B_norm,n):
    i=int((x)*n)
    if i==n:
        i=n-1
    # print i
    a=1.0/n
    b_error=lambda s:B_norm[2*i]*dia_trans(s, a, i  / float(n), phi_1_m2)+\
                    B_norm[2*i+1]*dia_trans(s, a, i  / float(n), phi_2_m2)
    return b_error(x)
def norm_it(B1_points,B2_points,n):
    B1_norm=[0]*2*n
    B2_norm=[0]*2*n
    max_point=max(max(B1_points),max(B2_points))
    for i in range(2*n):
        B1_norm[i]=B1_points[i]/max_point
        B2_norm[i]=B2_points[i]/max_point
    return B1_norm,B2_norm

    
def get_points(B1_proj,B2_proj,n):
    B1_points=[0]*2*n
    B2_points=[0]*2*n
    for i in range(n):
        B1_points[2*i]=B1_proj[2*i]-B1_proj[2*i+1]
        print B1_points[2*i]
        B2_points[2*i]=B2_proj[2*i]-B2_proj[2*i+1]
        B1_points[2*i+1]=B1_proj[2*i]+B1_proj[2*i+1]
        B2_points[2*i+1]=B2_proj[2*i]+B2_proj[2*i+1]
    return B1_points,B2_points
def project_it(B1,B2,n):
    B1_proj=[0]*2*n
    B2_proj=[0]*2*n
    a=1.0/n
    for i in range(n):
        B1_proj[2*i]=dia_trans(0,a,0,phi_1_m2)*B1[2*i]
        B2_proj[2*i]=dia_trans(0,a,0,phi_1_m2)*B2[2*i]
        B1_proj[2*i+1]=-dia_trans(0,a,0,phi_2_m2)*B1[2*i+1]
        B2_proj[2*i+1]=-dia_trans(0,a,0,phi_2_m2)*B2[2*i+1]
    return B1_proj,B2_proj
def plot_it():
    dist=0.0625
    n=16
    B1,B2=main_fn(n,0.001,n*n*4,dist) 
    # B1 = [ 1]*8
    # B2 =  [ 1]*8
    # B1 = [   0.0179987374259207,  0.00109046436648919,   0.0210336946311762, 0.000612308039260389,   0.0218859058672152,-0.000140315475224752,    0.520100786697704,-0.000860807260604174]
    # B2 = [   0.0400960410471698,  0.00372009417756244,   0.0536139064281069,  0.00394566599548252,   0.0654478637104089,   0.0026243170250629,   0.0695522576520381,-0.000400838040769403]
    # B1_proj,B2_proj=project_it(B1,B2,n)
    # print B1_proj
    # print B2_proj
    # B1_points,B2_points= get_points(B1_proj,B2_proj,n)
    # print B1_points
    # print B2_points
    # B1_norm,B2_norm=norm_it(B1_points,B2_points,n)
    # print B1_norm,B2_norm
    # print get_pix(0.8,B1,n)
    # print B1_proj,B2_proj
    # B1=matrix(1,4)
    # print B1
    # print B1[1]
    # print B2.tolist()
    # B1 = [ 0.48474296547776,0.551969023948957,0.558567032354462, 1.50100351629426]
    # B2 = [0.537557976096806, 0.64004051936919,0.688031083731422,0.656995808363111]
    # B_max=max(max(B1),max(B2))
    # B1=B1/B_max
    # B2=B2/B_max
    # B1=newList = [x / B_max for x in B1]
    # B2=newList = [x / B_max for x in B2]
    # # print B1
    # x=linspace(0,0.74,250)
    # y =[get_pix(m,B1,4) for m  in x] 
    # pyplot.plot(x,y)
    # # print y ,"y"
    # pyplot.show()
    x=1024
    y=1024/2
    th=x/n
    pix1=[0]*x
    # diff=[0]*x
    # print pix1[x-1][y-1]
    max=-10
    for i in range(x):
        # print i/float(x)
        pix1[i]=get_pix(i/float(x),B1,n)
        if pix1[i]>max:
            max = pix1[i]
    pix2=[0]*x
    print "max",max
    for i in range(x):
        # print i/float(x)
        pix2[i]=get_pix(i/float(x),B2,n)
        if pix2[i]>max:
            max = pix2[i]
    print "max",max
    pyplot.plot(pix2)
    # print y ,"y"
    pyplot.show()
    pyplot.plot(pix1)
    # print y ,"y"
    pyplot.show()
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
    # img2 = Image.new( 'RGB', (x,y), "black") # create a new black image
    # pixels = img2.load() # create the pixel map
     
    # for i in range(img2.size[0]):    # for every pixel:
    #     for j in range(img2.size[1]):
    #         # pixels[i,j] = (i, i,j) # set the colour accordingly
    #         val=int(pix2[i]*255)
    #         pixels[i,j]=(val,val,val)
    #         # print pixels[i,j]
     
    # img2.show()

    # img2.save("./b2_"+str(n)+"_","bmp")

    # img1 = Image.new( 'RGB', (x,y), "black") # create a new black image
    # pixels1 = img1.load() # create the pixel map
     
    # for i in range(img1.size[0]):    # for every pixel:
    #     for j in range(img1.size[1]):
    #         # pixels[i,j] = (i, i,j) # set the colour accordingly
    #         val1=int(pix1[i]*255.0/max)
    #         # print val1
    #         pixels1[i,j]=(val1,val1,val1)
    #         # print pixels[i,j]
     
    # img1.show()
    # img1.save("./b1_"+str(n)+"_","bmp")

plot_it()