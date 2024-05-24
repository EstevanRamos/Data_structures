import numpy as np
import matplotlib.pyplot as plt
import os
import time #used for timing the methods

def read_image(imagefile):
    # Reads image in imagefile and returns color and gray-level images
    img = (plt.imread(img_dir+file)*255).astype(int)
    img = img[:,:,:3]  # Remove transparency channel
    img_gl = np.mean(img,axis=2).astype(int)

    return img, img_gl

def draw_rect_on_image(im,ax,r,c,h,w):
    #draws a square given a top left corner and length and width
    p = np.array([[r,c],[r+w,c],[r+w,c+h],[r,c+h],[r,c]])#creates an array with the points of the square
    ax.imshow(im, cmap='gray')#shows the image
    ax.plot(p[:,0],p[:,1],linewidth=3,color='R')#plots the square on the image
    
def box_brightest_pixel(im,ax):
    #finds the brightest pixwl in an image
    P = 0 #pixel number
    m,n = im.shape #nums of rows and columns
    for i in range(m):
        for j in range(n):
            if P < im[i,j]: #finds the brightest pixel
                P = im[i,j] #sets p to brightest pixel
                inx,iny = i,j # saves the index of the brightest pixel
    print(P)
    print(inx)
    print(iny)
    draw_rect_on_image(im,ax,inx-10,iny-10,10,10)           
            
def region_sumV1(im,ax,rows,columns,height,width):
    #finds the brightest region in a picture using 4 loops
    start = time.time()
    sum_region = 0
    max_region = 0
    m,n = width - 1, height -1 #used for fnding the index of the left corner of the region
    for i in range(rows-width+1):#rows of picture
        for j in range(columns-height+1):#columns of the picture
            for h in range(height):#height of the sub region
                 for w in range(width):#width of the subregion
                    sum_region = sum_region + im[i+w][j+h] # sums the sub region
                    if sum_region > max_region:# finds the greatest subregion
                        max_region = sum_region#sets the greatest sum region
                        inx,iny = i+w-m,j+h-n#indexs the left corner of the sum rgion
                 if h == height-1:      #resets the sum region to 0
                    sum_region = 0
    end = time.time()
    draw_rect_on_image(im,ax,inx,iny,height,width) #draws the rectangular region
    return (end-start)
    
def region_sumV2(im,ax,rows,columns,height,width):
    #finds the sum of region using slices and indexes with 2 loops
    start = time.time()
    sum_region = 0
    max_region = 0
    for i in range(rows-width):# rows of image
        for j in range(columns-height): # columns of image
            sum_region = np.sum(im[i:i+width, j:j+height]) #sums the region using array slicing and sum funciong
            if sum_region > max_region:
                max_region = sum_region     #finds the max region
                inx,iny = i,j               #index the max region
            sum_region = 0
    end = time.time()            
    draw_rect_on_image(im,ax,inx,iny,height,width) #draws the region
    return (end-start)
    
    
def create_integral_image(arr,rows,columns):
    #creates integral image table
    S = (rows+1,columns+1) # creates the integral image table
    img_table = np.zeros(S)# fills the table with zeros
    for i in range( 1 , rows+1):
        for j in range(1 , columns + 1):
            integral_sum = np.sum(arr[:i,:j])#sums the orignal array and stores the value
            img_table[i , j] = integral_sum  #takes the sum and places it into the integral image table
            integral_sum=0#resets the sum to 0
    return img_table

def region_sumV3(im,ax,og,rows,columns,height,width):
    #determines the greatest sum region using integral table
    #A = create_integral_image(im,rows,columns)#takes a very long time
    start = time.time()
    sum_region = 0
    max_region = 0
    
    for i in range(rows-width):
        for j in range(columns-height):
            sum_region = im[i+width, j + height]- im[ i, j+height] - im[i + width,j]+im[i,j] # gets the 4 corners of the integral image table
            if sum_region > max_region:
                max_region = sum_region#finds the sum of the region
                inx,iny = i,j#indexes the region
            sum_region = 0
    end = time.time()
    draw_rect_on_image(og,ax,inx,iny,height,width) # draws retangular region
    return (end-start)

    
    
img_dir = '.\\lab_2\\' # Directory where imagea are stored

img_files = os.listdir(img_dir)  # List of files in directory

plt.close('all')

x1 = [0, 4, 8]
x2 = [1,5,9]
x3 = [2,6,10]

y1 = []
y2 = []
y3 = []

for file in img_files:
    print(file)
    if file[-4:] == '.png': # File contains an image
        img, img_gl = read_image(img_dir+file)

        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
        ax1.imshow(img)    #Display color image
        m,n = img_gl.shape
        
        #A = create_integral_image(img_gl,m,n)
        y1.append(region_sumV1(img_gl,ax2,m,n,60,60))
      #  y2.append(region_sumV2(img_gl,ax2,m,n,60,60))
       # y3.append(region_sumV3(A,ax2,img_gl,m,n,60,60))
        
       # y1.append(region_sumV1(img_gl,ax2,m,n,60,100))
       # y2.append(region_sumV2(img_gl,ax2,m,n,60,100))
       # y3.append(region_sumV3(A,ax2,img_gl,m,n,60,100))
        
        #y1.append(region_sumV1(img_gl,ax2,m,n,100,100))
       # y2.append(region_sumV2(img_gl,ax2,m,n,100,100))
      #  y3.append(region_sumV3(A,ax2,img_gl,m,n,100,100))
        plt.show()

plt.bar(x1,y1, align = 'center')
plt.bar(x2,y2, color = 'g', align = 'center')
plt.bar(x3,y3, color = 'r', align = 'center')

plt.show()