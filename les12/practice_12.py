# На позиционные аргументы

#Напишите функцию greet(name, city), которая принимает имя и город и
# возвращает строку приветствия вида "Привет, [имя]! Как погода в [город]?".

def greet(name, city):
   return (f'Привет, {name}! Как погода в {city} ?')

print(greet('Ann', 'SPb'))
 

# Напишите функцию rectangle_area(width, height), 
# которая вычисляет и возвращает площадь прямоугольника.

def rectangle_area(width, height):
   return width * height

print(rectangle_area(40, 30))


# Напишите функцию join_with_separator(str1, str2, separator), 
# которая объединяет две строки через указанный разделитель.

def join_with_separator(str1, str2, separator):
   return separator.join([str1, str2])

print(join_with_separator('Hello', 'World', '---'))
      

# Напишите функцию is_in_range(number, min_val, max_val), которая возвращает True,
# если число number находится в диапазоне 
# от min_val до max_val (включительно), и False в противном случае.

def is_in_range(number, min_val, max_val):
   if min_val < number < max_val:
      return True
   else:
      return False

print(is_in_range(8, 15, 100))
      

# Напишите функцию find_in_slice(data, element, start, end), которая
# ищет element в списке data только в срезе от start до end (не включая end).
# Если элемент найден, функция должна вернуть его индекс в исходном списке, иначе — -1.

data = [45, 58, 0, -5, 125, 6, 77, 1, 100]

def find_in_slice(data, element, start, end):
   for i in range(len(data)):
      if data[i] == element and start <= element < end:
         return i
   return -1
   
print(find_in_slice(data, 100, 1, 100))



# На именованные аргументы

# Напишите функцию create_user_profile(name, city="Не указан"), 
# которая возвращает строку с профилем. Город является необязательным параметром.




# Напишите функцию power(base, exponent=2), которая возводит число base в степень exponent.
#  По умолчанию степень равна 2 (возведение в квадрат).



# Напишите функцию format_header(text, level=1, char="=") 
# которая создает заголовок. level — количество строк из символов char до и после текста.
# Длина строки из символов = длине текста

# Пример вывода
# format_header("Заголовок", level=1, char="=")
# =========
# Заголовок
# =========


# def format_header(text, level=1, char="="):
#    line = char * len(text)
#    header_lines = [line] * level
#    final_line = '\n'.join(header_lines)
#    return final_line + f'\n{text}\n' + final_line

# print(format_header('Заголовок', level=5, char='='))


# Задача с пометкой для самостоятельного изучения
# Напишите функцию create_html_tag(tag, content, style=None, id_name=None), 
# которая создает строку с HTML-тегом. Атрибуты style и id_name необязательны.
# <p> Простой параграф </p>
# <div id="main-block">Блок с ID</div>
# <span style="color: red;">Цветной текст</span>

# Напишите функцию для расчета ежемесячного платежа по кредиту. 
# Формула аннуитетного платежа: 
# Платеж = Сумма * (Ставка * (1 + Ставка)^Срок) / ((1 + Ставка)^Срок - 1).
# Установите годовую ставку по умолчанию 10% (0.1) и срок в годах 5 лет.

# Задачи на *args

# Напишите функцию sum_all(*numbers), которая принимает любое количество чисел и 
# возвращает их сумму.

# Напишите функцию find_longest_word(*words), которая принимает любое количество строк 
# и возвращает самую длинную из них.

# Напишите функцию smart_join(separator, *items), которая объединяет все items в одну строку,
#  используя separator между ними. Первый аргумент — обязательный.
# Используйте функцию высшего порядка внутри функции (подсказка)

# Напишите функцию average_numbers(*args), которая принимает любое количество аргументов
#  разных типов и вычисляет среднее арифметическое только для числовых аргументов
#  (int или float).

# Задачи на **kwargs

     
      