from . import usage

def solution():
    # PyPy ~ 3.3 ms

    x = 40755
    d = 286
    while True:
        x += d
        d += 1
        
        pdet = 1+24*x
        if int(pdet**.5)**2 == pdet and (int(pdet**.5)+1) % 6 == 0:
            hdet = 1+8*x
            if int(hdet**.5)**2 == hdet and (int(hdet**.5)+1) % 4 == 0:
                return x


if __name__ == '__main__':
    usage.usage(solution, n=100)