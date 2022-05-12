# print(list(map(int, ["1", "2", "3"])))

# def hello_word(h):
#     def world(w):
#         print(h, w)
#     return world ## returning functions

# h = hello_world ##assigning
# x = h("hello") ##assigning
# x
# <function world at 0x7fec47afc668>
# x("world")

# function_list = [h, x]
# function_list [<function hell0_world at 0x7fec47afc5f0>, <function world at 0x7fec47afc668>]



# def naive_sum(list):
#     s = 0
#     for l in list:
#         s += l
#     return s
# sum(list)

# for x in l:
#     func(x)
# map(func, l)

# def func1():
#     pass

# def func2():
#     pass

# def func3():
#     pass

# print(executing = lambda f: f())


# def fib(n):
#     if n == 0: return 0
#     elif n == 1: return 1
#     else: return fib(n-1)+fib(n-2)

# starting_number = 96
# square = starting_number ** 2
# increment = square + 1
# cube = increment ** 3
# decrement = cube - 1
# result = print(decrement)


# def call(x, f):
#     return f(x)

# square = lambda x : x*x
# increment = lambda x : x+1
# cube = lambda x : x*x*x
# decrement = lambda x : x-1
# funcs = [square, increment, cube, decrement]
# from functools import reduce
# print(reduce(call, funcs, 96))