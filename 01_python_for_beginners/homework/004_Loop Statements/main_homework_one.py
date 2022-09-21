# Даны числа a и b (a < b). Выведите сумму всех натуральных чисел от a до b (включительно).

while True:
	number_one = int(input('Введите первое натуральное число: '))
	number_two = int(input('Введите второе натуральное число: '))
	print('='*40, end='\n\n')

	if number_one < number_two:
		for number in range(number_one, number_two + 1):
			print(f'В диапазоне натуральное число: {number}')
		break
	else:
		print('\nПервое натуральное число не может быть больше второго. Повторите ввод.')
		print('=' * 70, end='\n\n')
