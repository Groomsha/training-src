# Создайте класс, описывающий книгу. Он должен содержать информацию об авторе,
# названии, годе издания и жанре. Создайте несколько разных книг.
# Определите для него операции проверки на равенство и неравенство, методы __repr__ и __str__.

from typing import Tuple


class Book:
	def __init__(self, author: str, title: str, city: str, genre: str) -> None:
		self.author: str = author
		self.title: str = title
		self.city: str = city
		self.genre: str = genre

	def __str__(self):
		return f'Книга за авторством: {self.author}, написана в городе: {self.city}, '\
			   f'жанр книги: {self.genre}, назание книги: {self.title}'

	def __repr__(self):
		return self.author


class BookStore:
	def __init__(self) -> None:
		self.books: Tuple = (Book('Джон Р. Р. Толкин', 'London', '20x', 'Властелин колец'),
							 Book('Джейн Остин', 'London', '20x', 'Гордость и предубеждение'),
							 Book('Филип Пулман', 'London', '20x', 'Тёмные начала'))

		counter: int = 0
		for book in self.books:
			if book.author == repr(self.books[counter]):
				print(f'{counter+1}. {book}')

			counter += 1


if __name__ in '__main__':
	book_store = BookStore()
