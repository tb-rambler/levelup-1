# saved_pwd = 'right_password'

# pwd = input('введите пароль для входа')

# while pwd != saved_pwd:
#    pwd = input('введите пароль для входа')
# print('Пароль верный. Вход разрешен')

# saved_pwd = 'right_password'
# while input('введите пароль для входа') != saved_pwd:
#    pass
# print('Пароль верный. Вход разрешен')
# 
# name = input('введите имя')
# while name != 'стоп':
#    print(f'Привет, {name}!')
# print('Программа завершена')

# while (name := input('введите имя: ')) != 'стоп':
#    print(f'Привет, {name}!')
# print('Программа завершена')

# range(n)

# n = int(input('введите кол-во чисел '))
# for i in range(n):
#    print(i)
# print('end')

# k = int(input('введите начало дипазона '))
# n = int(input('введите конец диапазона '))
# for i in range(k, n+1): # n+1 -> для человеческой логики, а не компьютерной
#    print(i)
# print('end')

# n = int(input('введите конец диапазона '))
# for i in range(0, n+1, 2): 
#    print(i)
# print('end')

# n = int(input('введите первое число '))
# for i in range(n, -1, -1): # обратный отсчет
#    print(i)
# print('end')

# for i in range(1, 5, -1): # будет ошибка, тк конфликт последовательности
# print(i)

# for i in range(0, 10):
#    print(i)
#    i = 100
#    # print(i)

# for i in 'Hello world':
#    print(i)

# for i in 'Hello world':
#    if i != 'o':
#       print(i)

for i in range(1, 11):
   if i == 5:
      break
   print(i)

for num in range(1, 6):
   if num == 3:
      continue
   print(num)

for _ in range(100): # что-то не значащее, нигде далее исп-ся не будет
   print('hello!')
