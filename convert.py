#!/usr/bin/python3

import os
import sys

def convert(file: str):
    with open(file, 'r') as fi, open('out', 'w') as fo:
        while line := fi.readline():
            if '\\tag' not in line:
                line = line.replace('$', '$$').replace('$$$$', '$$')
                line = line.replace('\\exist ', '\\exists ')
            fo.write(line.replace('\\tag{\\sf ','\\tag{'))


def f(n:int)->int:
    res = 0
    st = [n];
    while len(st) > 0:
        print(2 * sum(k ** 2 for k in st) - 2 * sum(st) + len(st), st)
        num = st.pop()
        if num <= 1:
            res += num
        else:
            res = res - num % 2
            fl = num // 2
            ce = (num + 1) // 2
            st += [fl, fl, ce, ce]
    return res


def main():
    print('res = ', f(3))


if __name__ == '__main__':
    # main()
    os.chdir(os.path.dirname(__file__))
    convert(sys.argv[1])
