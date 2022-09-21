import math


number_one = int(input("Введите число: "))
step = input("Действие. Доступно ('+', '-', '/', '*', '**', 'cos', 'sin': ")

if 'cos' != step and 'sin' != step:
    number_two = int(input("Введите число: "))

if '+' in step:
    res = number_one + number_two
elif '-' in step:
    res = number_one - number_two
elif '/' in step:
    res = number_one / number_two
elif '*' in step:
    res = number_one * number_two
elif '**' in step:
    res = number_one ** number_two
elif 'cos' in step:
    res = math.cos(number_one)
elif 'sin' in step:
    res = math.sin(number_one)

print(res)