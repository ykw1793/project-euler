# import numpy as np
from . import usage

def solution():
    # Vanilla Python + CPython ~ 930 ms
    # Vanilla Python + PyPy ~ 34 ms

    n = 2_000_000
    sieve = [1] * n

    s = 2
    for i in range(3, n, 2):
        if sieve[i]:
            s += i
            j = i
            while i*j < n:
                sieve[i*j] = 0
                j += 1
    return s

    # Numpy + CPython ~ 208 ms

    # n = 2_000_000
    # sieve = np.ones(n, dtype=bool)
    # sieve[0] = sieve[1] = False

    # s = 2
    # for i in range(3, n, 2):
    #     if sieve[i]:
    #         s += i
    #         sieve[i*i::i] = False
    # return s

if __name__ == '__main__':
    usage.usage(solution, n=30)