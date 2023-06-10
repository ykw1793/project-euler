import os
import sys
from . import usage

def solution():
    # PyPy ~ 5 ms

    names = []
    with open(os.path.join(os.path.dirname(__file__), 'names_22.txt')) as f:
        for line in f.readlines():
            lst = line.replace('"', '').split(',')
            names += lst
    names.sort()

    alphs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for i, name in enumerate(names):
        s = sum([alphs.index(x)+1 for x in name])
        names[i] = s * (i+1)
    
    return sum(names)

if __name__ == '__main__':
    usage.usage(solution, n=100)