from collections import defaultdict

# word_counts = defaultdict(int)
# print type(word_counts)
# print word_counts
# print type(int)
# print type(dict)
# print int()
#
# sorted()

# for i in range(1, 5):
#     print i
#
# for x in range(5):
#     for y in range(x+1, 5):
#         print (x, y)


# pairs = [(x,y) for x in range(10)
#                 for y in range(x+1, 10)]

# lazy_evens = (i for i in range(10) if i%2 == 0)
# print type(lazy_evens)
# print list(lazy_evens)

pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
print list(letters)
print list(numbers)


x = [1, 2, 3, 8, 9]
y = [4, 5, 6, 7]
xy = zip(x, y)
print xy-
