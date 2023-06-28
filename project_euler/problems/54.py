import os
from . import usage

HIGH_CARD = 1
ONE_PAIR = 2
TWO_PAIRS = 3
THREE_OF_A_KIND = 4
STRAIGHT = 5
FLUSH = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
STRAIGHT_FLUSH = 9
ROYAL_FLUSH = 10

HAND_DICT = {
    1: 'HIGH CARD',
    2: 'ONE PAIR',
    3: 'TWO PAIR',
    4: 'THREE OF A KIND',
    5: 'STRAIGHT',
    6: 'FLUSH',
    7: 'FULL HOUSE',
    8: 'FOUR OF A KIND',
    9: 'STRAIGHT FLUSH',
    10: 'ROYAL FLUSH'
}

VAL_DICT = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
    '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
}

class Pair:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'({self.value}, {self.suit})'

class Hand:
    def __init__(self, lst: list[Pair]):
        self.lst = lst
        self.hand = None
        self.handval = None
    
    def evaluate(self):
        valset = set([x.value for x in self.lst])
        suitset = set([x.suit for x in self.lst])

        if (len(suitset) == 1 and len(valset) == 5 and 
              max(valset) - min(valset) == 4):
            if VAL_DICT['A'] in valset:
                self.hand = ROYAL_FLUSH
            else:
                self.hand = STRAIGHT_FLUSH
                self.handval = max(valset)
        elif len(valset) == 2:
            l = list(valset)
            c0 = sum([1 for x in self.lst if x.value == l[0]])
            if c0 in [1, 4]:
                self.hand = FOUR_OF_A_KIND
                self.handval = l[1] if c0 == 1 else l[0]
            else:
                self.hand = FULL_HOUSE
                self.handval = l[1] if c0 == 2 else l[0]
        elif len(suitset) == 1:
            self.hand = FLUSH
            self.handval = sorted(list(valset), reverse=True)
        elif len(valset) == 5 and max(valset) - min(valset) == 4:
            self.hand = STRAIGHT
            self.handval = max(valset)
        elif len(valset) == 3:
            l = list(valset)
            c0 = sum([1 for x in self.lst if x.value == l[0]])
            c1 = sum([1 for x in self.lst if x.value == l[1]])
            c2 = sum([1 for x in self.lst if x.value == l[2]])
            if set([c0,c1,c2]) == set([3,1,1]):
                self.hand = THREE_OF_A_KIND
                if c0 == 3:
                    self.handval = l[0]
                elif c1 == 3:
                    self.handval = l[1]
                else:
                    self.handval = l[2]
            else:
                self.hand = TWO_PAIRS
                self.handval = []
                if c0 == 1:
                    self.handval += [max(l[1], l[2]), min(l[1], l[2]), l[0]]
                elif c1 == 1:
                    self.handval += [max(l[0], l[2]), min(l[0], l[2]), l[1]]
                else:
                    self.handval += [max(l[0], l[1]), min(l[0], l[1]), l[2]]
        elif len(valset) == 4:
            self.hand = ONE_PAIR
            l = sorted([x.value for x in self.lst])
            pairval = None
            for i in range(len(l)-1):
                if l[i] == l[i+1]:
                    pairval = l[i]
                    break
            rest = sorted([x for x in l if x != pairval], reverse=True)
            self.handval = [pairval] + rest
        else:
            self.hand = HIGH_CARD
            self.handval = sorted(list(valset), reverse=True)

class Round:
    def __init__(self, p1, p2, line):
        self.p1: Hand = p1
        self.p2: Hand = p2
        self.line = line
        self.p1win = None

    def __repr__(self):
        if self.p1win:
            o = f'Round: {self.line[:14]} -> {HAND_DICT[self.p1.hand]}'
            if self.p1.hand == self.p2.hand:
                o += f' -> {self.p1.handval}'
            o += ' -> WIN\n' + f'       {self.line[15:]} -> {HAND_DICT[self.p2.hand]}'
            if self.p1.hand == self.p2.hand:
                o += f' -> {self.p2.handval}'
            o += '\n'
        else:
            o = f'Round: {self.line[:14]} -> {HAND_DICT[self.p1.hand]}'
            if self.p1.hand == self.p2.hand:
                o += f' -> {self.p1.handval}'
            o += '\n' + f'       {self.line[15:]} -> {HAND_DICT[self.p2.hand]}'
            if self.p1.hand == self.p2.hand:
                o += f' -> {self.p2.handval} -> WIN'
            o += '\n'
        
        return o
        
    def tie_break(self):
        p1 = self.p1.handval
        p2 = self.p2.handval

        if type(p1) == list:
            for i in range(len(p1)):
                if p1[i] != p2[i]:
                    return p1[i] > p2[i]
        else:
            return p1 > p2

    def evaluate(self):
        self.p1.evaluate()
        self.p2.evaluate()

        if self.p1.hand == self.p2.hand:
            self.p1win = self.tie_break()
        else:
            self.p1win = self.p1.hand > self.p2.hand

def parse(f):
    l = []
    for line in f.readlines():
        ls = [Pair(VAL_DICT[x[0]], x[1]) for x in line.split()]
        p1 = Hand(ls[:5])
        p2 = Hand(ls[5:])
        l.append(Round(p1, p2, line.rstrip('\n')))
    return l

def solution():
    # PyPy ~ 33 ms

    with open(os.path.join(os.path.dirname(__file__), 'poker_54.txt'), 'r') as f:
        l: list[Round] = parse(f)
        tot = 0
        for x in l:
            x.evaluate()
            if x.p1win:
                tot += 1
        return tot

if __name__ == '__main__':
    usage.usage(solution, n=20)