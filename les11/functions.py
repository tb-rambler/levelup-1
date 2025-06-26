# Функции выполняются многократно

# def <имя функции> (<аргументы ф-ии>):
#    <тело функции>
# return # результат функци и конец   

# def only_even(numbers):
#    result = True
#    for x in numbers:
#       if x % 2 != 0:
#          result = False
#          break
#    return result

# print(only_even([2, 4, 5]))
# print(only_even([2, 4, 8]))

# def only_even(numbers): # тоже самое, но проще
#    for x in numbers:
#       if x % 2 != 0:
#          return False
#    return True
   
# print(only_even([2, 4, 5]))
# print(only_even([2, 4, 8]))


# def only_even(numbers): # можно вернуть неск. результатов через запятую
#    for i, x in enumerate(numbers):
#       if x % 2 != 0:
#          return False, i
#    return True
   
# print(only_even([2, 4, 5])) # вернулось кортежем с индексом 1го вхождения выполненного условия
# print(only_even([2, 4, 8]))

# a, b = only_even([2, 4, 5]) # развернуть кортеж по известному количеству вывода
# print(a)
# print(b)


# def only_even(numbers): # можно вернуть неск. результатов через запятую
#    for i, x in enumerate(numbers):
#       if x % 2 != 0:
#          return False, i
#    return True
# print(numbers) # не работает, т.к. локальная функция, работает только внутри, снаружи не видно. Но изнутри наружу видно


# def check_password(pwd):
#    return pwd == check_password

# password = 'Python'
# print(check_password('123'))


# def list_mdf():
#    del sample[-1]

# sample = [1, 2, 3]
# list_mdf()
# print(sample)


# def list_mdf():
#    sample = [4, 5, 6] # не изменить список, так не работает

# sample = [1, 2, 3]
# list_mdf()
# print(sample)

#исправить!
# def hello(x):
#    print(hello)

# x = 'hello'


# def list_modify_1(list_arg):

#    list_arg = [1, 2, 3, 4]

# def list_modify_2(list_arg):

#    list_arg += [4]

# sample_1 = [1, 2, 3,]
# sample_2 = [1, 2, 3,]

# list_modify_1(sample_1)
# list_modify_2(sample_2)
# print(sample_1)
# print(sample_2)


# def inc():
#    global x # глобальная переменная, исп-ть в исключит. случаях
#    x += 1
#    print(f'Кол-во вызовов функции равно {x}.')
# x = 0
# inc()
# inc()
# inc()

# так правильно использовать глобальную переменную:

def f(count):
   count += 1
   print(f'Кол-во вызовов функции равно {count}.')
   return count

count_f = 0
count_f = f(count_f)
count_f = f(count_f)
count_f = f(count_f)
count_f = f(count_f)

