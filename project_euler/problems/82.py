import os
from . import usage

def solution():
    # PyPy ~ 80 ms

    with open(os.path.join(os.path.dirname(__file__), 'matrix_82.txt'), 'r') as f:
        mat = []
        for line in f.readlines():
            mat.append([int(x) for x in line.strip().split(',')])

        for col in range(1, len(mat[0])):
            orig_col = [mat[row][col] for row in range(len(mat))]
            for row_i in range(len(mat)):
                mat[row_i][col] += mat[row_i][col-1]
                for row_j in range(row_i):
                    s = mat[row_j][col-1] + sum(orig_col[row_j:row_i+1])
                    mat[row_i][col] = min(mat[row_i][col], s)
                for row_j in range(row_i+1, len(mat)):
                    s = mat[row_j][col-1] + sum(orig_col[row_i:row_j+1])
                    mat[row_i][col] = min(mat[row_i][col], s)
        return min([mat[row][-1] for row in range(len(mat))])

if __name__ == '__main__':
    usage.usage(solution, n=10)