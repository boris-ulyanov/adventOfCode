#!/usr/bin/python

data_file = open('./data', 'r')
data_lines = data_file.readlines()
data_file.close()

nodes = {}

for line in data_lines:
    chunks = line.split()
    name = chunks[0]
    node = {'weight' : int(chunks[1][1 : -1])}
    if len(chunks) > 2:
        node['childs'] = ''.join(chunks[3:]).split(',')
    nodes[name] = node

data_lines = None

for name in nodes:
    node = nodes[name]
    if 'childs' in node:
        for child_name in node['childs']:
            child = nodes[child_name]
            child['parent'] = name

for name in nodes:
    node = nodes[name]
    if 'parent' not in node:
        print 'root:', name

