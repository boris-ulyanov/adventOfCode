#!/usr/bin/python

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()


counter = 0
for v in data_lines:
    counter += int(v)

print 'counter:' , counter
