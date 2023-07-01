from . import usage

def solution():
    # PyPy ~ 17 ms

    is_triangle = lambda x: (lambda det: (int(det**.5)**2 == det and
                                          (int(det**.5)-1) % 2 == 0))(8*x+1)
    
    is_square = lambda x: int(x**.5)**2 == x

    is_pentagon = lambda x: (lambda det: (int(det**.5)**2 == det and
                                          (int(det**.5)+1) % 6 == 0))(24*x+1)
    
    is_hexagon = lambda x: (lambda det: (int(det**.5)**2 == det and
                                         (int(det**.5)+1) % 4 == 0))(8*x+1)
    
    is_heptagon = lambda x: (lambda det: (int(det**.5)**2 == det and
                                          (int(det**.5)+3) % 10 == 0))(40*x+9)
    
    is_octagon = lambda x: (lambda det: (int(det**.5)**2 == det and
                                         (int(det**.5)+1) % 3 == 0))(3*x+1)

    _map = {3: is_triangle, 4: is_square, 5: is_pentagon, 
            6: is_hexagon, 7: is_heptagon, 8: is_octagon}
    
    lim = 8
    
    def recursion(f2, typs, hist):
        lst = []
        for l2 in range(10, 100):
            num = f2*100+l2
            slst = []
            for typ in typs:
                if _map[typ](num):
                    slst.append((num, typs.difference(set([typ])), hist+[num], typ))
            lst.extend(slst)

        for tup in lst:
            if len(tup[1]) > 0:
                ret = recursion(tup[0]%100, tup[1], tup[2])
                if ret:
                    return ret
            else:
                if (tup[2][-1] % 100) == (tup[2][0] // 100):
                    return tup[2]

    for f2 in range(10, 100):
        ret = recursion(f2, set(range(3, lim+1)), [])
        if ret:
            return sum(ret)

if __name__ == '__main__':
    usage.usage(solution, n=100)