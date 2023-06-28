from . import usage

def solution():
    # PyPy ~ 1.8 ms

    c = {}

    def comb(n, k):
        if n >= 0 and k == 0:
            c[(n,k)] = 1
        if 1 <= n <= 100 and 0 < k < n:
            c[(n,k)] = c[(n-1,k-1)]*n//k
            c[(n,n-k)] = c[(n,k)]

    for n in range(1,101):
        for k in range(n//2+1):
            comb(n,k)

    tot = len([x for x in c.values() if x > 1_000_000])
    return tot

if __name__ == '__main__':
    usage.usage(solution, n=100)