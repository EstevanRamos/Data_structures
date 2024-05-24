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

def draw_squares(ax,n,p,w):
    if n>0:
        ax.plot(p[:,0],p[:,1],linewidth=0.5,color='k') # Draw rectangle
        i1 = [1,2,3,0,1]
        q = p*(1-w) + p[i1]*w  
        print()
        print(q)
        draw_squares(ax,n-1,q,w)

def draw_four_circles(ax,n,center,radius):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,linewidth=0.5,color='k')
        draw_four_circles(ax,n-1,[center[0],center[1]+radius],radius/2)
        draw_four_circles(ax,n-1,[center[0],center[1]-radius],radius/2)
        draw_four_circles(ax,n-1,[center[0]+radius,center[1]],radius/2)
        draw_four_circles(ax,n-1,[center[0]-radius,center[1]],radius/2)

if __name__ == "__main__":  
    
    plt.close("all") # Close all figures
    
    orig_size = 1000.0
    p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
    print('Points in original square:')
    print(p)
    
    fig, ax = plt.subplots()
    draw_squares(ax,6,p,.2)
    ax.set_aspect(1.0)
    #ax.axis('off') # Uncomment to see coordinates in drawing
    plt.show()
    fig.savefig('squaresa.png')
    
    fig, ax = plt.subplots()
    draw_squares(ax,10,p,.2)
    ax.set_aspect(1.0)
    #ax.axis('off')
    plt.show()
    fig.savefig('squaresb.png')
    
    fig, ax2 = plt.subplots()
    draw_squares(ax2,5,p,.3)
    ax2.set_aspect(1.0)
    #ax2.axis('off')
    plt.show()
    fig.savefig('squaresc.png')
    
    fig, ax = plt.subplots() 
    draw_four_circles(ax, 2, [0,0], 100)
    ax.set_aspect(1.0)
    #ax.axis('off')
    plt.show()
    fig.savefig('four_circlesa.png')
    
    fig, ax = plt.subplots() 
    draw_four_circles(ax, 3, [0,0], 100)
    ax.set_aspect(1.0)
    #ax.axis('off')
    plt.show()
    fig.savefig('four_circlesb.png')
    
    fig, ax = plt.subplots() 
    draw_four_circles(ax, 4, [0,0], 100)
    ax.set_aspect(1.0)
    #ax.axis('off')
    plt.show()
    fig.savefig('four_circlesc.png')
    
    
    