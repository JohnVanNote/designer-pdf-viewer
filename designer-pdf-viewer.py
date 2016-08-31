#!/bin/python

import sys

def main():
    h = map(int,raw_input().strip().split(' '))
    word = raw_input().strip()
    c = 97

    letters = list(word)
    if len(letters) == 0:
        print 0
    else:
        max_h = 0
        for i in letters:
            max_h = max(max_h, h[ord(i)-c])
        print max_h * len(word)

if __name__ == '__main__':
    main()
