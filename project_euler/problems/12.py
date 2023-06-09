from . import usage

def solution():
    # PyPy ~ 325 ms

    nf = 500

    n = 1
    while True:
        tri = n * (n+1) // 2
        num_fac = 0
        fac = 1
        if tri % 2 == 0:
            while fac*fac <= tri:
                if tri % fac == 0:
                    num_fac += 2
                fac += 1
        else:
            while fac*fac <= tri:
                if tri % fac == 0:
                    num_fac += 2
                fac += 2
        if num_fac > nf:
            return tri
        n += 1

if __name__ == '__main__':
    usage.usage(solution, n=7)