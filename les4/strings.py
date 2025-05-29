# text = input()
# print(text[0])

# text = input()
# i = int(input('index: '))
# if i < len(text):
#    print(text[i])
# else:
#    print('индекс за пределами строки')

# text = input()
# # print(text[len(text)-1]) # последний символ
# print(text[-1]) # или так

# text = input()
# for i in range(len(text)):
#    print(text[i])

# text = input()
# for i, letter in enumerate(text): # вывод символа для индекса
#    print(f'{i}. {letter}')

text = 'hello world'
# конструкция: "СТРОКА" [начало:конец:интервал]
print(text[6:9])
print(text[:9])
print(text[6:])
print(text[:]) # вывод полной строчки
print(text[::9]) # только интервал

# МЕТОДЫ

s = 'Hello world'
print(s.count('1')) # не перекрывающиеся подстроки

print(s.endswith('world'))
print(s.find('w')) #первое вхождение символа
print(s.index('l')) 
print(s.isalnum()) 
print(s.startswith('Hello'))
print(s.zfill(5))   # добивает строку до нужного кол-ва символов нулями
s = 'ABCDGFgfgdafGDABC'
print(s.lstrip('ABC')) # для начала строки удаляет эти символы если их нет
print(s.rstrip('ABC')) # для конца строки удаляет эти символы    
   