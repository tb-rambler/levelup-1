# вывести список чисел через , 1/диапазон

# print(';'.join(str(1/x) for x in range(int(input(), int(input()+1)))))

# interval = range(int(input()), int(input())+1)
# if 0 in interval:
#    print('Диапазон содержит 0')
# else:
#    print(';'.join(str(1/x) for x in interval))

# try:
#    <код, который может вызвать исключение>
# except <КлассИсключения_1>:
#    <обработка ошибки этого типа>
# except <КлассИсключения_2>:
#    <обработка ошибки этого типа>
# ...
# else:
#    <выполняется, если исключений не было>
# finally:
#    <выполняется всегда, если -- и при ошибках, и без>

# except Exception # обработка всех ошибок сразу


# ПРАВИЛЬНЫЙ ПОРЯДОК:
# try:
#    print(1 / int(input()))
# except ZeroDivisionError:   # от частных ошибок к общим (дочерние классы)
#    print('ошибка деления на 0')
# except ValueError:
#    print('невозможно преобразовать в число')
# except Exception:             # Только в конце обработка для всего остального (родительский класс)
#    print('неизвестная ошибка')
   
# блок ELSE

# try:
#    print(1 / int(input()))
# except ZeroDivisionError:   # от частных ошибок к общим (дочерние классы)
#    print('ошибка деления на 0')
# except ValueError:
#    print('невозможно преобразовать в число')
# except Exception:             # Только в конце обработка для всего остального (родительский класс)
#    print('неизвестная ошибка')
# else:
#    print('операция выполнена успешно')


# блок FINALLY

# try:
#    print(1 / int(input()))
# except ZeroDivisionError:   # от частных ошибок к общим (дочерние классы)
#    print('ошибка деления на 0')
# except ValueError:
#    print('невозможно преобразовать в число')
# except Exception:             # Только в конце обработка для всего остального (родительский класс)
#    print('неизвестная ошибка')
# else:
#    print('операция выполнена успешно')
# finally:
#    print('программа завершена')  # выполняется всегда, при любом раскладе


# перепишем:

# try:
#    print(';'.join(str(1/x) for x in range(int(input()), int(input())+1)))
# except ValueError:
#    print('введите 2 числа')
# except ZeroDivisionError:
#    print('диаппазон содержит 0')

# оператор raise  <КлассИсключения> (сообщение) - если программа зашла в опасное состояние

# x = int(input())
# if x < 0:
#    raise ValueError('число должно быть положительным') # разъяснить подробно ошибку и остановить программу


# исключение, если есть 

# class NumbersError(Exception):
#    pass
# class EvenError(NumbersError):
#    pass
# class NegativeError(NumbersError):
#    pass

# def no_even(numbers):
#    if all(x % 2 != 0 for x in numbers):
#       return True
#    raise EvenError('в списке не должно быть отрицат. чисел')

# def main():
#    print('введите числе в одну строку через пробел')
#    try:
#       numbers = [int(x) for x in input(.split())]
#           if no_negative(numbers) and no_even(numbers):
#             print(f'сумма чисел равна:{sum(numbers)}')
#    except NumbersError as e:
#       print(f'произошла ошибка: {e}')
#    except Exception as e:
#       print(f'произошла непредвиденная ошибка: {e}')


# if __name__ == '__main__': # файл запущен напрямую или импортирван как модуль
#    main()


# import Example_module

# Example_module.some_function()

# from example_module import some_function, ExampleClass

# some_function()


# cоздать класс Animal: name, species, метод display_info
# создать подкласс Mammal: warm_blood = True; display_info
# cоздать подкласс Bird: can_fly = True; display_inf0
# создать класс Zoo: animal = []; add_animal, show_all_animals

class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def display_info(self):
        print(f"{self.name} - {self.species}")

class Mammal(Animal):
    def __init__(self, name, species, warm_blood = True):
        super().__init__(name, species)
        self.warm_blood = warm_blood
    def display_info(self):
        print(f"{self.name} - {self.species} {self.warm_blood}")

class Bird(Animal):
    def __init__(self, name, species, can_fly = True):
        super().__init__(name, species)
        self.can_fly = can_fly
    
    def display_info(self):
        print(f"{self.name} - {self.species} {self.can_fly}")

class Zoo():
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        self.animals.append(animal)
    def show_all_animals(self):
        for animal in self.animals:
            animal.display_info()

cow = Animal("Корова", "травоядное")
cat = Mammal("Кошка", "Хищник")
eagle = Bird("Орел", "Хищник")
zoo = Zoo()
zoo.add_animal(cow)
zoo.add_animal(eagle)
zoo.add_animal(cat)
zoo.show_all_animals()
