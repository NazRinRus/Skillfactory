PI_CONSTANT = 3.14

def square_round(radius):
    return PI_CONSTANT * (radius ** 2)

def square_rectangle(a, b):
    return a * b

if __name__ == '__main__':
   # проверяем работоспособность функции, дальнейшая часть не будет импортирована
   assert square_round(5) == 78.5  # если ответы будут отличаться, то будет вызвана ошибка
   assert square_rectangle(5, 4) == 20