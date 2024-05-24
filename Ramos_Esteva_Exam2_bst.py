import matplotlib.pyplot as plt
import numpy as np
import bst

def bst_3nodes(L):
    T=bst.BST()
    T.root = bst.BSTNode(L[0])
    T.root.left = bst.BSTNode(L[1])
    T.root.right = bst.BSTNode(L[2])
    return T

def has_depth(T,d):
    if T == None:
        return
    
    if type(T) == bst.BST:
        T = T.root
    
    if d < 1:
        if T != None:
            return True
        else:
            return False
        
    return has_depth(T.left, d-1) and has_depth(T.right, d-1)
    

def add_n(T,n):
    if T == None:
        return
    
    if type(T) == bst.BST:
        T = T.root
        
    T.data = T.data + n
    add_n(T.left,n)
    add_n(T.right,n)
        
def get_path(T,k):
    if T == None:
        return
    
    if type(T) == bst.BST:
        T = T.root
        if T.data == k:
            return ''
        
    if T.left.data == k:
        return 'L'
    if T.right.data ==k:
        return 'R'
    
    
    if T.data < k:
        p = p + get_path(T.right,k)
    else:
        p = p + get_path(T.left, k)
        
    return p
    
        
    

if __name__ == "__main__":
    plt.close('all')
    
    print('Question 1')   
    L = [10,20,30]
    T=bst_3nodes(L)
    T.draw()
    
    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1,  20, 13]
    T = bst.BST()
    for a in A:
        T.insert(a)
    T.draw()
    
    print('Question 2')     
    print(has_depth(T,0))                    # True
    print(has_depth(T,1))                    # True
    print(has_depth(T,2))                    # True
    print(has_depth(T,3))                    # True
    print(has_depth(T,4))                    # True
    print(has_depth(T,5))                    # False    
    print(has_depth(T,6))                    # False        
    
    print('Question 3')     
    print(add_n(T,5))   
    T.draw()
    
    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1,  20, 13]
    T = bst.BST()
    for a in A:
        T.insert(a)
    T.draw()

    print('Question 4')     
    print(get_path(T,15))  # RLR
    print(get_path(T,1))   # LLL
    print(get_path(T,10))  # None
    
    
    
    
    
    
    
    
    
    
    
    