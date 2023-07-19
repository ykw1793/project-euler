from . import usage

def solution():
    # PyPy ~ 17 s
    
    cnt = l = sq_idx = 0
    sq = set()
    while cnt < 1_000_000:
        l += 1
        for _ in range(3):
            sq_idx += 1
            sq.add(sq_idx*sq_idx)
        for w in range(l, 0, -1):
            for h in range(w, 0, -1):
                s = l+w+h
                d = s*s - 2 * max(l*(h+w), w*(h+l), h*(l+w))
                if d in sq:
                    cnt += 1
    return l

if __name__ == '__main__':
    usage.usage(solution, n=1)