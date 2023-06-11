from . import usage

def solution():
    # PyPy ~ 630 ms

    def rotations(n):
        ns = str(n)
        rots = [n]
        while True:
            ns = ns[-1] + ns[:-1]
            if ns == str(n):
                break
            rots.append(int(ns))
        return rots
    
    lim = 1_000_000
    sieve = [1] * lim
    sieve[0] = sieve[1] = 0
    primes = set()
    
    for i in range(2, lim):
        if sieve[i] == 1:
            primes.add(i)
            for j in range(i*i, lim, i):
                sieve[j] = 0
    
    tot = 0
    for n in range(2, lim):
        if all([x in primes for x in rotations(n)]):
            tot += 1
    return tot

if __name__ == '__main__':
    usage.usage(solution, n=1)