import os
from pprint import pprint
from . import usage

def solution():
    # PyPy ~ 750 µs

    with open(os.path.join(os.path.dirname(__file__), 'triangle_67.txt'), 'r') as f:
        tri = []
        for line in f.readlines():
            tri += [[int(x) for x in line.split()]]
        
        for i in range(len(tri[-1])-2,-1,-1):
            for j in range(i+1):
                tri[i][j] += max(tri[i+1][j], tri[i+1][j+1])
        
        return tri[0][0]

if __name__ == '__main__':
    usage.usage(solution, n=1000)