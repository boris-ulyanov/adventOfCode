#!/usr/bin/python

import sys
from collections import defaultdict


data = [3,7]

STOP_AFTER = 939601

# test
# STOP_AFTER = 59414

pattern = [int(c) for c in str(STOP_AFTER)]

print 'pattern', pattern
pattern_len = len(pattern)

e1, e2 = 0, 1

last_checked = -1

while True:
    v1, v2 = data[e1], data[e2]
    v = v1 + v2

    if v >= 10:
        data.append(v / 10)
    data.append(v % 10)

    l = len(data)
    e1 = (e1 + v1 + 1) % l
    e2 = (e2 + v2 + 1) % l
    # print data

    for si in xrange(last_checked + 1, l - pattern_len):
        last_checked = si
        for x in xrange(pattern_len):
            equal = True
            if pattern[x] != data[si + x]:
                equal = False
                break

        if equal:
            print 'Answer', si
            sys.exit()

# Answer1 5832873106
