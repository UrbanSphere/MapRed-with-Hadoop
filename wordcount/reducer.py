#!/usr/bin/env python3

import sys


words = {}
for line in sys.stdin:
    try:
        word, count = line.split('\t')
    except:
        continue
    if word in words.keys():
        words[word] += 1
    else:
        words.update({word: int(count)})

for elem in words:
    print(elem, '\t', words[elem])
