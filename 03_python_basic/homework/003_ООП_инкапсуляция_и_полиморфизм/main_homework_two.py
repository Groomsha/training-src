# Создайте 2 класса – языка, например, английский и испанский. У обоих классов должен быть метод greeting().
# Оба создают разные приветствия. Создайте два соответствующих объекта из двух классов выше и вызовите действия
# этих двух объектов в одной функции (функция hello_friend).


class English:
	@staticmethod
	def greeting() -> None:
		print('Glory to Ukraine. Glory to heroes!')


class Spanish:
	@staticmethod
	def greeting() -> None:
		print('Gloria a Ucrania. ¡Gloria a los héroes!')


if __name__ == '__main__':
	def hello_friend():
		eng_speak.greeting()
		spa_speak.greeting()

	eng_speak = English()
	spa_speak = Spanish()
	hello_friend()
