#!/usr/bin/python

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

buff = ''.join(data_lines)
buff_len = len(buff)

data_lines = None

print 'buff len', len(buff)

level = 0
level_sum = 0
state = 'body'
idx = 0

while True:

    if idx >= buff_len:
        print 'EOF'
        break

    sym = buff[idx]
    idx += 1

    if state == 'body':

        if sym == '{':
            level += 1
            level_sum += level

        elif sym == '}':
            level -= 1

        elif sym == '!':
            idx += 1

        elif sym == '<':
            state = 'garbage'

    elif state == 'garbage':

        if sym == '!':
            idx += 1

        elif sym == '>':
            state = 'body'


print 'level', level
print 'level_sum', level_sum
print 'state', state
