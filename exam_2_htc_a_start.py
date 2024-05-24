import matplotlib.pyplot as plt
import numpy as np
import hash_table_chain as htc

def same_hash_as_k(h,k):
    sh = []
    for b in h.bucket:
        for i in b:
            if h.h(k) == h.h(i.key):
                sh.append(i.key)
    return sh
    
def intersection(L1,L2):
    ints = []
    return ints
    
def invert_hash(h):
    hi = htc.HashTableChain(len(h.bucket))
    return hi
    

if __name__ == "__main__":  
    plt.close('all') 
    
    countries = ['Russia','Canada', 'USA', 'Brazil', 'Australia', 'China','Spain','France']
    capitals = ['Moscow','Ottawa', 'Washington', 'Brasilia', 'Canberra', 'Beijing','Madrid','Paris']
    h = htc.HashTableChain(len(countries))

    for i in range(len(countries)):
        h.insert(countries[i],capitals[i])
    h.print_table()
    '''
    Table contents:
    bucket 0: [ [Australia, Canberra] ]
    bucket 1: [ [Spain, Madrid] ]
    bucket 2: [ ]
    bucket 3: [ [Russia, Moscow] [USA, Washington] [France, Paris] ]
    bucket 4: [ [Brazil, Brasilia] ]
    bucket 5: [ ]
    bucket 6: [ [Canada, Ottawa] ]
    bucket 7: [ [China, Beijing] ]
    '''    
    
    print(same_hash_as_k(h,'Russia')) # ['Russia', 'USA', 'France']
    print(same_hash_as_k(h,'Canada')) # ['Canada']
    
    h2 = invert_hash(h)
    h2.print_table()
    '''
    Table contents:
    bucket 0: [ [Washington, USA] ]
    bucket 1: [ ]
    bucket 2: [ [Moscow, Russia] ]
    bucket 3: [ [Paris, France] ]
    bucket 4: [ [Ottawa, Canada] ]
    bucket 5: [ [Madrid, Spain] [Brasilia, Brazil] ]
    bucket 6: [ [Canberra, Australia] [Beijing, China] ]
    bucket 7: [ ]
    '''
    L1 = [2,3,5,7,11,13]
    L2 = [3,4,5,11,17]
        
    print(intersection(L1,L2))  # [3, 5, 11]