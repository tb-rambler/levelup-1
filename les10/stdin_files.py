# ввод данных с клавы

# from sys import stdin

# lines = []
# for line in stdin:
#    lines.append(line.rstrip('\n')) # ctrl + z + enter - остановить ввод
# print(lines)

# lines = stdin.readline()
# print(lines)


# text = stdin.read()
# print([text])


# ввод данных из файлов (OPEN)  - обязательно потом закрыть методом CLOSE

# лучше использовать относит, а не абсолют. путь к файлу
# C:\Users\tb\Desktop\Pyton\levelup-1-1\les10\input.txt

# file_in = open('les10\input_1.txt', encoding='UTF-8')
# for line in file_in:
#    print(line)
# file_in.close()

# with open('les10\input_1.txt', encoding='UTF-8') as file_in:
#    for line in file_in:
#       print(line.rstrip('\n')) # не нужно закрывать файл, он сам закрывается

# with open('les10\input_1.txt', encoding='UTF-8') as file_in:
#    lines = file_in.readlines()
# print(lines)


# with open('les10\input_1.txt', encoding='UTF-8') as file_in:
#    symbols = file_in.read(10)
# print([symbols])

# with open('les10\input_1.txt', 'w', encoding='UTF-8') as file_out:
#    n = file_out.write('это первая строка\nэто вторая \nэто последняя')
# print(n)


# lines = ["Это первая строка\n", "А это вторая\n", "И третья - последняя"]
# with open('les10\\output_2.txt', 'w', encoding="UTF-8") as file_out:
#     file_out.writelines(lines)

# with open('les10\\output_3.txt', 'a', encoding="UTF-8") as file_out:
#     print("Вывод в файл с помощью функции print()", file=file_out)
