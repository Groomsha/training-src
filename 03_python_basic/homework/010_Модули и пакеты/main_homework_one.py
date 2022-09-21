# Перепишите домашнее задание предыдущего урока (сервис для сокращения ссылок) таким образом, чтобы у него была
# основная часть, которая отвечала бы за логику работы и предоставляла обобщённый интерфейс, и модуль представления,
# который отвечал бы за взаимодействие с пользователем. При замене последнего на другой, взаимодействующий с
# пользователем иным способом, программа должна продолжать корректно работать.

from link_shorteners.work_with_base import WorkWithBase
from link_shorteners.menu_interface import MenuInterface


if __name__ == '__main__':
	work = WorkWithBase()
	menu = MenuInterface()

	while True:
		temp_menu = menu.temp_menu()

		if temp_menu == 1:
			temp_link = input('\nlink: ')
			temp_name = input('link name: ')
			print(f'Ссылка внесена в базу под именем - {temp_name}', end='\n\n')

			work.work_to_db(temp_name, temp_link)
		elif temp_menu == 2:
			temp_name = input('\nlink name: ')

			print(f'ваша ссылка - {work.work_to_db(temp_name, work=False)}', end='\n\n')
		elif temp_menu == 3:
			break
