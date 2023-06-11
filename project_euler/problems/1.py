from . import usage

def solution():
    # PyPy ~ 14 µs

    return (sum(range(0, 1000, 3))+
            sum(range(0, 1000, 5))-
            sum(range(0, 1000, 15)))

if __name__ == '__main__':
    usage.usage(solution)