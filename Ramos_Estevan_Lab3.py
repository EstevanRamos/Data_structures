# Code to implement and display singly-linked lists
# Programmed by Estevan Ramos
# Last modified March 1, 2020

import matplotlib.pyplot as plt
import numpy as np

class ListNode:
    # Constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class List:
    # Constructor
    def __init__(self,head = None,tail = None):
        self.head = head
        self.tail = tail

    def print(self):
        t = self.head
        while t is not None:
            print(t.data,end=' ')
            t = t.next
        print()

    def append(self,x):
        #add item x to the list
        if self.head is None: #List is empty
            self.head = ListNode(x)
            self.tail = self.head
        else:
            self.tail.next = ListNode(x)
            self.tail = self.tail.next

    def extend(self,python_list):
        #adds list of items to the list
        for d in python_list:
            self.append(d)

    def _rectangle(self,x0,y0,dx,dy):
        # Returns the coordinates of the corners of a rectangle
        # with bottom-left corner (x0,y0), dx width and dy height
        x = [x0,x0+dx,x0+dx,x0,x0]
        y = [y0,y0,y0+dy,y0+dy,y0]
        return x,y

    def draw(self,figure_name=' '):
        # Assumes the list contains no loops
        fig, ax = plt.subplots()
        ax.plot()
        x, y = self._rectangle(0,0,20,20)
        ax.plot(x,y,linewidth=1,color='k')
        ax.plot([0,20],[10,10],linewidth=1,color='k')
        ax.text(-2,15, 'head', size=10,ha="right", va="center")
        ax.text(-2,5, 'tail', size=10,ha="right", va="center")
        t = self.head
        x0 = 40
        while t !=None:
            x, y = self._rectangle(x0,0,30,20)
            ax.plot(x,y,linewidth=1,color='k')
            ax.plot([x0+15,x0+15],[0,20],linewidth=1,color='k')
            ax.text(x0+7,10, str(t.data), size=10,ha="center", va="center")
            if t.next == None:
                ax.text(x0+22,10, '/', size=15,ha="center", va="center")
            else:
                ax.plot([x0+22,x0+40],[10,10],linewidth=1,color='k')
                ax.plot([x0+37,x0+40,x0+37],[7,10,13],linewidth=1,color='k')
            t = t.next
            x0 = x0+40
        if self.head == None:
            ax.text(12,15, '/', size=10,ha="center", va="center")
        else:
            ax.plot([10,40],[15,15],linewidth=1,color='k')
            ax.plot([37,40,37],[12,15,18],linewidth=1,color='k')

        if self.tail == None:
            ax.text(12,5, '/', size=10,ha="center", va="center")
        else:
            xt = 40
            t = self.head
            while t!= self.tail:
                t = t.next
                xt+=40
            ax.plot([10,10,xt+15,xt+15],[5,-10,-10,0],linewidth=1,color='k')
            ax.plot([xt+12,xt+15,xt+18],[-3,0,-3],linewidth=1,color='k')

        ax.set_title(figure_name)
        ax.set_aspect(1.0)
        ax.axis('off')
        fig.set_size_inches(1.2*(x0+200)/fig.get_dpi(),100/fig.get_dpi())
        plt.show()
        
        
    def insert(self,i,x):
        #inserts x and inex i
            if i == 0 : # for if i is 0
                node = ListNode(x)
                node.next = self.head
                self.head = node
            
            j = self.head
            
            for k in range(i-1):# otherwise do this
                j = j.next
            node = ListNode(x)
            node.next = j.next
            j.next = node
            
                
    def remove(self, x):
        # removes item x from the list
        j = self.head
        if j.data == x:# for if x is the first item
            self.head = j.next
        
        while j != None:# otherwise do this
            if j.next.data == x:
                j.next = j.next.next
                break
            j = j.next
                
    def pop(self, i = None):
        # pops item i if i isnt specified it pops the tail
        j = self.head
        while j.next != None:
            if j == i:
                break
            j = j.next
        return j
    
    def clear(self):
        #clears the list
        self.head = None
        self.tail = None
        
#    def index(self,x , start = 0 , end = 0):
#        j = self.head
#        i = 0
#        for i in range(end)
            
    def count(self,x):
        #counts how many times x appears in the list
        counter = 0# keeps count
        j = self.head
        while j != None:
            if j.data == x:
                counter += 1
            j = j.next
        
        return counter
        
    def sort(self):
        #sorts the list 
        j = self.head
        while j != None:#runs for how many nodes there are in the list
            k = self.head # starts at the heads
            while k.next != None: 
                if k.data > k.next.data: # if k.next is greater the k swap them
                    k.data, k.next.data = k.next.data , k.data# swap happens here
                k = k.next#indexes k
            j = j.next#indxes j
        
    def reverse(self):
        #reverses the list in place
        j = self.head #for current node
        prev = None # for the previous node
        while j != None:
            k = j.next # k is the next node
            j.next = prev # sets current node to point to the previous
            prev = j# sets the prev to j
            j = k # sets j to the next node
        self.head = prev
        
    def copy(self):
        #creates and returns a copy of the list
        L1 = List(self.head,self.tail)
        return L1
    
            
            

if __name__ == "__main__":
    # It won't execute when this file is imported

#    plt.close('all')
#    L1 = List()
#    L1.draw('Empty list')
#    L1.extend(list(np.random.permutation(10)))
#    L1.draw('Unsorted list')
#    L1 = List()
#    L1.extend(list(np.arange(10)))
#    L1.draw('Sorted list')
#    L1.tail = L1.head.next.next
#    L1.draw('Bad list!')
#    L1.tail = None
#    L1.draw('Another bad list!')
    
    L1 = List()
    L1.extend(list(np.random.permutation(10)))
    L1.draw('Unsorted og list')
    
    L2 = L1.copy()
    L2.reverse()
    L2.draw('reverse copy list')
    
    L2.sort()
    L2.draw('sorted list')
    
    L2.clear()
    L2.draw('cleared list')
    
    L2.extend([1,2,3,1,4,5,1,6,7,1])
    L2.draw('count 4')
    print(L2.count(1))
    
    L2.remove(1)
    L2.draw('removed 1s')
    print(L2.pop())
    
    L2.insert(2,44)
    L2.draw('inserted 44 at 2')
    



