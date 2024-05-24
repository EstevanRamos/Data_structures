import numpy as np
import matplotlib.pyplot as plt
import os

def read_image(imagefile):
    # Reads image in imagefile and returns color and gray-level images
    #
    img = (plt.imread(img_dir+file)*255).astype(int)
    img = img[:,:,:3]  # Remove transparency channel
    img_gl = np.mean(img,axis=2).astype(int)

    return img, img_gl

img_dir = '.\\lab_2\\' # Directory where imagea are stored

img_files = os.listdir(img_dir)  # List of files in directory

plt.close('all')

for file in img_files:
    print(file)
    if file[-4:] == '.png': # File contains an image
        img, img_gl = read_image(img_dir+file)

        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
        ax1.imshow(img)                  #Display color image
        ax2.imshow(img_gl,cmap='gray')#Display gray-leval image
        print(img_gl)
        plt.show()
