import os
from . import usage

def solution():
    # PyPy ~ 1.3 ms

    words = []
    with open(os.path.join(os.path.dirname(__file__), 'words_42.txt')) as f:
        for line in f.readlines():
            lst = line.replace('"', '').split(',')
            words += lst
    
    alphs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphs = {c:i+1 for i,c in enumerate(alphs)}

    cnt = 0
    for word in words:
        val = 0
        for c in word:
            val += alphs[c]
        val *= 2
        det = (4*val)+1
        if int(det ** .5) ** 2 == det:
            if (det-1) % 2 == 0:
                cnt += 1
    return cnt


if __name__ == '__main__':
    usage.usage(solution)