import numpy as np
import matplotlib.pyplot as plt
import math
import singly_linked_list as sll

def draw_circle(ax,center,rad):
    # Draws a circle in object ax given center and radius
    n = int(4*rad*math.pi)*2
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    ax.plot(x,y,linewidth=2.0,color='b')

def set_drawing_parameters_and_show(ax):
    show_axis = 'on'
    show_grid = 'True'
    ax.set_aspect(1.0)
    ax.axis(show_axis)
    plt.grid(show_grid)
    plt.show()

def nested_circles(ax, n, x0, y0, r):
    if n > 0:
        draw_circle(ax,[x0,y0],r)
        nested_circles(ax,n-1,x0-r,y0+r,r/2)
        nested_circles(ax,n-1,x0+r,y0+r,r/2)
        
def sum_until(L,i):
    if len(L)> 0:
        sum = 0
        for j in range(len(L)):
            if L[j] == i:
                break
            sum += L[j]
        return sum
    return 0

def first_plus_last(L):
    if L.head == None:
        return 0
    return L.head.data + L.tail.data

def smallest(L):
    if L.head == None:
        return math.inf
    T = L.head
    smallest = L.head.data
    while T != None:
        if T.data < smallest:
            smallest = T.data
        T = T.next 
            
    return smallest

def sum_edge(A):
    n,m = A.shape
    j,k = 1,1
    w = 0
    while j < n-1:
        while k < m-1:
            w += A[j,k]
            k+=1
        j+=1
    print(w)
    S = np.sum(A)
    S = S-w
    return S

if __name__ == "__main__":

    print('Question 1')
    plt.close("all") # Close all figures
    
    fig, ax = plt.subplots()
    nested_circles(ax,2,10,10,10)
    set_drawing_parameters_and_show(ax)
    fig.savefig('fig1.png')
    
    fig, ax = plt.subplots()
    nested_circles(ax,5,10,10,10)
    set_drawing_parameters_and_show(ax)
    fig.savefig('fig2.png')
    
    L1 = [2,5,7,4,1,6]
    L2 = [2302]
    L3 = []
    
    print('Question 2')
    print(sum_until(L1,7)) # 7
    print(sum_until(L1,9)) # 25
    print(sum_until(L2,7)) #2302
    print(sum_until(L3,9)) # 0
    
    L1 = sll.List()
    L2 = sll.List()
    L2.extend([2302])
    L3 = sll.List()
    L3.extend([302,2])
    L4 = sll.List()
    L4.extend([2,5,7,4,1,6])
    
    print('Question 3')
    print(first_plus_last(L1)) # 0
    print(first_plus_last(L2)) # 4604
    print(first_plus_last(L3)) # 304
    print(first_plus_last(L4)) # 8
    
    print('Question 4')
    print(smallest(L1)) # inf
    print(smallest(L2)) # 2302
    print(smallest(L3)) # 2
    print(smallest(L4)) # 1
    
    print('Question 5')
    A = np.arange(12).reshape((3,4))
    print(A)
    print(sum_edge(A)) # 
   