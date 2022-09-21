# Используя вложенные циклы и функции print(‘*’, end=’’), print(‘ ‘, end=’’)
# и print() выведите на экран прямоугольный треугольник.


triangle_size = 10
for star in range(0, triangle_size):
	print(' ', end='\n')

	for facet in range(0, star + 1):
			print('*', end='')
