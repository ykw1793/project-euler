from . import usage

def solution():
    # PyPy ~ 30 µs

    lst = [2]
    for k in range(1,34):
        lst += [1,2*k,1]
    
    n = 1
    d = lst[-1]
    for i in range(-2,-len(lst)-1,-1):
        n += d*lst[i]
        n,d = d,n
    return sum([int(x) for x in str(d)])

if __name__ == '__main__':
    usage.usage(solution, n=1000)