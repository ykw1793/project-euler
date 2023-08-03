from itertools import product
from . import usage

def solution():
    # PyPy ~ 240 ms

    sq = ['01', '04', '09', '16', '25', '36', '49', '64', '81']

    lst1 = []
    lst2 = []

    checked = set()

    def count(cnt):
        cube1 = set(lst1)
        cube2 = set(lst2)
        if len(cube1) <= 6 and len(cube2) <= 6:
            extra1 = []
            extra2 = []
            if len(cube1) < 6:
                extra1 = [c for c in '0123456789' if c not in cube1]
                extra1 = [set(x) for x in list(product(extra1, repeat=6-len(cube1)))]
                extra1 = [x for x in extra1 if len(x) != 6-len(cube1)-1]
            if len(cube2) < 6:
                extra2 = [c for c in '0123456789' if c not in cube2]
                extra2 = [set(x) for x in list(product(extra2, repeat=6-len(cube2)))]
                extra2 = [x for x in extra2 if len(x) != 6-len(cube2)-1]
            if len(extra1) > 0 and len(extra2) > 0:
                for d1 in extra1:
                    for d2 in extra2:
                        t1 = tuple(sorted(cube1.union(d1)) + sorted(cube2.union(d2)))
                        t2 = tuple(sorted(cube2.union(d2)) + sorted(cube1.union(d1)))
                        if t1 not in checked and t2 not in checked:
                            checked.add(t1)
                            checked.add(t2)
                            cnt += 1
            elif len(extra1) > 0:
                for d1 in extra1:
                    t1 = tuple(sorted(cube1.union(d1)) + sorted(cube2))
                    t2 = tuple(sorted(cube2) + sorted(cube1.union(d1)))
                    if t1 not in checked and t2 not in checked:
                        checked.add(t1)
                        checked.add(t2)
                        cnt += 1
            elif len(extra2) > 0:
                for d2 in extra2:
                    t1 = tuple(sorted(cube1) + sorted(cube2.union(d2)))
                    t2 = tuple(sorted(cube2.union(d2)) + sorted(cube1))
                    if t1 not in checked and t2 not in checked:
                        checked.add(t1)
                        checked.add(t2)
                        cnt += 1
            else:
                t1 = tuple(sorted(cube1) + sorted(cube2))
                t2 = tuple(sorted(cube2) + sorted(cube1))
                if t1 not in checked and t2 not in checked:
                    checked.add(t1)
                    checked.add(t2)
                    cnt += 1
        return cnt

    def loop(depth, cnt):
        if depth > 8:
            return
        
        for i in range(2):
            d1 = sq[depth][i]
            d2 = sq[depth][(i+1)%2]
            lst1.append(d1)
            lst2.append(d2)

            if d1 in ['6', '9']:
                if d2 in ['6', '9']:
                    lst1.pop()
                    lst2.pop()
                    for nd1 in ['6', '9']:
                        for nd2 in ['6', '9']:
                            lst1.append(nd1)
                            lst2.append(nd2)
                            if depth == len(sq)-1:
                                cnt = count(cnt)
                            else:
                                cnt = loop(depth+1, cnt)
                            lst1.pop()
                            lst2.pop()
                            
                else:
                    lst1.pop()
                    for nd in ['6', '9']:
                        lst1.append(nd)
                        if depth == len(sq)-1:
                            cnt = count(cnt)
                        else:
                            cnt = loop(depth+1, cnt)
                        lst1.pop()
                    lst2.pop()
            else:
                if d2 in ['6', '9']:
                    lst2.pop()
                    for nd in ['6', '9']:
                        lst2.append(nd)
                        if depth == len(sq)-1:
                            cnt = count(cnt)
                        else:
                            cnt = loop(depth+1, cnt)
                        lst2.pop()
                    lst1.pop()
                else:
                    if depth == len(sq)-1:
                        cnt = count(cnt)
                    else:
                        cnt = loop(depth+1, cnt)
                    lst1.pop()
                    lst2.pop()
        return cnt

    cnt = loop(0, 0)
    return cnt
    

if __name__ == '__main__':
    usage.usage(solution, n=1)