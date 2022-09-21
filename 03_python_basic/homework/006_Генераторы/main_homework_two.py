# Выведите из списка чисел список квадратов четных чисел. Используйте 2 варианта решения: генератор и цикл.

if __name__ == '__main__':
	list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

	list_res_gen = [x ** 2 for x in list_number if x % 2 == 0]
	print(list_res_gen)

	list_res_for = []
	for l in list_number:
		if l % 2 == 0:
			list_res_for.append(l ** 2)

	print(list_res_for)
