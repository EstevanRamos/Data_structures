import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d
import graph_AL 
import graph_EL 

def num_vertices(G):
    #given am G return the number of vertices
    return(len(G.am))

def count_edges(G):
    #given AM G return the number of edges
    counter = 0
    for i in range(len(G.am)):
        for j in range(len(G.am[i])):
            if G.am[i][j] != -1:
                counter += 1
        
    return counter

def highest_weight_edge(G):
    #given graph G find the highest weighted edge
    max_weight = 0
    for i in range(len(G.am)):
        for j in range(len(G.am[i])):
            if G.am[i][j] > max_weight:
                max_weight = G.am[i][j]
    return max_weight

def reverse_edges(G):
    #given an am G reverse the direction of the edges
    temp = G.am[0][0]
    for i in range(len(G.am)):
        for j in range(len(G.am[i])):
            if G.am[i][j] != -1:
                temp = G.am[j][i]
                G.am[j][i] = G.am[i][j]
                G.am[i][j] = temp




if __name__ == "__main__":   
    plt.close("all")   
    g = Graph(5)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
  #  g.display()
   # g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    print(highest_weight_edge(g))
    print(count_edges(g))
    print(num_vertices(g))
    
    
    g = Graph(5,directed = True)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
   # g.display()
   # g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    print(highest_weight_edge(g))
    print(count_edges(g))
    print(num_vertices(g))
    
    g = Graph(5,weighted=True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
   # g.display()
   # g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    print(highest_weight_edge(g))
    print(count_edges(g))
    print(num_vertices(g))
    
    g = Graph(5,weighted=True,directed = True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
   # g.display()
   # g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    
    print(highest_weight_edge(g))
    print(count_edges(g))
    print(num_vertices(g))
    reverse_edges(g)
    g.display()