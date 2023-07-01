import math
from . import usage

def solution():
    # PyPy ~ 45 µs

    count = 0
    num_digs = 1
    while True:
        low = 10**(num_digs-1)
        high = (10**num_digs)-1
        low_val = math.ceil(low**(1/num_digs))
        high_val = math.floor(high**(1/num_digs))
        if len(str(high_val**num_digs)) > num_digs:
            high_val -= 1
        diff = (high_val-low_val)+1
        if diff == 0:
            break
        count += (high_val-low_val)+1
        num_digs += 1
    return count

if __name__ == '__main__':
    usage.usage(solution, n=1000)