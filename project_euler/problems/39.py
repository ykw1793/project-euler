from . import usage

def solution():
    # PyPy ~ 160 ms

    lim = 1001
    maxcnt = 0
    maxp = 0
    for p in range(10, lim):
        cnt = 0
        for a in range(1, p//3):
            for b in range(a, a+((p-a)//2)):
                c = p-a-b
                if a*a + b*b == c*c:
                    cnt += 1
        if cnt > maxcnt:
            maxcnt = cnt
            maxp = p
    return maxp
        

if __name__ == '__main__':
    usage.usage(solution, n=3)