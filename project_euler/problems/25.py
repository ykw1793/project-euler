from . import usage

def solution():
    # PyPy + string integers ~ 240 ms

    def add(x, y):
        maxlen = max(len(x), len(y))
        s = ''
        carry = 0
        for i in range(1, maxlen+1):
            si = carry
            for n in [x, y]:
                if len(n) >= i:
                    si += int(n[-i])
            carry = si // 10
            s = str(si % 10) + s
        if carry:
            s = str(carry) + s
        return s
    
    f0 = '1'
    f1 = '1'

    i = 3
    while True:
        # Compute F[i]
        t = f1
        f1 = add(f0, f1)
        f0 = t

        if len(f1) == 1000:
            return i
        i += 1

    # PyPy + built in integers ~ 57 ms
    
    # f0 = 1
    # f1 = 1

    # i = 3
    # while True:
    #     # Compute F[i]
    #     t = f1
    #     f1 = f0 + f1
    #     f0 = t

    #     if len(str(f1)) == 1000:
    #         return i
    #     i += 1

if __name__ == '__main__':
    usage.usage(solution, n=7)