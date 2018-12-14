#!/usr/bin/python

import sys
from collections import defaultdict

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

# test
if False:
    data_lines = ['2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2\n']

data = [ int(s) for s in data_lines[0].split()]
data_lines = None
data_len = len(data)

idx = 0
meta_total = 0

# return next idx
def proc_node(d, start):
    global meta_total
    child_count = d[start]
    meta_count = d[start + 1]
    start += 2

    for i in xrange(child_count):
        start = proc_node(d, start)

    meta_total += sum(data[start: start + meta_count])
    start += meta_count

    return start

proc_node(data, 0)


print 'Answer', meta_total

# results
# Answer 45865
