# number = [10, 20, 30]
# print(number)
# print(type(number))

# mix = [10, 'text', 30.3]
# print(mix)
# print(type(mix))

# numbers = [10, 20, 30, 40, 50]
# print(numbers[0])  # срезы
# print(numbers[-1])
# print(numbers[1:3])
# print(numbers[::-1])

# numbers = [10, 20, 30, 40, 50]
# numbers[2] = 50
# print(numbers)

# numbers = [10, 20, 30, 40, 50]
# numbers.append(60) # добавить в конце 60
# print(numbers)

# 10 раз ввести цифры с клавы и сделать из них список
# numbers = []
# for i in range(10):
#    numbers.append(int(input()))
# print(numbers)

# numbers = [10, 20, 30, 40, 50] 
# del numbers[-1] # удаление из списка элемента
# print(numbers)

# del numbers[::2]
# print(numbers)

# присутствует ли элемент в списке (очень медленно)
#  x in list_name
print(1 in [2,3,4,5,1]) # 1 есть в списке

# x not in list_name
print(1 not in [2,3,4,5,1]) 

# списки можно сложить, умножить

s = [1,2]
t = [3,40,50]
print(s+t)
print(s*5) # 5 раз повторим

print(len(t)) # длина списка

print(min(t)) # min зачение в списке
print(max(t)) # max зачение в списке

print(t.index(50)) # возвращает индекс элемента в списке

numbers = [1, 1, 1, 2, 3, 4 ,5]
print(numbers.count(1)) # посчитать кол-во "1" в списке

# удалить список (очистить список), но оставить условия
print(numbers.clear())

numbers = [1, 1, 1, 2, 3, 4 ,5]

numbers2 = numbers.copy() # сделать копию списка
print(numbers)
print(numbers2)

print(id(numbers)) # посмотреть место в памяти

numbers2 = numbers
numbers2.append('new_element')

print(numbers is numbers2) # 2 одинаковых списка в памяти
print(numbers == numbers2) # находятся в разных местах памяти


# a = [1,2,3]
# b = a   # одна и таже коробка, разные ссылки на нее
# print(id(a))
# print(id(b))

# a.append(4)
# print(a)
# print(b)

# print(a == b)
# print(a is b) # один и тот же объект в памяти


# a = [1,2,3]
# b = a.copy() # копия коробки А, лежат в разных местах
# print(id(a))
# print(id(b))

# a.append(4)
# print(a)
# print(b)

# print(a == b)
# print(a is b) # разные объекты в памяти 

# a = [[1,2],[3,4]] # вложенные списки
# print(a)
# print(a[0])
# print(a[0][0]) # достать элемент из вложенного списка внутри другого 

# a = [[[5],1,2],[3,4]] # вложенные списки
# print(a)
# print(a[0])
# print(a[0][0][0]) # достать элемент из вложенного списка внутри другого 

# a = [[1,2],[3,4]] 
# b = a.copy()
# b.append(999)
# print(a)
# print(b)

# a = [[1,2],[3,4]] 
# b = a.copy()
# b[0].append(999) # cломалась копия, заменяет список и в другой коробке
# print(a)
# print(b)


# import copy # не проходили (писать в самом верху файла)

# a = [[1,2],[3,4]] 
# b = copy.deepcopy()  # метод копирования правильного списка для создания глубоких вложенных копий списков 
# b[0].append(999)
# print(a)
# print(b)


# метод, расширяющий список на те эл-ты, кот находятся в другом списке
# s = [1,2]
# t = [3,4,5]
# # s.append(t)
# # s.extend(t)
# # print(s)

# s = [1,3,4]
# s.insert(1,'2') # вставка
# print(s)

# s = [1,2,3]
# x = s.pop() # метод удалит последний элемент
# print(s)

# s = [1,2,3]
# x = s.pop(1) # метод удалит указанный элемент
# print(s)
# print(x) # указывает какой элемент удален

s = [1,2,3,2,1]
s.remove(2) # удаляет указанный элемент 1 раз
print(s)

s = [1,2,3]
s.reverse() # меняет список задом наперед
# s = s[::-1] не меняет список, только отображение
print(s)

s = [2,3,1]
s.sort() # сортировка по возрастанию
print(s)
s.sort(reverse=True) # сортировка по убыванию
print(s)

sorted(s, reverse=True) # не путать другой метод
print(s)
