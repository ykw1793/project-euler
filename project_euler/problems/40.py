from . import usage

def solution():
    # PyPy ~ 4 ms

    limit = 1_000_000
    max_length = 1

    number = 1
    tot_length = 0
    num_length = len(str(number))

    product = 1
    while True:
        while tot_length + num_length < max_length:
            tot_length += num_length
            number += 1
            num_length = len(str(number))

        position = max_length - tot_length
        product *= int(str(number)[position-1])

        if max_length < limit:
            max_length *= 10
        else:
            break
    
    return product

if __name__ == '__main__':
    usage.usage(solution, n=100)