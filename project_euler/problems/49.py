from itertools import permutations
from . import usage

def solution():
    # PyPy ~ 3.7 ms

    n = 10000
    sieve = [1] * n
    sieve[0] = sieve[1] = 0

    primes = []

    i = 2
    while i < n:
        if sieve[i] == 1:
            if i >= 1000:
                primes.append(i)
            for j in range(i*i, n, i):
                sieve[j] = 0
        i += 1

    checked = set()

    for p in primes:
        if p not in checked:
            perms = [int(''.join([x for x in y])) for y in permutations(str(p))]
            perms = set([x for x in perms if x in primes])
            checked = checked.union(perms)
            perms = sorted(list(perms))
            if len(perms) >= 3:
                for i in range(len(perms)):
                    diff = [perms[j]-perms[i] for j in range(i+1, len(perms))]
                    for m in range(len(diff)-1):
                        if diff[m]*2 in diff:
                            v1 = str(perms[i])
                            v2 = str(perms[i+1+m])
                            v3 = str(perms[i+1+diff.index(diff[m]*2)])
                            if v1 != '1487':
                                return v1+v2+v3


if __name__ == '__main__':
    usage.usage(solution, n=100)