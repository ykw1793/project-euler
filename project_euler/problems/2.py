from . import usage

def solution():
    s = 2
    f0, f1 = 1, 2
    while f1 <= 4_000_000:
        f0, f1 = f1, f0+f1
        if f1 % 2 == 0:
            s += f1
    return s

if __name__ == '__main__':
    usage.usage(solution)