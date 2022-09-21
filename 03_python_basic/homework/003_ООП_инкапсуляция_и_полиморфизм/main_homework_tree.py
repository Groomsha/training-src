# Используя ссылки в конце данного урока, ознакомьтесь с таким средством инкапсуляции как свойства.
# Ознакомьтесь с декоратором property в Python. Создайте класс, описывающий температуру и позволяющий
# задавать и получать температуру по шкале Цельсия и Фаренгейта, причём данные могут быть заданы в одной шкале,
# а получены в другой.


class Temperature:
	def __init__(self) -> None:
		self.__celsius: float = 19.0
		self.__fahrenheit: float = 66.2

	def current_temperature(self) -> None:
		print(f'Текущая температура за бортом {self.celsius} градусов по Цельсию.')
		print(f'Текущая температура за бортом {self.fahrenheit} градусов по Фаренгейта.')

	@property
	def celsius(self):
		return self.__celsius

	@celsius.setter
	def celsius(self, number: int):
		self.__celsius = number
		self.__fahrenheit = round(((number*9)/5)+32, 1)

	@property
	def fahrenheit(self):
		return self.__fahrenheit

	@fahrenheit.setter
	def fahrenheit(self, number: int):
		self.__fahrenheit = number
		self.__celsius = round(((number-32)*5)/9, 1)


if __name__ == '__main__':
	temperature = Temperature()
	temperature.current_temperature()
	print('='*60, end='\n\n')

	temperature.celsius = 15
	temperature.current_temperature()
	print('='*60, end='\n\n')

	temperature.fahrenheit = 212
	temperature.current_temperature()
