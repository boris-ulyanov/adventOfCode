#!/usr/bin/python

tgt_num = 368078
# tgt_num = 1024

side_size = 0
last_num = 1

while True:
    side_size += 2
    level_size = side_size * 4
    last_num += level_size

    if last_num >= tgt_num:
        break


print side_size, last_num


result = side_size / 2

n = (last_num - tgt_num) % side_size

result += abs(side_size / 2 - n)

print result
