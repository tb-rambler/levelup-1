# условные операторы

# булевыми операторами являются and, or и not, которые используются для работы с логическими значениями. Логический тип данных (bool или булевый тип) — это примитивный тип данных, он принимает 2 значения — истина или ложь. True и False

# True это число 1
# False это число 0

# Функция bool() вернет False если это:
# пустая строка, нулевое число или пустой список/кортеж.
# В остальных случаях функция bool() вернет True

# # Оператор and
# result1 = True and True  # True
# result2 = True and False # False
# result3 = False and True # False

# # Оператор or
# result4 = True or False  # True
# result5 = False or False # False

# # Оператор not
# result6 = not True       # False
# result7 = not False      # True


x = 3
y = 3
print(x != y)

print(type(True))

print(False + 3) # False + 3 = 0+3 = 3
print(True + 5) # True + 5 = 1+5 = 6

print(bool(1110)) 

# Функция bool() преобразует любое значение в True или False по правилам:
   # Ложные (False) значения: 0, 0.0, "", None, [], (), {}, set()
   # Все остальные числа, строки, коллекции дают True.
