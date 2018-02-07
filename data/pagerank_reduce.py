#!/usr/bin/env python

import sys

d = {} # dictionary to hold node x, and PR(x)
SCALE = 0.85 # scale factor


first = sys.stdin.readline().split("\t")
node = int(first[0]) # get node
p = 0
flag = 0


for line in sys.stdin:

    values = line.split("\t")
    node = int(values[0])

    try:
        r = float(values[1]) # value is a float
    except ValueError:
        if values[1].find('r'):

            d = SCALE * p + 1. - SCALE
            p = 0

        # value is list of outlinks or previous rank, just emit it
            sys.stdout.write(str(node)+'\t'+str(d)+'\n')
        sys.stdout.write(str(node)+'\t'+values[1]) 
        continue
    p += r





