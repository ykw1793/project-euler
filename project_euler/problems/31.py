from . import usage

def solution():
    # PyPy ~ 13 µs

    coins = [1,2,5,10,20,50,100,200]
    target = 200
    
    num_ways = [0] * (target+1)
    num_ways[0] = 1
    
    for coin_idx in range(len(coins)):
        for _target in range(coins[coin_idx], target+1):
            num_ways[_target] = (num_ways[_target] 
                                 + num_ways[_target-coins[coin_idx]])
    
    return num_ways[target]


if __name__ == '__main__':
    usage.usage(solution)