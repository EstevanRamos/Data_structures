import btree
import matplotlib.pyplot as plt
import numpy as np

def nodeRange(t):
    return t.data[-1] - t.data[0]

def countNodes(t):
    count = 1
    if t.is_leaf:
        return count
    
    for c in t.child:
        count += countNodes(c)
    return count

def countItemsAtDepthD(t,d)  :
    count = 0
    if d ==0:
        return len(t.data)
    
    for c in t.child:
        count += countItemsAtDepthD(c,d-1)
    return count 

if __name__ == "__main__":
    plt.close('all')
    T = btree.BTree()

    nums = [6, 3, 23,16, 11, 25, 7, 17,27, 30, 21, 14, 26, 8, 29, 
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
  
    t = T.find(4)
    for num in nums:
        T.insert(num)
        
    T.draw()
    
    print(nodeRange(T.root))  # 0
    t = T.find(4)
    print(nodeRange(t))       # 4
    t = T.find(25)
    print(nodeRange(t))       # 2
    
    print(countNodes(T.root))  # 9
    
    print(countItemsAtDepthD(T.root,0))   # 1
    print(countItemsAtDepthD(T.root,1))   # 4
    print(countItemsAtDepthD(T.root,2))   # 25
    print(countItemsAtDepthD(T.root,3))   # 0
    