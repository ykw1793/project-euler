from . import usage

def solution():
    # PyPy + Doubling 1000 times ~ 7 ms

    # def double(x: str):
    #     xl = len(x)
    #     carry = 0
    #     y = ''
    #     for i in range(1, xl+1):
    #         p = int(x[-i]) * 2 + carry
    #         carry = p // 10
    #         y = str(p % 10) + y
    #     if carry:
    #         y = str(carry) + y
    #     return y
    
    # e = '1'
    # for _ in range(1000):
    #     e = double(e)

    # s = sum([int(x) for x in e])
    # return s

    # --------------------------------

    # PyPy + exp(a+b)=exp(a)*exp(b) ~ 4 ms

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
    
    def product(x, y=None):
        if y == None:
            y = x
        add_list = []
        for i in range(1, len(y)+1):
            add_list.append(multiply(x, y[-i]) + '0' * (i-1))
        return add(add_list)
        
    def exponential(e):
        le = e//2
        re = e-le
        if le == re:
            if le == 1:
                return product('2')
            return product(exponential(le))
        else:
            if le == re == 1:
                return product('2', '2')
            if le == 1:
                if re == 0:
                    return product('2', '1')
                return product('2', exponential(re))
            if re == 1:
                return product(exponential(le), '1')
            return product(exponential(le), exponential(re))
        
    s = sum([int(x) for x in exponential(1000)])
    return s

if __name__ == '__main__':
    usage.usage(solution, n=50)