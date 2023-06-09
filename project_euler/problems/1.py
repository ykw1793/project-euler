import numpy as np

from . import usage

def solution():
    s = np.arange(0, 1000, 3).sum()
    s += np.arange(0, 1000, 5).sum()
    s -= np.arange(0, 1000, 15).sum()

    return s

if __name__ == '__main__':
    usage.usage(solution)