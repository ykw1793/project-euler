import time

def usage(solution, n = 1000):
    sol = None
    t = 0
    for iter in range(n):
        i = time.perf_counter_ns()
        sol = solution()
        f = time.perf_counter_ns()
        t += f-i
    print(f'Solution = {sol}')

    t /= n
    s = 'ns'
    if len(str(t).split('.')[0]) > 3:
        t /= 1000
        s = 'µs'
    if len(str(t).split('.')[0]) > 3:
        t /= 1000
        s = 'ms'
    if len(str(t).split('.')[0]) > 3:
        t /= 1000
        s = 's'
    print(f'Time = {t:.4f} {s}')