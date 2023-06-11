from . import usage

def solution():
    # PyPy ~ 115 ms

    def convert(n):
        b2 = ''
        while n > 0:
            b2 = str(n%2) + b2
            n //= 2
        return b2

    lim = 1_000_000
    tot = 0
    for n in range(lim):
        b10 = str(n)
        if b10 == b10[::-1]:
            b2 = convert(n)
            if b2 == b2[::-1]:
                tot += n
    return tot


if __name__ == '__main__':
    usage.usage(solution, n=10)