# Создайте иерархию классов транспортных средств. В общем классе опишите общие для всех
# транспортных средств поля, в наследниках – специфичные для них. Создайте несколько экземпляров.
# Выведите информацию о каждом транспортном средстве.


class Cars:
	def __init__(self, make: str, type: str, year: int, price: int) -> None:
		self.make: str = make
		self.type: str = type
		self.year: int = year
		self.price: int = price

	def get_info(self) -> str:
		return f'Модель машины: {self.make}. Тип кузова: {self.type}. Год выпуска: {self.year}. Цена: {self.price}$.'


class Honda(Cars):
	def __init__(self, make: str, type: str, year: int, price: int, gas: int) -> None:
		super().__init__(make, type, year, price)

		self.gas: int = gas

	def get_info(self) -> str:
		info: str = super(Honda, self).get_info()
		info += f' Обьем бензобака {self.gas}.'
		return info


class Tesla(Cars):
	def __init__(self, make: str, type: str, year: int, price: int, battery: int) -> None:
		super().__init__(make, type, year, price)

		self.battery: int = battery

	def get_info(self) -> str:
		info: str = super(Tesla, self).get_info()
		info += f' Обьем батарей {self.battery}.'
		return info


if __name__ == '__main__':
	accord = Honda('Honda Accord', 'Седан', 2010, 6900, 60)
	model3 = Tesla('Tesla Model 3', 'Седан', 2019, 30000, 900)

	print(accord.get_info(), end='\n')
	print((model3.get_info()))
