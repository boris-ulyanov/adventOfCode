#!/usr/bin/python

import sys
from collections import defaultdict

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

# test
# data_lines = ['dabAcCaCBAcCcaDA\n']
data = data_lines[0][:-1]
data_lines = None

print 'initial data size', len(data)

def react(d):
    iter_count = 0
    while True:
        iter_count += 1
        was_changes = False

        dest = []
        i = 0
        max_i = len(d) - 1
        while i < max_i:
            cur, nxt = ord(d[i]), ord(d[i + 1])

            if abs(cur - nxt) == 32:
                i += 2
                was_changes = True
                continue

            dest.append(d[i])
            i += 1

        # last sym
        if i == max_i:
            dest.append(d[max_i])

        if not was_changes:
            break
        d = dest
    return len(d)

def remove_code(source, symbol):
    symbol2 = chr(ord(symbol) + 32)
    return [s for s in source if (s != symbol) and (s != symbol2)]

# all used syms
used_symbols = []
for code in xrange(ord('A'), ord('Z') + 1):
    s1 = chr(code)
    s2 = chr(code + 32)
    if (s1 in data) or (s2 in data):
        used_symbols.append(s1)

# print 'used_symbols', used_symbols

best_len = None
best_code = None

for symbol in used_symbols:
    cutted_data = remove_code(data, symbol)
    len_after_react = react(cutted_data)
    if (best_len is None) or best_len > len_after_react:
        best_len = len_after_react
        best_code = code

print 'best_len', best_len
print 'best_code', best_code


# results
# initial data size 50000
# best_len 5122
# best_code 90
