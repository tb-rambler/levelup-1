# наследование (продолжение)

class GreetingFormal:

   def __init__(self):
      self.formula_greeting = 'Good day, '

   def greet_formal(self, name):
      return f'{self.formula_greeting} {name}'
   
class GreetingInFormal():

   def __init__(self):
      self.informal_greeting = 'Hello, '
 

