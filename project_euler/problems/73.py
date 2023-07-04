import math
from . import usage

def solution():
    # PyPy ~ 370 ms

    n = 12_000
    a,b,c,d = 0,1,1,n

    while (a,b) != (1,3):
        k = (n + b) // d
        a,b,c,d = c, d, k*c-a, k*d-b
    
    cnt = 0
    while (a,b) != (1,2):
        k = (n + b) // d
        a,b,c,d = c, d, k*c-a, k*d-b
        cnt += 1
    
    return cnt-1

    # PyPy ~ 1.4 s

    # s = 0
    # for d in range(4, 12_001):
    #     low = math.ceil(d/3)
    #     high = math.floor(d/2)
    #     s += len([n for n in range(low, high+1) if math.gcd(n,d) == 1])
    # return s

if __name__ == '__main__':
    usage.usage(solution, n=1)