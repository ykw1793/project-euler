from . import usage

def solution():
    # PyPy ~ 145 ms

    tot = 0
    checked = set()

    for i in range(10, 100):
        for j in range(100, 1000):
            ij = i*j
            s = str(i) + str(j) + str(ij)
            ss = sorted(list(set(s)))
            if (len(s) == 9 and 
                ss == sorted(list(set('123456789'))) and 
                ij not in checked):
                checked.add(ij)
                tot += ij

    for i in range(1, 10):
        for j in range(1000, 10000):
            ij = i*j
            s = str(i) + str(j) + str(ij)
            ss = sorted(list(set(s)))
            if (len(s) == 9 and 
                ss == sorted(list(set('123456789'))) and 
                ij not in checked):
                checked.add(ij)
                tot += ij

    return tot

if __name__ == '__main__':
    usage.usage(solution, n=5)