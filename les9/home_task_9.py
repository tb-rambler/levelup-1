#  1. Фильтрация email-адресов по домену "ivan@gmail.com", "kate@yahoo.com", "john@gmail.com", "test@outlook.com"

emails = ["ivan@gmail.com", "kate@yahoo.com", "john@gmail.com", "test@outlook.com"]
gmail = [mail for mail in emails if mail.endswith("gmail.com")]
print(gmail)


#  2. Список длины строк исключая пустые "Hello", "", "Data", "Science", "", "Python"

lines = ["Hello", "", "Data", "Science", "", "Python"]
lenghts = [len(word) for word in lines if word]
print(lenghts)


#  3. Квадраты нечетных чисел

square = [x**2 for x in range(11) if x % 2 != 0]


#  4. Строки в числа игнорируя нечисловые "42", "100", "abc", "NaN", "7" - [42, 100, 7]

list_of_strings = ["42", "100", "abc", "NaN", "7"]
numbers_in_list = [int(x) for x in list_of_strings if x.isnumeric()] # x.isdigit()
print(numbers_in_list)


#  5. Плоский список из матрицы 
#  [[1, 2], 
#  [3, 4], 
#  [5, 6]]

matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)


#  6. Словарь: слово - длина слова ["apple", "banana", "kiwi"]

words = ["apple", "banana", "kiwi"]
word_lenghts = {word: len(word) for word in words}
print(word_lenghts)


#  7. Привести имена к нормальной форме ["john", "DOE", "alice", "Bob"]

names = ["john", "DOE", "alice", "Bob"]

names_upd = [name.lower() and name.capitalize() for name in names]
print(names_upd)


#  8. Список уникальных слов в нижнем регистре ["Hello", "world", "HELLO", "World", "python"]

words = ["Hello", "world", "HELLO", "World", "python"]

words_upd = [word.lower() for word in words]

print(set(words_upd)) # set - это мн-во уникальных эл-тов


#  9. Генерация пар i,j где i!=j [(0, 1), (0, 2), (1, 0), (2,0), (2, 1)] (если range(3))

pari = []

pari = [(i, j) for i in range(0, 3) for j in range(0, 3) if i !=j]

print(pari)


#  10. Генератор квадратов числе до миллиона

generators = (x ** 2 for x in range(1, 10))
for x in generators: 
   print(x)


#  11. Построчная фильтрация логов через генератор. Фильтр на ERROR

def errors(logs):

   for line in logs:
      if 'ERROR' in line:
         yield line



#  12. Генератор чисел кратных 3 и 5

def gen_3_5(val):
   for x in range(1, val + 1):
      if x % 3 == 0 and x % 5 == 0:
         yield x 
    
gen = gen_3_5(100)



#  13. Генератор всех слов длиной > 4 из текста "This is a demonstration of how generator expressions work in Python"

text = "This is a demonstration of how generator expressions work in Python"

words_4 = (word for word in text.split() if len(word) >= 4)

print(list(words_4))


#  14. Генератор координат сетки (x, y) 0–9 - (0, 0), (0, 1), ...,

#  15. Создание матрицы 3×3, заполненной нулями

matrix = [[0] * 3] * 3
print(matrix)


#  16. Сумма элементов в каждом ряду матрицы

import random

matrix = [[random.randint(1, 10) for i in range(5)] for i in range(5)]

print('\nМатрица:')
for row in matrix:
   print(row)

row_sum = [sum(row) for row in matrix]
print('сумма по ряду: ', row_sum)


#  17. Создание шахматной доски из 0 и 1

chess =[]

for row in range(8):
   line = []
   for col in range(8):
      line.append((row + col) % 2)
   chess.append(line)

for line in chess:
   print(' '.join(str(el) for el in line))
