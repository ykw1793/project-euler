from . import usage

def solution():
    # PyPy ~ 300 ms

    def is_prime(n):
        if n < 4:
            return n > 1
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i*i <= n:
            if n % i == 0 or n % (i+2) == 0:
                return False
            i += 6
        return True

    primes = [2,3]
    mem_val = {2:{(2,)}, 3:{(3,)}}
    n = 4
    while True:
        vals = set()
        if is_prime(n):
            primes.append(n)
            vals.add((n,))
        for i in range(len(primes)-2,-1,-1):
            diff = n-primes[i]
            for tup in mem_val[diff]:
                comb = tuple(sorted([primes[i]] + list(tup)))
                vals.add(comb)
        if len(vals) > 5000:
            return n
        mem_val[n] = vals
        n += 1

if __name__ == '__main__':
    usage.usage(solution, n=10)