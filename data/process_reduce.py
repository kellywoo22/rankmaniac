#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#
# HELLLLOOOO

NUM_ITERATIONS = 3
final_rank = False
iter_key_received = False

# Variables used in create a line of output (reused)
curr_node = 0
new_rank = 0
prev_rank = 0
outlinks = ''

# Count to check that all 3 kinds of values have been received for a given key
value_count = 0

# dict of top 20 values
pr_dict = {}

# output string which is read as new input
output = ''

# Handle first line
first = sys.stdin.readline().split("\t")

# key is num interations
if first[0] == 'k':
    k = int(first[1])
    if (k+1 >= NUM_ITERATIONS):
        final_rank = True
    else:
        sys.stdout.write('k'+'\t'+str(k+1)+','+str(prev_rank)+'\n')
    iter_key_received = True

# key is a node
else:
    curr_node = int(first[0])
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

    # key is num interations
    if split[0] == 'k':
        k = int(split[1])
        if (k+1 >= NUM_ITERATIONS):
            final_rank = True
        else:
            sys.stdout.write('k'+'\t'+str(k+1)+'\n')
        iter_key_received = True
        continue

    # otherwise key is a node
    node = int(split[0])

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
            if outlinks != '\n':
                output += 'NodeId:'+str(curr_node)+'\t'+str(new_rank)+','+str(prev_rank)+','+outlinks
            else:
                output += 'NodeId:'+str(curr_node)+'\t'+str(new_rank)+','+str(prev_rank)+'\n'
            value_count = 0
            # update the top 20 dict
            if len(pr_dict) < 20:
                pr_dict[curr_node] = float(new_rank)
            else:
                if min(pr_dict.values()) < float(new_rank):
                    del pr_dict[min(pr_dict, key=pr_dict.get)]
                    pr_dict[curr_node] = float(new_rank)
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
            if outlinks != '\n':
                output += 'NodeId:'+str(curr_node)+'\t'+str(new_rank)+','+str(prev_rank)+','+outlinks
            else:
                output += 'NodeId:'+str(curr_node)+'\t'+str(new_rank)+','+str(prev_rank)+'\n'
            value_count = 0
            # update the top 20 dict
            if len(pr_dict) < 20:
                pr_dict[curr_node] = float(new_rank)
            else:
                if min(pr_dict.values()) < float(new_rank):
                    del pr_dict[min(pr_dict, key=pr_dict.get)]
                    pr_dict[curr_node] = float(new_rank)

#if iterations key hasn't been received, generate a new one 
if not iter_key_received:
    sys.stdout.write('k'+'\t'+'1'+'\n')

if final_rank:
    sorted_dict = sorted(pr_dict, key=pr_dict.get)
    sorted_dict.reverse()
    for key in sorted_dict:
        sys.stdout.write('FinalRank:'+str(pr_dict[key])+'\t'+str(key)+'\n')
else:
    sys.stdout.write(output)