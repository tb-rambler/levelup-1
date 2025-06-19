# id() - посмотреть место в памяти

# x = 5
# print(id(x))
# x = 10
# print(id(x))

# x = 1
# y = x
# print(id(x))
# print(id(y))
# print(x is y) # одно и тоже

# x = [el ** 2 for el in range(5)]
# y = [el ** 2 for el in range(5)]
# print(x == y)
# print(x is y)


# numbers = [1, 2, 3]
# print(f'{numbers}, id = {id(numbers)}')
# numbers += [4] # также как и numbers.append(4) , расширение списка
# print(f'{numbers}, id = {id(numbers)}')

# numbers = [1, 2, 3]
# print(f'{numbers}, id = {id(numbers)}')
# numbers = numbers + [4] # переписывание объекта в памяти, перезапись
# print(f'{numbers}, id = {id(numbers)}')

# x = [1, 2, 3]
# y = x
# print(x is y)
# x[0] = 0
# print(x)
# print(y)
# print(x is y)

# x = [1, 2, 3]
# y = x[:]
# x[0] = 0
# print(x)
# print(y)
# print(x is y)

# numbers = [[1, 2, 3], 
#            [4, 5, 6],
#            [7, 8, 9]]
# numbers_copy = numbers[:]
# print([numbers_copy[i] is numbers[i] for i in range(len(numbers))])

# numbers = [[1, 2, 3], 
#            [4, 5, 6],
#            [7, 8, 9]]
# numbers_copy = [el[:] for el in numbers] # глубокая копия списка \ deepcopy
# print([numbers_copy[i] is numbers[i] for i in range(len(numbers))])

from copy import deepcopy

numbers = [[1, 2, [0, 5, 55]], 
           [4, 5, 6],
           [7, 8, 9]]
numbers_copy = deepcopy(numbers) # более правильное легкая замена внутр. списков
print([numbers_copy[i] is numbers[i] for i in range(len(numbers))])
print(numbers[0][2] is numbers_copy[0][2])

