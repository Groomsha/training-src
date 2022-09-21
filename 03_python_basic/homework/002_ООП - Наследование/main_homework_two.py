# Опишите классы графического объекта, прямоугольника и объекта, который может обрабатывать нажатия мыши.
# Опишите класс кнопки. Создайте объект кнопки и обычного прямоугольника. Вызовите метод нажатия на кнопку.

from typing import List


class Rectangle:
	def __init__(self) -> None:
		pass

	def great_rectangle(self, height: int, width: int) -> None:
		for h in range(0, height):
			print('', end='\n')

			for w in range(0, width):
				print('+', end='')

		print('\n')


class NewObject:
	def __init__(self) -> None:
		self.mouse_x: float = 0
		self.mouse_y: float = 0

	def push(self, mouse_touch: List):
		self.mouse_x = mouse_touch[0]
		self.mouse_y = mouse_touch[1]

		print(f'Нажатие по кнопке в координатах x:{self.mouse_x} и y:{self.mouse_y} ')


class Button(Rectangle, NewObject):
	def __init__(self, name: str) -> None:
		super(Rectangle, self).__init__()

		self.name = name
		self.great_button()

	def great_button(self) -> None:
		self.great_rectangle(3, 10)
		print(f'Created -> {self.name}', end='\n')


if __name__ == '__main__':
	rectangle = Rectangle()
	rectangle.great_rectangle(3, 5)

	button = Button('New button')
	button.push([23.44, 55.72])
