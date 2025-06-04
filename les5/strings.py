string = 'Hello world'

print(string[::-1])
print(string.replace('1', 'd', 2))

print('2 числа {}, {}'.format(1, 2))
print('2 числа {1}, {0}'.format(1, 2)) # можно указать индексы для подстановки
print('2 числа {1}, {0}, {1}'.format(1, 2))
print('2 числа {first}, {second}, {third}'.format(first=1, second =2))
