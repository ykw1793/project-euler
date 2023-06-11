from . import usage

def solution():
    # Time ~ 45 ms

    # m = 0
    # for i in range(100, 1000):
    #     for j in range(i, 1000):
    #         p = str(i*j)
    #         if p == p[::-1]:
    #             m = max(m, i*j)

    # ------------------------------

    # PyPy (get palindromes) ~ 650 µs

    p = []
    for i in range(10, 100):
        for j in range(10):
            n = i * 10 + j
            n = n * 100 + int(str(i)[::-1])
            p.append(n)
    for i in range(100, 999):
        n = i * 1000 + int(str(i)[::-1])
        p.append(n)

    # PyPy ~ 13 ms

    # m = 0
    # for n in p:
    #     for f in range(100, 1000):
    #         if n % f == 0:
    #             nf = n//f
    #             if 100 <= nf <= 999:
    #                 m = max(m, n)
    

    # PyPy ~ 6 ms

    m = 0
    for n in p:
        if n % 2 == 0:
            i = 100
            while i*i <= n:
                if n % i == 0:
                    j = n//i
                    if 100 <= j <= 999:
                        m = max(m, n)
                i += 1
        else:
            i = 101
            while i*i <= n:
                if n % i == 0:
                    j = n//i
                    if 100 <= j <= 999:
                        m = max(m, n)
                i += 2

    return m

if __name__ == '__main__':
    usage.usage(solution, n=20)