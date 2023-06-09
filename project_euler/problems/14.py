from . import usage

def solution():
    # PyPy ~ 780 ms
    # CPython ~ 1.7 s

    col = {1: 1}
    ceil = 1_000_000

    for n in range(ceil//2, ceil):
        i = n
        chain = []
        while True:
            ni = i // 2 if i % 2 == 0 else (3 * i + 1)//2
            if ni in col:
                col[i] = col[ni] + 1
                break
            else:
                chain.append((i, 1 if i % 2 == 0 else 2))
                i = ni
        while len(chain) > 0:
            j = chain.pop()
            col[j[0]] = col[i] + j[1]
            i = j[0]

    return max(col, key=col.get)


if __name__ == '__main__':
    usage.usage(solution, n=5)