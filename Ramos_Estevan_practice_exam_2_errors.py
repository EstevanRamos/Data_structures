import matplotlib.pyplot as plt
import numpy as np
import bst
import btree
import hash_table_chain as htc

def path_to_largest(T):
    p = []
    if T==None:
        return []
    if type(T)==bst.BST:
        T=T.root
    if T.right== None:
        return [T.data]
    
    p.append(T.data)    
    p = p + path_to_largest(T.right)
    return p

def path_to_k(T,k):
    if T == None:
        return []
    if type(T)==bst.BST:
        T=T.root
    
    if T.data == k:
        return [T.data]

    if T.data < k:
        p = path_to_k(T.right,k)
    else:
        p = path_to_k(T.left,k)
    
    p = [T.data]+p
    
    
    if p[-1] != k:
        return[]
    return p

def prune_BST(T,d):
    if type(T)==bst.BST:
        T=T.root
    if T == None:
        return
    
    if d <= 0:
        T.left = T.right=None
    else:
        prune_BST(T.left,d-1)
        prune_BST(T.right,d-1)

def keys_in_path_to_smallest(T):
    p = []
    if type(T)==btree.BTree:
        T=T.root
    p = p + T.data
    if not T.is_leaf:
        p = p + keys_in_path_to_smallest(T.child[0])
    return p

def smallest_in_nodes(T):
    if type(T)==btree.BTree:
        T=T.root
        
    s = [T.data[0]]   
    
    if T.is_leaf:
        return s
    
    for c in T.child:
        s = s + smallest_in_nodes(c)
        
    return sorted(s)

def prune_Btree(T,d):
    if type(T)==btree.BTree:
        T=T.root
        
    if d <= 0:
        T.is_leaf = True
        
    else:
        for c in T.child:
            prune_Btree(c,d-1)

def item_status(h,k):
    b = h.h(k)
    for rec in h.bucket[b]:
        if rec.key == k:
            if len(h.bucket) == 1:
                return 0
            else:
                return 1
    return -1
    #for b in h.bucket:
       # for rec in b:
        #    if rec.key == k:
         #       if len(b)==1:
          #          return 0
           #     else:
            #        return 1
   
def repeats(S,c):
    h = htc.HashTableChain(len(S))
    repeat = []
    for i in range(len(S)-c+1):
        s = S[i:i+c]
        count = h.retrieve(s)
        if count == None:
            h.insert(s,1)
        else:
            count +=1
            h.update(s,count)
            repeat.append(s)      
    return repeat

def build_index_table(L):
    h = htc.HashTableChain(len(L))
    repeat = []
    for i in range(len(L)):
        pos = h.retrieve(L[i])
        if pos == None:
            h.insert(L[i],[i])
        else:
            pos = [pos] + [i]
            h.update(L[i],pos)
    return h


if __name__ == "__main__":
    plt.close('all')
    
    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1,  20, 13]
    T = bst.BST()

    for a in A:
        T.insert(a)
        
    T.draw()
    
    print('Question 1')     
    print(path_to_largest(T))    # [11, 16, 17, 18, 20]
    
    print('Question 2')
    print(path_to_k(T,7))   # [11, 6, 7]
    print(path_to_k(T,15))  # [11, 16, 14, 15]
    print(path_to_k(T,19))  # []
    
    print('Question 3')
    prune_BST(T,3)
    T.draw()
    prune_BST(T,2)
    T.draw()
    prune_BST(T,1)
    T.draw()
    prune_BST(T,0)
    T.draw()
    
    print('Question 4')
    T = btree.BTree()    
    nums = [6, 3, 16, 11, 7, 17, 14, 8, 5, 19, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12, 21]
    for num in nums:
        T.insert(num)
    T.draw()

    print(keys_in_path_to_smallest(T))  

    print('Question 5')
    print(smallest_in_nodes(T))

    print('Question 6')
    prune_Btree(T,3)
    T.draw()
    prune_Btree(T,2)
    T.draw()
    prune_Btree(T,1)
    T.draw()
    
    print('Question 7')
    h = htc.HashTableChain(5)
    
    players = ['Bellinger','Betts', 'Hernandez', 'Pederson', 'Pollock', 'Taylor']
    numbers= [35, 50, 14, 31, 11, 3]

    for i in range(len(players)):
        h.insert(numbers[i],players[i])
    h.print_table()
    
    print(item_status(h,99))  # -1
    print(item_status(h,3))   # 0
    print(item_status(h,11))  # 1
    
   
    print('Question 8')
    S = 'GACCGAATCCG'
    print(repeats(S,1)) # ['C', 'G', 'A']
    print(repeats(S,2)) # ['GA', 'CC', 'CG']
    print(repeats(S,3)) # ['CCG']
    print(repeats(S,4)) # []
    
    print('Question 9')
    L = [2,4,6,1,2,3,1,12]   
    h = build_index_table(L)
    h.print_table()
    
#    Table contents:
#    bucket 0: [ ]
#    bucket 1: [ [1, [3, 6]] ]
#    bucket 2: [ [2, [0, 4]] ]
#    bucket 3: [ [3, [5]] ]
#    bucket 4: [ [4, [1]] [12, [7]] ]
#    bucket 5: [ ]
#    bucket 6: [ [6, [2]] ]
#    bucket 7: [ ]

    print(h.retrieve(2))    # [0, 4]
    print(h.retrieve(4))    # [1]
    print(h.retrieve(23))   # None
    
    
    