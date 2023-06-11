from . import usage

def solution():
    # PyPy ~ 7 ms

    pn = 10_001
    
    n = 110_000
    sieve = list(range(n))
    sieve[0] = None
    sieve[1] = None

    pi = 1
    for i in range(n):
        if sieve[i] == None:
            continue
        pi += 1
        j = 2
        while i*j < n:
            sieve[i*j] = None
            j += 1
    
    if pi < pn:
        print(f'Only {pi} primes out of {pn} found. Increase n.')
    else:
        sieve = [x for x in sieve if x is not None]
        return sieve[pn-1]

        

if __name__ == '__main__':
    usage.usage(solution, n=100)