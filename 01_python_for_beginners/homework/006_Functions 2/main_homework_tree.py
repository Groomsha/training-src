# Напишите рекурсивную функцию, которая вычисляет сумму натуральных чисел, которые входят в заданный промежуток.
# Простая формула: сумма чисел от 1 до n = n * (n+1). Таким образом, сумма натуральных чисел от 1 до 100 равна 5050.


def natural_numbers(number: int) -> int:
	if number <= 1:
		return number
	else:
		return number + natural_numbers(number - 1)


if __name__ == '__main__':
	number_input: int = int(input('Введите число для вычисляет сумму натуральных чисел: '))
	print('*' * 55)

	print(f'\nСумму натуральных чисел равна: {natural_numbers(number_input)}')
