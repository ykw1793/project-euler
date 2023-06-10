from . import usage

def solution():
    # PyPy + factorial number system ~ 18 µs

    d = list(range(10))
    ld = len(d)

    fac = {0:1, 1:1}
    for i in range(ld):
        if i not in fac:
            fac[i] = fac[i-1] * i

    v = ''
    
    n = 1_000_000
    r = n-1
    i = ld-1
    while r > 0:
        div = r // fac[i]
        v += str(d.pop(div))
        r %= fac[i]
        i -= 1
    
    if len(d) > 0:
        v += str(d.pop())

    return v

if __name__ == '__main__':
    usage.usage(solution)