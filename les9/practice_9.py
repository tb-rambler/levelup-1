# 1/ cделать список емейлов по домену gmail.com
# ["ivan@gmail.com", "kate@yahoo.com", "john@gmail.com", "test@outlook.com"]

emails = ["ivan@gmail.com", "kate@yahoo.com", "john@gmail.com", "test@outlook.com"]
gmail = [mail for mail in emails if mail.endswith('gmail.com')]
print(gmail)


# 2/ список длины строк исключая пустые
words = ['Hello', '', 'Data', 'Science', '', '', 'Pyton']
word = [len(word) for word in words if len(word) > 0]
# word = [len(word) for word in words if word] # этот способ проще
print(word)


# 3 квадраты нечетных чисел

lists = [1, 5, 8, 6, 57, 61, 22, 45, 0]
qwadro = [x **2 for x in lists if x % 2 !=0]
print(qwadro)


# 4 строки в числа игнорируя нечисловые

string = ['42', '100', 'abc', 'nAn', '&', '7']
list = [int(x) for x in string if x.isnumeric()]
print(list)


# 5 Плоский список из матрицы

matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
# sum(matrix, []) # очень просто , сложение внутри списка всех эл-тов
print(flat)


# 6 Cловарь слово - длина слова 

dictr = ['apple', 'banana', 'kiwi']
len_word = {word: len(word) for word in dictr}
print(len_word)
