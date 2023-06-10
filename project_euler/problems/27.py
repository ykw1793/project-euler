from . import usage

def solution():
    # PyPy ~ 23 ms

    n = 20_000
    sieve = [1] * n

    primes = set([2])
    for i in range(3, n, 2):
        if sieve[i]:
            primes.add(i)
            j = i
            while i*j < n:
                sieve[i*j] = 0
                j += 1
    
    blst = set([x for x in primes if x <= 1000])
    blst = blst.union(set([-x for x in primes if x <= 1000]))

    ca, cb = None, None
    consec = 0
    for b in blst:
        for a in range(-999, 1000):
            x = 0
            while True:
                fx = x*x + a*x + b
                if fx >= n:
                    print('Not Enough Primes')
                else:
                    if fx not in primes:
                        break
                    else:
                        x += 1
            if x > consec:
                consec = x
                ca, cb = a, b
    return ca * cb

if __name__ == '__main__':
    usage.usage(solution, n=20)