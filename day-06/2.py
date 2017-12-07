#!/usr/bin/python

def banks2str(b):
    s = [str(x) for x in b]
    return '-'.join(s)


banks = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]

history = {}
history[banks2str(banks)] = 0

l = len(banks)
step = 0

print 'len:', l
print 'banks:', banks

while True:

    step += 1

    # find bank
    selected = 0
    blocks_in_selected = banks[0]

    for i in xrange(1, l):
        blocks = banks[i]
        if blocks > blocks_in_selected:
            selected = i
            blocks_in_selected = blocks

    # print selected, blocks_in_selected

    # distribute blocks
    banks[selected] = 0
    selected += 1
    for i in xrange(selected, selected + blocks_in_selected):
        idx = i % l
        banks[idx] += 1

    my_hash = banks2str(banks)

    if my_hash in history:
        print 'step', step, 'history len', len(history)
        print 'my_hash', my_hash
        print 'prev step', history[my_hash]
        print 'delta', step - history[my_hash]
        break

    history[my_hash] = step


print step
