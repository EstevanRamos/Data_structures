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
    longB = 0
    longestBucket = 0
    print("analysis of",name, "hash:")
    for b in h.bucket:
        if len(b) < 1:
            emptyB += 1
        if len(b) > 1:
            longB += 1
        if len(b) > longestBucket:
            longestBucket = len(b)
        for rec in b:
            count += 1
    
    print("Total Buckets:", len(h.bucket), "total records:" , count, "Load Factor:", round(count/len(h.bucket),3))
    print("Empty bucket fraction in table:", round(emptyB/len(h.bucket),3 ))
    print("long bucket fraction in table:", round(longB/len(h.bucket),3))
    print("length of longest bucket", longestBucket)

    
def create_hash_table(L):
    #given a list returns a hash table of the list and a list of repeat words
    R = []
    h = htc.HashTableChain(len(L))
    for i in range(len(L)):
        h.insert(L[i],L[i])
        if h.insert(L[i],L[i]) == -1:
            R.append(L[i])
    return h, R

def print_repeats(L):
    #given a list print the most common word is and how many times it repeats
    counter = 0
    word = L[0]
    for i in L:
        repeats = L.count(i)
        if repeats > counter:
            counter = repeats
            word = i
    print("the most common word is:", word, "- occurs", counter, "times")
    print()
    
    
    


abs_dir = '.\\abstracts\\'  # abstracts folder must be in current folder. You may want to use an absolute path
file_list =   sorted(os.listdir(abs_dir)) # Abstract contains a list with all abstract file names


s = open('stop_words.txt', 'r', encoding = "utf8")
text = s.read()
stopWords = get_word_list(text)
s.close()


sw,r = create_hash_table(stopWords)
print_hash_table_data(sw, "stopWords")

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
    
    for k in wl[:]:
        if k in stopWords:
            wl.remove(k)
    
    print()
    print("File:", filename)
    print("Total Words: ",length, " Total Non-Stop-words:", len(wl))
    
    h , repeats = create_hash_table(wl)
    print_hash_table_data(h, filename)
    print_repeats(repeats)
        
    break # Uncomment to run a single iteration