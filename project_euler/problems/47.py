from . import usage

def solution():
    # PyPy ~ 90 ms

    def get_prime_factors(n):
        fac = set()
        
        i = 2
        while n % i == 0:
            fac.add(i)
            n //= i
        
        i = 3
        while i*i <= n:
            if n % i == 0:
                fac.add(i)
                n //= i
            else:
                i += 2

        if n != 1:
            fac.add(n)

        return fac
    
    n = 2
    while True:
        if len(get_prime_factors(n)) == 4:
            if len(get_prime_factors(n+1)) == 4:
                if len(get_prime_factors(n+2)) == 4:
                    if len(get_prime_factors(n+3)) == 4:
                        return n
        n += 1

if __name__ == '__main__':
    usage.usage(solution, n=10)