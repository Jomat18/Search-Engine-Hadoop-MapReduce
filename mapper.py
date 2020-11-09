#!/usr/bin/env python

from sys import stdin
import re
import os

stopwords = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']

for line in stdin:

        # Get the file path
        doc_id = os.environ["map_input_file"]

		#temp = doc_id.split('_')        

		#doc_id = temp[1]

        # Get the name of the file from the path
        file = os.path.split(doc_id)[-1]  #get the names

        doc_id = file.split('_')[1]

        # Get an array of all the words inside the document
        line = " ".join(re.findall("[a-zA-Z]+", line))

        line = line.split()

        words = [word for word in line if word not in stopwords]

        #words = re.findall(r'\w+', line.strip())

        # Map the words
        for word in words:
        #for index in range(len(words)):
        #	word = words[index]	

            print("%s\t%s:1" % (word.lower(), doc_id))#, index))
        	#print ('{0}, {1}, {2}'.format( word.lower(), doc_id, index))
