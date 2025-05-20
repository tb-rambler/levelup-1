# 1 запросить 2 целых числа и вывести сумму
print("задача 1, \nвведите два целых числа")
x = int(input())
y = int(input())
sum = x + y
print(sum)

# 2 принять строку и преобразовать в целое число
line = str(input("задача 2, \nнапишите строчку: "))
line = int(line)
print(type(line), line)

# 3 запросить 2 целых числа и вывести разность
a = int(input("задача 3, \nвведите 2 целых числа "))
b = int(input())
print(a - b)

# 4 запросить 2 дробных числа и вывести их умножение и деление
a = float(input("задача 4, \nвведите 2 дробных числа "))
b = float(input())
res1 = a * b
res2 = a / b
print(res1,', ', res2)

# 5 принять число и преобразовать в строку
dig = int(input('задача 5, \nвведите число: '))
dig = str(dig)
print(type(dig), dig)

# 6 принять 2 строки и сложить их через пробел
line1 = input("задача 6, \nвведите 2 строки ")
line2 = input()
print(line1 + ' ' + line2)

# 7 принять строку и число и вывести их сложение (число)
string = int(input("задача 7, \nвведите строку: "))
digit = 505
result = string + digit
print(result)
