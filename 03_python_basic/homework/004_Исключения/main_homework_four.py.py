# Опишите свой класс исключения. Напишите функцию, которая будет выбрасывать данное исключение,
# если пользователь введёт определённое значение, и перехватите это исключение при вызове функции.

class YearException(Exception):
	def __init__(self) -> None:
		pass

	def __str__(self) -> str:
		return f"Недопустимое значение:"


class YouYear:
	def __init__(self, year: int) -> None:
		if year == 2022:
			self.__year: int = year
		else:
			raise YearException


if __name__ == '__main__':
	my_year = YouYear(2021)
