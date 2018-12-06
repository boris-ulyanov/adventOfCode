#!/usr/bin/python

import sys

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

# test
# data_lines = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']

print 'readed recs:', len(data_lines)

unic_stor = set()

finished = False

for d in data_lines:
    d = d.strip()
    for x in xrange(len(d)):
        cutted_str = d[0:x] + d[x + 1:] + str(x)
        # print d, ':', cutted_str

        if cutted_str in unic_stor:
            print 'answer:', cutted_str, '(remove number in the end)'
            finished = True
            break

        unic_stor.add(cutted_str)

    if finished:
        break
