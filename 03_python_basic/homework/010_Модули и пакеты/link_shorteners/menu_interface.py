class MenuInterface:
	def __init__(self) -> None:
		self.link_menu = [['1. Создать ссылку\n2. Найти ссылу\n3. Выход\n\nВведите желаемое: ']]

	def temp_menu(self):
		return int(input(self.link_menu[0][0]))