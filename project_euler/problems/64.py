from . import usage

def solution():
    # PyPy ~ 80 ms

    def con_frac(r):
        lst = []
        w = int(r**.5)
        lst.append(w)

        d = [1,r,-w]
        n = [1,0,1]
        mem = set()
        
        while True:
            n = [n[2],d[1],-d[2]]
            d = [1,0,d[0]*(d[1]-d[2]*d[2])]
            if d[2] % n[0] == 0:
                d[2] = d[2] // n[0]
                n[0] = 1
            
            num = n[0] * (n[1]**.5 + n[2])
            denom = d[2]
            w = int(num/denom)
            
            rem = (n[0] * n[2]) - (denom * w)
            if rem % n[0] != 0:
                raise ValueError
            n[2] = rem // n[0]

            n[0], d[0] = d[0], n[0]
            n[1], d[1] = d[1], n[1]
            n[2], d[2] = d[2], n[2]

            if (w, *n, *d) in mem:
                break
            else:
                lst.append(w)
                mem.add((w, *n, *d))
        return lst

    count = 0
    for x in range(2, 10_001):
        if round(x**.5)**2 != x:
            lst = con_frac(x)
            if len(lst) % 2 == 0:
                count += 1
    return count

if __name__ == '__main__':
    usage.usage(solution, n=10)