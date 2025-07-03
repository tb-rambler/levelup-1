# Факториал  рекурсивная функция

# n! = 1*2*3*...*n, n>0 , 0! = 1

# def fact(n):
#    factorial = 1
#    for i in range(2, n+1):
#       factorial *= i
#    return factorial

# print(fact(5))

# иначе факториал
# n! = (1*2*3... (n-1)*n) = (n-1)!*n

def fact(n):
   if n==0:
      return 1 # декларативная функция
   return fact(n-1) * n # n! = (n-1)! * n
print(fact(5))

# последовательность фибаначи 
# 1 1 2 3 5 8 13 21 34
# fib(n) = fib(n-1) + fib(n-2), n - индекс последовательности (fib(9))

from timeit import timeit # посчитать время выполнения

# def fib(n):
#    if n in (0, 1):
#       return 1
#    return fib(n-1) + fib(n-2)

# print(fib(9))
# print(fib(35)) # очень долго

# print(f'Среднее время вычисления: ')
# print(f'{round(timeit('fib(35)', number = 10, globals = globals())/10, 3)} cek,')

# намного быстрее рекурсивная функция:

# def fib(n):
#    f_1, f = 1, 1
#    for i in range(n-1):
#       f_1, f = f, f_1 + f
#    return f
# print(f'Среднее время вычисления: ')
# print(f'{round(timeit('fib(35)', number = 10, globals = globals())/10, 3)} cek,')

# посчитать сколько раз вызвалась функция (30 млн. раз)

# def fib(n):

#    global count
#    count +=1

#    if n in (0, 1):
#       return 1
#    return fib(n-1) + fib(n-2)

# count = 0
# fib(35)
# print(count)


# кеширование (минимизация)

# def fib(n):

#    global count
#    count +=1

#    if n not in cache:
#       cache[n] = fib(n-1) + fib(n-1)
#    return cache[n]
# count = 0
# cache={0:1, 1:1}

# fib(35)
# print(count)

# print(f'Среднее время вычисления: ')
# print(f'{round(timeit('fib(999)', number = 10, globals = globals())/10, 3)} cek,')

# def countdown(n):
#    if n == 0:
#       print('Поехали!')
#    else:
#       print(n)
#       countdown(n-1)
# print(countdown(10))

# factorial(4)
# 4 * factorial(3)
# 3 * factorial(3)
# 2 * factorial(3)
# 1

# 2*1 = 2
# 3*2 = 6
# 4*6 = 24


# def factorial(n, depth=0):
#    print(' ' * depth + f'-> factorial({n})')
#    if n == 1:
#       print(' ' * depth + f'<- return 1')
#       return 1
#    else:
#       result = n * factorial(n-1, depth +1)


from functools import lru_cache

@lru_cache

def fib(n):
   if n in (0, 1):
      return 1
   return fib(n-1) + fib(n-2)

print(f'Среднее время вычисления: ')
print(f'{round(timeit('fib(999)', number = 10, globals = globals())/10, 3)} cek,')

