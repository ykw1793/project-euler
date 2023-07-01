from . import usage

def solution():
    # PyPy ~ 6 ms

    def evaluate(lst):
        n = 1
        d = lst[-1]
        for i in range(-2, -len(lst)-1, -1):
            n += d * lst[i]
            n,d = d,n
        return (d,n)

    def solve(D):
        pell = lambda x,y: x*x - D*y*y == 1

        compact = []
        w = int(D**.5)
        compact.append(w)

        d = [1,D,-w]
        n = [1,0,1]
        mem = set()

        while True:
            n = [n[2], d[1], -d[2]]
            d = [1, 0, d[0] * (d[1] - d[2]*d[2])]
            if d[2] % n[0] == 0:
                d[2] = d[2] // n[0]
                n[0] = 1

            nval = n[0] * (n[1]**.5 + n[2])
            dval = d[2]
            w = int(nval/dval)

            rem = (n[0] * n[2]) - (dval * w)
            n[2] = rem // n[0]

            n[0], d[0] = d[0], n[0]
            n[1], d[1] = d[1], n[1]
            n[2], d[2] = d[2], n[2]

            aval = (w, *n, *d)
            if aval in mem:
                break
            else:
                compact.append(w)
                mem.add(aval)

                frac = evaluate(compact)
                if pell(*frac):
                    return frac[0]
        
        i = 1
        while True:
            compact.append(compact[i])
            i += 1
            frac = evaluate(compact)
            if pell(*frac):
                return frac[0]

    max_x, max_D = 0,0
    for D in range(2, 1001):
        if round(D**.5)**2 == D:
            continue
        x = solve(D)
        if x > max_x:
            max_x = x
            max_D = D
    return max_D

 
if __name__ == '__main__':
    usage.usage(solution, n=100)