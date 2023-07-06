from . import usage

def solution():
    # PyPy ~ 160 µs

    # Euler's pentagonal number theorem (partitions)
    
    pent = []
    for i in range(1, 10):
        pent += [i*(3*i-1)//2, -i*(-3*i-1)//2]

    n = 100
    plst = [0] * (n+2)
    plst[1] = 1
    for p in range(2, n+2):
        s = 0
        for i,pn in enumerate(pent):
            if p-pn <= 0:
                break
            if (i//2) % 2 == 0: 
                s += plst[p-pn]
            else:
                s -= plst[p-pn]
        plst[p] = s
    return plst[n+1]-1

if __name__ == '__main__':
    usage.usage(solution, n=100)