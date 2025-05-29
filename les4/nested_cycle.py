# print(ord('a'))
# print(chr(97))
# print(chr(ord('a')+1))
# for i in range(26):
#    for j in range(26):
#       print(f'{chr(ord('a')+i)}{chr(ord('a')+j)}') # перебор всех букв алфавита внутри другого цикла по перебору всех букв алфавита

# flag = False
# for i in range(26):
#    for j in range(26):
#       text = f'{chr(ord('a')+i)}{chr(ord('a')+j)}' # перебор всех букв алфавита  до ya
#       if text =='ya':
#          print(text)
#          flag = True
#          break
#       print(text)
#    if flag == True: # или проще: if flag:
#       break   

# for i in range(26):
#    for j in range(26):
#       if i == j:
#          continue
#       print(f'{chr(ord('a')+i)}{chr(ord('a')+j)}') # кроме одинаковых букв
            
# for i in range(26):
#    for j in range(26):
#       if i !=j:
#          print(f'{chr(ord('a')+i)}{chr(ord('a')+j)}') # более простой логичный вариант

# while input('введите строку: ') != 'STOP':
#    print('Hi')
# else:
#    print('The end')

while (text := input('введите строку: ')) != 'STOP':
   print('Hi')
   if text == 'ignore':
      break
else:
   print('The end')
