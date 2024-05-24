# Starter code for Lab 5

import numpy as np
import os
import hash_table_chain as htc

def get_word_list(text):
    # Receives a string containing a document
    # Returns a list of strings containing the words in the document
    text = text.lower()
    word_list = []
    curr_wrd = ''
    for c in text:
        if ord(c)>=97 and ord(c)<=122:
            curr_wrd = curr_wrd+c
        else:
            if len(curr_wrd)>0:
                word_list.append(curr_wrd)
                curr_wrd = ''
    return word_list

def print_hash_table_data(h,name):
    #recieves a has table and prints all of its data 
    count = 0
    emptyB = 0
    longB = 0           #counts all the different things of he hash
    longestBucket = 0
    print("analysis of",name, "hash:")
    for b in h.bucket:
        if len(b) < 1:          #empty bucket fraction
            emptyB += 1
        if len(b) > 1:
            longB += 1          #long bucket fraction
        if len(b) > longestBucket:
            longestBucket = len(b)  #gets the length of the longest bucket
        for rec in b:
            count += 1          #counts total records
    
    print("Total Buckets:", len(h.bucket), "total records:" , count, "Load Factor:", round(count/len(h.bucket),3))
    print("Empty bucket fraction in table:", round(emptyB/len(h.bucket),3 ))
    print("long bucket fraction in table:", round(longB/len(h.bucket),3))
    print("length of longest bucket", longestBucket)
    #prints everyting in format

    
def create_hash_table(L):
    #given a list returns a hash table of the list and a list of repeat words
    R = []#repeated words
    h = htc.HashTableChain(len(L)) # makes hash table based on the size of the list
    max,word = 0,""
    for i in range(len(L)): 
        h.insert(L[i],L[i])         #inserts the words from the list into the table
        if h.insert(L[i],L[i]) == -1:   
            R.append(L[i])  
            
        value = h.retrieve(L[i])
        if value == None: h.insert(L[i],1)#if its a repeat word append it to the list
        else: h.update(L[i],h.retrieve(L[i])+1)
        if h.retrieve(L[i])> max: max=h.retrieve(L[i] , word=L[i])
        return h, R


    
    
    


abs_dir = '.\\abstracts\\'  # abstracts folder must be in current folder. You may want to use an absolute path
file_list =   sorted(os.listdir(abs_dir)) # Abstract contains a list with all abstract file names


s = open('stop_words.txt', 'r', encoding = "utf8")# opens and reads the stop words file
text = s.read()
stopWords = get_word_list(text)
s.close()


sw,r = create_hash_table(stopWords)#makes a hashtable from the stopwords
print_hash_table_data(sw, "Stop Words")#prints the stop word hash table data

print('The list of files to analyze is:')
print(file_list)

for filename in file_list:
    f = open(abs_dir+filename, 'r', encoding="utf8")
   # print('\nFile:',filename)
    text = f.read()
    f.close()
   # print('Original text')
    #print(text)
    wl = get_word_list(text)
   # print('Word list')
   # print(wl)
   
    length = len(wl)
    k = 0
    
    for k in wl[:]:#removes the stopword from the list
        if sw.retrieve(k) != None:
            wl.remove(k)
    
    print()
    print("File:", filename)
    print("Total Words: ",length, " Total Non-Stop-words:", len(wl))
    
    h , repeats = create_hash_table(wl)#creates a hashtable from the wl
    print_hash_table_data(h, filename)#prints the has table info
    print_repeats(repeats)#prints the repeat words and how many times it comes up
        
    break # Uncomment to run a single iteration