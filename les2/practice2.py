# 1 принять на вход 2 числа и сравнить какое больше

val1 = int(input("1 число "))
val2 = int(input("2 число "))
if val1 > val2:
   print("число 1 больше числа 2")
elif val1 < val2:
   print("число 1 меньше числа 2")
else:
   print("число 1 равно числу 2")


# 2. Напишите программу, которая на вход принимает число и  выводит четное оно или не четное 

val = int(input('введите число \t'))

if val % 2 == 0:
   print('число четное')
else:
   print('число нечетное')


# 3. Напишите программу, которая на вход принимает число и определяет положительное оно, отрицательное или ноль

val = int(input('введите число \t'))

if 0 < val :
   print('положительное')
elif 0 > val:
   print('отрицательное')
else:
   print('ноль')


# 4 Калькулятор

val1 = float(input('введите 1 число \t'))
val2 = float(input('введите 2 число \t'))
oper = input('введите опрерацию вычисления (+, -, *, / ): \n')

if oper == '+':
   print(val1 + val2)
elif oper == '-':
   print(val1 - val2)
elif oper == '*':
   print(val1 * val2)
elif oper == '/':
   if val2 == 0:
      print('деление на ноль запрещено')
   else:
      print(val1 / val2)   
else:
   print('выбирайте только из 4-х опереций')
   

# 5. Напишите программу, которая на вход принимает год и определяет високосный он или нет. Високосный год тот, что делится на 4, но не делится на 100, за исключением деления на 400

year = int(input('введите год \t'))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
   print('високосный год')
else:
   print('обычный год')


# 6. Запросите у пользователя время в часах от 0 до 23 и выведите время дня

time = int(input('введите который час \n'))

if 6 <= time <= 11:
   print('утро')
elif 12 <= time <= 17:
   print('день')
elif 18 <= time <= 23:
   print('вечер')
elif 0 <= time <= 5:
   print('ночь')
else:
   print('недопустимый формат часов')

# 7. Напишите программу которая проверяет, совпадает ли введенный пользователем пароль с заданным (напр. secret12345). Если совпадает, то "Доступ разрешен", в противном случае "Доступ запрещен"

pasword = input('ваш пароль \t')   
if pasword == 'qwerty1234':
   print('доступ разрешен')
else:
   print('доступ запрещен')

# 8. Напишите программу, которая:
# Спрашивает у юзера число
# Если делится на 3, то выводит Fizz
# Если делится на 5, то Buzz
# Если делится на 3 и на 5 FizzBuzz
# Иначе просто выводит число

dig = int(input('Задай число: \n'))

if dig % 3 == 0 and dig % 5 == 0:
   print('FizzBuzz')
elif dig % 5 == 0:
   print('Buzz')
elif dig % 3 == 0:
   print('Fizz')
else:
   print(dig)


# 9. Напишите программу вычисления площади фигуры 
# (круг, прямоугольник, треугольник). Нужно выбрать фигуру, 
# затем ввести параметры нужные для вычисления

print('\n Выберите фигуру, площадь которой нужно вычислить:')
fig = int(input('\n 1 - круг, \n 2 - треугольник, \n 3 - квадрат \n'))

if fig == 1:
   print('формула площади S = п * r^2 \n задайте параметры: \n')
   r = int(input('радиус круга: r = '))
   s = 3.14 * r ** 2
   print('Площадь круга: ', s)


elif fig == 2:
   print('формула площади S = (a * h)/2 \n задайте параметры: \n')
   a = int(input('длина основания: a = '))
   h = int(input('высота к основанию: h = '))
   s = (a * h) / 2
   print('Площадь треугольника = ', s)

elif fig == 3:
   print('формула площади S = a * b \n задайте параметры: \n')
   a = int(input('длина стороны: a = '))
   b = int(input('высота стороны: b = '))
   s = a * b
   print('Площадь прямоугольника = ', s)   
else:
   print('Введите корректные значения от 1 до 3')


# 10. Преобразуйте температуру из цельсия в Фаренгейт  

temp = float(input('температура в градусах Целсия: \n'))
fareng = temp * 9 / 5 + 32
print('температура в Фаренгейтах: ', fareng)
