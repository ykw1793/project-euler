from . import usage

def solution():
    # PyPy ~ 18 ms

    tot = 0
    for n in range(1, 10_000):
        s = n
        i = 0
        while i < 50:
            s += int(str(s)[::-1])
            ss = str(s)
            if ss == ss[::-1]:
                break
            i += 1
        if i == 50:
            tot += 1
    return tot

if __name__ == '__main__':
    usage.usage(solution, n=30)