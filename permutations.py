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

def permutations(inStr):
	# a, b, c, ...
	# a -> b, c, ...
	# a -> c, b, 
	# a
	# b, c
	# de, fg
	k = 0
	output = [inStr]
	while( k > 1):
		
		for i in range(0, k-1):
			#see heaps algorithm
	
	
start_of_tree = Node('Start', 'a')
start_of_tree.add_child(Node('End', 'b'))
print(start_of_tree.children[0].name)

