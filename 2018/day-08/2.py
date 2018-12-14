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
def proc_node(start):
    child_count = data[start]
    meta_count = data[start + 1]
    start += 2

    if child_count == 0:
        weight = sum(data[start: start + meta_count])
        start += meta_count
        return start, weight

    child_weights = []
    for i in xrange(child_count):
        start, weight = proc_node(start)
        child_weights.append(weight)

    weight = 0
    for m in data[start: start + meta_count]:
        m -= 1
        if m < len(child_weights):
            weight += child_weights[m]

    start += meta_count
    return start, weight

start, weight = proc_node(0)
assert(start == data_len)

print 'Answer', weight

# results
# Answer 22608
