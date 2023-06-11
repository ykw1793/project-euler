from . import usage

def solution():
    # PyPy ~ 190 ms

    def is_prime(n):
        if n < 4:
            return n > 1
        if n % 2 == 0 or n % 3 == 0:
            return False

        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    n = 11
    num_found = 0
    tot = 0
    while num_found < 11:
        if is_prime(n):
            lst = []
            ns = str(n)
            for i in range(1, len(ns)):
                lst += [int(ns[i:]), int(ns[:i])]
            if all([is_prime(x) for x in lst]):
                num_found += 1
                tot += n
        n += 1
    return tot

if __name__ == '__main__':
    usage.usage(solution, n=10)