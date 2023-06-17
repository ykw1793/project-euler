from . import usage

def solution():
    # PyPy ~ 8 ms

    def get_primes(n):
        sieve = [1] * n
        sieve[0] = sieve[1] = 0
        
        primes = []

        i = 2
        while i < n:
            if sieve[i] == 1:
                primes.append(i)
                for j in range(i*i, n, i):
                    sieve[j] = 0
            i += 1
        return primes
    
    lim = 6_000
    primes = get_primes(lim)
    pset = set(primes)

    x = 35
    while True:
        if x not in pset:
            found = False
            for i in range(len(primes)):
                if primes[i] >= x:
                    break
                xi = x-primes[i]
                if xi % 2 == 0:
                    xi //= 2
                    if int(xi**.5)**2 == xi and int(xi**.5) > 0:
                        found = True
                        break
            if not found:
                return x
        x += 2


if __name__ == '__main__':
    usage.usage(solution, n=100)