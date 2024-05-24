import btree
import matplotlib.pyplot as plt
import numpy as np
import math

def largestAtDepthD(T,d):
    t = T.root
    while d > 0:
        if t.is_leaf:
            return -math.inf
        t = t.child[-1]
        d -= 1
    return t.data[-1]

def findDepth(T,k):
    depth = 0
    t =  T.root
    for c in t.child:
        if k in t.data:
            return depth
        depth += 1
        t = c
    
    return depth

def printAtDepthD(T,d):
    print(t)

def numLeaves(T):
    return 0

def fullNodes(T):
    return 1

def printDescending(T):
    print(t)
    
def printDescending(T):
    print(t)
    

if __name__ == "__main__":
    plt.close('all')
    T = btree.BTree()

    nums = [6, 3, 23,16, 11, 25, 7, 17,27, 30, 21, 14, 26, 8, 29, 
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
  
    t = T.find(4)
    for num in nums:
        T.insert(num)
        
    T.draw()
    
    
    
    
    print(largestAtDepthD(T,2))
    print(findDepth(T,23))