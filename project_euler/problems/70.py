import math
from . import usage

def solution():
    # PyPy ~ 120 ms

    lim = 10_000_000

    prime_lim = int(10**3.6)
    primes = list(range(prime_lim))
    primes[0] = primes[1] = 0
    i = 2
    while i*i <= prime_lim:
        if primes[i] > 0:
            for j in range(i*i, prime_lim, i):
                primes[j] = 0
        i += 1
    primes = [x for x in primes if x > 0]

    tots = []

    for i in range(len(primes)):
        pi = primes[i]
        for j in range(i+1, len(primes)):
            pj = primes[j]
            if pi*pj >= lim:
                break
            ij = sorted(str(pi*pj))
            tot = sorted(str((pi-1)*(pj-1)))
            if ij == tot:
                tots.append((pi*pj, (pi*pj)/((pi-1)*(pj-1))))  
    return min(tots, key=lambda x: x[1])[0]

if __name__ == '__main__':
    usage.usage(solution, n=1)