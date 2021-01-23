# Filename: Permutations.py
# Author: Kyle C Larson
# Description: this file defines a functon that gives all permutations of a string
class Node(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.children = []
    def add_child(self, obj):
        self.children.append(obj)

#def remove_duplicates(iStrs):
#remove all duplicate strings in the array of strings iStrs
#led to inneficient 12000ms timeout on codewars server
#    if(len(iStrs)==0):
#       return []
#    else:
#        elements=[iStrs[0]]
#        i = 0
#        for c1 in iStrs:
#            i=0
#            c2 = elements[0]
#            while(c1 != c2):
#                i+=1
#                if(i==len(elements)):
#                    elements+=[c1]
#                c2 = elements[i]
#        return elements
def not_contains(arr, Str):
    for c1 in arr:
        if(c1 == Str):
             return False
    return True 

def swap(arr, i1, i2):
#swaps the elements at the given indices and returns the new array
    out = arr
    out = out[:i1] + out[i2] + out[i1+1:]
    out = out[:i2] + arr[i1] + out[i2+1:]
    return [out]

def permutations(inStr):
#this function returns the number of permutations of the characters in the input (inStr)
#this python implementation is based on the psuedocode provided on the wikipedia page for 
#Heap's algorithm at https://en.wikipedia.org/wiki/Heap%27s_algorithm
    c =[]
    n = len(inStr)
    for i in range(0, n):
        c+=[0]
        
    output = [inStr]
    i =0
    while( i<n ):
        if(c[i] < i):
            if(i %2 == 0):
                temp = swap(output[len(output)-1], 0, i)
                if(not_contains(output, temp[0])):
                    output += temp
            else:
                temp = swap(output[len(output)-1], c[i], i)
                if(not_contains(output, temp[0])):
                    output += temp
            
            c[i]=c[i]+1
            i =0
        else:
            c[i] = 0
            i+=1
            
    return output

print(permutations('aabb'))