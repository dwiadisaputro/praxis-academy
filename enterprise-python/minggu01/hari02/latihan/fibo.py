##-- Modules

##Fibonacci numbers module
###---blm ketemu
# def fib(n):  # write Fibonacci series up to n
#     a, b = 0, 1
#     while a < n:
#         print(a, end='')
#         a, b = b, a+b
#     print()
# def fib2(n):  #return Fibonacci series up to n
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a+b
#     return result

# if __name__ == "__main__":
#     import sys
#     fib(int(sys.argv[1]))

# import fibo
# print(fibo.fib(1000))
# print(fibo.fib2(100))
# print(fibo.__name__)

# fib = fibo.fib
# print(fib(500))

# More on Modules

# from fibo import fib, fib2
# print(fib(500))

# from fibo import *
# print(fib(500))

#blm ketemu
# import fibo as fib
# print (fib.fib(500))

# from fibo import fib as fibonacci
# print(fibonacci(500))

# import fibo
# import sys
# sys.ps1
# sys.ps2
# sys.ps1 = 'C> '

# import sys
# sys.path.append('/home/Adi/NOVICE/01-02/latihan')

# import fibo, sys
# print(dir(fibo))

# print(dir(sys))

# a = [1, 2, 3, 4, 5]
# import fibo
# fib = fibo.fib
# print(dir())
###---Packages
# import sound.effects.echo
# from sound.effects import echo