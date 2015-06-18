import Image
from mpmath import *
from main import *
def max2d(B):
    max=0
    n=len(B[0])
    for i in range(n):
        for j in range(n):
            if max < B1[i][j]:
                max=B1[i][j]
    return max
def max2(a,b):
    if a>b:
        return a
    else:
        return b
def divit(B,max):
    n=len(B[0])
    for i in range(n):
        for j in range(n):
            B[i][j]=B[i][j]/float(max)  
    return B  
dist=0.25
n=16
B1,B2=main_fn(n,0.001,dist,n*n*n*n/4)
# B1=matrix(1,4)
# print B1
# print B1[1]
# print B2.tolist()
# B1 = [ 0.48474296547776,0.551969023948957,0.558567032354462, 1.50100351629426]
# B2 = [0.537557976096806, 0.64004051936919,0.688031083731422,0.656995808363111]
B_max=max2(max2d(B1),max2d(B2))
B1=divit(B1,B_max)
B2=divit(B2,B_max)
# B1=newList = [x / B_max for x in B1]
# B2=newList = [x / B_max for x in B2]
# print B1
x=1024/2
y=1024/2
print B1
th=x/len(B1[0])
img1 = Image.new( 'RGB', (x,y), "black") # create a new black image
pixels = img1.load() # create the pixel map
 
for i in range(img1.size[0]):    # for every pixel:
    for j in range(img1.size[1]):
        # pixels[i,j] = (i, i,j) # set the colour accordingly
        val=int(B2[i/th][j/th]*255.0)
        pixels[i,j]=(val,0,0)
        # print pixels[i,j]
 
img1.show()

img2 = Image.new( 'RGB', (x,y), "black") # create a new black image
pixels = img2.load() # create the pixel map
 
for i in range(img2.size[0]):    # for every pixel:
    for j in range(img2.size[1]):
        # pixels[i,j] = (i, i,j) # set the colour accordingly
        val=int(B1[i/th][j/th]*255.0)
        pixels[i,j]=(val,0,0)
        # print pixels[i,j]
 
img2.show()