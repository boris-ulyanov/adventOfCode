#!/usr/bin/python

start_a = 873
start_b = 583

# test
# start_a = 65
# start_b = 8921

value_a = start_a
value_b = start_b

result = 0

for x in xrange(5000000):

    while True:
        value_a = (value_a * 16807) % 2147483647
        if (value_a % 4) == 0:
            break

    while True:
        value_b = (value_b * 48271) % 2147483647
        if (value_b % 8) == 0:
            break

    # print value_a, value_b

    if (value_a & 0xffff) == (value_b & 0xffff):
        result += 1


print 'Result', result
