from . import usage

def solution():
    digfac = [1]
    for i in range(1,10):
        digfac.append(digfac[-1]*i)

    # PyPy ~ 5.5 s

    lim = 1_000_000
    mem = {}
    cnt = 0
    for n in range(1, lim):
        if n not in mem:
            mem[n] = [False, list()]
        if mem[n][0] == False:
            curr = n if len(mem[n][1]) == 0 else mem[n][1][-1]
            seen = mem[n][1]
            if len(seen) == 0:
                seen.append(curr) 
            next = 0
            while True:
                next = sum([digfac[int(x)] for x in str(curr)])
                if next in seen:
                    break
                if next in mem:
                    for val in mem[next][1]:
                        if val in seen:
                            break
                        seen.append(val)
                else:
                    seen.append(next)
                curr = seen[-1]
            curr = next
            mem[n][0] = True
            passed = False
            for i in range(1, len(seen)):
                si = seen[i]
                passed = passed or (si == curr)
                if si > n:
                    if si not in mem:
                        mem[si] = [False, list()]
                    if mem[si][0] == False:
                        mem[si][1] = seen[i:]
                        if not passed:
                            mem[si][0] = True
                    else:
                        if (len(seen)-i) > len(mem[si][1]):
                            mem[si][1] = seen[i:]
                            if passed:
                                mem[si][0] = True
            mem[curr][0] = True
            if len(seen) == 60:
                cnt += 1
        else:
            pass
    return cnt

if __name__ == '__main__':
    usage.usage(solution, n=1)