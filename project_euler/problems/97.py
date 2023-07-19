from . import usage

def solution():
    # PyPy ~ 6.3 ms

    n = 28433 * (2 ** 7830457) + 1
    return n % (10 ** 10)

if __name__ == '__main__':
    usage.usage(solution, n=1)