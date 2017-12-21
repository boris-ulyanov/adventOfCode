#!/usr/bin/python

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

# test
# data_lines = [
#     '     |          ',
#     '     |  +--+    ',
#     '     A  |  C    ',
#     ' F---|----E|--+ ',
#     '     |  |  |  D ',
#     '     +B-+  +--+ ',
# ]


def check_sym(_x, _y):
    w = len(data_lines[0])
    h = len(data_lines)
    if (_x < 0) or (_x >= w) or (_y < 0) or (_y >= h):
        return False
    return data_lines[_y][_x] != ' '


y = 0
x = data_lines[y].index('|')

my_from = 'up'

from2step = {
    'up': [0, 1],
    'down': [0, -1],
    'left': [1, 0],
    'right': [-1, 0],
}

collected_syms = []


counter = 0

while True:

    print counter,
    counter += 1

    cur_sym = data_lines[y][x]

    if cur_sym == ' ':
        print 'SPACE => Finish???'
        break

    elif cur_sym in '|-':
        print 'Line', cur_sym

    elif (cur_sym >= 'A') and (cur_sym <= 'Z'):
        print 'Symbol', cur_sym
        collected_syms.append(cur_sym)

    elif cur_sym == '+':
        if (my_from == 'up') or (my_from == 'down'):
            to_left = check_sym(x - 1, y)
            to_right = check_sym(x + 1, y)

            if to_left and not to_right:
                print 'Turn to left'
                my_from = 'right'

            elif not to_left and to_right:
                print 'Turn to right'
                my_from = 'left'

            else:
                print 'Both or no one:', to_left, to_right
                break
        else:
            to_up = check_sym(x, y - 1)
            to_down = check_sym(x, y + 1)

            if to_up and (not to_down):
                print 'Turn to up'
                my_from = 'down'

            elif (not to_up) and to_down:
                print 'Turn to down'
                my_from = 'up'

            else:
                print 'Both or no one:', to_up, to_down
                break

    else:
        print 'Unexpected symbol [%s]' % cur_sym
        break

    step = from2step[my_from]
    x += step[0]
    y += step[1]


print '------------'
print 'pos:', x, y
print 'collected_syms:', ''.join(collected_syms)
