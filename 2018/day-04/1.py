#!/usr/bin/python

import sys

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

# def dump_field():
#     for y in xrange(max_y + 1):
#         print field[y]
#     print


# parse input line, return
def parse_line(line):
    date_str = line[1:12]
    hour_str = line[12:14]
    mins_str = line[15:17]
    text_str = line[19:-1]

    date_chunks = date_str.split('-')
    year = int(date_chunks[0])
    month = int(date_chunks[1])
    day = int(date_chunks[2])
    assert(year == 1518)
    d = month * 100 + day

    h = int(hour_str)
    m = int(mins_str)

    assert(h == 0 or h == 23)
    assert(m >= 0 or m <= 59)

    t = 'x'
    gid = -1
    text_header = text_str[:5]
    if text_header == 'Guard':
        t = 'g'
        # 'Guard #99 begins shift\n'
        gid = int(text_str.split()[1][1:])
    elif text_header == 'wakes':
        t = 'w'
    elif text_header == 'falls':
        t = 'f'
    else:
        print 'header for', line, ' == ', text_header

    assert(t != 'g' or gid != -1)
    return (d, h, m, t, gid)

IDX_D = 0
IDX_H = 1
IDX_M = 2
IDX_T = 3
IDX_G = 4

recs = map(parse_line, data_lines)
data_lines = None

# sort by hrono
def compaareByHrono(a, b):
    if a[IDX_D] < b[IDX_D]:
        return -1
    if a[IDX_D] > b[IDX_D]:
        return 1
    if a[IDX_H] < b[IDX_H]:
        return -1
    if a[IDX_H] > b[IDX_H]:
        return 1
    if a[IDX_M] < b[IDX_M]:
        return -1
    if a[IDX_M] > b[IDX_M]:
        return 1
    return 0
recs.sort(cmp=compaareByHrono)


# agregate time (separate for each guard) + grouping intervals
summary = {}
cur_gid = False
cur_start = False

for r in recs:
    print r
    t = r[IDX_T]
    if t == 'g':
        assert(not cur_start)
        gid = r[IDX_G]
        if gid == 57 or gid == 26:
            print '>>>>>>>'
        if gid not in summary:
            summary[gid] = {'total': 0, 'intervals': []}
        cur_gid = summary[gid]

    elif t == 'f':
        assert(not cur_start)
        cur_start = r[IDX_M]

    elif t == 'w':
        assert(not cur_start is False)
        end = r[IDX_M]
        dt = end - cur_start
        cur_gid['total'] += dt
        cur_gid['intervals'].append((cur_start, end))
        cur_start = False

    else:
        assert(False)

# select best guard
max_total = 0
max_gid = False
for e in summary:
    t = summary[e]['total']
    if max_total < t:
        max_total = t
        max_gid = e
    # print e, '==>>', summary[e]
    print e, '==>> total:', t, 'intervals:', len(summary[e]['intervals'])

print 'Best guard id = ', max_gid

# select best minute
used_mins = [0] * 60
for interval in summary[max_gid]['intervals']:
    for x in xrange(interval[0], interval[1]):
        used_mins[x] += 1

print used_mins

max_min = 0
max_min_idx = 0
for m in xrange(60):
    if max_min < used_mins[m]:
        max_min = used_mins[m]
        max_min_idx = m

print 'Best min idx:', max_min_idx, 'value:', max_min

print 'Answer:', max_gid * max_min_idx
sys.exit()
