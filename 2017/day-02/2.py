#!/usr/bin/python
 
data_file = open('./data', 'r')

lines = data_file.readlines()

result = 0

for line in lines:
    nums_str = line.split()
    nums_int = [int(x) for x in nums_str]
    nums_int.sort()
    nums_len = len(nums_int)

    for i1 in xrange(0, nums_len - 1):
        v1 = nums_int[i1]

        for i2 in xrange(i1 + 1, nums_len):
            v2 = nums_int[i2]
            if (v2 % v1) == 0:
                result += v2 / v1
                break

print result
