from itertools import combinations

from . import usage


def solution():
    # PyPy ~ 750 ms

    lim = 1000000
    sieve = list(range(lim))
    sieve[0] = sieve[1] = 0

    i = 2
    while i*i <= lim:
        for j in range(i*i, lim, i):
            sieve[j] = 0
        i += 1

    primes = set([x for x in sieve if x > 0])

    famnum = 8

    def replace(n):
        ns = str(n)
        for num_replace in range(1, len(ns)):
            comb = list(combinations(range(len(ns)), num_replace))
            for indices in comb:
                digs = '123456789' if 0 in indices else '0123456789'
                l = set()
                num = list(ns)
                for dig in digs:
                    for idx in indices:
                        num[idx] = dig
                    inum = int(''.join(num))
                    if inum in primes:
                        l.add(inum)
                if len(l) == famnum:
                    return min(l)

    for n in range(10, lim):
        if n not in primes:
            continue
        minval = replace(n)
        if minval:
            return minval

if __name__ == '__main__':
    usage.usage(solution, n=1)