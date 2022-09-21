# Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список автомобилей,
# доступных для продажи, и функцию продажи заданного автомобиля.

from typing import Tuple


class Car:
	def __init__(self, brand: str, volume: float) -> None:
		self.car_type: str = 'internal combustion engine'
		self.brand: str = brand
		self.volume: float = volume


class CarShowroom:
	def __init__(self) -> None:
		self.cars: Tuple = (Car('BMW', 2.0), Car('Mazda', 1.3), Car('Honda', 3.0))

	def car_info(self) -> None:
		counter: int = 0

		for car in self.cars:
			counter += 1
			print(f'{str(counter)}. Car name: {car.brand}, {car.car_type}, volume: {car.volume}', end='\n')

	def sale_car(self, number: int) -> None:
		print(f'\nCar name: {self.cars[number-1].brand}, {self.cars[number-1].car_type}, '
		f'volume: {self.cars[number-1].volume} -> ПРОДАНА ВАМ!')
		print('*'*80)


if __name__ in '__main__':
	showroom = CarShowroom()

	while True:
		showroom.car_info()

		check = int(input('\n1-3. Выберите доступную машину для покупки. 0. Покинуть салон :'))

		if check == 0:
			break
		elif check == 1 or check == 2 or check == 3:
			showroom.sale_car(check)
