import Image
from kernel_haar_phi import *
from wavedecs import *
import ImageDraw
# from save_read import *
def drawspars(K,n):
    block=50
    sx=n*block+block
    sy=n*block+block
    img2 = Image.new( 'RGB', (sx,sy), "black") # create a new black image
    pixels = img2.load() # create the pixel map
    max=K[0,0]
    min=K[0,0]
    for i in range(n):
        for j in range(n):
            if max<K[i,j]:
                max=K[i,j]
            if min>K[i,j]:
                min = K[i,j]
    for i in range(sx):
        for j in range(sy):
            pixels[i,j]=(255,255,255)
    for i in range(n):
        for j in range(n):
            draw = ImageDraw.Draw(img2)
            x=block*i+block
            y=block*j+block
            val=(K[i,j]-min)*(1)/(max-min)
            # if abs(val)>0.001:
            r=(val)*(block/3)
            draw.ellipse((x-r, y-r, x+r, y+r), fill=(0,0,0))

    # for i in range(img2.size[0]):    # for every pixel:
    #     for j in range(img2.size[1]):
    #         # pixels[i,j] = (i, i,j) # set the colour accordingly
    #         val=i
    #         pixels[i,j]=(val,val,val)
    #         # print pixels[i,j]

    img2.show()
if __name__=="__main__":
    n=16
    dist =0.25
    # K=readit(n,"haar_scale_K_mat_dist_"+str(dist))
    K = project_kernel_haar_phi(n)
    drawspars(K,n)
    drawspars(dwt2(K),n)


# drawspars()