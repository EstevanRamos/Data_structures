import numpy as np
import matplotlib.pyplot as plt
import math
import singly_linked_list as sll

def set_drawing_parameters_and_show(ax):
    show_axis = 'on'
    show_grid = 'True'
    ax.set_aspect(1.0)
    ax.axis(show_axis)
    plt.grid(show_grid)
    plt.show()

def nested_squares(ax,n,x0,y0,size):
    if n>1:
         square = np.array([[x0-size,y0+size],[x0+size,y0+size],[x0+size,y0-size],[x0-size,y0-size],[x0-size,y0+size]])
         print (square)
         ax.plot(square[0:])
         nested_squares(ax, n-1,x0-size, y0, size/2)
         nested_squares(ax, n-1,x0+size, y0, size/2)

def list_n_to_0(n): 
    return []
    

def sum_first_n(L,n):
    sum = 0
    j = L.head
    if L.size < n:
        while j != None:
            sum += j.data
            j = j.next
        return sum
    
    for k in range(n):
        sum += j.data
        j= j.next
        
    return sum

def sum_until(L,i):
    j = L.head
    in_L = False
    counter = 1
    sum = 0
    
    while j != None:
        if j.data == i:
            in_L = True
            counter +=1
            break
        counter += 1
        j = j.next
            
    if in_L == False:
        j = j.head
        while j != None:
            sum += j.data
        return sum
    
    j = L.head
    for k in range(counter):
        sum += j.data
        j = j.next

def next_to_last(L):
    if L.size < 2:
        return None
    j = L.head
    while j != None:
        if j.next.next.next == None:
            return j.next.next.data , j.next.data 

if __name__ == "__main__":

    plt.close("all") # Close all figures
    fig, ax = plt.subplots()
    nested_squares(ax,2,0,0,100)
    set_drawing_parameters_and_show(ax)
    
    print(list_n_to_0(0)) # [0]
    print(list_n_to_0(5)) # [5, 4, 3, 2, 1, 0]
    
    L= sll.List()
    L.extend([3,6,1,2,5])
    L.draw()
    
    print(sum_first_n(L,4))  # 12
    print(sum_first_n(L,10)) # 17
    
    print(sum_until(L,3))  # 0
    print(sum_until(L,1))  # 9
    print(sum_until(L,10)) # 17
    
    L1= sll.List()
    print(next_to_last(L1)) # None
    print(next_to_last(L))  # 2

