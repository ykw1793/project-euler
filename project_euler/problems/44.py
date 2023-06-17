from . import usage

def solution():
    # PyPy ~ 300 ms

    def is_pentagon(x):
        r = (1+24*x)**.5
        return (r+1) % 6 == 0
    
    ps = [1]
    n = 1
    pn = 1
    while True:
        n += 3
        pn += n
        ps.append(pn)

        for i in range(len(ps)):
            a = pn - ps[i]
            b = ps[i]

            if is_pentagon(a) and is_pentagon(abs(a-b)):
                return abs(a-b)


if __name__ == '__main__':
    usage.usage(solution, n=5)