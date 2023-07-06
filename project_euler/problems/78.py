from . import usage

def solution():
    # PyPy ~ 2 s

    denom = 1_000_000
    plst = [1,1]
    n = 2
    while True:
        s = 0
        k = 1
        while True:
            pent = k*(3*k-1)//2
            if n - pent <= 0:
                break
            if k % 2 == 1:
                s += plst[n-pent]
            else:
                s -= plst[n-pent]
            k = -k if k > 0 else -k+1
        if s % denom == 0:
            return n-1
        plst.append(s)
        n += 1

if __name__ == '__main__':
    usage.usage(solution, n=1)