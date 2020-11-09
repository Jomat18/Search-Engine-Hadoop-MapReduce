#!/usr/bin/env python
"""mapper.py"""

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    #line = line.strip()
    line = " ".join(re.findall("[a-zA-Z]+", line))
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print ('%s\t%s' % (word, 1))


"""

from sys import stdin
import re

for line in stdin:
    # input comes from STDIN (standard input)
    #if len(line.strip())!=0:

    #line = " ".join(re.findall("[a-zA-Z]+", line))
    line = line.strip()

    words = line.split()
    # increase counters
    for word in words:
    # write the results to STDOUT (standard output);
    # what we output here will be the input for the
    # Reduce step, i.e. the input for reducer.py
    #
    # tab-delimited; the trivial word count is 1
        print ('%s\t%s' % (word, 1))
        #sys.stdout.write("{}\t1\n".format(word))
                    

"""
"""        
from sys import stdin
import re
import os

for line in stdin:

                # Get the file path
                doc_id = os.environ["files"]

                # Get the name of the file from the path
                doc_id = re.findall(r'\w+', doc_id)[-1]

                # Get an array of all the words inside the document
                words = re.findall(r'\w+', line.strip())

                # Map the words
                for word in words:
                                print("%s\t%s:1" % (word.lower(), doc_id))
"""
