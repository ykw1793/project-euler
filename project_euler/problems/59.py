import os
from . import usage

def solution():
    # PyPy ~ 1.6 ms

    with open(os.path.join(os.path.dirname(__file__), 'cipher_59.txt'), 'r') as f:
        ctext = []
        for line in f.readlines():
            ctext += [int(x) for x in line.split(',')]
        
        for a in range(97, 123):
            for b in range(97, 123):
                for c in range(97, 123):
                    key = [a, b, c]
                    text = []
                    for i in range(len(ctext)):
                        tchar = ctext[i] ^ key[i % 3]
                        if tchar < 32 or tchar > 126:
                            break
                        elif tchar == 123:
                            break
                        elif tchar in [33, 44, 58, 59]:
                            if i < len(ctext)-1:
                                nchar = ctext[i+1] ^ key[(i+1) % 3]
                                if nchar != 32:
                                    break
                                else:
                                    text.append(tchar)
                        else:
                            text.append(tchar)
                    else:
                        if text[-1] in [46, 63, 33]:
                            return sum(text)

if __name__ == '__main__':
    usage.usage(solution, n=1000)