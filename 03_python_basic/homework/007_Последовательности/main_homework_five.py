# Напишите программу, которая вводит с клавиатуры последовательность чисел и
# выводит её отсортированной в порядке возрастания.


if __name__ == '__main__':
	input_number = list(input('number: '))

	sorted_number = [int(n) for n in input_number]
	print(sorted(sorted_number))
