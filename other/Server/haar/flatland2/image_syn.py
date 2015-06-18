import Image
from mpmath import *
from main import *
B1,B2,K=main_fn(16,0.001) 
# B1=matrix(1,4)
# print B1
# print B1[1]
# print B2.tolist()
# B1 = [ 0.48474296547776,0.551969023948957,0.558567032354462, 1.50100351629426]
# B2 = [0.537557976096806, 0.64004051936919,0.688031083731422,0.656995808363111]
B_max=max(max(B1),max(B2))
B1=B1/B_max
B2=B2/B_max
# B1=newList = [x / B_max for x in B1]
# B2=newList = [x / B_max for x in B2]
# print B1
x=1024
y=1024/8
th=x/len(B1)
img1 = Image.new( 'RGB', (x,y), "black") # create a new black image
pixels = img1.load() # create the pixel map
 
for i in range(img1.size[0]):    # for every pixel:
    for j in range(img1.size[1]):
        # pixels[i,j] = (i, i,j) # set the colour accordingly
        val=int(B2[i/th]*255.0)
        pixels[i,j]=(val,val,val)
        # print pixels[i,j]
 
img1.show()

img2 = Image.new( 'RGB', (x,y), "black") # create a new black image
pixels = img2.load() # create the pixel map
 
for i in range(img2.size[0]):    # for every pixel:
    for j in range(img2.size[1]):
        # pixels[i,j] = (i, i,j) # set the colour accordingly
        val=int(B1[i/th]*255.0)
        pixels[i,j]=(val,val,val)
        # print pixels[i,j]
 
img2.show()