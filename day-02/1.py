#!/usr/bin/python


data_file = open('./data', 'r')

lines = data_file.readlines()

result = 0

for line in lines:
    nums_str = line.split()
    nums_int = [int(x) for x in nums_str]
    lmin = min(nums_int)
    lmax = max(nums_int)
    result += lmax - lmin

print result
