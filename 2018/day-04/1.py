#!/usr/bin/python

import sys
from collections import defaultdict

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

# test
if False:
    data_lines = [
        '[1518-11-01 00:00] Guard #10 begins shift\n',
        '[1518-11-01 00:05] falls asleep\n',
        '[1518-11-01 00:25] wakes up\n',
        '[1518-11-01 00:30] falls asleep\n',
        '[1518-11-01 00:55] wakes up\n',
        '[1518-11-01 23:58] Guard #99 begins shift\n',
        '[1518-11-02 00:40] falls asleep\n',
        '[1518-11-02 00:50] wakes up\n',
        '[1518-11-03 00:05] Guard #10 begins shift\n',
        '[1518-11-03 00:24] falls asleep\n',
        '[1518-11-03 00:29] wakes up\n',
        '[1518-11-04 00:02] Guard #99 begins shift\n',
        '[1518-11-04 00:36] falls asleep\n',
        '[1518-11-04 00:46] wakes up\n',
        '[1518-11-05 00:03] Guard #99 begins shift\n',
        '[1518-11-05 00:45] falls asleep\n',
        '[1518-11-05 00:55] wakes up\n',
    ]

print 'readed recs:', len(data_lines)

data_lines.sort()

def chunks2mins(c):
    return int(c[1][3:5])

guard = None
total = {}
used_mins = defaultdict(lambda: [0] * 60)

for line in data_lines:
    chunks = line.split()
    record_type = chunks[2]

    if 'Guard' in record_type:
        guard = int(chunks[3][1:])
        asleep = None

    elif 'falls' in record_type:
        asleep = chunks2mins(chunks)

    elif 'wakes' in record_type:
        t = chunks2mins(chunks)
        dt = t - asleep
        total[guard] = total.get(guard, 0) + dt
        um = used_mins[guard]
        for m in xrange(asleep, t):
            um[m] += 1
        asleep = None

data_lines = None

# select best guard
max_total = 0
best_guard = None
for e in total:
    v = total[e]
    if max_total < v:
        max_total = v
        best_guard = e
    # print e, '==>> total:', v

print 'Best guard = ', best_guard
bg_used_mins = used_mins[best_guard]

# select best minute
max_mins = bg_used_mins[0]
max_mins_idx = 0
for m in xrange(1, 60):
    if max_mins < bg_used_mins[m]:
        max_mins = bg_used_mins[m]
        max_mins_idx = m

print 'Best min idx:', max_mins_idx, 'value:', max_mins
print 'Answer:', best_guard * max_mins_idx

# Best min idx: 54 value: 12
# Answer: 84834
