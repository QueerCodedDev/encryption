from obj.Letter import Letter
# read from file
# parse each line into a cell
# cells stored as board

collection_original = []

with open('./collection.txt') as coll_file:
    collection_original = coll_file.read().splitlines()

for i in range(len(collection_original)):
    collection_original[i] = list(collection_original[i])
    x = 0
    y = 0
    for j in range(len(collection_original[i])):
        collection_original[i][j] = Letter(collection_original[i][j], (x, y))



print(collection_original)

# test list to see how find works in multi dim. lists
# test = [['a', 'b', 'c'], ['b', 'd']]

# try:
#     print(test.index('a'))

# except ValueError: 
#     print('I tried')