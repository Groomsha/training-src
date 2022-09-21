# Создайте две функции, вычисляющие значения определённых алгебраических выражений.
# Выведите на экран таблицу значений этих функций от -5 до 5 с шагом 0.5.


def expression_one(numb_a: int, numb_c: int) -> int:
	return numb_a * numb_c


def expression_two(numb_a: int) -> int:
	return (numb_a ** 2) - numb_a


def print_result(number):
	for numb in range(-5, number):
		if numb / 2 <= 5:
			print(numb / 2)

	print('='*5, end='\n')


while True:
	menu_calc: str = input('\n1. Вывести таблицу на основание параметров \n2. Exit\n\nВведите действие: ')

	if menu_calc == '1':
		number_one = int(input('Введите первое число: '))
		number_two = int(input('Введите второе число: '))

		print_result(expression_two(number_one)); print('', end='\n')
		print_result(expression_one(number_one, number_two))
	elif menu_calc == '2':
		break
