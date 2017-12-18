#!/usr/bin/python

step_size = 329

# test
# step_size = 3

data = [0]

position = 0

for i in xrange(1, 2017 + 1):
    position = (position + step_size) % len(data) + 1
    data.insert(position, i)

print data[position - 2:position + 3]
