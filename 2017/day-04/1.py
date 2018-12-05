#!/usr/bin/python


data_file = open('./data', 'r')
lines = data_file.readlines()
data_file.close()

result = 0

for line in lines:
    words = line.split()
    uniq_words = set(words)
    if len(words) == len(uniq_words):
        result += 1

print result
