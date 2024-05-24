import singly_linked_list as sll
import matplotlib.pyplot as plt
import math

def first(L):
    # Your code goes here
    if L.head== None:
        return -math.inf
    else:
        return L.head.data

def last(L):
    # Your code goes here
    if L.tail ==None:
        return -math.inf
    else:
        return L.tail
    return 0

def swap_first_and_last(L):
    # Your code goes here
    i = L.head
    while i != None:
        if i.next.next == None:
            j = i.next.next
            i.next = L.head
            break
        i = i.next
    
    
    j.next = L.head.next
    L.head.next = None
    L.head = j
    
    
    
    return None

def length(L): 
    # Your code goes here
    counter = 0
    t = L.head
    while t != None:
        counter += 1
        t = t.next
    return counter

def sum_list(L):
    # Your code goes here
    t = L.head
    sum = 0
    while t != None:
        sum = sum + t.data
        t = t.next
    return sum
    

def max_list(L):
    # Your code goes here
    t = L.head
    max , i = 0 ,0
    while t != None:
        i = t.data
        if i>max:
            max = i
        t = t.next
    return max

def to_list(L):
    # Your code goes here
    i = L.head
    A = []
    while i != None:
        A.append[i]
        i = i.next
        
    return A
    
    return []

def identical(L1,L2):
    # Your code goes here
    i = L1.head
    j = L2.head
    while i != None and j != None:
        if i != j:
            return False
    if i == None and j == None:
        return True

def delete_first(L):
    # Your code goes here
    if L.head != None:
        L.head = L.head.next
    

if __name__ == "__main__":
    plt.close('all')
    L1 = sll.List()
    L1.draw()
    L2 = sll.List()
    L2.extend([3,6,1,2,9,7,4,8,5])
    L2.draw()
    
    print(first(L1))   # -inf
    print(first(L2))   # 3
    
    print(last(L1))    # -inf
    print(last(L2))    # 5
    
    swap_first_and_last(L1)
    L1.print()              # []
    swap_first_and_last(L2) # [5, 6, 1, 2, 9, 7, 4, 8, 3]
    L2.print()          
    
    print(length(L1))   # 0
    print(length(L2))   # 9
    
    print(sum_list(L1)) # 0
    print(sum_list(L2)) # 45
    
    print(max_list(L1)) # -inf
    print(max_list(L2)) # 9
    
    print(to_list(L1))  # []
    print(to_list(L2))  # [5, 6, 1, 2, 9, 7, 4, 8, 3]
    
    L3 = sll.List()
    L3.extend([3,6,1,2,9,7,4,8,5]) 
    
    L4 = sll.List()
    L4.extend([3,6,1,2,9,7,4,8,5])
    
    L5 = sll.List()
    L5.extend([3,6,1,2])
    
    print(identical(L1,L2))  # False
    print(identical(L2,L3))  # False
    print(identical(L3,L4))  # True
    print(identical(L4,L5))  # False

    delete_first(L2) 
    L2.print()       # [6, 1, 2, 9, 7, 4, 8, 3]