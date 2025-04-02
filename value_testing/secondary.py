import random

def calculate_word_value(word):
    sum = 0
    for i in range(0, len(word)):
        v = alphabet.index(word[i])+1
        sum += (26**i) * v
    return sum


lst = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
temp = ['a', 'b']
generation_limit = 1000000
letter_set_length = 0
value_set_length = 0

for i in range(0, generation_limit):
    word = ''
    for i in range (random.randint(1,20)):
        word += random.choice(temp)
    lst.append(word)

letter_set_length = len(set(lst))

v_lst = []
for i in range(0, len(lst)):
    v_lst.append(calculate_word_value(lst[i]))

value_set_length = len(set(lst))

print(f'{letter_set_length} == {value_set_length}')

# with open("randomized_letter_combos.csv", "w") as f:
#     for s in lst:
#         f.write(f'{s},\n')

# with open("randomized_letter_combos_values.csv", "w") as f:
#     for s in v_lst:
#         f.write(f'{s},\n')