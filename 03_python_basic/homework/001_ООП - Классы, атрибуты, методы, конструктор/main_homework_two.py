# Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов.
# Сделайте так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.


class Book:
	def __init__(self) -> None:
		self.title: str = 'Властелин колец'
		self.reviews: str = Reviews().review()

	def __str__(self):
		return self.reviews


class Reviews:
	def review(self) -> str:
		return 'Интересная книга'


if __name__ in '__main__':
	lord_of_the_rings = Book()
	print(lord_of_the_rings)
