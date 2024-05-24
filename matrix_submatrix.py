import numpy as np
import matplotlib.pyplot as plt
import os


def region_sumV1(arr,rows,columns,height,width):
    sum_region = 0
    max_region = 0

    for i in range(rows-width+1):
        for j in range(columns-height+1):
            for h in range(height):
                 for w in range(width):
                    print(arr[i+w][j+h])
                    sum_region = sum_region + arr[i+w][j+h]
                    if sum_region > max_region:
                        max_region = sum_region
                 if h == height-1:
                    sum_region = 0
               
    print(max_region)


def region_sumV2(arr,rows,columns,height,width):
    sum_region = 0
    max_region = 0
    for i in range(rows-width):
        for j in range(columns-height):
            sum_region = np.sum(arr[i:i+width, j:j+height])
            if sum_region > max_region:
                max_region = sum_region
            sum_region = 0
    print(max_region) 
    
def create_integral_image(arr,length,width):
    S = (width+1,length+1)
    img_table = np.zeros(S)
    for i in range( 1 , width+1):
        for j in range(1 , length + 1):
            integral_sum = np.sum(arr[:i,:j])
            img_table[i , j] = integral_sum
            integral_sum=0
    return img_table

def region_sumV3(im,rows,columns,height,width):
    #determines the greatest sum region using integral table
    A = create_integral_image(im,rows,columns)
    print(A)
    sum_region = 0
    max_region = 0
    for i in range(rows-width):
        for j in range(columns-height):
            sum_region = A[i+width,j+height]- A[i,j+height] - A[i + width,j] + A[i,j]
            if sum_region > max_region:
                max_region = sum_region
            sum_region = 0
                






P = np.array([[3,4,6,5,1],
             [1,2,8,4,2],
             [3,8,9,3,1],
             [7,3,4,2,7],
             [3,7,5,7,6]
             ])
    
A = np.random.randint(1,10,size=(20,20))
B = np.random.randint(1,10,size=(30,30))
C = np.random.randint(1,10,size=(30,60))
D = np.random.randint(1,10,size=(60,60))
E = np.random.randint(1,10,size=(60,100))
A = np.random.randint(1,10,size=(,20))
#region_sumV1(P,5,5,2,2)
#region_sumV3(P,5,5,2,2)
#create_integral_image(P,5,5)



