# [x for x in seq if condition] - фильтрует эл-ты
# [A if condition else B for x in seq] - выбирает знач-я по условию

# lst = [x**2 for x in range(11) if x % 2 == 0]
# print(lst)

# lst = ['even' if x % 2 == 0 else 'odd' for x in range(1, 11)] # чет нечет
# print(lst)

# # классификация оценок студентов

# lst = ['pass' if x >= 50 else 'fail' for x in [70, 40, 55, 50, 90, 100]]
# print(lst)

# # заменить отрицат. числа на 0

# lst = [x if x > 0 else 0 for x in [3, 5, 0, -10, -2, 34, 5, -11]]
# print(lst)

scors = [70, 40, 55, 50, 90, 100] # проставить оценки в зависимости от баллов
grades = [5 if x >= 90 else
         4 if x >= 70 else
         3 if x >= 55 else
         2 for x in scors ]
print(grades)
