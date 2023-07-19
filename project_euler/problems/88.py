import math
from . import usage

def solution():
    # PyPy ~ 600 ms

    lim = 12000
    fac = {}

    def is_prime(n):
        if n < 4:
            return n > 1
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    def resolve(lst):
        f = set([lst[0]])
        for i in range(1, len(lst)):
            f.add(lst[i])
            t = lst[i]
            f0 = fac[t[0]]
            f1 = fac[t[1]]
            if len(f0) > 1 and len(f1) > 1:
                for tf0 in f0:
                    for tf1 in f1:
                        f.add(tuple(sorted([*tf0, *tf1])))
            elif len(f0) > 1:
                for tf0 in f0:
                    f.add(tuple(sorted([*tf0, t[1]])))
            elif len(f1) > 1:
                for tf1 in f1:
                    f.add(tuple(sorted([t[0], *tf1])))
        return f
    
    def factors(n):
        f = [(n,)]
        if not is_prime(n):
            for i in range(2, int(n**.5)+1):
                if n % i == 0:
                    t = (i, n//i)
                    f.append(t)
        f = resolve(f)
        fac[n] = f

    klst = set(range(2, lim + 1))
    kdict = {}
    kdict_lst = {}

    minlst = set()
    i = 1
    while len(klst) > 0:
        i += 1
        factors(i)
        tbr = set()
        for l in fac[i]:
            if len(l) == 1:
                continue
            s = sum(l)
            p = math.prod(l)
            k = p-s+len(l)
            if k in klst and k not in tbr:
                minlst.add(p)
                kdict[k] = p
                kdict_lst[k] = l
                tbr.add(k)
        for v in tbr:
            klst.remove(v)

    return sum(minlst)


    # k = 2
    # l = None

    # def s():
    #     return sum(l) + (k - len(l))

    # def p():
    #     return math.prod(l)

    # def add_one_prod():
    #     return p() * (l[-1]+1) // l[-1]
    
    # def add_one_sum():
    #     return s() + 1
    
    # def append_two_prod():
    #     return p() * 2
    
    # def append_two_sum():
    #     return s() + 1
    
    # def last_two_equal():
    #     return l[-1] == l[-2]
    
    # def add_one():
    #     if len(l) > 1 and last_two_equal():
    #         l.pop()
    #         return add_one()
    #     l[-1] += 1

    # def append_two():
    #     l.append(2)

    # def next_seq():
    #     if len(l) == k:
    #         if add_one_prod() > add_one_sum():
    #             l.pop()
    #         add_one()
    #     else:
    #         if append_two_prod() > append_two_sum():
    #             add_one()
    #         else:
    #             append_two()
            
    #         if len(l) == 1:
    #             append_two()
    #         elif len(l) == 2 and l[1] == 2 and l[0] != k:
    #             if append_two_prod() > append_two_sum():
    #                 add_one()
    #             else:
    #                 append_two()

    # fin = set()
    # psbl = []
    # psbl_lst = []

    # while k <= lim:
    #     l = [2]
    #     while l[0] <= k:
    #         if l[0] == k:
    #             psbl.append(k*2)
    #             break
    #         else:
    #             next_seq()
    #             sval = s()
    #             if s() == p():
    #                 psbl.append(sval)
    #                 psbl_lst.append(l.copy())
    #             if len(psbl) >= 4:
    #                 break
    #     fin.add(min(psbl))
    #     # print('k =', k, 'prodsum =', min(psbl))
    #     if kdict[k] != min(psbl):
    #         print('Did not match -> k =', k, '| actual =', min(psbl), '~', psbl_lst[psbl.index(min(psbl))], '| found =', kdict[k], '~', kdict_lst[k])
    #     psbl = []
    #     psbl_lst = []
    #     k += 1

    # return sum(fin)


if __name__ == '__main__':
    usage.usage(solution, n=1)