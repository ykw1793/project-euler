import math
from . import usage

def solution():
    # PyPy ~ 600 ms

    lim = 12000
    fac = {}

    def is_prime(n):
        if n < 4:
            return n > 1
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    def resolve(lst):
        f = set([lst[0]])
        for i in range(1, len(lst)):
            t = lst[i]
            f.add(t)
            f0, f1 = fac[t[0]], fac[t[1]]
            if len(f0) > 1 and len(f1) > 1:
                for tf0 in f0:
                    for tf1 in f1:
                        f.add(tuple(sorted([*tf0, *tf1])))
            elif len(f0) > 1:
                for tf0 in f0:
                    f.add(tuple(sorted([*tf0, t[1]])))
            elif len(f1) > 1:
                for tf1 in f1:
                    f.add(tuple(sorted([t[0], *tf1])))
        return f
    
    def factors(n):
        f = [(n,)]
        if not is_prime(n):
            for i in range(2, int(n**.5)+1):
                if n % i == 0:
                    t = (i, n//i)
                    f.append(t)
        fac[n] = resolve(f)

    klst = set(range(2, lim + 1))

    minlst = set()
    i = 1
    while len(klst) > 0:
        i += 1
        factors(i)
        tbr = set()
        for l in fac[i]:
            if len(l) == 1:
                continue
            s, p = sum(l), math.prod(l)
            k = p-s+len(l)
            if k in klst and k not in tbr:
                minlst.add(p)
                tbr.add(k)
        for v in tbr:
            klst.remove(v)

    return sum(minlst)

if __name__ == '__main__':
    usage.usage(solution, n=1)