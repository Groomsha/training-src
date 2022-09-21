# Напишите скрипт, который создаёт текстовый файл и записывает в него 10000 случайных действительных чисел.
# Создайте ещё один скрипт, который читает числа из файла и выводит на экран их сумму.


def write_file():
	with open('temp.txt', 'w') as file:
		for n in range(1, 10001):
			file.writelines(str(n))
			file.writelines('\n')


def read_file():
	with open('temp.txt', 'r') as file:
		return [int(n) for n in file.read().split()]


if __name__ == '__main__':
	write_file()
	print(sum(read_file()))
