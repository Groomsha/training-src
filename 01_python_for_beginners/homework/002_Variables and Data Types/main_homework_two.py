# Напишите программу, которая запрашивает три целых числа a, b и x и выводит True,
# если x лежит между a и b, иначе – False.

number_a = int(input("Первое число для вывода: "))
number_b = int(input("Второе число для вывода: "))
number_x = int(input("Третье число для вывода: "))

result = number_x > number_a and number_x < number_b

print("=" * 45)
print(f"Результат сравнения числа: {result}", end="\n\n" )
print("Слава Україні! Героям слава! Смерть ворогам!")
