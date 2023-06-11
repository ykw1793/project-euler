from . import usage

def solution():
    # PyPy ~ 300 µs

    s = 1000
    for a in range(1,s//3): # A can at most be 1/3 of S (since A<B<C)
        for b in range(a, a+(s-a)//2): # B can at most be 1/2 of S-A (since B<C)
            c = 1000 - a - b
            if a*a + b*b == c*c:
                return a*b*c

if __name__ == '__main__':
    usage.usage(solution)