from . import usage

def solution():
    # PyPy ~ 25 ms

    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
    
    def reduce(n, d):
        while True:
            g = gcd(n, d)
            if g > 1:
                n //= g
                d //= g
            else:
                break
        return n, d

    np = 1
    dp = 1

    for denom in range(11, 100):
        for num in range(10, denom):
            if num % 10 == 0 and denom % 10 == 0:
                continue
            ns = str(num)
            ds = str(denom)
            for (nid, did) in [(0,0), (1,0), (0,1), (1,1)]:
                if ns[nid] == ds[did] and ns[(nid+1)%2] != ds[(did+1)%2]:
                    ns = ns[(nid+1)%2]
                    ds = ds[(did+1)%2]
                    break
            else:
                continue

            if '0' not in [ns, ds]:
                ns, ds = reduce(int(ns), int(ds))
                _num, _denom = reduce(num, denom)
                if _num == ns and _denom == ds:
                    np *= ns
                    dp *= ds

    _, dp = reduce(np, dp)
    return dp

if __name__ == '__main__':
    usage.usage(solution, n=10)