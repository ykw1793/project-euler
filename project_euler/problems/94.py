from . import usage

def solution():
    # PyPy ~ 290 ns

    # OEIS - A120893

    a = [1,1,5]
    while a[-1] < 333_333_334:
        a.append(3 * a[-1] + 3 * a[-2] - a[-3])
    a = a[2:-1]
    return 3*sum(a)

    # PyPy ~ 1.9 s

    # def area_plus(a):
    #     sq = 3*a*a - 2*a - 1
    #     sqrt = round(sq ** .5)
    #     if sqrt ** 2 == sq:
    #         a4 = (a+1) * sqrt
    #         if a4 % 4 == 0:
    #             return True
    #     return False
            
    # def area_minus(a):
    #     sq = 3*a*a + 2*a - 1
    #     sqrt = round(sq ** .5)
    #     if sqrt ** 2 == sq:
    #         a4 = (a-1) * sqrt
    #         if a4 % 4 == 0:
    #             return True
    #     return False

    # tot = 0
    
    # l = []
    # a = 3
    # da = 2
    # while a < 333_333_334:
    #     if area_plus(a):
    #         tot += 3*a + 1
    #         l.append(a)
    #         da = 4
    #         a *= 10
    #         rem = (a - l[-1] + da - 1) % da
    #         a += da - 1 - rem
    #     else:
    #         a += da

    # l = []
    # a = 3
    # da = 2
    # while a < 333_333_334:
    #     if area_minus(a):
    #         tot += 3*a - 1
    #         l.append(a)
    #         da = 16
    #         a *= 10
    #         rem = (a - l[-1] + da - 1) % da
    #         a += da - 1 - rem
    #     else:
    #         a += 2
    
    # return tot

if __name__ == '__main__':
    usage.usage(solution, n=1)