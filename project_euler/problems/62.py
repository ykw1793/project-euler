from . import usage

def solution():
    # PyPy ~ 30 ms

    count = {}
    vals = {}

    target = 5
    lim = 100
    n = 1
    while True:
        while n < lim:
            nc = n**3
            tup = tuple(sorted([int(x) for x in list(str(nc))]))
            if tup in count:
                count[tup] += 1
                vals[tup] += [nc]
            else:
                count[tup] = 1
                vals[tup] = [nc]
            n += 1
        if target in set(count.values()):
            for k in count:
                if count[k] == target:
                    return min(vals[k])
        else:
            lim += 100

if __name__ == '__main__':
    usage.usage(solution, n=10)