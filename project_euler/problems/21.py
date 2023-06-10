from . import usage

def solution():
    # PyPy ~ 8 ms

    def d(n):
        f = 0
        if n % 2 == 0:
            i = 1
            while i*i <= n:
                if n % i == 0:
                    if i*i == n:
                        f += i
                    else:
                        f += i + n//i
                i += 1
        else:
            i = 1
            while i*i <= n:
                if n % i == 0:
                    if i*i == n:
                        f += i
                    else:
                        f += i + n//i
                i += 2
        return f - n

    s = 0
    dl = {0:-1, 1:0}
    for n in range(2, 10_000):
        if n not in dl:
            dl[n] = d(n)
            dns = dl[n]
            if dns not in dl:
                dl[dns] = d(dns)
            if dl[dns] == n and dns != n: # is amicable
                s += dns + n
    return s

if __name__ == '__main__':
    usage.usage(solution, n=100)