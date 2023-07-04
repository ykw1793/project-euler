import math
from . import usage

def solution():
    # PyPy ~ 650 ms

    lim = 1_000_001
    phi = [0] * lim
    phi[1] = 1

    for n in range(2, lim):
        if phi[n] == 0:
            phi[n] = n-1
        for i in range(2, n+1):
            if i*n >= lim:
                break
            gcd = math.gcd(i, n)
            phi[i*n] = (phi[i] * phi[n] * gcd) // phi[gcd]
    
    return sum(phi)-1

if __name__ == '__main__':
    usage.usage(solution, n=1)