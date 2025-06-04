# Кортеж. Не изменяемая коллекция в отличие от списка
# numbers = (1, 2, 3, 4, 5)
# print(numbers)
# print(type(numbers))

a = 1, 2, 3, 4
print(a)

a = 1
b = 2
(a, b) = (b, a) # помекнять местами (можно без скобок)
print(f'a={a}, b={b}')

text = 'Hwllo'
list_symbol = list(text) # превратить строку в список
tuple_symbol = tuple(text) # перевести список в строку
print(list_symbol)
print(tuple_symbol)

