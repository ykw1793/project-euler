from . import usage

def solution():
    # PyPy ~ 292 ms

    def is_prime(n):
        if n < 4:
            return n > 1
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i*i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    layer_num = 0
    n = 0
    d = 1
    while True:
        layer_num += 1
        mid = 1 + 4*(layer_num)*(layer_num+1) - 3*(layer_num)
        diags = [mid+layer_num, mid-layer_num, mid+(3*layer_num), mid-(3*layer_num)]
        pdiags = sum([is_prime(x) for x in diags])
        d += 4
        n += pdiags
        if n/d < .1:
            return 2*layer_num + 1

if __name__ == '__main__':
    usage.usage(solution, n=5)