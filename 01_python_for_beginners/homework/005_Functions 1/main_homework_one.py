# Создайте функцию, которая выводит приветствие для пользователя с заданным именем.
# Если имя не указано, она должна выводить приветствие для пользователя с Вашим именем.


def print_name(name) -> None:
	if name.title() == '':
		print('С возвращением Ihor!')
	else:
		print(f'Приятно познакомится {name.title()}!')


if __name__ == '__main__':
	current_name: str = input('Введите ваше имя: ')
	print_name(current_name)
