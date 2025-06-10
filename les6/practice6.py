# 1) найти первую заглавную букву, если ее нет, то вывести сообщение что нет.

# text = 'Hello world'
# found = False

# for char in text:
#    if char.isupper():
#       print(f'Первая заглавная буква: {char}')
#       found = True
#       break
# if not found:
#    print('нет заглавных')


# 2) Удалить все  !!! только в конце строки, но не в середине

# text = '!!!Hello!!! world!!!'
# while text.endswith('!'): # если текст кончается на !, продолжаем..
#    text = text[:-1]
# print(text)

# 3) Удалите числа из строки

# text = "Pyton 3.13 is awesome in 2025"
# result = ''
# for char in text:
#    if not char.isdigit():
#       result =+ char
# print(result)

# 4) подсчет гласных и согласных

# text = "Hello world 2362156 1235 brothers"
# vowels = 'aeiouy'
# total_v = 0
# total_c = 0

# for v in text:
#    if v.isalpha():
#       if v.lower() in vowels:
#          total_v += 1
#       else:
#          total_c += 1
# print('согласных ', total_c)
# print('гласных ', total_v)

# 5) Пропустить слова с длиной менее 5

# text = 'This is a simple Pyton string example'
# words = text.split()
# for word in words:
#    if len(word) > 4:
#       print(word)

# 6) Есть список животных. Посчитать сколько раз каждое животное встречается

animals = ["слон", "тигр", "слон", "зебра", "тигр", "тигр", "зебра"]
un_animals = []
counts = []
for animal in animals:
   if animal not in un_animals:
      un_animals.append(animal)
      counts.append(1)
   else:
      index = un_animals.index(animal)
      counts[index] += 1
for i in range(len(un_animals)):
   print(f'{un_animals[i]}: {counts[i]}')
