# СЛОВАРИ PYTON
# по ключам можно сразу найти столицы по странам

# countries_capitals = [('Россия', "Москва"), ("США", "Вашингтон"), ("Франция", "Париж")]
# for country in countries_capitals:
#    if country[0] == "Франция":
#       print(country[1]) # найти столицу Франции
#       break

# обращение к словарям по паре ключ: значение

# countries_capitals = {'Россия' : "Москва", "США" : "Вашингтон", "Франция" : "Париж"}
# print(countries_capitals["Франция"]) # указание ключа

# countries_capitals = {'Россия' : "Москва", "США" : "Вашингтон", "Франция" : "Париж"}
# print(countries_capitals["Франция"]) # указание ключа
# countries_capitals["Сербия"] = "Белград" # добавление к сущ. словарю дополнит. ключа
# print(countries_capitals)


# d = {'key': 'old_value'}
# d['key'] = 'new_value' # новый ключ перезаписывает старый!
# print(d['key'])

# countries_capitals = {'Россия' : "Москва", "США" : "Вашингтон", "Франция" : "Париж"}
# if 'Сербия' in countries_capitals:
#    print(countries_capitals["Сербия"])
# else:
#    print('страны нет в словаре')

# countries_capitals = {'Россия' : "Москва", "США" : "Вашингтон", "Франция" : "Париж"}
# for country in countries_capitals:
#    print(f'У страны {country} столица - {countries_capitals[country]}')


# Ввод стран с клавы и добавление в словарь, подсчет кол-ва ввода

# countries = dict()
# country = input()
# str_number = 0

# while country != 'стоп':
#    if country not in countries:
#       countries[country] = [str_number]
#    else:
#       countries[country].append(str_number)
#    str_number += 1
#    country = input()
# for country in countries:
#    print(f'{country}: {countries[country]}')



# d = {'a': 1, 'b': 2, 'c': 3}
# print(len(d))
# del d['a'] # удалить ключ
# print(d)

# d = {'a': 1, 'b': 2, 'c': 3}
# d_new = d.copy() # сделать копию словаря
# print(d_new)

# d = {'a': 1, 'b': 2, 'c': 3}
# d_get = d.get('e', 'ключа нет') # не дает ошибку, если нет ключа, но вместо этого выдает какое-то знчение
# print(d_get)

# d = {'a': 1, 'b': 2, 'c': 3}
# for key, value in d.items():
#    print(key, value)

# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d.keys():
#    print(key)

# d = {'a': 1, 'b': 2, 'c': 3}
# for value in d.values():
#    print(value)

# d = {'a': 1, 'b': 2, 'c': 3}
# x = d.pop('a')
# print(x)
# print(d)


# Ввод стран с клавы и добавление в словарь, подсчет кол-ва ввода (простой способ)

# countries = dict()
# country = input()
# str_number = 0

# while country != 'стоп':

#    countries[country] = countries.get(country, []) + [str_number] # вместо ошибки получаем новое значение

#    str_number += 1
#    country = input()

# for country in countries:
#    print(f'{country}: {countries[country]}')


# str_1 = "Ну тут какая то строка"
# d = {"a":[1], "b": [2], "c": [3]}
# print(d.get("a", []) + [str_1]) 
# print(d['b'])



my_dict = {'a': 1, 'b': 2, 'c': 3}

# Получение значения по ключу
value = my_dict.get('b')  # value будет 2
value_default = my_dict.get('d', 0) # value_default будет 0
print(f"Значение по ключу 'b': {value}, значение по ключу 'd': {value_default}")

# Получение пар ключ-значение
items = my_dict.items() # items будет view object
print(f"Элементы словаря: {list(items)}") # Преобразование в список для наглядности

# Получение ключей
keys = my_dict.keys() # keys будет view object
print(f"Ключи словаря: {list(keys)}")

# Удаление элемента
removed_value = my_dict.pop('b') # удален элемент {'c': 3, 'a': 1}
print(f"Удаленное значение: {removed_value}, словарь после удаления: {my_dict}")

# Удаление случайного элемента
try:
    popped_item = my_dict.popitem()
    print(f"Удаленный элемент: {popped_item}, словарь после удаления: {my_dict}")
except KeyError:
    print("Словарь пуст")

# Добавление или обновление элемента
my_dict.setdefault('d', 4) # {'a': 1, 'd': 4}
my_dict.setdefault('a', 5) # {'a': 1, 'd': 4} - 'a' уже существует
print(f"Словарь после setdefault: {my_dict}")

# Обновление словаря
new_dict = {'b': 2, 'e': 5}
my_dict.update(new_dict) # {'a': 1, 'd': 4, 'b': 2, 'e': 5}
print(f"Словарь после обновления: {my_dict}")

# Получение значений
values = my_dict.values() # values будет view object
print(f"Значения словаря: {list(values)}")
