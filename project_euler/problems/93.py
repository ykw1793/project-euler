from itertools import combinations
from . import usage

def solution():
    # PyPy ~ 46 ms

    def binop(a,b):
        l = [a+b, a-b, b-a, a*b]
        l.append(a/b if b != 0 else b/a)
        return set(l)
    
    def triop(a,b,c):
        s = set()
        cycles = [(a,b,c), (b,c,a), (c,a,b)]
        for cyc in cycles:
            [s.update(binop(x,cyc[0])) for x in binop(cyc[1],cyc[2])]
        return s

    def quadop(a,b,c,d):
        s = set()
        cycles = [(a,b,c,d), (b,c,d,a), (c,d,a,b), (d,a,b,c)]
        for cyc in cycles:
            [s.update(binop(x,cyc[0])) for x in triop(cyc[1], cyc[2], cyc[3])]
        return s
    
    def maxseq(s):
        n = 1
        while n in s:
            n += 1
        return n-1
    
    d = {}
    for k in combinations(range(1,10), 4):
        d[k] = maxseq(quadop(*k))
    
    return ''.join([str(x) for x in max(d, key=d.get)])

if __name__ == '__main__':
    usage.usage(solution, n=10)