import numpy as np
from random import shuffle
import time


def knapsack_backtracking(W,D,v,w):
    if W < 0:
        return False
    if D < 0:
        return True
    
    if not v or not w:
        return False
    
    return knapsack_backtracking(W-w[0],D-v[0],v[1:],w[1:]) or knapsack_backtracking(W,D,v[1:],w[1:])


def knapsack_greedy(W,D,v,w):
    v = np.array(v)
    w = np.array(w)
    wvr = v/w
    ind = np.argsort(-wvr)
    
    for i in range(len(wvr)):
        if W <= 0 or D <= 0:
            break
        W = W - w[ind[i]]
        D = D - v[ind[i]]
    
    if W >= 0 and D <= 0:
        return True
    return False

def knapsack_random(W,D,v,w):
    for i in range(10000):
        wv = list(zip(w,v))
        shuffle(wv)
        w, v = zip(*wv)
        for j in range(len(w)):
            if W <= 0 or D <= 0:
                break
            W = W - w[j]
            D = D - v[j]
        if W >= 0 and D <= 0:
            return True
    return False


if __name__ == "__main__":
    print('\n *********** Problem Set 1 **************')
    W = 35
    D = 221
    w = [10,  6, 10,  6, 14,  8,  5, 13,  4,  1]
    v = [39, 47, 47, 29, 71, 22, 50, 29, 51, 20]
    
    start = time.time()
    print("Can this problem be solved using random algorithim?",knapsack_random(W,D,v,w))
    end = time.time()
    print("this algorithim took ", end-start, " seconds")
    #print("Can this problem be solved using backtracking?",knapsack_backtracking(W,D,v,w)
    #print("Can this problem be solved using greedy algorithim?",knapsack_greedy(W,D,v,w))
    #print("Can this problem be solved using random algorithim?",knapsack_random(W,D,v,w))
       
    print('\n *********** Problem set 2 **************')
    W =  10
    D = 130
    w = [10,  6, 10,  6, 14,  8,  5, 13,  4,  1]
    v = [39, 47, 47, 29, 71, 22, 50, 29, 51, 20]
    
    start = time.time()
    print("Can this problem be solved using random algorithim?",knapsack_random(W,D,v,w))
    end = time.time()
    print("this algorithim took ", end-start, " seconds")
    #print("Can this problem be solved using backtracking?",knapsack_backtracking(W,D,v,w)
    #print("Can this problem be solved using greedy algorithim?",knapsack_greedy(W,D,v,w))
    #print("Can this problem be solved using random algorithim?",knapsack_random(W,D,v,w))

    print('\n *********** Problem set 3 **************')
    W = 102
    D = 404
    w = [10,  8,  5,  6,  9, 13, 13, 14, 13, 14,  6, 11, 12,  5, 13, 11,  9, 10, 14,  9]
    v = [47, 15,  7, 17, 29, 12, 45, 24, 26, 10, 37, 38, 14, 35, 44, 37, 27,45, 36, 40]
    
    start = time.time()
    print("Can this problem be solved using random algorithim?",knapsack_random(W,D,v,w))
    end = time.time()
    print("this algorithim took ", end-start, " seconds")
    #print("Can this problem be solved using backtracking?",knapsack_backtracking(W,D,v,w)
    #print("Can this problem be solved using greedy algorithim?",knapsack_greedy(W,D,v,w))
    #print("Can this problem be solved using random algorithim?",knapsack_random(W,D,v,w))

    
    print('\n *********** Problem set 4 **************')
    W = 150
    D = 600
    w = [10, 14,  4,  5,  8, 12,  5,  7,  7, 11,  9,  5, 10, 14,  4,  4, 14, 7,  8,  9]
    v = [39, 49, 47, 40, 20, 27, 31, 34, 17, 10, 29, 36, 41, 48, 45, 24, 15,17, 14, 40]
    
    start = time.time()
    print("Can this problem be solved using random algorithim?",knapsack_random(W,D,v,w))
    end = time.time()
    print("this algorithim took ", end-start, " seconds")
    #print("Can this problem be solved using backtracking?",knapsack_backtracking(W,D,v,w)
    #print("Can this problem be solved using greedy algorithim?",knapsack_greedy(W,D,v,w))
    #print("Can this problem be solved using random algorithim?",knapsack_random(W,D,v,w))
    
    print('\n *********** Problem set 5 **************')
    W = 200
    D = 960
    w = [ 8, 13, 13,  9,  5, 14, 13,  4,  8,  7, 13,  8, 12,  9, 13,  8,  5,
        9,  5,  7,  4,  7, 13, 13,  6,  8,  4,  5,  9, 10,  5,  4,  6, 10,
        7,  9, 13, 14, 12,  5, 10,  7,  9, 12,  9, 10,  5,  8, 11,  9]
    v = [21, 26, 25, 23, 42, 32, 45, 33, 40, 20, 44, 13,  9, 31, 47, 21, 31,
       18, 41, 36, 32, 43, 20, 40, 23, 16, 10, 44, 38,  6, 11, 13, 43,  7,
       35, 21,  7, 25, 47, 34, 33, 46, 26, 17, 23, 28, 42, 16, 28, 30]
    
    start = time.time()
    print("Can this problem be solved using random algorithim?",knapsack_random(W,D,v,w))
    end = time.time()
    print("this algorithim took ", end-start, " seconds")
    #print("Can this problem be solved using backtracking?",knapsack_backtracking(W,D,v,w))
    #print("Can this problem be solved using greedy algorithim?",knapsack_greedy(W,D,v,w))
    #print("Can this problem be solved using random algorithim?",knapsack_random(W,D,v,w))


    