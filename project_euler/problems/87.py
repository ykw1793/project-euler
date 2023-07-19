from . import usage

def solution():
    # PyPy ~ 250 ms

    lim = 50_000_000
    prime_lim = int(lim**.5) + 1

    sieve = list(range(prime_lim))
    sieve[0] = sieve[1] = 0
    i = 2
    while i*i < prime_lim:
        if sieve[i] != 0:
            for j in range(i*i, prime_lim, i):
                sieve[j] = 0
        i += 1
    p = set(sieve)
    p.remove(0)
    p = sorted(p)

    nums = set()
    i = 0
    while i < len(p):
        s = p[i]**2
        if s >= lim:
            break
        j = 0
        while j < len(p):
            pj = p[j]**3
            s += pj
            if s >= lim:
                s -= pj
                break
            k = 0
            while k < len(p):
                pk = p[k]**4
                s += pk
                if s >= lim:
                    s -= pk
                    break
                else:
                    nums.add(s)
                s -= pk
                k += 1
            s -= pj
            j += 1
        i += 1
    
    return len(nums)

if __name__ == '__main__':
    usage.usage(solution, n=1)