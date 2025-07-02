#  Списочные выражения (работают быстрее обычного итератора)

# numbers =[]
# for i in range(5):
#    numbers.append(int(input())
# print(numbers)

# numbers = [int(input()) for i in range(5)]
# avg = sum(numbers) // len(numbers)
# numbers = [element for element in numbers if element > avg] # в список попадут только те эл-ты, которые больше ср. арифмитеч.
# print(numbers)

# numbers = [int(input()) for i in range(5)]
# numbers = [element for element in numbers if element > sum(numbers) // len(numbers)] # тоже самое короче
# print(numbers)

# более простой пример цикла:
# new_numbers = []
# for element in numbers:
#    if element > avg:
#       new_numbers.append(element)


# Матрица 5х5

matrix = [[int(x) for x in input().split()] for i in range(5)]
print(matrix)

# matrix = []
# for i in range(5):
#     line = input() #"1 2 4 5 3"
#     list_line = line.split()#['1', '2', '4', '5', '3']
#     new_list = []
#     for j in list_line:
#         new_list.append(int(j))
#     matrix.append(new_list)
# print(matrix)


# cоздание 2х мерного списка, 
zeros = [[0] *5] * 5
print(zeros)
zeros[0][0] = 1
print(zeros)

# zeros = [[0] *5 for i in range(5)] # правильно \без ошибок,
# print(zeros)
# zeros[0][0] = 1
# print(zeros)

# text = 'строка символов'
# codes = [ord(simbol) for simbol in text]
# print(text)

# выбрать список стран, у которых более 1 языка

# countries = {'Россия': ['русский'], 'Беларусь': ['беларусский', "русский"], "Бельгия": ["немецкий", "французский", "нидерландский"]}
# multi_lang = [country for country, lang in countries.items() if len(lang) > 1]
# print(multi_lang)

# из списка пар генерируем словарь

# countries = {country: capital for country, capital in [('Russia', 'Moscow'), ("Belarus", 'Minsk'), ('Serbia', 'Belgrad')]}
# print(countries)

# Размеры памяти
# numbers = (int(input()) for i in range(5)) # генератор 
# print(numbers)

# from sys import getsizeof
# numbers_iter = (i for i in range(10**6))
# print(getsizeof(numbers_iter)) # память, занимаемая итератором намного меньше списка   

# numbers_list = list(range(10**6))
# print(getsizeof(numbers_list))

# засечь время исполнения задачи
# from timeit import timeit
# print(round(timeit("s = '; '.join(str(x) for x in range(10**7))", number = 10), 3)) # итератор (должен работать быстрее)
# print(round(timeit("s = '; '.join([str(x) for x in range(10**7)])", number = 10), 3)) # списки (их можно обойти через генератор)
