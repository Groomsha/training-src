# Реализуйте цикл, который будет перебирать все значения итерабельного объекта iterable.

if __name__ == '__main__':
	homework = 'Реализуйте цикл, который будет перебирать все значения итерабельного объекта iterable'
	iterable = iter(homework)

	while True:
		try:
			print(next(iterable))
		except StopIteration:
			break
