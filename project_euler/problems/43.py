from . import usage

def solution():
    # PyPy ~ 17 ms

    pan = '0123456789'
    slst = {i:pan for i in range(1,11)}
    slst[4] = '02468'
    slst[6] = '05'

    seen = []

    def basic(idx):
        return [x for x in slst[idx] if x not in seen]
    
    pfs = {i:basic for i in range(1,11)}

    primes = [2,3,5,7,11,13,17]

    def divcheck(idx, d):
        if idx < 4:
            return True
        check = int(seen[-2]+seen[-1]+d) % primes[idx-4] == 0
        return check
    
    iters = []

    def f(idx):
        d_psbl = pfs[idx](idx)
        for d in d_psbl:
            if divcheck(idx, d):
                seen.append(d)
                if idx == 10:
                    s = ''
                    for i in range(9):
                        s += seen[i]
                    iters.append(int(s+d))
                else:
                    f(idx+1)
                seen.pop()
    f(1)
    return sum(iters)


if __name__ == '__main__':
    usage.usage(solution, n=70)