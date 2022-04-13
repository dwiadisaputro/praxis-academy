##-- Modules

##Fibonacci numbers module
###---blm ketemu
def fib(n):  # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
def fib2(n):  #return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = a, a+b
    return result

import fibo
print(fibo.fib(1000))
print(fibo.fib2(100))
print(fibo.__name__)

fib = fibo.fib
print(fib(500))

from fibo import fib, fib2fibo
print(fib(500))

from fibo import *
print(fib(500))

import fibo as fib
print(fib.fib(500))

from fibo import fib as fibonacci
print(fibonacci(500))