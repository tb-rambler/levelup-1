# Объекто ориентированное програмирование

# объекты: машины, цвет, объем бака, расход топлива, запас топлива, пробег, расстояние (задаем степень детализации сами)

# условия: действия, которые выполняют объекты (машины)
# запуск двигателя, езда на N км, остановка двигателя, заправить машину
# Это процедурный тип программирования (громоздкий)
# для создания модели пока мы умеем использовать словари:

def create_car(color, consumption, tank_volume, mileage=0): # по умолчанию у всех машин пробег 0
    return {'color':color, 
            'consumption':consumption, 
            'tank_volume':tank_volume,
            'reserve':tank_volume, # резерв будет меняться, а V бака - нет
             'mileage': mileage,
             "engine_on":False} # по умолчанию у всех машин двигатель выключен

def start_engine(car): # функция запуска двигателя 
    if not car['engine_on'] and car['reserve'] > 0: # при резерве топлива >0 и при выкл. двигателе
        car['engine_on'] = True
        return "Двигатель запущен"
    return "Двигатель уже был запущен или нет топлива"

def stop_engine(car):  # функция остановки двигателя
    if car['engine_on']:
        car['engine_on'] = False
        return "Двигатель остановлен"
    return "Двигатель уже был остановлен"

def drive(car, distance):  # функция езды на N km
    if not car['engine_on']:   # при условии вкл. двигателя и достаточ. запасе топлива
        return "Двигатель не запущен"
    if car['reserve'] / car['consumption'] * 100 < distance:
        return "Малый запас топлива"
    
    car['mileage'] += distance  # добавляем сколько проехали
    car['reserve'] -= distance / 100 * car['consumption']   # вычитаем сколько потратили топлива
    return f"Проехали {distance} км. Остаток топлива: {car['reserve']} л."

def refuel(car):  # дозаправка
    car['reserve'] = car['tank_volume']  # после заправки объем = полному баку
    return "Бак заправлен полностью!"

def get_mileage(car):  # функция пробег автомобиля
    return f"Пробег {car['mileage']} км."

def get_reserve(car):   # функция остаток топлива
    return f'Запас топлива {car['reserve']} л.'

#  создаем машины, запускаем наши функции и смотрим что они возвращают

car_1 = create_car(color='black', consumption=10, tank_volume=55)

print(start_engine(car_1)) # заведи двигатель
print(drive(car_1, 100))  # проедь на 100 км
print(drive(car_1, 100))  # проедь еще 100 км
print(drive(car_1, 100))  # проедь еще 100 км
print(drive(car_1, 300))  # проехать 300 км уже не можем
print(get_mileage(car_1))  # смотрим пробег
print(get_reserve(car_1))  # смотрим остаток топлива
print(refuel(car_1))       # заправляем до полного
print(drive(car_1, 300))   # проедь еще 300 км
print(stop_engine(car_1))  # заглуши двигатель
print(drive(car_1, 100))   # поехать с выкл. двигателем не можем


print(type(1))  # тип int - это класс


# class <ИмяКласса>:  синтаксис создания класса, всегда с большой буквы
#     <описание класса>

# синтаксис создания атрибутов (свойств или признаков объекта)
# <имя_объекта>.<имя_атрибута> = <значение> 

# синтаксис создания метода (вызываются после создания объекта)
# def <имя_метода>(self, <аргументы>): self - вызывает метод и работает с атрибутами для определенного объекта внутри класса
    # <тело метода>
#  метод __init__

# <имя_объекта> = <ИмяКласса>(<аргументы метода __init__()>)


class Car:
    
   def __init__(self, color, consumption, tank_volume, mileage=0): # инициализация объектов класса (задание аргументов)
        self.color = color  # объявление аргументов
        self.consumption = consumption
        self.tank_volume = tank_volume
        self.reserve = tank_volume
        self.mileage = mileage
        self.engine_on = False

   def start_engine(self): # описание следующего метода
        if not self.engine_on and self.reserve > 0: # self - отсылает выше, откуда взять аргументы
            self.engine_on = True
            return "Двигатель запущен"
        return "Двигатель уже был запущен или нет топлива"

   def stop_engine(self):   # описание следующего метода
        if self.engine_on:
            self.engine_on = False
            return "Двигатель остановлен"
        return "Двигатель уже был остановлен"  

   def drive(self, distance):  # - distance - это внешний объект, поэтому без '.self'
        if not self.engine_on:
            return "Двигатель не запущен"
        if self.reserve / self.consumption * 100 < distance:
            return "Малый запас топлива"
        self.mileage += distance
        self.reserve -= distance / 100 * self.consumption
        return f"Проехали {distance} км. Остаток топлива: {self.reserve} л."  
    
   def refuel(self):
        self.reserve = self.tank_volume
        return "Бак заправлен полностью!"

   def get_mileage(self):
        return f"Пробег {self.mileage} км."

   def get_reserve(self):
        return self.reserve
    
   def get_consumption(self):
        return self.consumption



car_1 = Car(color='black', consumption=10, tank_volume=55)   # <имя_объекта> = <ИмяКласса>(<аргументы метода __init__()>)

# print(car_1.start_engine())
# print(car_1.drive(100))
# print(car_1.drive(100))
# print(car_1.drive(100))
# print(car_1.drive(300))
# print(car_1.get_mileage())
# print(car_1.get_reserve())
# print(car_1.stop_engine())
# print(car_1.drive(100))
# car_2 = Car(color='red', consumption=15, tank_volume=70)
# print(car_2.color)
# print(car_1.color)
# car_1.mileage = 1000
# print(car_1.get_mileage())
# print(car_1.get_reserve())

class ElectricCar:
    
    def __init__(self, color, consumption, bat_capacity, mileage=0):
        self.color = color
        self.consumption = consumption
        self.bat_capacity = bat_capacity
        self.reserve = bat_capacity
        self.mileage = mileage
        self.engine_on = False

    def start_engine(self):
        if not self.engine_on and self.reserve > 0:
            self.engine_on = True
            return "Двигатель запущен"
        return "Двигатель уже был запущен или нет топлива"

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            return "Двигатель остановлен"
        return "Двигатель уже был остановлен"  

    def drive(self, distance):
        if not self.engine_on:
            return "Двигатель не запущен"
        if self.reserve / self.consumption * 100 < distance:
            return "Малый запас заряда"
        self.mileage += distance
        self.reserve -= distance / 100 * self.consumption
        return f"Проехали {distance} км. Остаток заряда: {self.reserve} кВт*ч."  
    
    def refuel(self):
        self.reserve = self.bat_capacity
        return "Батарея заряжена полностью!"

    def get_mileage(self):
        return f"Пробег {self.mileage} км."

    def get_reserve(self):
        return self.reserve

    def get_consumption(self):
        return self.consumption

def range_reserve(car):
    return car.get_reserve() / car.get_consumption() * 100


car_1 = Car(color='black', consumption=10, tank_volume=55)
car_2 = ElectricCar(color='white', consumption=15, bat_capacity=90)
print(f"Запас хода: {range_reserve(car_1)} км.")
print(f"Запас хода: {range_reserve(car_2)} км.")
