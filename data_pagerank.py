
from os import listdir
import random

files = listdir('static/corpus/')

lines = ""
nodes = []

for file in files: 
	nodes.append(file)

last = len(nodes)-1
pos = 0

for file in files: 
	edges = random.randint(3, 7)

	for i in range(edges):
		neighbour = random.randint(0,last)

		while pos==neighbour:
			neighbour = random.randint(0,last)

		lines += file + '\t'+ nodes[neighbour] + '\n'

	pos +=1	

lines = lines[:-1]	

with open('pagerank.txt', 'w') as f:
	f.writelines(lines)

f.close()	
