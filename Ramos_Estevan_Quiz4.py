import bst

def childrenOfRoot(t):
    count = 0
    if t.root.left != None:
        count +=1
    if t.root.right != None:
        count +=1
    
    return count
    
def rootPredecessor(t):
    t = t.left
    while t.right != None:
        t = t.right
    return t.data

def treeToList(t):
    if t == None:
        return []
    
    return treeToList(t.left) + [t.data] + treeToList(t.right)
        
        


if __name__ == "__main__":

    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1,  20, 13]
    B =[25, 13, 11, 6, 7, 18, 14]
    

    T = bst.BST()
    T2 = bst.BST()
    
    for a in A:
        T.insert(a)

    for b in B:
        T2.insert(b)

    plt.close('all')
    T.draw()
    T2.draw()
    
    print(childrenOfRoot(T))  # 2
    print(childrenOfRoot(T2)) # 1
    
    print(rootPredecessor(T.root))  # 8
    print(rootPredecessor(T2.root)) # 18
    
    print(treeToList(T.root))  # [1, 2, 4, 6, 7, 8, 11, 13, 14, 15, 16, 17, 18, 20]
    print(treeToList(T2.root)) # [6, 7, 11, 13, 14, 18, 25]
    
    
