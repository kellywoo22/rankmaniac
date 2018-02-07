#!/usr/bin/env python

import sys

d = {} # dictionary to hold node x, and PR(x)
SCALE = 0.85 # scale factor


first = sys.stdin.readline().split("\t")
node = int(first[0]) # get node
p = 0
try:
    p = float(first[1]) # value is a float
except ValueError:
    # value is list of outlinks or previous rank, just emit it
    sys.stdout.write(str(node)+'\t'+first[1]) 

infile = sys.stdin
next(infile) # skip the first line, already counted
node_count = 1

for line in infile:

    values = line.split("\t")
    node1 = int(values[0])
    r = 0
    try:
        r = float(values[1]) # value is a float
    except ValueError:
        # value is list of outlinks or previous rank, just emit it
        sys.stdout.write(str(node)+'\t'+values[1]) 
        continue
    if node1 == node:
        p += r
        node = node1
    else:
        node_count += 1
        d[node] = p
        p = r
        node = node1

d[node] = p
C = (1. - SCALE) / node_count

for key in d:
    d[key] = SCALE * d[key] + C
    sys.stdout.write(str(key)+'\t'+str(d[key])+'\n')


