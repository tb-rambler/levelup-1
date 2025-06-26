# есть встроенные библиотеки, есть импортируемые
# импорт всегда пишется в начале программы и с отступом в одну строку после

# import itertools # вся библеотека

# print(itertools.product('ABC', repeat=2))


# from itertools import product # выбор одного итератора из библиотеки

# print(product('ABC', repeat=2))
# print(list(product('ABC', repeat=2)))

# from itertools import count # генератор чисел

# for value in count(0, 0.1):
#    if value <= 1:
#       print(value, 1)
#    else:
#       break

# from itertools import cycle

# max_len = 10
# s = ''
# for letter in cycle('ABC'):
#    if len(s) < max_len:
#       s += letter
#    else:
#       break
# print(s)

# from itertools import repeat

# result = list(repeat('ABC', 5))
# print(result)

# from itertools import accumulate # аккумулирует каждое сложение

# for value in accumulate([1, 2, 3, 4, 5]):
#    print(value)

# from itertools import chain # объединение списков

# value = list(chain('ABC', 'DEF', 'JHIG'))
# print(value)

# from itertools import chain # объединение списков подфункция

# value = list(chain.from_iterable(['ABC', 'DEF', 'JHIG']))
# print(value)


# from itertools import product

# value = list(product([1, 2, 3], 'ABCD'))
# print(value)


# from itertools import product

# value = list(product([1, 2, 3], 'ABCD', repeat = 2)) # повтор 2 раза
# print(value)

# from itertools import permutations # перебор всех возм. комбинаций без повторений

# value = list(permutations('ABC'))
# print(value)


# from itertools import combinations

# value = list(combinations('ABC', r=2)) # длина последовательности
# print(value)

# from itertools import combinations_with_replacement

# value = list(combinations_with_replacement('ABC', r=2))
# print(value)

# for index, value in enumerate('ABC', 1):
#    print(index, value)

# print(list(zip('ABC', [1, 2, 3])))

# print(list(zip('ABCDE', [1, 2, 3]))) # по самому короткому передается

# print(list(zip('ABCDE', [1, 2, 3], strict=True))) # искл. ошибку

from itertools import zip_longest # если не хватает эл-тов, они добиваются None

# print(list(zip_longest('ABCDE', [1, 2, 3])))
# print(list(zip_longest('ABCDE', [1, 2, 3], fillvalue=('IIIII')))) 
print(list(zip_longest('ABCDE', [1, 2, 3], fillvalue=15)))


