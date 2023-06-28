from . import usage

def solution():
    # PyPy ~ 80 ms

    n = 1
    while True:
        ns = str(n)
        for f in range(2,7):
            if sorted(str(f*n)) != sorted(ns):
                break
        else:
            return n
        n += 1

if __name__ == '__main__':
    usage.usage(solution, n=10)