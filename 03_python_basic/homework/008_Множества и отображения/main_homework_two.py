# Создайте программу, которая эмулирует работу сервиса по сокращению ссылок. Должна быть реализована
# возможность ввода изначальной ссылки и короткого названия и получения изначальной ссылки по её названию.
# https://ua.korrespondent.net/sport/football/4484066-zinchenko-zatsikavyv-vest-khem-ta-arsenal


if __name__ == '__main__':
	link_dict = {}

	link_menu = [['1. Создать ссылку\n2. Найти ссылу\n3. Выход\n\nВведите желаемое: ']]

	while True:
		temp_menu = int(input(link_menu[0][0]))

		if temp_menu == 1:
			temp_link = input('\nlink: ')
			temp_name = input('link name: ')
			print(f'Ссылка внесена в базу под именем - {temp_name}', end='\n\n')

			link_dict.update({temp_name: temp_link})
		elif temp_menu == 2:
			temp_name = input('\nlink name: ')

			print(f'ваша ссылка - {link_dict.get(temp_name, "В базе нет такой ссылки!")}', end='\n\n')
		elif temp_menu == 3:
			break
