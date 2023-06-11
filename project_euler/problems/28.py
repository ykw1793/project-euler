from . import usage

def solution():
    # PyPy ~ 1.4 µs

    n = 1001
    n //= 2
    f = 8*n*n + 15*n + 13
    f *= 2*n
    f //= 3
    return f + 1

if __name__ == '__main__':
    usage.usage(solution)