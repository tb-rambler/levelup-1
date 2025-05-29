# 1. Построить треугольник где строки - цифры от 1 до № строки
#1
#12
#123
#1234
#12345

# for i in range(1, 5):
#    for j in range(1, i+1):
#       print(j, end='')
#    print('')   

# # 2. Вывести квадрат из # размером 4 ч 4
# for i in range(4):
#    for j in range(4):
#       print('#', end="")
#    print('')

   # 3. построить треугольник начиная с 5 звездочек до 1
# star = '*'
# size = 5
# # while size > 0:
# #    print(star * size)
# #    size -= 1

# for i in range(size, 0, -1):
#    for _ in range(i):
#       print(star, end ="")
#    print('')

# 4. нарисовать:
#####
#   #
#   #
#   #
#####

for row in range(5):
   for col in range(7):
      if row == 0 or row == 4 or col == 0 or col == 6:
         print('#', end = "")
      else:
         print(" ", end = "")
   print('')
