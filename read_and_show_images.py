import numpy as np
import matplotlib.pyplot as plt
import os

def read_image(imagefile):
    # Reads image in imagefile and returns color and gray-level images
    img = (plt.imread(img_dir+file)*255).astype(int)
    img = img[:,:,:3]  # Remove transparency channel
    img_gl = np.mean(img,axis=2).astype(int)

    return img, img_gl

def draw_rect_on_image(im,ax,r,c,h,w):
    p = np.array([[r,c],[r+w,c],[r+w,c+h],[r,c+h],[r,c]])
    ax.imshow(im, cmap='gray')
    ax.plot(p[:,0],p[:,1],linewidth=3,color='R')
    
def box_brightest_pixel(im,ax):
    P = 0
    m,n = im.shape
    for i in range(m):
        for j in range(n):
            if P < im[i,j]:
                P = im[i,j]
                inx,iny = i,j
    print(P)
    print(inx)
    print(iny)
    draw_rect_on_image(im,ax,inx-10,iny-10,10,10)           
            
def region_sumV1(im,ax,rows,columns,height,width):
    sum_region = 0
    max_region = 0
    m,n = width - 1, height -1
    for i in range(rows-width+1):
        for j in range(columns-height+1):
            for h in range(height):
                 for w in range(width):
                    sum_region = sum_region + im[i+w][j+h]
                    if sum_region > max_region:
                        max_region = sum_region
                        inx,iny = i+w-m,j+h-n
                 if h == height-1:
                    sum_region = 0
    draw_rect_on_image(im,ax,inx,iny,height,width)
    
def region_sumV2(im,ax,rows,columns,height,width):
    sum_region = 0
    max_region = 0
    for i in range(rows-width):
        for j in range(columns-height):
            sum_region = np.sum(im[i:i+width, j:j+height])
            if sum_region > max_region:
                max_region = sum_region
                inx,iny = i,j
            sum_region = 0
    draw_rect_on_image(im,ax,inx,iny,height,width) 
    
def create_integral_image(arr,length,width):
    S = (width+1,length+1)
    img_table = np.zeros(S)
    print(img_table)
    for i in range( 1 , width+1):
        for j in range(1 , length + 1):
            integral_sum = np.sum(arr[:i,:j])
            img_table[i , j] = integral_sum
            integral_sum=0
    return img_table


    
    
img_dir = '.\\lab_2\\' # Directory where imagea are stored

img_files = os.listdir(img_dir)  # List of files in directory

plt.close('all')

for file in img_files:
    print(file)
    if file[-4:] == '.png': # File contains an image
        img, img_gl = read_image(img_dir+file)

        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
        ax1.imshow(img)    #Display color image
        #box_brightest_pixel(img_gl,ax2)
        m,n = img_gl.shape
        region_sumV2(img_gl,ax2,m,n,20,20)
        #ax2.imshow(img_gl,cmap='gray')   #Display gray-leval image
        plt.show()
