from . import usage

def solution():
    # PyPy ~ 20 ms

    def decimal(t):
        denom_len = len(str(t[1]))
        ns = str(t[0])
        q = []
        n = int(ns[:denom_len-1]) if denom_len > 1 else 0
        nidx = denom_len-1
        first = True
        while len(q) < 102:
            n *= 10
            if nidx < len(ns):
                n += int(ns[nidx])
            if first and len(q) > 0 and nidx >= len(ns):
                q.append('.')
                first = False
            nidx += 1
            if n < t[1] and nidx-1 >= len(ns):
                if '.' in q:
                    q.append('0')
                else:
                    first = False
                    if len(q) > 0:
                        q.append('.')
                    else:
                        q += ['0', '.']
                continue
            qval = str(n//t[1])
            q.append(qval)
            n = n - t[1]*int(q[-1])
            if qval == '0':
                q.pop()
        return ''.join(q).replace('.', '')

    def evaluate(lst):
        n = 1
        d = lst[-1]
        for i in range(-2, -len(lst)-1, -1):
            n += d * lst[i]
            n,d = d,n
        return (d,n)

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
    
    s = 0
    for n in range(2, 101):
        if round(n**.5)**2 != n:
            l = con_frac(n)
            w = [l[0]]
            f = l[1:]

            prev_dec = ''
            curr_dec = None
            m = 1
            while True:
                curr_dec = decimal(evaluate(w+f*m))
                if len(curr_dec) == 101 and curr_dec == prev_dec:
                    break
                prev_dec = curr_dec
                m += 20
            ns = sum([int(x) for x in curr_dec])-int(curr_dec[-1])
            s += ns
    return s

if __name__ == '__main__':
    usage.usage(solution, n=10)