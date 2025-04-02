alphabet = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def calc_value_for_ranges(letter, amount):    
    val = 0

    for i in range(0, amount):
        val += letter * (26**i) 

    return val

def create_ranges():
    a =  1
    z = 26

    for i in range(1, 20):
        print(f'A*{i:>2}: {calc_value_for_ranges(a, i):>30}')
        print(f'Z*{i:>2}: {calc_value_for_ranges(z, i):>30}')
        print()


def find_range(val):
    i = 0
    for r in ranges: #doesn't have access
        if r[0] <= val and r[1] >= val:
            return i
        i += 1
    return 'out of range'


def main_test():
    '''
        The word is 'test'
        The value of that word is...
        (26^0 * 20) + (26^1 * 5) + (26^2 * 19) + (26^3 * 20)
        (1 * 20)    + (26 * 5)   + (676 * 19)  + (17576 * 20)
        20 + 130 + 12844 + 351520
        --> 364514 <--
    '''

    ranges = [
        (0, 0),
        (1, 26),
        (27, 702),
        (703, 18278),
        (18279, 475254)
    ]

    word_value = 364514

    word_range = find_range(word_value)
    # print(ranges[word_range])

    end_of_range_closest_to = 0 if (word_value-ranges[word_range][0] < ranges[word_range][1]-word_value) else 1

    print(end_of_range_closest_to)

    if end_of_range_closest_to == 0:
        decoded_word = 'A' * word_range
    else:
        decoded_word = 'Z' * word_range

    print(decoded_word)


def calc_value(word):
    val = 0

    for i in range(len(word)):
        val += alphabet.index(word[i]) * (26**i) 

    return val



aaa = calc_value('aaa')
aab = calc_value('aac')
print(aab - aaa)