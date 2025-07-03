# def func():
#    pass

# def decorator(old_func):
#    def new_func():
#       return old_func
#    return new_func

# print(func)
# func = decorator(func)
# print(func)


# def decorator(old_func):
#    def new_func():
#       return old_func
#    return new_func

# @decorator
# def func():
#    pass


def count(f):
   total = 0

   def decorated(*args, **kwargs):
      nonlocal total
      total +=1
      return f(*args, **kwargs), total
   return decorated

@count
def hello(name):
   return f'Привет, {name}!'

print(hello('user_1'))
print(hello('user_2'))
