from . import usage

def solution():
    # PyPy ~ 26 ms

    max_val = 0
    max_n = 0
    for d in range(8, 1_000_001):
        n = 3*d
        n //= 7
        if n*7 == 3*d:
            n -= 1
        if n/d > max_val:
            max_val = n/d
            max_n = n
    return max_n

if __name__ == '__main__':
    usage.usage(solution, n=20)