from . import usage

def solution():
    # PyPy ~ 320 ms

    def is_right_triangle(x1,y1,x2,y2):
        s1_sq = x1**2 + y1**2
        s2_sq = x2**2 + y2**2
        s3_sq = abs(x2-x1)**2 + abs(y2-y1)**2
        if 0 in [s1_sq, s2_sq, s3_sq]:
            return False
        hypot = max(s1_sq, s2_sq, s3_sq)
        if s1_sq == hypot:
            return s2_sq + s3_sq == hypot
        if s2_sq == hypot:
            return s1_sq + s3_sq == hypot
        if s3_sq == hypot:
            return s1_sq + s2_sq == hypot

    lim = 50
    cnt = 0
    chk = set()
    for x1 in range(lim+1):
        for y1 in range(lim+1):
            for x2 in range(lim+1):
                for y2 in range(lim+1):
                    if is_right_triangle(x1,y1,x2,y2):
                        t1 = (x1,y1,x2,y2)
                        t2 = (x2,y2,x1,y1)
                        if t1 not in chk and t2 not in chk:
                            chk.add(t1)
                            chk.add(t2)
                            cnt += 1
    return cnt

if __name__ == '__main__':
    usage.usage(solution, n=1)