#!/usr/bin/env python

from sys import stdin

index = {}

for line in stdin:

        row = line.rstrip('\n').split()

        print ('%s\t%s' % (row[0], row[2]))

