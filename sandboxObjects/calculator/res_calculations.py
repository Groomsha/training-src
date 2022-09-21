from typing import List, Any
import math


class ResCalculations:
	def __init__(self, operants: List) -> None:
		self.operants: List = operants

	def mathematical_action(self) -> str:
		result: Any = ''

		if self.operants[2] != '':
			temp_one: int = int(self.operants[0])
			temp_two: int = int(self.operants[2])
		else:
			temp_one: int = int(self.operants[0])
			temp_two: int = 0

		if self.operants[1] == '+':
			result = temp_one + temp_two
		elif self.operants[1] == '-':
			result = temp_one - temp_two
		elif self.operants[1] == '*':
			result = temp_one * temp_two
		elif self.operants[1] == '/':
			if self.operants[2] != '0':
				result = float(temp_one) / float(temp_two)
			else:
				result = 'Error'
		elif self.operants[1] == '%':
			result = float(temp_one) % float(temp_two)
		elif self.operants[1] == 'sin':
			result = math.sin(float(temp_one))
		elif self.operants[1] == 'cos':
			result = math.cos(float(temp_one))
		elif self.operants[1] == 'tan':
			result = math.tan(float(temp_one))

		return str(round(result, 4))
