import numpy as np
import singly_linked_list as sll
import matplotlib.pyplot as plt
import math

def sorted_rows(A):
    m,n = A.shape
    for i in range(m-1):
        for j in range(n-1):
            if A[i,j] > A[i, j+ 1]:
                return False
    return True

def second(L):
    if L.head.next == None:
        return None
    return L.head.next.data

def count_occurrences(L,i):
    j = L.head
    count = 0
    while j != None:
        if i == j.data:
            count += 1
        j = j.next
    return count

def remove_all_but_first_and_last(L):
    if L.head.next != None:
        L.head.next = L.tail
    
    
if __name__ == "__main__":
    plt.close('all')
    A1 = np.array([[1,2,3],[4,5,6],[2,3,9]])
    A2 = np.array([[1,2,3],[4,3,6],[7,8,9]])
    print(A1)
    print(A2)
    print(sorted_rows(A1)) # True 
    print(sorted_rows(A2)) # False
    
    L1 = sll.List()
    L1.append(2302)
    L1.draw()
    L2 = sll.List()
    L2.extend([3,6,1,2,9,7,4,8,6,5])
    L2.draw()
    
    print(second(L1))  # None
    print(second(L2))  # 6
    
    L= sll.List()
    L.extend([3,6,1,2,9,7,4,8,6,5])
    L.draw()
    
    print(count_occurrences(L,0)) # 0
    print(count_occurrences(L,6)) # 2
    print(count_occurrences(L,5)) # 1
    
    L= sll.List()
    L.extend([3,6,1,2,9,7,4,8,6,5])
    L.draw()
    
    remove_all_but_first_and_last(L)
    
    L.print() # [3, 5]
    