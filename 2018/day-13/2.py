#!/usr/bin/python

import sys
from collections import defaultdict

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

# test
if False:
    data_lines = [
        r"/>-<\  x",
        r"|   |  x",
        r"| /<+-\x",
        r"| | | vx",
        r"\>+</ |x",
        r"  |   ^x",
        r"  \<->/x",
    ]

def print_state(s, title):
    print title
    for line in s:
        print line

# initial state
data = [ bytearray(line[:-1]) for line in data_lines]
data_lines = None
w, h = len(data[0]), len(data)
print 'area width', w
print 'area height', h
# print_state(data, 'initial')

symbols = {
    ord('<'): {
        'type': 'car',
        'step': (-1, 0),
        'initial_replace': ord('-'),
        'rotate-to-lft':  ord('v'),
        'rotate-to-rgt':  ord('^'),
    },
    ord('>'): {
        'type': 'car',
        'step': (1, 0),
        'initial_replace': ord('-'),
        'rotate-to-lft':  ord('^'),
        'rotate-to-rgt':  ord('v'),
    },
    ord('^'): {
        'type': 'car',
        'step': (0, -1),
        'initial_replace': ord('|'),
        'rotate-to-lft':  ord('<'),
        'rotate-to-rgt':  ord('>'),
    },
    ord('v'): {
        'type': 'car',
        'step': (0, 1),
        'initial_replace': ord('|'),
        'rotate-to-lft':  ord('>'),
        'rotate-to-rgt':  ord('<'),
    },
    ord('-'): {
        'type': 'straight',
    },
    ord('|'): {
        'type': 'straight',
    },
    ord('+'): {
        'type': 'cross',
    },
    ord('/'): {
        'type': 'turn',
        'from-to': {
            ord('<'): ord('v'),
            ord('>'): ord('^'),
            ord('^'): ord('>'),
            ord('v'): ord('<'),
        }
    },
    ord('\\'): {
        'type': 'turn',
        'from-to': {
            ord('<'): ord('^'),
            ord('>'): ord('v'),
            ord('^'): ord('<'),
            ord('v'): ord('>'),
        }
    },
    ord(' '): {
        'type': 'space',
    },
}

cars = []
for row in xrange(h):
    for col in xrange(w):
        b = data[row][col]
        if symbols[b]['type'] != 'car':
            continue
        cars.append({
            'sym': b,
            'pos': (col, row),
            'under': symbols[b]['initial_replace'],
            'cross_ctr': 0
        })

# print 'cars', cars
print 'cars size', len(cars)

def cars_sort_key(item):
    p = item['pos']
    return (p[1] * h) + p[0]

iteration = 0
while True:
    iteration += 1

    cars.sort(key=cars_sort_key)

    for car in cars:
        if 'crached' in car:
            continue
        cur_pos = car['pos']
        car_sym = data[cur_pos[1]][cur_pos[0]]
        step = symbols[car_sym]['step']
        next_pos = (cur_pos[0] + step[0], cur_pos[1] + step[1])
        next_symbol = data[next_pos[1]][next_pos[0]]

        # unconditional
        data[cur_pos[1]][cur_pos[0]] = car['under']
        car['under'] = next_symbol
        car['pos'] = next_pos

        next_symbol_prop = symbols[next_symbol]
        next_symbol_type = next_symbol_prop['type']

        if next_symbol_type == 'car':
            # crach !!!
            car['crached'] = True
            # find pair
            pair_car = None
            for c in cars:
                if 'crached' in c:
                    continue
                if c['pos'] != next_pos:
                    continue
                pair_car = c
                break
            assert(pair_car)
            pair_car['crached'] = True
            car_sym = pair_car['under']
            print 'crash pos', next_pos

        elif next_symbol_type == 'straight':
            pass

        elif next_symbol_type == 'cross':
            # left, straight, right
            # straight don't need action
            cross_ctr = car['cross_ctr']
            car['cross_ctr'] = cross_ctr + 1

            r = cross_ctr % 3

            if r == 0:
                car_sym = symbols[car_sym]['rotate-to-lft']
            elif r == 2:
                car_sym = symbols[car_sym]['rotate-to-rgt']

        elif next_symbol_type == 'turn':
            car_sym = next_symbol_prop['from-to'][car_sym]

        else:
            print 'unrecognized type', next_symbol_type

        data[next_pos[1]][next_pos[0]] = car_sym

    # delete crached
    cars = [car for car in cars if 'crached' not in car]

    # check Finish !!!
    if len(cars) <= 1:
        print 'Ansver: last car pos - ', cars[0]['pos']
        sys.exit()

    # print_state(data,  'iteration' + str(iteration))

# Answer1 29,74
