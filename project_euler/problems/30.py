from . import usage

def solution():
    # PyPy ~ 50 ms

    power = 5
    lim = 354294 # Upper limit
    lim = 194979 + 1 # Max value found below upper limit

    tot = 0

    for n in range(2, lim):
        s = sum([int(x)**power for x in str(n)])
        if s == n:
            tot += s
    
    return tot
if __name__ == '__main__':
    usage.usage(solution, n=7)