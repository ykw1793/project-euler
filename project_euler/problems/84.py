import random
from pprint import pprint
from . import usage

def solution():
    # PyPy ~ 100 ms

    n = 40

    go = 0
    j = 10  # jail
    g2j = 30  # go to jail
    cc = [2, 17, 33]  # com. chest
    ch = [7, 22, 36]  # chancee
    r = [5, 15, 25, 35]  # railway
    u = [12, 28]  # utility

    def next_railway(pos):
        if pos == 7:
            return 15
        if pos == 22:
            return 25
        if pos == 36:
            return 5
        
    def next_utility(pos):
        if pos == 7:
            return 12
        if pos == 22:
            return 28
        if pos == 36:
            return 12
        
    def go_back_3(pos):
        return pos-3

    cc_cards = [go, j] + [None] * 14
    ch_cards = [go, j, 11, 24, 39, 5, next_railway, next_railway, next_utility, go_back_3] + [None] * 6

    random.shuffle(cc_cards)
    random.shuffle(ch_cards)

    num_visits = {k:0 for k in range(n)}

    num_rounds = 0
    curr = 0

    while num_rounds < 5000:
        dbl = [False] * 3
        tot = 0
        for roll in range(3):
            dice1 = random.randint(1,4)
            dice2 = random.randint(1,4)
            tot += dice1 + dice2
            if dice1 == dice2:  # rolled a double
                dbl[roll] = True
                continue
            break
        
        if all(dbl):  # if rolled 3 doubles -> g2j
            if curr <= j:
                tot = j - curr
            else:
                tot = (n - curr) + j

        curr += tot
        if curr > (n-1):
            num_rounds += 1
            curr %= n

        if curr == g2j:
            curr = j
        elif curr in cc:
            card = cc_cards.pop(0)
            if card is not None:
                if card == go:
                    num_rounds += 1
                curr = card
            cc_cards.append(card)
        elif curr in ch:
            card = ch_cards.pop(0)
            if card is not None:
                if type(card) == int:
                    if card == go:
                        num_rounds += 1
                    curr = card
                else:
                    curr = card(curr)
            ch_cards.append(card)
        
        num_visits[curr] += 1
    
    num_visits[curr] -= 1
    sorted_keys = sorted(num_visits.items(), key=lambda x: x[1], reverse=True)

    return f'{sorted_keys[0][0]}{sorted_keys[1][0]}{sorted_keys[2][0]}'

if __name__ == '__main__':
    usage.usage(solution, n=1)