import numpy as np

def swap_first_and_last(L):
    x = L[0]
    y = L[len(L)-1]
    
    L[0] = y
    L[len(L)-1] = x
    
def diagonal(A):
    B = np.zeros((len(A),len(A)))
    
    for i in range(len(A)):
        B[i][i] = A[i]
    return B


def greater_than_List(L,x):
    A = []
    for i in range(len(L)):
        if x<L[i]:
            A.append(L[i])
    return A

      

if __name__ == '__main__':
    L=[1,2,3,4,5]
    swap_first_and_last(L)
    print(L)
    print(diagonal(L))
    print(greater_than_List(L,2))