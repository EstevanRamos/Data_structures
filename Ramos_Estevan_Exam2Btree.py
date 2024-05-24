import matplotlib.pyplot as plt
import numpy as np
import btree

def find_k(T,k):
    if type(T)==btree.BTree:
        T=T.root
        
    if k in T.data:
        return True
    
    if T.is_leaf:
        return False
    
    ch = 0
    for i in range(len(T.data)):
        if k > T.data[i]:
            ch = i+1
        else:
            ch = i

        
    return find_k(T.child[ch],k)

def roots_children(T):
    T = T.root
    L = []
    for c in T.child:
        L = L + c.data
    return L

def prune_leaves(T):
    if type(T)==btree.BTree:
        T=T.root
    for c in T.child:
        if c.is_leaf:
            T.is_leaf = True
        else:
            prune_leaves(c)


def make_binary(T):
    if type(T) == btree.BTree:
        T = T.root
    
    if T.is_leaf:
        del T.data[1:]
    
    
    #del T.child[0].data[1:]
    #del T.child[1].data[1:]
    
    #make_binary(T.child[0])
    #make_binary(T.child[1])
    
    for c in T.child:
        del c.data[1:]
        make_binary(c)
    return

if __name__ == "__main__":  
    plt.close('all') 
    T = btree.BTree()  
    T_empty = btree.BTree()  
    nums = [6, 3, 16, 11, 7, 17, 14, 8, 5, 19, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12, 21]
    for num in nums:
        T.insert(num)
    T.draw('Original tree')  
    
    print('Question 1')
    print(find_k(T,10))    # True
    print(find_k(T,14))    # True
    print(find_k(T,9))     # True
    print(find_k(T,25))    # False
    
    print('Question 2')
    print(roots_children(T))        # [3, 7, 14, 17]
    print(roots_children(T_empty))  # []

    print('Question 3')
    T = btree.BTree()  
    for num in nums:
        T.insert(num)    
    prune_leaves(T)
    T.draw('Question 3') 
    
    print('Question 4')
    T = btree.BTree()  
    for num in nums:
        T.insert(num)    
    make_binary(T)
    T.draw('Question 4') 
    