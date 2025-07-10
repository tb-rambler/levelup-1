# Объекто ориентированное програмирование

# объекты: машины, цвет, объем бака, расход топлива, расстояние

def create_car(color, consumption, tank_volume, mileage=0):
    return {'color':color, 
            'consumption':consumption, 
            'tank_volume':tank_volume,
            'reserve':tank_volume,
             'mileage': mileage,
             "engine_on":False}

def start_engine(car):
    if not car['engine_on'] and car['reserve'] > 0:
        car['engine_on'] = True
        return "Двигатель запущен"
    return "Двигатель уже был запущен или нет топлива"

def stop_engine(car):
    if car['engine_on']:
        car['engine_on'] = False
        return "Двигатель остановлен"
    return "Двигатель уже был остановлен"

def drive(car, distance):
    if not car['engine_on']:
        return "Двигатель не запущен"
    if car['reserve'] / car['consumption'] * 100 < distance:
        return "Малый запас топлива"
    car['mileage'] += distance
    car['reserve'] -= distance / 100 * car['consumption']
    return f"Проехали {distance} км. Остаток топлива: {car['reserve']} л."

def refuel(car):
    car['reserve'] = car['tank_volume']
    return "Бак заправлен полностью!"

def get_mileage(car):
    return f"Пробег {car['mileage']} км."

def get_reserve(car):
    return f'Запас топлива {car['reserve']} л.'

car_1 = create_car(color='black', consumption=10, tank_volume=55)

print(start_engine(car_1))
print(drive(car_1, 100))
print(drive(car_1, 100))
print(drive(car_1, 100))
print(drive(car_1, 300))
print(get_mileage(car_1))
print(get_reserve(car_1))
print(refuel(car_1))
print(drive(car_1, 300))
print(stop_engine(car_1))
print(drive(car_1, 100))

print(type(1))


# class <ИмяКласса>:
#     <описание класса>

# синтаксис создания атрибута
# <имя_объекта>.<имя_oтрибута> = <значение> 


# синтаксис создания метода
# def <имя_метода>(self, <аргументы>):
    # <тело метода>

# <имя_объекта> = <ИмяКласса>(<аргументы метода __init__()>)


class Car:
    
   def __init__(self, color, consumption, tank_volume, mileage=0):
        self.color = color
        self.consumption = consumption
        self.tank_volume = tank_volume
        self.reserve = tank_volume
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



car_1 = Car(color='black', consumption=10, tank_volume=55)
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
