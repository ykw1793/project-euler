from . import usage

def solution():
    # PyPy ~ 850 µs

    def translate(n):
        vocab = {
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen',
            20: 'twenty',
            30: 'thirty',
            40: 'forty',
            50: 'fifty',
            60: 'sixty',
            70: 'seventy',
            80: 'eighty',
            90: 'ninety',
            100: 'hundred',
            1000: 'thousand'
        }

        ns = str(n)
        w = ''
        r2 = n % 100
        
        if r2 > 0:
            if r2 <= 20:
                w = vocab[r2]
            else:
                w = vocab[(r2 // 10) * 10]
                if r2 % 10 > 0:
                    w += vocab[r2 % 10]
        
        l2 = n // 100
        temp_words = ''
        if l2 > 0:
            if l2 <= 9:
                temp_words = vocab[l2] + vocab[100]
                if r2 > 0:
                    temp_words += 'and'
            else:
                temp_words = vocab[l2 // 10] + vocab[1000]
                if l2 % 10 > 0:
                    temp_words += vocab[l2 % 10] + vocab[100]
                if r2 > 0:
                    temp_words += 'and'
        w = temp_words + w
        return w

    n = 1000
    nums = list(range(1, n+1))
    for i in range(n):
        nums[i] = translate(nums[i])
    
    return len(''.join(nums))
    

if __name__ == '__main__':
    usage.usage(solution)