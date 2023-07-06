import math
from . import usage

def solution():
    # PyPy ~ 350 ms

    lim = 1_500_000
    mem = {}

    m = 3
    # sum(a,b,c) = m^2 + m -> m^2 + m - 1_500_000 <= 0 -> m < 1225
    while m < 1225:
        n = 1
        while n < m:
            if math.gcd(m,n) == 1:
                a,b,c = m*n, (m*m-n*n)//2, (m*m+n*n)//2
                if a % 2 == 0:
                    a,b = b,a
                if a+b+c <= lim:
                    s = a+b+c
                    if s in mem:
                        mem[s] += 1
                    else:
                        mem[s] = 1
                k = 2
                while k*(a+b+c) <= lim:
                    ks = k*(a+b+c)
                    if ks in mem:
                        mem[ks] += 1
                    else:
                        mem[ks] = 1
                    k += 1
            n += 2
        m += 2
    return len([k for k,v in mem.items() if v == 1])

if __name__ == '__main__':
    usage.usage(solution, n=1)