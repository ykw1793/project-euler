from . import usage

def solution():
    # PyPy ~ 7 ms

    pn = 1
    pd = 1

    n = 3
    d = 2

    i = 1
    tot = 0
    while i <= 1000:
        tn = n * 2 + pn
        td = d * 2 + pd
        pn = n
        pd = d
        n = tn
        d = td
        i += 1
        if len(str(n)) > len(str(d)):
            tot += 1
    return tot

if __name__ == '__main__':
    usage.usage(solution, n=100)