# Создайте список и введите его значения. Найдите наибольший и наименьший элемент списка,
# а также сумму и среднее арифметическое его значений.

from typing import List


number: List = [2, 6, 22, 97, 55, 9, 42]


def print_res() -> None:
	print(f'Наибольший элемент в списке -> {max(number)}', end=f'\n{"*" * 35}\n')
	print(f'Наименьший элемент в списке -> {min(number)}', end=f'\n{"*" * 35}\n')
	print(f'Сумма элементов в списке -> {sum(number)}', end=f'\n{"*"*35}\n')
	print(f'Среднее арифметическое значений в списке -> {round(sum(number) / len(number), 2)}', end=f'\n{"*"*50}\n')


if __name__ == '__main__':
	print_res()
