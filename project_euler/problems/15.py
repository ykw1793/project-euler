from . import usage

def solution():
    # 20x20 grid -> total 20 R (right) and 20 D (down)
    # If R distributon is known, D is known
    # Solution: Comb(40, 20)

    # PyPy ~ 8 µs

    rows = 20
    cols = 20

    n = rows + cols
    k = rows

    num = 1
    denom = 1
    for i in range(1, min(k, n-k)+1):
        num *= (n+1-i)
        denom *= i

    return num//denom

if __name__ == '__main__':
    usage.usage(solution)