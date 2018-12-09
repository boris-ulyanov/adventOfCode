#!/usr/bin/python

import sys
from collections import defaultdict

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

# test
# data_lines = ['dabAcCaCBAcCcaDA\n']
data = data_lines[0][:-1]
data_lines = None

iter_count = 0
while True:
    iter_count += 1
    was_changes = False

    dest = []
    i = 0
    max_i = len(data) - 1
    while i < max_i:
        cur, nxt = ord(data[i]), ord(data[i + 1])

        if abs(cur - nxt) == 32:
            i += 2
            was_changes = True
            continue

        dest.append(data[i])
        i += 1

    # last sym
    if i == max_i:
        dest.append(data[max_i])

    if not was_changes:
        break
    data = dest

print 'iter_count', iter_count
print 'Answer', len(data)

# results
# iter_count 519
# Answer 10774
