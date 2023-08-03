from . import usage
import random

def solution():
    # PyPy ~ 17 s

    def d(n):
        f = 0
        if n % 2 == 0:
            i = 1
            while i*i <= n:
                if n % i == 0:
                    if i*i == n:
                        f += i
                    else:
                        f += i + n//i
                i += 1
        else:
            i = 1
            while i*i <= n:
                if n % i == 0:
                    if i*i == n:
                        f += i
                    else:
                        f += i + n//i
                i += 2
        return f - n

    lim = 1_000_000

    c = {}
    l = {}
    def chain(n: int, on: int, h: list):
        dn = d(n)
        if dn == 1:
            for i in range(len(h)):
                if h[i] not in l:
                    l[h[i]] = 0
            return
        if dn > lim:
            for i in range(len(h)):
                if h[i] not in l:
                    l[h[i]] = 0
            return
        if dn == on:
            if dn not in l:
                c[dn] = h.copy()
                l[dn] = len(h)
            for i in range(1, len(h)):
                if h[i] not in l:
                    c[h[i]] = h[i:] + h[:i]
                    l[h[i]] = len(h)
        elif dn in h:
            if dn not in l:
                i = h.index(dn)
                for j in range(i):
                    if h[j] not in l:
                        l[h[j]] = 0
                for j in range(i, len(h)):
                    if h[j] not in l:
                        c[h[j]] = h[j:] + h[i:j]
                        l[h[j]] = len(h) - i
        else:
            h.append(dn)
            chain(dn, on, h)

    r = list(range(2, lim+1))
    random.seed(0)
    random.shuffle(r)

    for n in r:
        if n not in l:
            chain(n, n, [n])

    return min(c[max(l, key=l.get)])

if __name__ == '__main__':
    usage.usage(solution, n=1)