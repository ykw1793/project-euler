from . import usage

def solution():
    # PyPy ~ 5.5 ms

    s = 0
    for i in range(1, 1001):
        s += i**i
    return str(s)[-10:]

if __name__ == '__main__':
    usage.usage(solution, n=100)