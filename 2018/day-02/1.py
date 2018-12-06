#!/usr/bin/python

import sys

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

# test
# data_lines = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']

print 'readed recs:', len(data_lines)

ctr2 = 0
ctr3 = 0

for d in data_lines:
    sorted_string = sorted(d)

    has2 = False
    has3 = False

    prev = sorted_string[0]
    repeats = 1
    for c in sorted_string[1:]:
        if c == prev:
            repeats += 1
            continue
        has2 = has2 or (repeats == 2)
        has3 = has3 or (repeats == 3)
        repeats = 1
        prev = c

    has2 = has2 or (repeats == 2)
    has3 = has3 or (repeats == 3)

    if has2:
        ctr2 +=1
    if has3:
        ctr3 +=1

print 'ctr2', ctr2
print 'ctr3', ctr3
print 'answer', ctr2 * ctr3
