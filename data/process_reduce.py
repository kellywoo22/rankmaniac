#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#
# HELLLLOOOOO

for line in sys.stdin:
   pass #sys.stdout.write(line)

for i in range(20):
	sys.stdout.write('FinalRank:' +str(float(20 - i)) + '\t' +str(i) + '\n')

