# Создайте программу, которая состоит из функции, которая принимает три числа
# и возвращает их среднее арифметическое, и главного цикла, спрашивающего у
# пользователя числа и вычисляющего их средние значения при помощи созданной функции.


def return_average(numb_a: int, numb_b: int, numb_c: int) -> float:
	return (numb_a + numb_b + numb_c) / 3


while True:
	menu: str = input('\n1. Вычесление среднего арифметического\n2. Exit\n\nСделайте выбор: ')

	if menu == '1':
		number_one: int = int(input('\nВведите первое числительное: '))
		number_two: int = int(input('Введите второе числительное: '))
		number_tree: int = int(input('Введите третье числительное: '))
	else:
		break

	result: float = return_average(number_one, number_two, number_tree)
	print(f'\nСреднее арифметическое введенных значений равно: {result}')
	print('*' * 55)
