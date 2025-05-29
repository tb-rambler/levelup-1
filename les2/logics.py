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

a = True
b = False

p = a ^ a
q = a ^ b
r = b ^ a
s = b ^ b
print(a, 'XOR', a, '=', p)
print(a, 'XOR', b, '=', q)
print(b, 'XOR', a, '=', r)
print(b, 'XOR', b, '=', s)

# print("{0:b}".format(15))

print(15^32)
print(bin(47))
print(bin(15))
print(bin(32))

15 = 001111
32 = 100000
XOR = 101111