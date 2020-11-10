#!/usr/bin/env python

from re import findall
from sys import stdin
from os import path, environ

for line in stdin:

        # Get the file path
        doc_id = environ["map_input_file"]

        # Get the name of the file from the path
        doc_id = path.split(doc_id)[-1]

        #doc_id = doc_id.split('_')[1]
        #doc_id = "1_libro1827.txt"

        # Get an array of all the words inside the document
        words = line.rstrip('\n').split()
        #words = findall(r'\w+', line.strip())
        
        
        # Map the words
        for word in words:
        #for index in range(len(words)):
        #       word = words[index]     
                print ("%s\t%s:1" % (word, doc_id))#, index))
                #print ('{0}, {1}, {2}'.format( word.lower(), doc_id, index))
        
