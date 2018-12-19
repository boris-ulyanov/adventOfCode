#!/usr/bin/python

import sys
from collections import defaultdict

GENERATIONS1 = 20
GENERATIONS2 = 50000000000

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

# test
if False:
    data_lines = [
        'initial state: #..#.#..##......###...###\n',
        '\n',
        '...## => #\n',
        '..#.. => #\n',
        '.#... => #\n',
        '.#.#. => #\n',
        '.#.## => #\n',
        '.##.. => #\n',
        '.#### => #\n',
        '#.#.# => #\n',
        '#.### => #\n',
        '##.#. => #\n',
        '##.## => #\n',
        '###.. => #\n',
        '###.# => #\n',
        '####. => #\n'
    ]

# initial state
source = [ 1 if sym == '#' else 0 for sym in data_lines[0][15:-1] ]
print 'source (initial):', source

# rules
rules = [0] * 32
for stroke in data_lines[2:]:
    result = stroke[9:10]
    if result != '#':
        continue
    idx = 1 if stroke[0] == '#' else 0
    idx += 2 if stroke[1] == '#' else 0
    idx += 4 if stroke[2] == '#' else 0
    idx += 8 if stroke[3] == '#' else 0
    idx += 16 if stroke[4] == '#' else 0
    rules[idx] = 1

assert(rules[0] == 0)  # empty not expand
print 'rules', rules
data_lines = None

# apply template
def app_rule(src, src_idx):
    l = len(src)
    def get_unbound(idx):
        if (idx < 0) or (idx >= l):
            return 0
        return src[idx]
    idx = 1 * get_unbound(src_idx - 2)
    idx += 2 * get_unbound(src_idx - 1)
    idx += 4 * get_unbound(src_idx)
    idx += 8 * get_unbound(src_idx + 1)
    idx += 16 * get_unbound(src_idx + 2)
    return rules[idx]

# proc
dest = [0]
dest_si = 0
shift = 0
repeated_generation = 0

# for g in xrange(GENERATIONS1):
for g in xrange(GENERATIONS2):
    l = len(source)
    si = source.index(1)

    ei = 0
    for i in xrange(l - 1, 0, -1):
        if source[i] == 1:
            ei = i
            break

    min_dest_len = ei - si + 1 + 4

    len_dest = len(dest)
    if len_dest < min_dest_len:
        # enlarge dest array
        dest.extend([0] * (min_dest_len - len_dest))

    shift = si - 2
    dest_si += shift

    if len_dest == min_dest_len:
        # check if stabilized
        equal = True
        for i in xrange(l):
            if source[i] != dest[i]:
                equal = False
                break
        if equal:
            print 'Found repeat on', g, 'generation => stabilized'
            print 'dest_si, shift', dest_si, shift
            repeated_generation = g
            break

    for dest_idx in xrange(min_dest_len):
        src_idx = dest_idx + shift
        dest[dest_idx] = app_rule(source, src_idx)

    # clean tail
    for dest_idx in xrange(min_dest_len, len(dest)):
        dest[dest_idx] = 0

    source, dest = dest, source


# only for
if repeated_generation > 0:
    dest_si += (GENERATIONS2 - repeated_generation - 1) * shift

print 'result source len:', len(source)
print 'result dest_si', dest_si

answer = 0
for x in xrange(len(source)):
    if source[x] == 1:
        answer += x + dest_si

print 'Answer', answer

# results
# Answer1 2767
# Answer2 2650000001362
