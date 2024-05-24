# Implementation of binary search trees using lists
import matplotlib.pyplot as plt
import numpy as np
import math


def insert(T,newItem): # Insert newItem to BST T
    if T == None:  # T is empty
        T = [newItem,None,None]
    else:
        if newItem< T[0]:
            T[1] = insert(T[1],newItem) # Insert newItem in left subtree
        else:
            T[2] = insert(T[2],newItem) # Insert newItem in right subtree
    return T

def inOrder(T):
    if T!=None:
        inOrder(T[1])
        print(T[0],end=' ')
        inOrder(T[2])
        
def size(T): # returnds the number of data items stored in the tree
    if T == None:#base case
        return 0
    return 1 + size(T[1])+size(T[2])#returns t1 for the root and the size of the left subtree and the right subrtree

def minimum(T):#returns the smallest item stored in the tree
    if T[1] != None:
        return minimum(T[1])#traverses to the left
    return T[0]


def maximum(T):#returns the largest item stored in the tree
    if T[2] != None:
        return maximum(T[2])#traverses to the right
    return T[0]


def height(T):#returns the height of the tree
    if T == None:
        return 0
    return 1+ max(height(T[1]),height(T[2]))# returns the maximum height of the left and right subtree


def inTree(T,i):# returns true if item is in the tree
    if T != None:#base case
        if T[0] == i:#checks if item is in the tree
            return True
        else:
            return inTree(T[1],i) or inTree(T[2],i)#returns left and right subtree
    return False
    
def printByLevel(T):#prints the data items in the tree ordered by depth
    if T == None:#base case
        return None
    Q = [T]#creates a queue
    while len(Q)>0 :#while the q has items in it run this loop
        l = Q.pop(0)#pops the first item and stores it in l
        if l!= None:
            print(l[0], end = ' ')#prints the level
            Q.append(l[1])#adds the left subtree to the queue
            Q.append(l[2])#adds the right subtree to the queue

def tree2List(T):#returns a sorted list containing all the items in the tree
    if T == None:#base case
        return[]
    return tree2List(T[1]) + [T[0]] + tree2List(T[2]) #returns list of left root and right subtree

def leaves(T):#returns a list of items in the tree that are sorted in leaf nodes
    if T == None:#base case
        return []
    if T[1] == None and T[2] == None:# if it is a leaf return it
        return [T[0]]
    return leaves(T[1]) + leaves(T[2])# returns the left and right subtrees

def itemsAtDepthD(T,d):
    if T == None:# base case
        return []
    if d == 1:# if were at the depth return the node in a list
        return [T[0]]
    return itemsAtDepthD(T[1],d-1) + itemsAtDepthD(T[2],d-1)#return the left and right subtree untill were at correct depth

def depthOfK(T,k):#returns the depth of the node k
    if T[0] == k:#checks if k is in the tee
        return 0
    if k > T[0]:#if k is bigger then the root traverse the right subtree
        depth = 1 + depthOfK(T[2],k)
    else:#if its smaller traverse to the left subtree
        depth = 1 + depthOfK(T[1],k)
        
    if depth > 0:
        return depth#return the depth
    return -1#otherwise return -1

def draw(T, ax, x0=0, y0=0, delta_x = 1000, delta_y = 1200):#draw function gibven in class
    delta_x = max([20,delta_x])
    if T[1] is not None:
        ax.plot([x0-delta_x,x0],[y0-delta_y,y0],linewidth=1,color='k')
        draw(T[1],ax, x0-delta_x, y0-delta_y, delta_x/2, delta_y)
    if T[2] is not None:
        ax.plot([x0+delta_x,x0],[y0-delta_y,y0],linewidth=1,color='k')
        draw(T[2],ax, x0+delta_x, y0-delta_y, delta_x/2, delta_y)
    ax.text(x0,y0, str(T[0]), size=14,ha="center", va="center",
            bbox=dict(facecolor='w',boxstyle="circle"))


        
if __name__ == "__main__":
    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1, 20, 13]             
    T = None

    for a in A:
        #print('Inserting',a)
        T = insert(T,a)   
        #print(T)
        
    printByLevel(T)
    print(depthOfK(T,5))
    print(itemsAtDepthD(T,3))
    print(tree2List(T))
    print(leaves(T))
    print(inTree(T , 17))
    print(size(T))
    print(height(T))
    inOrder(T)
    fi, ax = plt.subplots()
    draw(T,ax)
    ax.axis('off')
    plt.show

