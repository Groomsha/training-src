# Напишите итератор, который возвращает элементы заданного списка в обратном порядке (аналог reversed).

if __name__ == '__main__':
	homework = 'Реализуйте цикл, который будет перебирать все значения итерабельного объекта iterable'
	iterable = iter(homework[::-1])

	while True:
		try:
			print(next(iterable))
		except StopIteration:
			break
