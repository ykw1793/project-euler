from . import usage

def solution():
    # PyPy ~ 130 ms

    target = 2_000_000
    delta = 100

    close_w, close_h = None, None
    diff = target
    
    w = 1
    while w < (target + delta):
        h = w
        while True:
            if (w * h) >= target + delta:
                break
            cnt = (w * (w+1) * h * (h+1)) // 4
            _diff = abs(target - cnt)
            if _diff < delta:
                if _diff < diff:
                    diff = _diff
                    close_w, close_h = w, h
            h += 1
        w += 1

    return close_w * close_h

if __name__ == '__main__':
    usage.usage(solution, n=10)