# 1. ... вычисляет сумму всех чисел от 1 до 100 включительно используя for. 
# результат вывести на экран

total = 0
for i in range(1, 101):
      total += i
print(total)

# # # 2. запрашивает у пользователя строку и выводит каждый символ в новой строке (for)

line = input('Введите стоку: ')
for i in line:
   print(i)

# # 3. запрашивает число у юзера и выводит таблицу умножения этого числа от 1 до 15

dig = int(input('задайте число: '))
for i in range(1, 16):
   i = dig * i
   print(i)

# # 4. запрашивает у пользователя число n и вычисляет сумму всех четных чисел от 1 до n включительно. Используйте цикл for и условие.
   
n = int(input('задайте число: '))
total = 0
for i in range(1, n + 1):
   if i % 2 == 0:
      total += i
print(total)

# # 5. запрашивает у пользователя число n и находит сумму всех чисел от 1 до n, которые делятся на 3 без остатка. Используйте цикл while.

n = int(input('задайте число: '))
total = 0
i = 1
while i <= n:
   if i % 3 == 0:
      total += i
   i += 1
print(total)

# # 6. Напишите программу, которая запрашивает у пользователя число и проверяет,
# #  является ли оно простым. Число называется простым, если оно делится только 
# # на 1 и на само себя. Используйте цикл for для проверки делимости.

n = int(input('задайте число: \n'))
if n <= 1:
   print("числа могут быть только > 1")
else:
   for i in range(n-1, 1, -1):
      if n % i != 0:
         continue 
      print('Число составное')
      break
   else:   
      print('Число простое')   
       

# 7. Напишите программу, которая запрашивает у пользователя строку и проверяет, 
# является ли она палиндромом (читается одинаково слева направо и справа налево). Пробелы и регистр букв не учитываются.

phrase = input('Введите фразу: \n')

phrase_n = phrase.lower() # перевод фразы в нижний рег.
phrase_del = phrase_n.replace(' ', '') # убрать пробелы
phrase_rev = phrase_del[::-1] # переворот стоки

list_1 = [phrase_del]
list_2 = [phrase_rev]

# print(list_1)
# print(list_2)

if list_1 == list_2:
   print('это палиандром')
else:
   print('это фигня')
