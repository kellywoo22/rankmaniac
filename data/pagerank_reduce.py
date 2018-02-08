#!/usr/bin/env python

import sys

SCALE = 0.85 # scale factor

first = sys.stdin.readline().split("\t")
if first[0] == 'k':
    sys.stdout.write(first)
else:
    node = int(first[0]) # get node
    p = 0
    try:
        p = float(first[1]) # value is a float
    except ValueError:
        # value is not a float, just reemit it
        sys.stdout.write(str(node)+'\t'+first[1]) 

infile = sys.stdin
next(infile) # skip the first line, already counted

for line in infile:

    values = line.split("\t")
    # Let iteration key pass through
    if values[0] == 'k':
        sys.stdout.write(line)
    else:
        node1 = int(values[0])
        try:
            r = float(values[1]) # value is a float
        except ValueError:
            # value is not a float, just reemit it
            sys.stdout.write(str(node)+'\t'+values[1]) 
            continue
        # at this point the line must be an int, so it is the rank
        if node1 == node:
        # if node same as previous, then keep adding rank
            p += r
        else:
            # otherwise calculate the rank
            d = SCALE * p + 1. - SCALE
            p = r
            # output the node and rank
            sys.stdout.write(str(node)+'\t'+str(d)+'\n')
            # set new node
            node = node1
# account for the last node
d = SCALE * p + 1. - SCALE
sys.stdout.write(str(node)+'\t'+str(d)+'\n')
