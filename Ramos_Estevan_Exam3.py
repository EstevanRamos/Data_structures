import graph_AL 
import graph_AM
import dsf
import matplotlib.pyplot as plt
import numpy as np
import math

def remove_even_odd(G):
    oe = 1
    for i in range(len(G.am)):
        if i % 2 == 1:
            oe = -1
        else:
            oe = 1
            
        for j in range(len(G.am)):
            if oe == 1:
                if j %2 == 1:
                    G.delete_edge(i,j)
            if oe == -1:
                if j%2 == 0:
                    G.delete_edge(i,j)
    return

def reverse_edge(G,u,v):
    if G.al[u] == None:
        return
    for e in G.al[u]:
        if e.dest == v:
            w = e.weight
            G.insert_edge(v,u,w)
            G.delete_edge(u,v)
    return

def first_prim(G):
    first_edge = [-1,-1,math.inf]
    for e in G.al[0]:
        if e.weight < first_edge[1]:
            first_edge = [0,e.dest,e.weight]
            
    return first_edge       

def largest_set(s):
    largest=0
    w = s.set_list()
    for i in range(len(w)):
        if len(w[i]) > largest:
            largest = len(w[i])
            
    return largest

def subsetsum(S,goal): 
    # Determines if there is a subset of S that adds up to g, where elements of S are positive integers
    # Return the subset that adds up to g if it exists or None if no such subset exists
    if goal ==0:
        return []
    if goal<0 or len(S)==0:
        return None # There is no solution
    subset = subsetsum(S[1:],goal-S[0]) # Take S[0]
    if subset != None: # There is a solution when taking S[0]
        return [S[0]] + subset
    else:   # There is no solution when taking S[0], try leaving S[0]
        return subsetsum(S[1:],goal) # Don't take S[0]

def partition(S):
    sumS = sum(S)
    goal = sumS//2
    subset  = subsetsum(S,goal)
    if subset==None:
        return None
    Sc =S.copy()
    for s in subset:
        Sc.remove(s)
    

    if sum(Sc) != sum(subset):
        return None
    return [subset,Sc]

def edit_distance(s1,s2,return_array=False):
    # Finds edit distance from s1 to s2
    # If return_array is True it will return that array containing edit distances for all substrings of s1 and s2
    d = np.zeros((len(s1)+1,len(s2)+1),dtype=int)
    d[-1,:] = len(s2)-np.arange(len(s2)+1)  # Fill out last row
    d[:,-1] = len(s1)-np.arange(len(s1)+1)  # Fill out last column
    for i in range(len(s1)-1,-1,-1):
        for j in range(len(s2)-1,-1,-1):
            if s1[i] ==s2[j]:
                d[i,j] =d[i+1,j+1]
            else:
                d[i,j] = 1 + min(d[i,j+1],d[i+1,j+1],d[i+1,j]) 
    if not return_array:
        d = d[0,0]
    return d

def same_last_character(d):
    i = len(d)-2
    j = len(d[0])-2
    
    if d[i][j] == 0:
        return True
    return False

if __name__ == "__main__":   
    
    plt.close("all")   
    
    print('\n *********** Question 1 **************')   
    g = graph_AM.Graph(5)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(1,3)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.display()
#    Graph representation
#    directed: False, weighted: False
#    Adjacency matrix:
#    [[-1  1  1 -1 -1]
#     [ 1 -1  1  1  1]
#     [ 1  1 -1  1 -1]
#     [-1  1  1 -1  1]
#     [-1  1 -1  1 -1]]
    g.draw('Question 1 orignal')
    remove_even_odd(g)
    g.display()  
#    Graph representation
#    directed: False, weighted: False
#    Adjacency matrix:
#    [[-1 -1  1 -1 -1]
#     [-1 -1 -1  1 -1]
#     [ 1 -1 -1 -1 -1]
#     [-1  1 -1 -1 -1]
#     [-1 -1 -1 -1 -1]]
    g.draw('Question 1 result')
    
    print('\n *********** Question 2 **************')
    g = graph_AL.Graph(5,weighted=True, directed = True)
    g.insert_edge(0,1,2)
    g.insert_edge(1,2,4)
    g.insert_edge(2,3,6)
    g.insert_edge(3,4,3)
    g.insert_edge(4,0,5)
    g.display()
#    Graph representation
#    directed: True, weighted: True
#    Adjacency list:
#    al[0]=[(1,2)]
#    al[1]=[(2,4)]
#    al[2]=[(3,6)]
#    al[3]=[(4,3)]
#    al[4]=[(0,5)]
    
    g.draw('Question 2 orignal')
    reverse_edge(g,2,3)
    g.display()
    
#    Graph representation
#    directed: True, weighted: True
#    Adjacency list:
#    al[0]=[(1,2)]
#    al[1]=[(2,4)]
#    al[2]=[]
#    al[3]=[(4,3)(2,6)]
#    al[4]=[(0,5)]    
    g.draw('Question 2 result')
    
    print('\n *********** Question 3 **************')
    g = graph_AL.Graph(5,weighted=True)
    g.insert_edge(0,1,2)
    g.insert_edge(1,2,4)
    g.insert_edge(2,3,6)
    g.insert_edge(3,4,3)
    g.insert_edge(4,0,1)
    g.insert_edge(3,0,5)
    g.display()
    g.draw('Question 3')
    print(first_prim(g))    # [0, 4, 1]
    
    print('\n *********** Question 4 **************')
    s = dsf.DSF(8)
    s.union(0,1)
    s.union(7,2)
    s.union(3,5)
    s.union(1,5)
    s.union(6,2)
    print(s.parent)
    #s.draw('Question 4')
    print(largest_set(s))  # 4
   
    print('\n *********** Question 5 **************')
    mySet =[2,5,8,9,12,21,33]
    print(partition(mySet))  # [[2, 5, 8, 9, 21], [12, 33]]
    mySet =[2,5,8]
    print(partition(mySet))  # None
    
    print('\n *********** Question 6 **************')
    d = edit_distance('MINERS','NERD', return_array=True)
    print(d)
    print(same_last_character(d))   # False
    d = edit_distance('MINERS','DATA STRUCTURES', return_array=True)
    print(d)
    print(same_last_character(d))   # True
    
    
    
   
    