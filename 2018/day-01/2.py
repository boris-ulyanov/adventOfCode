#!/usr/bin/python

import sys

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

print 'readed recs:', len(data_lines)

increments = [int(l) for l in data_lines]
del data_lines[:]

# test
# increments = [1, -1]            #  0
# increments = [3, 3, 4, -2, -4]  # 10
# increments = [-6, 3, 8, 5, -6]  #  5
# increments = [7, 7, -2, -7, -4] # 14
# increments = [1, -2, 3, 1, 1, -2] #  2


length = len(increments)
print 'increments recs:', length

unic_stor = set([0])

# sys.exit()

counter = 0

for repeat in xrange(1000):
    found = False
    for i in xrange(length):
        inc = increments[i]
        counter += inc
        if counter in unic_stor:
            print 'answer:' , counter
            print 'i:' , i
            print 'inc:' , inc
            print 'repeat:' , repeat
            found = True
            break

        unic_stor.add(counter)

        # if repeat > 0:
        #     continue

        # # chek if stop there
        # ctr2 = counter
        # for i2 in xrange(i):
        #     ctr2 += increments[i2]
        #     if ctr2 in unic_stor:
        #         print 'answer:', ctr2
        #         print 'i:' , i
        #         print 'i2:' , i2
        #         found = True
        #         break

        # if found:
        #     break
    if found:
        break


print "len(unic_stor)", len(unic_stor)

print "finished"
