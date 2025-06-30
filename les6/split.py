# Метод SPLIT разделение строки для списков по словам

text = 'Pyton is awesome'
words = text.split() # метод разбивает строку на слова по пробелам
print(words)

data = 'apple, banana, orange,plum'
fruits = data.split(',') # разделение строки по заданному разделителю
print(fruits)

data = 'apple, banana,      orange,plum'
fruits = data.split(',', 1) # разделение строки по разделителю кол-во раз
print(fruits)

# Метод JOIN соединяет в одну строку 

words = ['pyton', 'is', 'awesome']
sentence = ' '.join(words) # соединяет элементы через пробел
print(sentence)


fields = ['name', 'age', 'sex'] 
csv_line = ','.join(fields) # получить CSV файл
print(csv_line)

chars = list('Pyton')
print(chars)
word = ''.join(chars)
print(word)

data = 'apple, banana,      orange,plum'
fruits = data.split(',')
line = '|'.join(fruits)
print(line)
