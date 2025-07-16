# наследование (производный класс)

# class Pencil:

#    def __init__(self, color='grey'):
#       self.color = color
   
#    def draw_picture(self):
#       return f'Нарисован рисунок цветом {self.color}'

# class Pen(Pencil):

#    def sign_doc(self):
#       if self.color not in ('blue', 'black', 'violet'):
#          return f'ручкой цвета {self.color} нельзя подписать документ'
#       return f'Документ подписан'
      
# blue_pen = Pen(color= 'blue')
# print(blue_pen.draw_picture())
# print(blue_pen.sign_doc())

# red_pen = Pen(color= 'red')
# print(red_pen.draw_picture())
# print(red_pen.sign_doc())



class Pencil:

   def __init__(self, color='grey'):
      self.color = color
   
   def draw_picture(self):
      return f'Нарисован рисунок цветом {self.color}'

class Pen(Pencil):

   def __init__(self, color, pen_type):
      super().__init__(color=color)
      self.pen_type = pen_type


   def sign_doc(self):
      if self.color not in ('blue', 'black', 'violet'):
         return f'ручкой цвета {self.color} нельзя подписать документ'
      return f'Документ подписан'
      
blue_pen = Pen(color= 'blue', pen_type='шариковая')
print(blue_pen.draw_picture())
print(blue_pen.sign_doc())

red_pen = Pen(color= 'red')
print(red_pen.draw_picture())
print(red_pen.sign_doc())


