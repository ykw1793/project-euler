from . import usage

def solution():
    done = []
    p = 1    
    for i in range(2,21):
        if i not in done:
            j = i
            for d in done:
                if j % d == 0:
                    j //= d
            done.append(j)
            p *= j
    return p

if __name__ == '__main__':
    usage.usage(solution)