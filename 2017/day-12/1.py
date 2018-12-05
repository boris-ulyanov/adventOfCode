#!/usr/bin/python

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

# fill records
records = []
for line in data_lines:
    pair = line.split(' <-> ')
    first = int(pair[0])
    other = [int(s) for s in ''.join(pair[1].split()).split(',')]
    record = set(other)
    record.add(first)
    records.append(record)

len_records = len(records)
print 'Len records', len_records

# merge all intersections
for idx in xrange(len_records):
    rec = records[idx]

    for rec2 in records[idx + 1:]:
        intersection = rec & rec2
        if len(intersection) > 0:
            rec2.update(rec)
            records[idx] = False
            break

print '\n======'

n = 0
for rec in records:
    # skip empty
    if not rec:
        continue

    n += 1
    print n, len(rec)

    if 0 in rec:
        print rec
