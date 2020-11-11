#!/usr/bin/env python

from sys import stdin

for line in stdin:

        row = line.rstrip('\n').split()        
        
        print ("%s\t%s\t%d" % (row[0], row[1], 1))        
