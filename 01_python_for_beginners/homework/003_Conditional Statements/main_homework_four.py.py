# Напишите программу-калькулятор, в которой пользователь сможет ввести выбрать операцию,
# ввести необходимые числа и получить результат. Операции, которые необходимо реализовать:
# сложение, вычитание, умножение, деление, возведение в степень, синус, косинус и тангенс числа.

import math


step = input("Действие. Доступно ('+', '-', '/', '*', '^', 'cos', 'sin', 'tan': ")
number_one = int(input("Введите число: "))

result = None
number_two = None

if step != 'cos' and step != 'sin' and step != 'tan':
    number_two = int(input("Введите число: "))

if '+' in step:
    result = number_one + number_two
elif '-' in step:
    result = number_one - number_two
elif '/' in step:
    if number_two != 0:
        result = number_one / number_two
    else:
        result = 'На 0 не делят!'
elif '*' in step:
    result = number_one * number_two
elif '**' in step:
    result = number_one ** number_two
elif 'cos' in step:
    result = math.cos(number_one)
elif 'sin' in step:
    result = math.sin(number_one)
elif 'tan' in step:
    result = math.tan(number_one)

print(result)
