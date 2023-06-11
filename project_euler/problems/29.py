from . import usage

def solution():
    # PyPy ~ 14 ms

    distinct_terms = set()
    
    for a in range(2, 101):
        for b in range(2, 101):
            distinct_terms.add(a**b)
    
    return len(distinct_terms)

if __name__ == '__main__':
    usage.usage(solution, n=50)