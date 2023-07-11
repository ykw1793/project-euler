import os
from . import usage

def solution():
    # PyPy ~ 1 ms

    with open(os.path.join(os.path.dirname(__file__), 'matrix_81.txt'), 'r') as f:
        mat = []
        for line in f.readlines():
            mat.append([int(x) for x in line.strip().split(',')])

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i-1 < 0 and j-1 < 0:
                    pass
                elif i-1 < 0:
                    mat[i][j] += mat[i][j-1]
                elif j-1 < 0:
                    mat[i][j] += mat[i-1][j]
                else:
                    mat[i][j] += min(mat[i-1][j], mat[i][j-1])
        return mat[-1][-1]

if __name__ == '__main__':
    usage.usage(solution, n=500)