#!/usr/bin/python

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

jumps = [int(line) for line in data_lines]
data_lines = None


pos = 0
steps = 0
l = len(jumps)

while True:
    j = jumps[pos]
    jumps[pos] = j + 1
    steps += 1
    pos = pos + j
    if pos >= l:
        break

print steps
