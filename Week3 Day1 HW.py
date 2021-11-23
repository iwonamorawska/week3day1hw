#!/usr/bin/env python
# coding: utf-8

# # Exercise 1
# Reverse the list below in-place using an in-place algorithm.
# For extra credit: Reverse the strings at the same time.

# In[7]:


words = ['this' , 'is', 'a', 'sentence', '.']

def swap(list,a,b,c,d,e):
    list[a], list[b],list[c], list[d], list[e]= list[e], list[d], list[c], list[b], list[a]
    return list

print(swap(words,0,1,2,3,4))


# # Exercise 2
# Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.
# Should output:
# {'a': 5,
# 'abstract': 1,
# 'an': 3,
# 'array': 2, ... etc...

# In[15]:


a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'
def word_count(str):
    counts= dict()
    words= str.split()
    
    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1
    return counts
print(word_count(a_text))


# # Exercise 3 
# Write a program to implement a Linear Search Algorithm. Also in a comment, write the Time Complexity of the following algorithm.

# In[20]:


def LinearSearch(nums_list,n,i):
    for nummies in range(0,n):
        if (nums_list[nummies]==i):
            return nummies
    return -1
nums_list = [10,23,45,70,11,15]
i=70
n=len(nums_list)
results=LinearSearch(nums_list,n,i)
if (results==-1):
    print("Element not found")
else:
    print("Element at index: ",results)


# # Regex Project 
# Use python to read the file regex_test.txt and print the last name on each line using regular expressions and groups (return None for names with no first and last name, or names that aren't properly capitalized)

# In[21]:
import re

with open("files/regex_test.txt") as f:
    data=f.readlines()
pattern=re.compile(("[A-Z][a-z]+),([A-Z][a-z]+),([A-Z][a-z])+"))

for person in data:
    match=pattern.search(person)
    if match:
        print('\n, f"{match.group(1)} {match.group(2)} {match.group(3)}')
    

