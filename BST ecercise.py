import bst

def printSmaller(t,k):
    if t == None:
        return
    if t.data < k:
        print(t.data)
    printSmaller(t.left,k)
    printSmaller(t.right,k)
  
def atDepthD(t,d):
    if t == None:
        return []
    if d == 0:
        return [t.data]
    return atDepthD(t.left,d-1) + atDepthD(t.right, d-1)

def tree2List(t):
    if t == None:
        return[]
    return tree2List(t.left) + t.data + tree2List(t.right)

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
        
    printSmaller(T.root,8)
    print(atDepthD(T.root,2))
    print(atDepthD(T2.root,2))
    
    print(tree2List(T.root))
    print(tree2List(T2.root))