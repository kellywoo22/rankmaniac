#!/usr/bin/env python

# import sys

# NUM_ITERATIONS = 15
# final_rank = False
# iter_key_received = False

# # Variables used in create a line of output (reused)

# new_rank = 0
# prev_rank = 0
# outlinks = ''

# # Count to check that all 3 kinds of values have been received for a given key
# value_count = 0

# # dict of nodeid and values
# d = {}

# # dict of top 20 values
# top20 = {}

# # output string which is read as new input
# output = ''

# for line in sys.stdin:
#     split = line.split('\t')

#     # key is num interations
#     if split[0] == 'k':
#         k = int(split[1])
#         if (k+1 >= NUM_ITERATIONS):
#             final_rank = True
#         else:
#             sys.stdout.write('k'+'\t'+str(k+1)+'\n')
#         iter_key_received = True
#         continue

#     # otherwise key is a node
#     node = int(split[0])

#     # parse the value
#     try:
#         new_rank = float(split[1]) # value is a new rank
#     except ValueError:
#         # value is a previous rank, save it
#         if split[1][0] == 'r':
#             prev_rank = float(split[1][1:])
#         # value is list of outlinks, save it
#         else:
#             outlinks = split[1][1:]

#     value_count += 1
#     # if done with this node, write it as output
#     if value_count == 3:
#         if outlinks != '\n':
#             output += 'NodeId:'+str(node)+'\t'+str(new_rank)+','+str(prev_rank)+','+outlinks
#         else:
#             output += 'NodeId:'+str(node)+'\t'+str(new_rank)+','+str(prev_rank)+'\n'
#         value_count = 0
#         # update the top 20 dict
#         if len(top20) < 20:
#             top20[node] = float(new_rank)
#         else:
#             if min(top20.values()) < float(new_rank):
#                 del top20[min(top20, key=top20.get)]
#                 top20[node] = float(new_rank)


# #if iterations key hasn't been received, generate a new one 
# if not iter_key_received:
#     sys.stdout.write('k'+'\t'+'1'+'\n')

# if final_rank:
#     sorted_dict = sorted(top20, key=top20.get)
#     sorted_dict.reverse()
#     for key in sorted_dict:
#         sys.stdout.write('FinalRank:'+str(top20[key])+'\t'+str(key)+'\n')
# else:
#     sys.stdout.write(output)


import sys

NUM_ITERATIONS = 15
final_rank = False
iter_key_received = False

# Count to check that all 3 kinds of values have been received for a given key
value_count = 0

# dict of new pageranks
new_rank = {}
# dict of old pageranks
old_rank = {}
# dict of outlinks
outlinks = {}

# dict of top 20 values
top20 = {}

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

    else:
        # otherwise key is a node
        node = int(split[0])

        # parse the value
        try:
            rank = float(split[1]) # value is a new rank
            new_rank[node] = rank
            # update the top 20 dict
            if len(top20) < 20:
                top20[node] = rank
            else:
                if min(top20.values()) < rank:
                    del top20[min(top20, key=top20.get)]
                    top20[node] = rank
        except ValueError:
            # value is a previous rank, save it
            if split[1][0] == 'r':
                old_rank[node] = float(split[1][1:])
            # value is list of outlinks, save it
            else:
                outlinks[node] = split[1][1:]

#if iterations key hasn't been received, generate a new one 
if not iter_key_received:
    sys.stdout.write('k'+'\t'+'1'+'\n')

if final_rank:
    sorted_dict = sorted(top20, key=top20.get)
    sorted_dict.reverse()
    for key in sorted_dict:
        sys.stdout.write('FinalRank:'+str(top20[key])+'\t'+str(key)+'\n')
else:
    for key in new_rank:
        sys.stdout.write('NodeId:'+str(key)+'\t'+str(new_rank[key])+','+str(old_rank[key])+','+str(outlinks[key]))
