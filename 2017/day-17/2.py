#!/usr/bin/python

step_size = 329
position = 0
pos1 = -1

for i in xrange(1, 50000000 + 1):
    position = (position + step_size) % i + 1
    if position == 1:
        pos1 = i

print pos1
