from . import usage

def solution():
    # PyPy ~ 18 µs

    n = 600_851_475_143

    i = 2
    while n % i == 0:
        n //= i
    
    i = 3
    while i*i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 2
    return n

if __name__ == '__main__':
    usage.usage(solution)