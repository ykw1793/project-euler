from itertools import permutations
from . import usage

def solution():
    # PyPy ~ 1.3 ms

    def is_prime(n):
        if n < 4:
            return n > 1
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i*i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    n = 9
    while (n*(n+1)//2) % 3 == 0:
        n -= 1
    
    pan = ''.join([str(x) for x in range(n, 0, -1)])
    iters = [int(''.join([x for x in y])) for y in permutations(pan)]
    iters.sort(reverse=True)
    for i in iters:
        if is_prime(i):
            return i

if __name__ == '__main__':
    usage.usage(solution, n=1000)