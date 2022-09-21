# Простым называется число, которое делится нацело только на единицу и само себя.
# Число 1 не считается простым. Напишите программу, которая находит все простые
# числа в заданном промежутке, выводит их на экран, а затем по требованию
# пользователя выводит их сумму либо произведение.

from typing import List


prime_list: List = []


def prime_numbers_res(value: int) -> None:
	global prime_list

	for numb_one in range(1, value + 1):
		for numb_two in range(2, numb_one):
			if numb_one % numb_two == 0:
				break
		else:
			prime_list.append(numb_one)


if __name__ == '__main__':
	while True:
		prime_number: int = int(input('\nВведите число для промежутка простых чисел: '))

		prime_numbers_res(prime_number)
		print(prime_list)

		menu: str = input('\n1. Сумма простых чисел \n2. Exit\n\nВведите действие: ')

		if menu == '1':
			print(f'\nСумма элементов в списке -> {sum(prime_list)}', end=f'\n{"*" * 35}\n')
		elif menu == '2':
			break
