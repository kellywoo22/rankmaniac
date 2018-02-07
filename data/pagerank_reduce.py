#!/usr/bin/env python

import sys

SCALE = 0.85 # scale factor
p = 0

for line in sys.stdin:

    values = line.split("\t")
    # Let iteration key pass through
    if values[0] == 'k':
        sys.stdout.write(line)
    else:
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

#    !/usr/bin/env python

# import sys

# d = {} # dictionary to hold node x, and PR(x)
# SCALE = 0.85 # scale factor

# first = sys.stdin.readline().split("\t")
# # Let iteration key pass through
# if first[0] == 'k':
#     sys.stdout.write(line)
# else:
#     node = int(first[0]) # get node
#     p = 0
#     try:
#         p = float(first[1]) # value is a float
#     except ValueError:
#         # value is not a float, just reemit it
#         sys.stdout.write(str(node)+'\t'+first[1]) 

# infile = sys.stdin
# next(infile) # skip the first line, already counted

# for line in infile:
#     # Let iteration key pass through
#     if line[0] == 'k':
#         print "hello"
#         print line
#         sys.stdout.write(line)
#         continue

#     values = line.split("\t")
#     node1 = int(values[0])
#     r = 0
#     try:
#         r = float(values[1]) # value is a float
#     except ValueError:
#         # value is not a float, just reemit it
#         sys.stdout.write(str(node)+'\t'+values[1]) 
#         continue
#     if node1 == node:
#         p += r
#         node = node1
#     else:
#         d[node] = SCALE * p + 1. - SCALE
#         p = r
#         node = node1

# d[node] = p

# for key in d:
#     sys.stdout.write(str(key)+'\t'+str(d[key])+'\n')
