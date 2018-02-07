#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#
# HELLLLOOOOO

# Variables used in create a line of output (reused)

# Handle first line
first = sys.stdin.readline().split("\t")
curr_node = first[0] # get node
new_rank = 0
prev_rank = 0
outlinks = ''
value_count = 0
try:
    new_rank = float(first[1]) # value is a new rank
except ValueError:
    # value is a previous rank, save it
    if first[1][0] == 'r':
        prev_rank = float(first[1][1:])
    # value is list of outlinks, save it
    else:
        outlinks = first[1][1:]

value_count += 1

for line in sys.stdin:
    split = line.split('\t')
    node = split[0]
    if node == curr_node:
        # parse the value
        try:
            new_rank = float(split[1]) # value is a new rank
        except ValueError:
            # value is a previous rank, save it
            if split[1][0] == 'r':
                prev_rank = float(split[1][1:])
            # value is list of outlinks, save it
            else:
                outlinks = split[1][1:]

        value_count += 1
        # if done with this node, write it as output
        if value_count == 3:
            sys.stdout.write('NodeId:'+str(curr_node)+'\t'+str(new_rank)+','+str(prev_rank)+','+outlinks)
            value_count = 0
    else:
        # update current node and parse the new value
        curr_node = node
        try:
            new_rank = float(split[1]) # value is a new rank
        except ValueError:
            # value is a previous rank, save it
            if split[1][0] == 'r':
                prev_rank = float(split[1][1:])
            # value is list of outlinks, save it
            else:
                outlinks = split[1][1:]

        value_count += 1
        # if done with this node, write it as output
        if value_count == 3:
            sys.stdout.write('NodeId:'+str(curr_node)+'\t'+str(new_rank)+','+str(prev_rank)+outlinks)
            value_count = 0
