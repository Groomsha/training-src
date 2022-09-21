# Создайте список целых чисел. Получите список квадратов нечётных чисел из этого списка.

import shelve


def work_to_db(*args, work: bool = True):
	with shelve.open('temp_db') as db:
		if work:
			db[args[0]] = args[1]
		else:
			return db.get(args[0], "В базе нет такой ссылки!")

if __name__ == '__main__':
	link_menu = [['1. Создать ссылку\n2. Найти ссылу\n3. Выход\n\nВведите желаемое: ']]

	while True:
		temp_menu = int(input(link_menu[0][0]))

		if temp_menu == 1:
			temp_link = input('\nlink: ')
			temp_name = input('link name: ')
			print(f'Ссылка внесена в базу под именем - {temp_name}', end='\n\n')

			work_to_db(temp_name, temp_link)
		elif temp_menu == 2:
			temp_name = input('\nlink name: ')

			print(f'ваша ссылка - {work_to_db(temp_name, work=False)}', end='\n\n')
		elif temp_menu == 3:
			break
