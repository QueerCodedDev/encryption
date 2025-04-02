# ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def append_letters():
#     temp = ''

#     return temp



# MAX_LENGTH = 5
# cur_length = 1

# for i in ALPHABET:
#     for j in range
#     print(i)
word = ''
expected_word_length = 2
alphabet = ['0', '1', '2']

def get_limit(alpha, ewl):
    return (len(alphabet) ** (expected_word_length-1))*len(alphabet)



for i in range(0, get_limit(alphabet, expected_word_length)):
    for a in alphabet:
        if len(word) >= expected_word_length:
            continue
        word += a
        #print(word)
    word = ''

word = ''
for i in range(0, 2):
    for a in alphabet:
        word += a
    print(word)
    if len(word) >= 2:
        word = ''