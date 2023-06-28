from . import usage

def solution():
    # PyPy ~ 38 ms

    tot = 0
    for a in range(1,100):
        for b in range(1,100):
            tot = max(tot, sum([int(x) for x in str(a**b)]))
    return tot

if __name__ == '__main__':
    usage.usage(solution, n=20)