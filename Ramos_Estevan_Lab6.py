import numpy as np
import matplotlib.pyplot as plt
import math
import random
import graph_AM as AMgraph
import graph_AL as ALgraph



def removeInfluence(G,v):
    #Given a graph and vertice removes all influence of vertice v in graph g
    if type(G) is ALgraph.Graph:
        for i in range(len(G.al)):#deletes the edges of al graph
            G.delete_edge(i,v)        
    else:
        for i in range(len(G.am)):
            G.delete_edge(i,v)#deltes the edges of an am graph
    
    

def findVimp(G, iters):
    #Given a graph and how many iterations prints out the most important vertice in the graph after each iteration
    if type(G) is ALgraph.Graph:#figures out the type of the grapj
        p = randomWalk(G,100000)
        print("Using random walk method and adjacency list representation")
    else:
        p = iterativeP(G)
        print("Using iterative method and adjacency matrix representation")
    
    v = 0
    for j in range(iters):
        for i in range(len(p)):#loop used to figure out gratest vertive
            if p[i] > p[v]:
                v = i        
                
        print("iteration", j,"most important vertex:",v,"with p =", p[v])
        removeInfluence(G,v)#removes the influence of the most important vertie
        if type(G) is ALgraph.Graph:
            p = randomWalk(G,10000)
        else:
            p = iterativeP(G)
        v = 0       #resets verice
        
        
def createGraphFromText(text, T):
    #gets a string representing a textfile and a type of tragph called T and creates a graph with the file based on the type
    E = list(text.split())#turns string into list
 
    if T is ALgraph.Graph:
        g = ALgraph.Graph(int(E[-1])+1) # creates graph for al graph
    else:
        g = AMgraph.Graph(int(E[-1])+1)#creates graph for am graph

    for i in range(0,len(E),2):
        g.insert_edge(int(E[i]),int(E[i+1]))#inserts edges into the graph
        
    return g
    
def outDegree(G,v):
    #given graph and vertice i returns the out degree of i
    count = 0
    for j in range(len(G.am[v])):
        if G.am[v][j] != -1:
            count += 1
    return count


def randomWalk(G,steps):
    #calculates the probability of visiting vertices of graph G in n number of steps 
    V  = []
    for i in range(len(G.al)):
        if G.al[i] != []:
            V.append(i)
    v = random.choice(V)
    visited = np.zeros(len(G.al))
    N = []
    for i in range(steps):
        visited[v] += 1
        for e in G.al[v]:
            N.append(e.dest)
        if not N:
            N = V
        u = random.choice(N)
        v = u
        N.clear()
        
    p = visited/steps
    p = [round(num, 6) for num in p]
    return p

def iterativeP(G):
    #calculates the probability of vesiting each matrix given graph G as a ajacency matrix
    p = np.zeros(len(G.am))
    p = p + 1/len(G.am)
    T = np.zeros((len(G.am),len(G.am)))
    
    for i in range(len(T)):
        out = outDegree(G , i)
        if out == 0:
            for j in range(len(T[i])):
                T[i][j] = 1/len(G.am)
        for j in range(len(T[i])):
            if G.am[i][j] != -1:
                T[i][j] = 1/out
    
    for i in range(1000):
        p = np.dot(p,T)
    
    p = np.round(p,5)
    return p

if __name__ == "__main__":   
    
    s = open('facebook_combined.txt', 'r', encoding = "utf8")# opens and reads the facebook combined text
    text = s.read() #reads the text
    
    G = createGraphFromText(text,ALgraph.Graph) # creates a graph for al case
    g = createGraphFromText(text,AMgraph.Graph)# creates a graph for am case
    
    s.close()
    
    findVimp(g,20)#finds the most important vertice over 10 iterations
    findVimp(G,20)
            
            
        
    