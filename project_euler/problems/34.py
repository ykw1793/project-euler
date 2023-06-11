from . import usage

def solution():
    '''
    n = d * 9!
    d-1 <= log(d)+log(9!) < d 
    d-1-log(d) <= log(9!) < d-log(d)
    d-log(d) <= log(9!)+1 = 6.56 < d-log(d)+1
    d-log(6) <= 6.56 < d-log(6)+1   {log(6) = 0.78}
    d <= 7.34 < d+1
    d = 7
    n = 7 * 9! = 2540160
    '''

    # PyPy ~ 12 ms

    fac = {0:1, 1:1}
    for i in range(2,10):
        fac[i] = fac[i-1]*i
    lim = 2540160  # Theoretical limit
    lim = 40585 + 1  # Value set after running with theoretical limit

    tot = 0
    for n in range(3, lim):
        s = sum([fac[int(x)] for x in str(n)])
        if s == n:
            tot += n
    return tot

if __name__ == '__main__':
    usage.usage(solution, n=50)