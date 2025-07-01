# yest_temp = int(input("вчера "))
# today_temp = int(input("сегодня "))

# if today_temp > yest_temp:
#    print("сегодня теплее чем вчера")
# elif today_temp < yest_temp:
#     print("сегодня хододнее чем вчера")
# else:
#      print("сегодня также")

# and, or, not
# ################

# let1 = input("1st letter ABC ")
# let2 = input("last letter ABC ")

# if (let1 == "a" or let1 =="A") and (let2 == "z" or let2 == "Z"): #true true true true
#    print("right")
# else:
#    print("mistake")   

x = 5
# if x >= 0 and x < 100:
#    pass 

# if 0 <= x < 100: # верный красивый код
#    pass

# UTF-8

# let1 = "t"
# let2 = "w"
# print(let1 > let2)
# print(ord(let1)) # возвращает номер буквы в UTS-8
# print(ord(let2))
# print(chr(116)) # код заглавной буквы
# print(chr(119))
# print(ord('W'))

# text = input()
# if "добр" in text:
#    print("встретилось 'доброе' слово")
# else:
#    print("добрых слов для вас нет")   


#XOR - ^

# Логическая операция ^ (XOR) в Python  возвращает True только если один из аргументов True, а другой False (2 различных значения).

# Оператор ^ выполняет побитовое исключающее ИЛИ (XOR). Но когда он применяется к bool (логическим) значениям, Python сначала преобразует их в целые числа (True → 1, False → 0), затем выполняет XOR и возвращает результат как целое число (0 или 1).


a = True
b = False

p = a ^ a  # True ^ True → 1 ^ 1 = 0 → False
q = a ^ b  # True ^ False → 1 ^ 0 = 1 → True
r = b ^ a  # False ^ True → 0 ^ 1 = 1 → True
s = b ^ b  # False ^ False → 0 ^ 0 = 0 → False

print(a, 'XOR', a, '=', p)  # True XOR True = False
print(a, 'XOR', b, '=', q)  # True XOR False = True
print(b, 'XOR', a, '=', r)  # False XOR True = True
print(b, 'XOR', b, '=', s)  # False XOR False = False

print(True ^ True)   # False
print(True ^ False)  # True
print(False ^ True)  # True
print(False ^ False) # False


print("{0:b}".format(15)) # 1111
# Эта строка форматирует число 15 в двоичный (бинарный) вид (0:b означает двоичное представление)

print(15^32) # 47
# сравнивает биты двух чисел и возвращает новое число, где каждый бит равен 1, если соответствующие биты исходных чисел различаются, и 0 — если одинаковые.

# Сравниваем биты по столбцам и применяем XOR:
# 15:    0 0 0 0 1 1 1 1
# 32:    0 0 1 0 0 0 0 0
# ----------------------
# 15^32: 0 0 1 0 1 1 1 1  (биты разные → 1, одинаковые → 0)

# Переводим 0010 1111 обратно в десятичную систему:
#    0*2⁷ + 0*2⁶ + 1*2⁵ + 0*2⁴ + 1*2³ + 1*2² + 1*2¹ + 1*2⁰
#    32 + 8 + 4 + 2 + 1 = 47

   # Операция XOR "переключает" биты числа 15 там, где у 32 стоят единицы.
   # У 32 единица стоит на 6-м бите слева (если считать с 0), поэтому в 15 этот бит инвертируется:
   #    Было: 15 = 00001111
   #    Стало: 00101111 = 47.

print(5 ^ 3)    # 5 = 101, 3 = 011 → 110 (6)
print(10 ^ 6)   # 10 = 1010, 6 = 0110 → 1100 (12)


print(bin(47))
print(bin(15))
print(bin(32))
