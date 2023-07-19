import os
from . import usage

def solution():
    # PyPy ~ 2.2 ms

    d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    def to_dec(rom):
        v = 0
        i = 0
        while i < (len(rom)-1):
            if d[rom[i]] < d[rom[i+1]]:
                v += d[rom[i+1]]-d[rom[i]]
                i += 2
            else:
                v += d[rom[i]]
                i += 1
        if i == len(rom)-1:
            v += d[rom[-1]]
        return v
    
    def mulsub(dec, v, c):
        mul = dec//v
        s = c * mul
        dec -= v * mul
        return s, dec

    def to_rom(dec):
        tups = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        v = ''
        for t in tups:
            if dec == 0:
                break
            if dec >= t[0]:
                if t[0] in [1000, 100, 10, 1]:
                        s, dec = mulsub(dec, *t)
                        v += s
                else:
                    v += t[1]
                    dec -= t[0]
        return v

    with open(os.path.join(os.path.dirname(__file__), 'roman_89.txt'), 'r') as f:
        roms = []
        for line in f.readlines():
            roms.append(line.strip())

        new_sum = sum([len(to_rom(to_dec(x))) for x in roms])
        roms_sum = sum([len(x) for x in roms])

        return roms_sum - new_sum

if __name__ == '__main__':
    usage.usage(solution, n=1)