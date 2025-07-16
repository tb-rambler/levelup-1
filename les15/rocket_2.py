# метод сообщающий расстояния от одной ракеты до другой

from math import sqrt

class Rocket():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment

   def get_distance(self, other_rocket):
      distance = sqrt((self.x - other_rocket.x)**2 + (self.y - other_rocket.y)**2)
      return distance


rocket_0 = Rocket()
rocket_1 = Rocket(10, 5)

distance = rocket_0.get_distance(rocket_1)
print(distance)

