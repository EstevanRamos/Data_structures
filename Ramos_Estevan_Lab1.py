import numpy as np
import matplotlib.pyplot as plt
import math

def circle(center,rad):
    # Returns the coordinates of the points in a circle given center and radius
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y
#
#below was supposed to be for constructing the multi triangles inside of triangles
#
#def triangle(point,direction,length):
#    l=length/2
#    if direction = "up  ":
#        triangle = np.array([point,[point[0]+ l/2,point[1]-l]],[point[0]-l/2,point[1]-l],point)
#def draw_triangles(ax,n,p,length):
#    if n>0:
#        ax.plot(p[:,0],p[:,1],linewidth=0.5,color='k')
    
def draw_inside_triangles(ax,n,p,w):
    #draws a triangle inside of another triangle
    if n>0:
        ax.plot(p[:,0],p[:,1],linewidth=0.5,color='k')#plots the first triangle
        i1 = [1,2,0,1]                                #index to create the second rotated triangle
        q = p*(1-w) + p[i1]*w                         #creates the new triangle after rotating it
        draw_inside_triangles(ax,n-1,q,w)             #calls itself with new triangle
        
def draw_tree_down(ax,n,center,dx,dy):
    #draws a tree in downward direction
    if n>0:
        dx = dx*.5
        dy = dy*.75
        p = np.array([[center[0],center[1]],[center[0]-dx,center[1]-dy]])#creates array from the center to the left
        q = np.array([[center[0],center[1]],[center[0]+dx,center[1]-dy]])#creates array from the center to the right
    
        ax.plot(p[:,0],p[:,1],linewidth=0.5,color='k')#plots left line
        ax.plot(q[:,0],q[:,1],linewidth=0.5,color='k')#plots right line
        
        draw_tree_down(ax,n-1,p[1,:2],dx,dy)#calls itself with the left point
        draw_tree_down(ax,n-1,q[1,:2],dx,dy)#calls itself with the right point
        
def square(center,length):
    #returns an array of points that make a square from a center point and a length of a side
    x = center[0]
    y = center[1]
    l = length/2 
    p = np.array([[x-l,y-l],[x-l, y+l],[x+l,y+l],[x+l,y-l],[x-l,y-l]])
    return p
    
        
def draw_four_squares(ax,n,center,length):
    #draws square with a square at the corners of that square
    if n>0:
        p = square(center,length)
        ax.plot(p[:,0],p[:,1],linewidth=0.5,color='k')
        draw_four_squares(ax,n-1,p[0],length/2)#calls itself for every point in the square
        draw_four_squares(ax,n-1,p[1],length/2)
        draw_four_squares(ax,n-1,p[2],length/2)
        draw_four_squares(ax,n-1,p[3],length/2)

def draw_four_circles(ax,n,center,radius):
    #given
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,linewidth=0.5,color='k')
        draw_four_circles(ax,n-1,[center[0],center[1]+radius],radius/2)
        draw_four_circles(ax,n-1,[center[0],center[1]-radius],radius/2)
        draw_four_circles(ax,n-1,[center[0]+radius,center[1]],radius/2)
        draw_four_circles(ax,n-1,[center[0]-radius,center[1]],radius/2)
    
def draw_inside_circles(ax,n,center,radius):
    #draws circles inside of circles
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,linewidth=0.5,color='k')
        draw_inside_circles(ax,n-1,center,radius*.75)
    

if __name__ == "__main__":  
    
    plt.close("all") # Close all figures
    
    #draws cirlces
    fig, ax = plt.subplots() 
    draw_inside_circles(ax, 3, [0,0], 100)
    ax.set_aspect(1.0)
   # ax.axis('off')
    plt.show()
    fig.savefig('inside_circlesa.png')
    
    #math to create a equilateral triangle
    size = 1000
    a = size*size + ((size/2)*(size/2))
    a = math.sqrt(a)
    p = np.array([[0,0],[size/2,a],[size,0],[0,0]])
    
    #draws triangles inside
    fig, ax = plt.subplots()
    draw_inside_triangles(ax,6,p,.50)
    ax.set_aspect(1.0)
    # ax.axis('off')
    plt.show()
    fig.savefig('inside_triangles.png')
    
    #draws squares
    fig, ax = plt.subplots()
    draw_four_squares(ax,5,[0,0],1000)
    ax.set_aspect(1.0)
    #ax.axis('off')
    plt.show()
    fig.savefig('squaresa.png')
    
    #drwas the downward tree
    fig, ax = plt.subplots()
    draw_tree_down(ax,5,[0,1000],1000,1000)
    #ax.axis('off')
    plt.show()
    fig.savefig('tree.png')