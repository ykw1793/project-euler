from . import usage

def solution():
    # PyPy + string integers ~ 2 ms

    def add(lx):
        maxlen = max([len(x) for x in lx])
        s = ''
        carry = 0
        for i in range(1, maxlen+1):
            si = carry
            for x in lx:
                if len(x) >= i:
                    si += int(x[-i])
            carry = si // 10
            s = str(si % 10) + s
        if carry:
            s = str(carry) + s
        return s

    def multiply(x, f):
        xl = len(x)
        carry = 0
        y = ''
        for i in range(1, xl+1):
            p = int(x[-i]) * int(f) + carry
            carry = p // 10
            y = str(p % 10) + y
        if carry:
            y = str(carry) + y
        return y
    
    def product(x, y):
        add_list = []
        for i in range(1, len(y)+1):
            add_list.append(multiply(x, y[-i]) + '0' * (i-1))
        return add(add_list)
    
    p = '1'
    n = 100
    for i in range(1, n+1):
        p = product(p, str(i))
    
    p = [int(x) for x in p]
    return sum(p)

    # PyPy + built in integers ~ 22 µs

    # p = 1
    # n = 100
    # for i in range(1, n+1):
    #     p *= i
    # p = [int(x) for x in str(p)]
    # return sum(p)

if __name__ == '__main__':
    usage.usage(solution, n=100)