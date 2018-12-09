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
guards_total = {}
guards_freqs = defaultdict(lambda: [0] * 60)

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
        guards_total[guard] = guards_total.get(guard, 0) + dt
        freqs = guards_freqs[guard]
        for m in xrange(asleep, t):
            freqs[m] += 1
        asleep = None

data_lines = None

# select best guard + freq strategy 2
best_guard = None
best_freq = 0
for guard, freqs in guards_freqs.items():
    max_freq = max(freqs)
    if best_freq < max_freq:
        best_freq = max_freq
        best_guard = guard

best_mins = guards_freqs[best_guard].index(best_freq)

print 'Best guard:', best_guard
print 'Best freq:', best_freq
print 'Best mins:', best_mins
print 'Answer:', best_guard * best_mins

# Best min idx: 54 value: 12
# Answer: 84834
