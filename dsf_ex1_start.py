import dsf

def is_singleton(s,v):
    if s.parent[v] == -1:
        for i in range(len(s.parent)):
            if s.parent[i] == v:
                return False
    else:
        return False
    
    return True

def is_compressed(s):
    for i in range(len(s.parent)):
        if s.parent[i] != -1 and s.parent[s.parent[i]] != -1:
            
            return False
    return True

if __name__ == "__main__":   
    plt.close("all")      
    s = dsf.DSF(8)
    s.union(0,7)
    
    s.union(0,1)
    print(s.parent)
    print(is_compressed(s))  # True
    
    s.union(7,2)
    print(s.parent)
    print(is_compressed(s))  # True
    
    s.union(3,5)
    print(s.parent)
    print(is_compressed(s))  # True
    
    s.union(1,5)
    print(s.parent)
    print(is_compressed(s))  # False
    
    print(is_compressed(s))
    s.draw()
    print('Set of sets:',s.set_list())
    # Set of sets: [[0, 1, 3, 5], [4], [6], [2, 7]]
    
    for v in range(8):
        print('is_singleton(s,{}): {}'.format(v,is_singleton(s,v)))
    '''
    is_singleton(s,0): False
    is_singleton(s,1): False
    is_singleton(s,2): False
    is_singleton(s,3): False
    is_singleton(s,4): True
    is_singleton(s,5): False
    is_singleton(s,6): True
    is_singleton(s,7): False
    '''
    
    
     