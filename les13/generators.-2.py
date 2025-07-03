# squares = (i ** 2 for i in range(10))
# print(squares)


def fib(n):
   n_1, n_2 = 1, 1
   for i in range(n):
      yield n_1
      n_1, n_2 = n_2, n_1 + n_2
   
print(fib(10)) # возврат самого генератора
print(', '.join(str(x) for x in fib(10)))


f = fib(10)
for i in range(5): # вывод только первых 5ти чисел из фибоначи
   print(next(f))
 

def fruit_gen():
   for item in ['apple', 'banana', 'cherry']:
      yield item

fruit = fruit_gen()
print(next(fruit))
print(next(fruit))
print(next(fruit))

  