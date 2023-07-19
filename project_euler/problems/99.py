import os
import math
from . import usage

def solution():
    # PyPy ~ 790 µs

    with open(os.path.join(os.path.dirname(__file__), 'base_exp_99.txt'), 'r') as f:
        mv, me = -1, 0
        for i, line in enumerate(f.readlines()):
            t = [int(x) for x in line.strip().split(',')]
            e = math.log2(t[0]) * t[1]
            if e > me:
                me, mv = e, i+1
        return mv

if __name__ == '__main__':
    usage.usage(solution, n=1)