# скопировать

# def add_value(x, list_arg = None):
#    if list_arg is None:
#       list_arg = []
#    list_arg += [x]
#    return list_arg

# print (add_value(0))
# print (add_value(0, [1, 2, 3]))
# print (add_value(0))
# print (add_value(1))
# print (add_value(0))


# позиционные и именованные аргументы

# def final_price(price, discount=1):
#    return price - price * discount / 100

# print(final_price(1000, discount=5))
# print(final_price(discount=15, price=1000))


# бесконечное кол-во неименованных аргументов задается *  args

# def final_price(*prices, discount=1): # *args - принятое обозначение
#    return [price - price * discount / 100 for price in prices]

# print(final_price(1000, 500, 350, 200, 46541, discount=5))


# бесконечное кол-во именованных аргументов задается **  kwargs

# def final_price(*prices, discount=1, **kwargs): # обращение как с обычным словарем
#    low = kwargs.get('price_low', min(prices))
#    high = kwargs.get('price_high', max(prices))
#    return [price - price * discount / 100 for price in prices if low <= price <=high]

# print(final_price(100, 200, 300, 500, 700, discount=5))
# print(final_price(100, 200, 300, 500, 700, discount=5, price_low=250))
# print(final_price(100, 200, 300, 500, 700, discount=5, price_high=500))
# print(final_price(100, 200, 300, 500, 700, discount=5, price_low=250, price_high=500))


# функции высшего порядка

def only_pos(x): # критерий отбора 
   return x > 0 

result = filter(only_pos, [-1, 5, 7, 10, 0, -11])
# print(list(result)) # вариант вывода
print(', '.join(str(x) for x in result))
