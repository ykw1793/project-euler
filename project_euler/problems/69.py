import math
from . import usage

def solution():
    # PyPy ~ 570 ms

    lim = 1_000_001
    primes = list(range(lim))
    primes[0] = primes[1] = 0
    i = 2
    while i*i <= lim:
        if primes[i] > 0:
            for j in range(i*i, lim, i):
                primes[j] = 0
        i += 1
    primes = [x for x in primes if x > 0]

    phi = [0] * lim
    phi[1] = 1
    for p in primes:
        phi[p] = p-1
        for i in range(2, ((lim-1)//p)+1):
            phi[i * p] = (phi[i] * phi[p] * math.gcd(i,p)) // phi[math.gcd(i,p)]
    
    max_ratio, max_n = 0, 0
    for n in range(2, lim):
        ratio = n/phi[n]
        if ratio > max_ratio:
            max_ratio = ratio
            max_n = n

    return max_n


    # PyPy ~ 1.4 s

    # pfactors = {}

    # def is_prime(n):
    #     if n < 4:
    #         return n > 1
    #     if n % 2 == 0 or n % 3 == 0:
    #         return False
    #     i = 5
    #     while i * i <= n:
    #         if n % i == 0 or n % (i + 2) == 0:
    #             return False
    #         i += 6
    #     return True

    # def prime_factors(n):
    #     if is_prime(n):
    #         pfactors[n] = set([n])
    #         return pfactors[n]
        
    #     i = 2
    #     while i * i <= n:
    #         if n % i == 0:
    #             pfactors[n] = pfactors[n//i].union(pfactors[i])
    #             break
    #         else:
    #             i += 1
    #     return pfactors[n]
    
    # max_ratio, max_n = 0, 0
    # for n in range(2, 1_000_001):
    #     pfac = prime_factors(n)
    #     num = 1
    #     denom = 1
    #     for p in pfac:
    #         num *= p
    #         denom *= (p-1)
    #     ratio = num/denom
    #     if ratio > max_ratio:
    #         max_ratio = ratio
    #         max_n = n
    
    # return max_n

if __name__ == '__main__':
    usage.usage(solution, n=1)