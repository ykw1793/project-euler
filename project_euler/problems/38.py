from . import usage

def solution():
    # PyPy ~ 3 ms

    lim = 10000

    maxval = 0
    for n in range(2, lim):
        s = ''
        m = 1
        while len(s) < 9:
            s += str(n * m)
            m += 1
        if len(s) == 9:
            if len(set(s)) == 9 and '0' not in s:
                maxval = max(maxval, int(s))
    
    return maxval

if __name__ == '__main__':
    usage.usage(solution, n=100)