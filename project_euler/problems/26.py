from . import usage

def solution():
    # PyPy ~ 177 ms

    def recur_len(d):
        # calculates 1/d exactly
        q = []
        r = []
        
        n = 10
        while True:
            if d > n:
                tq = 0
                tr = n
                tn = n * 10
            else:
                tq = n // d
                tr = n % d
                tn = tr * 10
            
            if tr == 0: # no recurring part
                return 0
            
            for i in range(len(q)):
                if q[i] == tq and r[i] == tr: # cycle found
                    return len(q) - i
            q.append(tq)
            r.append(tr)
            n = tn

    max_recur = 0
    max_denom = 0
    for d in range(2, 1000):
        rd = recur_len(d)
        if rd > max_recur:
            max_recur = rd
            max_denom = d
    return max_denom

if __name__ == '__main__':
    usage.usage(solution, n=7)