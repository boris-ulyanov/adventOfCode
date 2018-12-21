#!/usr/bin/python

import sys
from collections import defaultdict

data = [3,7]

STOP_AFTER = 939601

# test
# STOP_AFTER = 2018

min_size = STOP_AFTER + 10

e1, e2 = 0, 1
while True:
    if len(data) >= min_size:
        break

    v1, v2 = data[e1], data[e2]
    v = v1 + v2

    if v >= 10:
        data.append(v / 10)
    data.append(v % 10)

    l = len(data)
    e1 = (e1 + v1 + 1) % l
    e2 = (e2 + v2 + 1) % l
    # print data


def print_answer(d, after):
    if len(d) >= (after + 10):
        d = [ str(item) for item in data[after: after + 10]]
        print 'After', after, ''.join(d)
    else:
        print 'After', after, 'no data'


print_answer(data, 9)
print_answer(data, 5)
print_answer(data, 18)
print_answer(data, 2018)
print_answer(data, 939601)

# Answer1 5832873106
