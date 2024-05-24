import dsf



def singletons(s,v):
    #that receives a disjoint set forest and an integer v and determines if v 
    #is a singleton in s.
    if s[v] = -1:
        for i in range(len(s)):
            if s[i] == v:
                return false
    else:
        return false
    return true

def is_compressed(s):
    #that receives a disjoint set forest s and determines if s is compressed.
    for i in range(len(s)):
        if s[i] != -1 or s[s[i]] != -1:
            return False
    return True
            
            
            