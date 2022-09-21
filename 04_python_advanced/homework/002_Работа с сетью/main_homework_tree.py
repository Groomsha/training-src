# Изучите более подробно и попробуйте возможности настройки, pull-а соединений и его режимов.
# Используя утилиту ab протестируйте ваши наработки (https://ru.wikipedia.org/wiki/ApacheBench).

class WorkerTypeException(Exception):
	def __init__(self) -> None:
		pass

	def __str__(self) -> str:
		return f"Недопустимое значение:"


class Worker:
	def __init__(self, first_name: str, last_name: str, department: str, year: int) -> None:
		if type(first_name) == str and type(last_name) == str and type(department) == str:
			self.__first_name: str = first_name
			self.__last_name: str = last_name
			self.__department: str = department
		else:
			raise WorkerTypeException

		if type(year) == int:
			self.__year: int = year
		else:
			raise WorkerTypeException

	@property
	def get_year(self) -> int:
		return self.__year

	def info(self) -> str:
		return f'First name {self.__first_name}, Last_name {self.__last_name}, Department{self.__department},' \
			   f' Year of admission {self.__year}'


if __name__ == '__main__':
	worker_one = Worker('A', 'Y', 'One', 1939)
	worker_two = Worker('S', 'G', 'Two', 1954)
	worker_tree = Worker('T', 'O', 'Tree', 1954)

	worker = [worker_one, worker_two, worker_tree]

	key = int(input('Введите год прийома на работу: '))
	for w in worker:
		if w.get_year == key:
			print(w.info())
