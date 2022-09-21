# Создайте список, введите количество его элементов и сами значения, выведите эти значения на экран в обратном порядке.

from typing import List


numbers_list: List = []


def print_res(value: int) -> None:
	global numbers_list

	for number in reversed(range(value + 1)):
		numbers_list.append(number)

	print(f'Длина списка = {len(numbers_list)}')
	print(f'Значения списка с конца -> {numbers_list}')


if __name__ == '__main__':
	len_numbers: int = int(input('\nВведите длину списка (цифрами): '))
	print_res(len_numbers)
