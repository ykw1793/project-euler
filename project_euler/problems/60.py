from . import usage

def solution():
    # PyPy ~ 1.7 s

    def is_prime(n):
        if n < 4:
            return n > 1
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i*i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    lim = 10_000
    primes = list(range(lim))
    primes[0] = primes[1] = 0

    i = 2
    while i*i <= lim:
        if primes[i] != 0:
            for j in range(i*i, lim, i):
                primes[j] = 0
        i += 1
    primes = [x for x in primes if x != 0]

    sets: dict[set[int]] = dict()
    for i in range(len(primes)):
        pi = primes[i]
        sets[(pi)] = set([x for x in primes[i+1:] if is_prime(int(str(pi)+str(x))) and is_prime(int(str(x)+str(pi)))])

    def recursion(tup):
        if type(tup) == tuple and len(tup) == 4:
            mins = []
            for p in sets[tup]:
                s = sum(tup) + p
                mins.append(s)
            if len(mins) > 0:
                return min(mins)
            return None
        
        for x in sets[tup]:
            if type(tup) == int:
                ntup = tuple(sorted([tup, x]))
            else:
                ntup = tuple(sorted(list(tup)+[x]))
            if ntup not in sets:
                sets[ntup] = sets[tup].intersection(sets[(x)])
                ret = recursion(ntup)
                if ret:
                    return ret

    mins = set()
    for p in primes:
        if p in [2, 5]:
            continue
        ret = recursion(p)
        if ret:
            mins = mins.union(set([ret]))
    if len(mins) > 0:
        return min(mins)

if __name__ == '__main__':
    usage.usage(solution, n=1)