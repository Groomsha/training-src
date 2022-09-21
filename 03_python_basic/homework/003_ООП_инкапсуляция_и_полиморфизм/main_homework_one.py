# Создайте класс, описывающий автомобиль. Какие атрибуты и методы должны быть полностью инкапсулированы?
# Доступ к таким атрибутам и изменение данных реализуйте через специальные методы (get, set).


class Car:
	def __init__(self, price: int) -> None:
		self.price: int = price

		self.__engine_displacement: float = 2.6
		self.__suspension: str = "4x4"

	def car_info(self) -> None:
		print(f'Обьем двигателя: {self.engine}. Формула подвески: {self.suspension}. Цена машины: {self.price}.')

	@property
	def engine(self):
		return self.__engine_displacement

	@engine.setter
	def engine(self, number: int):
		self.__engine_displacement = number

	@property
	def suspension(self):
		return self.__suspension

	@suspension.setter
	def suspension(self, susp: str):
		self.__suspension = susp


if __name__ == '__main__':
	my_car = Car(2500)
	my_car.car_info()
	my_car.engine = 3.0
	my_car.car_info()
