from . import usage

def solution():
    # PyPy ~ 22 ms

    n = 1_000_000
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

    l = 0
    while sum(primes[:l]) < n:
        l += 1

    max_window_size = l-1

    for winsize in range(max_window_size, 1, -1):
        for i in range(len(primes)-winsize):
            s = sum(primes[i:i+winsize])
            if s >= n:
                break
            if s in primes:
                return s


if __name__ == '__main__':
    usage.usage(solution, n=40)