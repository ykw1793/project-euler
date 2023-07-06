import os
from . import usage

def solution():
    # PyPy ~ 240 µs

    with open(os.path.join(os.path.dirname(__file__), 'keylog_79.txt'), 'r') as f:
        vals = []
        for line in f.readlines():
            vals.append(int(line))
        vals = [str(x) for x in sorted(list(set(vals)))]

        passcode = list(vals.pop(0))

        tval = None
        idx = None
        while True:
            for i in range(len(vals)):
                if vals[i][1] == passcode[-1]:
                    tval = vals[i]
                    idx = -1
                    break
                elif vals[i][1] == passcode[0]:
                    tval = vals[i]
                    idx = 0
                    break
            if tval:
                if idx == -1:
                    passcode.append(tval[2])
                elif idx == 0:
                    passcode.insert(0, tval[0])
                tval = None
            else:
                break

        while len(vals) > 0:
            i = 0
            while i < len(vals):
                v = vals[i]
                if v[0] in passcode and v[1] in passcode and v[2] in passcode:
                    vals.pop(i)
                else:
                    i += 1

            for i in range(len(vals)):
                v = vals[i]
                for i in range(len(passcode)-1):
                    if v[0] == passcode[i] and v[2] == passcode[i+1]:
                        passcode.insert(i+1, v[1])

        return int(''.join(passcode))

if __name__ == '__main__':
    usage.usage(solution, n=1000)