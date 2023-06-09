from . import usage

def solution():
    # Using loops ~ 15 µs ~ O(n)

    # sqs = 0
    # s = 0
    # for i in range(1, 101):
    #     s += i
    #     sqs += i*i
    # d = s*s-sqs
    
    # Using closed expressions ~ 700 ns ~ O(1)

    n = 100
    sqs = n * (n+1) * (2*n+1) // 6
    s = n * (n+1) // 2
    d = s*s-sqs

    return d

if __name__ == '__main__':
    usage.usage(solution)