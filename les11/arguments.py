# скопировать

# def add_value(x, list_arg = None):
#    if list_arg is None:
#       list_arg = []
#    list_arg += [x]
#    return list_arg

# print (add_value(0))
# print (add_value(0, [1, 2, 3]))
# print (add_value(0))
# print (add_value(1))
# print (add_value(0))


# позиционные и именованные аргументы

# def final_price(price, discount=1):
#    return price - price * discount / 100

# print(final_price(1000, discount=5))
# print(final_price(discount=15, price=1000))


# бесконечное кол-во неименованных аргументов задается *  args

# def final_price(*prices, discount=1): # *args - принятое обозначение
#    return [price - price * discount / 100 for price in prices]

# print(final_price(1000, 500, 350, 200, 46541, discount=5))


# бесконечное кол-во именованных аргументов задается **  kwargs

# def final_price(*prices, discount=1, **kwargs): # обращение как с обычным словарем
#    low = kwargs.get('price_low', min(prices))
#    high = kwargs.get('price_high', max(prices))
#    return [price - price * discount / 100 for price in prices if low <= price <=high]

# print(final_price(100, 200, 300, 500, 700, discount=5))
# print(final_price(100, 200, 300, 500, 700, discount=5, price_low=250))
# print(final_price(100, 200, 300, 500, 700, discount=5, price_high=500))
# print(final_price(100, 200, 300, 500, 700, discount=5, price_low=250, price_high=500))


# функции высшего порядка

# def only_pos(x): # критерий отбора 
#    return x > 0 

# result = filter(only_pos, [-1, 5, 7, 10, 0, -11])
# # print(list(result)) # вариант вывода
# print(', '.join(str(x) for x in result))

# вытащить только буквы

# result = filter(str.isalpha, '12345ABCDefgh()#%$$^@@')
# print(''.join(result))

# функция принимает число и возвращает его квадрат

# def square(x):
#    return x ** 2

# result = map(square, range(5))
# print(', '.join(str(x) for x in result))

# result = map(str.lower, ['asdDFGH', 'FGHJgf', 'IJger'])
# print('\n'.join(result))


# ввести с клавы сразу список станд. функцими

# numbers = list(map(int, input().split())) # по умолчанию по пробелу
# print(numbers)


# для небольших функций и одноразовых исп-ся лямбда-функция

# lambda x: x > 0

# аналог lambda вот этого:
# def only_pos(x): # критерий отбора 
#    return x > 0 

# result = map(lambda x: x > 0, [-1, 5, 7, 10, 0, -11])
# print(list(result)) # вариант вывода


# критерии сортировки по ключу

# lines = ['abcd', '1fsD', 'abc', 'abcdef'] # отсортировать по длине строки
# print(sorted(lines)) # не верное, по кодировке

# print(sorted(lines, key=lambda line: len(line))) # верно


# lines = ['abcd', '1fsD', 'abc', 'abcdef', 'cba']
# print(sorted(lines, key=lambda line: (len(line), line))) # сортировка 1 по длне, 2 - по алфавиту, если длина одинаковая
# print(sorted(lines, key=lambda line: (-len(line), line))) # обратный порядок

# # найти самую длинную, а если их неск, то по алфавиту
# lines = ['abcd', '1fsD', 'abc', 'abcdef', 'cbalkh']
# print(min(lines, key=lambda line: (-len(line), line)))


# вот так проще отсеивать положит. числа:
result = (x for x in [-1, 5, 6, -10, 0] if x > 0)
print(', '.join(str(x) for x in result))


# сложение всех чисел в послед-ти:
from functools import reduce

numbeers = range(1, 6)
print(reduce(lambda x, y: x + y, numbeers))
