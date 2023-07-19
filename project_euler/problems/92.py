from . import usage

def solution():
    # PyPy ~ 6 s

    lim = 10_000_000
    e1 = {44,32,13,10,1}
    e89 = {85,89,145,42,20,4,16,37,58}
    n = 1
    while n < lim:
        if (n not in e1) and (n not in e89):
            v = None
            nn = n
            l = [nn]
            while True:
                nn = sum([int(x)**2 for x in str(nn)])
                if nn in e1:
                    v = 1
                    break
                elif nn in e89:
                    v = 89
                    break
                else:
                    l.append(nn)
            if v == 1:
                for e in l:
                    e1.add(e)
            else:
                for e in l:
                    e89.add(e)
        n += 1
    return len(e89)

if __name__ == '__main__':
    usage.usage(solution, n=1)