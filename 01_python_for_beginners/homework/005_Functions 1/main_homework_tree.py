# Создайте программу-калькулятор, которая поддерживает четыре операции:
# сложение, вычитание, умножение, деление. Все данные должны вводиться в цикле,
# пока пользователь не укажет, что хочет завершить выполнение программы.
# Каждая операция должна быть реализована в виде отдельной функции.
# Функция деления должна проверять данные на корректность и выдавать сообщение
# об ошибке в случае попытки деления на ноль.

from typing import List, Any


def introduction_numerals() -> List:
	number_one: int = int(input('\nВведите первое числительное: '))
	number_two: int = int(input('Введите второе числительное: '))

	return [number_one, number_two]


def result_calc(result) -> None:
	if type(result) == int or type(result) == float:
		print(f'\nРезультат математического действия: {result}')
	else:
		print('\nДеление на ноль не допустимо!')

	print('*' * 40)


def calc_plus(numbers: List) -> int:
	return numbers[0] + numbers[1]


def calc_minus(numbers: List) -> int:
	return numbers[0] - numbers[1]


def calc_multiplication(numbers: List) -> int:
	return numbers[0] * numbers[1]


def calc_division(numbers: List) -> Any:
	if numbers[1] != 0:
		return numbers[0] / numbers[1]


while True:
	menu_calc: str = input('\n1. Сумма \n2. Вычитание \n3. Умножение \n4. Деление\n5. Exit\n\nВведите действие: ')

	if menu_calc == '1':
		result_calc(calc_plus(introduction_numerals()))
	elif menu_calc == '2':
		result_calc(calc_minus(introduction_numerals()))
	elif menu_calc == '3':
		result_calc(calc_multiplication(introduction_numerals()))
	elif menu_calc == '4':
		result_calc(calc_division(introduction_numerals()))
	elif menu_calc == '5':
		break
