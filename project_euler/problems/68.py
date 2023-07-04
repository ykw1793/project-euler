from itertools import permutations
from . import usage

def solution():
    # PyPy ~ 45 ms

    digs = list(range(1,10))
    perms = []
    for xp in permutations(digs):
        x = [10, *xp]
        if (x[0]+x[2]) == (x[8]+x[9]) and (x[6]+x[7]) == (x[9]+x[1]):
            for i in range(0,5,2):
                if (x[i]+x[i+1]) != (x[i+3]+x[i+4]):
                    break
            else:
                ml = [x[0],x[3],x[5],x[7],x[9]]
                midx = ml.index(min(ml))
                
                groups = [(x[0],x[1],x[2])]
                for i in range(3,8,2):
                    groups.append((x[i],x[i-1],x[i+1]))
                groups.append((x[9],x[8],x[1]))

                p = []
                for i in range(midx, midx+5):
                    p += [*groups[i % 5]]
                perms.append(int(''.join([str(v) for v in p])))
    return max(perms)

if __name__ == '__main__':
    usage.usage(solution, n=20)