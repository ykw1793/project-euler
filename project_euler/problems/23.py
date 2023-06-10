from . import usage

def solution():
    # PyPy ~ 433 ms

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
        return (f - n) > n
    
    n = 28123
    abundant = {num:d(num) for num in range(1, n+1)}
    s = 1
    for num in range(2,n+1):
        for i in range(2, num//2+1):
            if abundant[i] and abundant[num-i]:
                break
        else:
            s += num
    return s

if __name__ == '__main__':
    usage.usage(solution, n=5)