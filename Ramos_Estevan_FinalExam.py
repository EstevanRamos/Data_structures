import numpy as np
import matplotlib.pyplot as plt
import math
import singly_linked_list as sll
import bst
import btree
import graph_AL
import graph_AM
import hash_table_chain as htc

def set_drawing_parameters_and_save(ax,title):
    show_axis = 'on'
    show_grid = 'True'
    ax.set_aspect(1.0)
    ax.axis(show_axis)
    plt.grid(show_grid)
    fig.suptitle(title, fontsize=16)
    plt.show()
    fig.savefig(title+'.png')

def draw_squares(ax,n,x0,y0,side):
    if n == 0:
        return
    s = side/2
    x = x0 + np.array([-s,-s,s,s,-s])
    y = y0 + np.array([-s,s,s,-s,-s])
    ax.plot(x,y,linewidth=1.0,color='b')
    draw_squares(ax,n-1,x0,y0+s,side/2)
    draw_squares(ax,n-1,x0-s,y0-s,side/2)
    draw_squares(ax,n-1,x0+s,y0-s,side/2)
        
def smaller(L,i):
    if not L:
        return []
    if L[0] < i:
        return [L[0]] + smaller(L[1:],i)
    return smaller(L[1:],i)

def remove_second(L):
    if L.head == None or L.head.next == None:
        return
    if L.head.next.next == None:
        L.head.next = None
        L.tail = L.head
        return
    
    L.head.next = L.head.next.next
    return
    
def equal_row(a):
    eq = []
    equal = True
    for i in range(len(a)):
        for j in range(len(a[i])-1):
            if a[i][j] != a[i][j+1]:
                equal = False
        if equal:
            eq.append(i)
        equal = True
    
    return eq
            
def max_at_depth_bst(T,d):
    if T == None:
        return -math.inf
    if d == 0:
        return T.data
    
    return max(max_at_depth_bst(T.left,d-1),max_at_depth_bst(T.right,d-1))

def max_at_depth_btree(T,d):
    while d > 0:
        if T.is_leaf:
            return -math.inf
        T = T.child[-1]
        d -= 1
    return T.data[-1]

def remove_duplicates(L):
    h = htc.HashTableChain(len(L))
    R =[]
    for i in range(len(L)):
       if h.insert(L[i],L[i]) != -1:
           R.append(L[i])
    return R

def clique(G,u,v,w):
    if G.am[u][v] != -1 and G.am[u][w] != -1 and G.am[v][w]:
        return True
    return False
   
def first_ts(G):
    T = []
    in_degree = [0 for i in range(len(G.al))]
    for i in range(len(G.al)):
      for e in G.al[i]:
          in_degree[e.dest] += 1
    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            T.append(i)
    return T

def subsetsum(S,g):
    # Determines if there is a subset of S that adds up to g, where elements of S are positive integers
    # Simple solution; does not return the subset that adds up to g if it exists
    if g==0:
        return True
    if g<0 or len(S)==0:
    		return False
    return subsetsum(S[1:],g-S[0]) or subsetsum(S[1:],g) 

def subsetsum_count(S,g):
    # Copy of subsetsum. Modify this function to return number of solutions
    if g==0:
        return 1
    if g<0 or len(S)==0:
    	return 0
    return subsetsum_count(S[1:],g-S[0]) + subsetsum_count(S[1:],g) 
    

if __name__ == "__main__":

    plt.close("all") # Close all figures
    
    print('================ Question 1 ===============')
    fig, ax = plt.subplots()
    draw_squares(ax, 2, 0, 0, 1000)
    set_drawing_parameters_and_save(ax,'draw_squares(ax, 2, 0, 0, 1000)')
    
    fig, ax = plt.subplots()
    draw_squares(ax, 3, 0, 0, 1000)
    set_drawing_parameters_and_save(ax,'draw_squares(ax, 3, 0, 0, 1000)')
    
    fig, ax = plt.subplots()
    draw_squares(ax, 4, 0, 0, 1000)
    set_drawing_parameters_and_save(ax,'draw_squares(ax, 4, 0, 0, 1000)')

    print('================ Question 2 ===============')
    L2 =  [1, 7, 4, 3, 0, 9, 2, 5, 8, 6]
    print(smaller(L2,3))    # [1, 0, 2]
    print(smaller(L2,6))    # [1, 4, 3, 0, 2, 5]
    print(smaller(L2,9))    # [1, 7, 4, 3, 0, 2, 5, 8, 6]
    
    print('================ Question 3 ===============')
    L3a = sll.List()
    L3b = sll.List()
    L3c = sll.List()
    L3d = sll.List()
    L3b.extend([5])
    L3c.extend([7,8])
    L3d.extend([3, 0, 9, 2, 5])
    for L in [L3a,L3b,L3c,L3d]:  # Show original lists
        L.print()
        L.draw('Original list')
    
    for L in [L3a,L3b,L3c,L3d]:  
        remove_second(L)
    
    for L in [L3a,L3b,L3c,L3d]:  # Show modified lists
        L.print()
        L.draw('new list')
    # []
    # [5]
    # [7]
    # [3, 9, 2, 5]
    
    print('================ Question 4 ===============')
    A1 = np.array([[1],[2],[3]])
    A2 = np.array([[1,3],[2,2],[3,5],[7,7]])
    A3 = np.array([[1,3,5],[2,2,12],[3,3,3],[7,8,7],[5,8,7]])
    A4 = np.array([[1,3,5,6],[2,2,2,1],[3,3,5,6],[7,8,7,6],[5,8,7,2]])
    for a in [A1,A2,A3,A4]:  # Show arrays
        print(a)
    for a in [A1,A2,A3,A4]:  # Show results
        print(equal_row(a))    
    #[0, 1, 2]
    #[1, 3]
    #[2]
    #[]
   
    print('================ Question 5 ===============')
    L6 =[11, 6, 7, 16, 2, 4, 14, 8, 15, 1,  13,0]
    T = bst.BST()
    for a in L6:
        T.insert(a)
    T.draw()
    for i in range(6):
        print('depth:{}, max:{}'.format(i,max_at_depth_bst(T.root,i)))
    #depth:0, max:11
    #depth:1, max:16
    #depth:2, max:14
    #depth:3, max:15
    #depth:4, max:0
    #depth:5, max:-inf   
    
    print('================ Question 6 ===============')
    T = btree.BTree()
    L7 = [6, 3, 23,16, 11, 25, 7, 17,27, 30, 21, 14, 26, 8, 29, 
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
  
    t = T.find(4)
    for n in L7:
        T.insert(n) 
    T.draw()
    
    for i in range(4):
        print('depth:{}, max:{}'.format(i,max_at_depth_btree(T.root,i)))
    #depth:0, max:17
    #depth:1, max:27
    #depth:2, max:30
    #depth:3, max:-inf
    
    print('================ Question 7 ===============')
    print(remove_duplicates([4,2,7,9,7,8,1,9,2,4]))   # [4, 2, 7, 9, 8, 1]
    print(remove_duplicates([4,2,7,9,9,2,4]))         # [4, 2, 7, 9]
    print(remove_duplicates([2,2,4,4,4,2,4,4,2]))     # [2, 4]
    print(remove_duplicates([2302]))                  # [2302]
    print(remove_duplicates([]))                      # []
    
    print('================ Question 8 ===============')
    g8 = graph_AM.Graph(5)
    g8.insert_edge(0,1)
    g8.insert_edge(1,2)
    g8.insert_edge(1,3)    
    g8.insert_edge(0,3)
    g8.insert_edge(2,3)
    g8.insert_edge(3,4)
    g8.insert_edge(2,4)
    g8.display()
    g8.draw()
    
    for i in range(5):
        for j in range(i+1,5):
            for k in range(j+1,5):
                print('(u,v,w) = ({},{},{}), clique = {}'.format(i,j,k,clique(g8,i,j,k)))
                
    #(u,v,w) = (0,1,2), clique = False
    #(u,v,w) = (0,1,3), clique = True
    #(u,v,w) = (0,1,4), clique = False
    #(u,v,w) = (0,2,3), clique = False
    #(u,v,w) = (0,2,4), clique = False
    #(u,v,w) = (0,3,4), clique = False
    #(u,v,w) = (1,2,3), clique = True
    #(u,v,w) = (1,2,4), clique = False
    #(u,v,w) = (1,3,4), clique = False
    #(u,v,w) = (2,3,4), clique = True                
    
    print('================ Question 9 ===============')
    g9 = graph_AL.Graph(6,directed=True)
    g9.insert_edge(1,0)
    g9.insert_edge(1,2)
    g9.insert_edge(1,3)    
    g9.insert_edge(0,3)
    g9.insert_edge(2,3)
    g9.insert_edge(3,4)
    g9.insert_edge(2,4)
    g9.display()
    g9.draw()
    print('A topological sort could start with the following vertices:',first_ts(g9)) # [1, 5]
    g9.insert_edge(1,5)
    g9.display()
    g9.draw()
    print('A topological sort could start with the following vertices:',first_ts(g9)) # [1]
    
    g9.insert_edge(4,1)
    g9.display()
    g9.draw()
    print('A topological sort could start with the following vertices:',first_ts(g9)) # []
    
    print('================ Question 10 ===============')
    S = [1,2,3,4,6,7]
    for i in range(sum(S)+2):
        print('S=',S,'goal=',i,'number of solutions',subsetsum_count(S,i))
        
    #S= [1, 2, 3, 4, 6, 7] goal= 0 number of solutions 1
    #S= [1, 2, 3, 4, 6, 7] goal= 1 number of solutions 1
    #S= [1, 2, 3, 4, 6, 7] goal= 2 number of solutions 1
    #S= [1, 2, 3, 4, 6, 7] goal= 3 number of solutions 2
    #S= [1, 2, 3, 4, 6, 7] goal= 4 number of solutions 2
    #S= [1, 2, 3, 4, 6, 7] goal= 5 number of solutions 2
    #S= [1, 2, 3, 4, 6, 7] goal= 6 number of solutions 3
    #S= [1, 2, 3, 4, 6, 7] goal= 7 number of solutions 4
    #S= [1, 2, 3, 4, 6, 7] goal= 8 number of solutions 3
    #S= [1, 2, 3, 4, 6, 7] goal= 9 number of solutions 4
    #S= [1, 2, 3, 4, 6, 7] goal= 10 number of solutions 5
    #S= [1, 2, 3, 4, 6, 7] goal= 11 number of solutions 4
    #S= [1, 2, 3, 4, 6, 7] goal= 12 number of solutions 4
    #S= [1, 2, 3, 4, 6, 7] goal= 13 number of solutions 5
    #S= [1, 2, 3, 4, 6, 7] goal= 14 number of solutions 4
    #S= [1, 2, 3, 4, 6, 7] goal= 15 number of solutions 3
    #S= [1, 2, 3, 4, 6, 7] goal= 16 number of solutions 4
    #S= [1, 2, 3, 4, 6, 7] goal= 17 number of solutions 3
    #S= [1, 2, 3, 4, 6, 7] goal= 18 number of solutions 2
    #S= [1, 2, 3, 4, 6, 7] goal= 19 number of solutions 2
    #S= [1, 2, 3, 4, 6, 7] goal= 20 number of solutions 2
    #S= [1, 2, 3, 4, 6, 7] goal= 21 number of solutions 1
    #S= [1, 2, 3, 4, 6, 7] goal= 22 number of solutions 1        
    #S= [1, 2, 3, 4, 6, 7] goal= 23 number of solutions 1
    #S= [1, 2, 3, 4, 6, 7] goal= 24 number of solutions 0
