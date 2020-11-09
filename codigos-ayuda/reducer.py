
#!/usr/bin/env python
"""reducer.py"""

import sys

current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print ('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print ('%s\t%s' % (current_word, current_count))




"""

from operator import itemgetter 
from sys import stdin

import re

index = {}

for line in stdin:
        word, postings = line.split('\t')

        index.setdefault(word, {})

        for posting in postings.split(','):
                doc_id, count = posting.split(':')
                count = int(count)

                index[word].setdefault(doc_id, 0)
                index[word][doc_id] += count

for word in index:
        postings_list = ["%s:%d" % (doc_id, index[word][doc_id])
                         for doc_id in index[word]]

        postings = ','.join(postings_list)
        print('%s\t%s' % (word, postings))


"""
"""
current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print ('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print ('%s\t%s' % (current_word, current_count))    

"""

"""
word2count = {}
 
for line in stdin:
    # remove leading and trailing whitespace
    line = line.strip()
 
    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    try:
        word2count[word] = word2count[word]+count
    except:
        word2count[word] = count
 
# write the tuples to stdout
# Note: they are unsorted
for word in word2count.keys():
    print ('%s\t%s'% ( word, word2count[word] ))
"""