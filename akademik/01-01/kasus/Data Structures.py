# # More on List
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# print(fruits.count('apple'))
# print(fruits.count('tangerin'))
# print(fruits.index('banana'))
# print(fruits.index('banana', 4))

# fruits.reverse()
# print(fruits)

# fruits.append('grape')
# print(fruits)

# fruits.sort()
# print(fruits)

# fruits.pop()


# #Using Lists as Stacks

# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# print(stack)
# print(stack.pop())
# print(stack)
# print(stack.pop())
# print(stack.pop())
# print(stack)


# #Using Lists as Queues
# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")
# queue.append("Graham")
# print(queue.popleft())
# print(queue.popleft())
# print(queue)


# #List Comprehension
# squares = []
# for x in range(10):
#     squares.append(x**2)
# print(squares)

# squares = list(map(lambda x: x**2, range(10)))
# squares = [x**2 for x in range(10)]
# print([(x, y) for x in [1,2,3] for y in [3,1,4] if x !=y])

# combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x, y))
# print(combs)

# vec = [-4, -2, 0, 2, 4]
# print([x*2 for x in vec]) ##creat a new list with the values double
# print([x for x in vec if x >= 0]) ##filter the list to exclude negative number
# print([abs(x) for x in vec]) ##apply a function to all the elements
# ##call a method on each element
# freshfruit = [' banana', ' loganberry', 'passion fruit ']
# print([weapon.strip() for weapon in freshfruit])
# ##creat a list of 2-tuples like (number, square)
# print([(x, x**2) for x in range(6)])
# ##the tuple must be parenthesized, otherwise an error is raised
# # #print([x, x**2 for x in range(6)])

# #flatten a list using a listcomp with two 'for'
# vec = [[1,2,3], [4,5,6], [7,8,9]]
# print([num for elem in vec for num in elem])

# from math import pi
# print([str(round(pi, i)) for i in range(1, 6)])


# # Nested List Comprehensions
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# print([[row[i] for row in matrix] for i in range(4)])


# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
# print(transposed)

# transposed = []
# for i in range(4):
#     #the folowing 3 line implement the nested listcomp
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
# print(transposed)

# print(list(zip(*matrix)))


# # The del statement
# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
# print(a)

# del a[2:4]
# print(a)

# del a[:]
# print(a)
# del a

# #Tuples and Sequences
# t = 12345, 54321, 'hello!'
# print(t[0])
# print(t)
# # Tuples may be nested:
# u = t, (1, 2, 3, 4, 5)
# print(u)
# Tuples are immutable:
# #t[0] = 88888
# #Traceback (most recent call last):
# #File "<stdin>", line l, in<module>
# #TypeError: 'tuple' object does not support item assignment
# ---but they can contain mutable objects:
# v = ([1, 2, 3], [3, 2, 1])
# print(v)

# empty = ()
# singleton = 'hello'
# print(len(empty))
# print(len(singleton))
# print(singleton)

##--x, y, z = t

## Sets
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)
# print('orange' in basket)
# print('crabgrass' in basket)
# ##--- Demonstrate set operations on unique letters from two word

# a = set('abracadabra')
# b = set('alacazam')
# print(a)
# print(a-b)
# print(a | b)
# print(a & b)
# print(a ^ b)

# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)

##Dictionaries
# tel = {'jack': 4098, 'sape': 41390}
# tel['guido'] = 4127
# print(tel)
# print(tel['jack'])

# del tel['sape']
# tel['irv'] = 4127
# print(tel)
# print(list(tel))
# print(sorted(tel))
# print('guido' in tel)
# print('jack' not in tel)

# print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
# print({x: x**2 for x in (2, 4, 6)})
# print(dict(sape=4139, guido=4127, jack=4098))

##- Looping Techniques

# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k, v)

# for i, v in enumerate(['tic', 'tac', 'toe']):
#     print(i, v)

# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print('What is your {0}? It is {1}.'.format(q, a))

# for i in reversed(range(1, 10, 2)):
#     print(i)

# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for i in sorted(basket):
#     print(i)

# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for f in sorted(set(basket)):
#     print(f)

# import math
# raw_data = [56.2, float('Nan'), 51.7, 55.3, 52.5, float('Nan'), 47.8]
# filtered_data = []
# for value in raw_data:
#     if not math.isnan(value):
#         filtered_data.append(value)
# print(filtered_data)

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)

# (1, 2, 3)               < (1, 2, 4)
# [1, 2, 3]               < [1, 2,4]
# 'ABC' < 'C' < 'Pascal' < 'Python'
# (1, 2, 3, 4)            < (1, 2, 4)
# (1, 2)                  < (1, 2, -1)
# (1, 2, 3)               == (1.0, 2.0, 3.0)
# (1, 2, ('aa', 'ab'))    < (1, 2, ('abc', 'a'), 4)