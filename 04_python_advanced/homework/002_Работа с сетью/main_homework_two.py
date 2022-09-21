# Создайте UNIX сокет, который принимает сообщение с двумя числами, разделенными запятой.
# Сервер должен конвертировать строковое сообщения в два числа и вычислять его сумму.
# После успешного вычисления возвращать ответ клиенту.

from typing import List, Tuple, Any


class Result:
	def __init__(self) -> None:
		pass

	@staticmethod
	def get_result(equation: Tuple) -> Any:
		op = equation[2]

		if '.' in equation[0] or '.' in equation[1]:
			a = float(equation[0])
			b = float(equation[1])
		else:
			a = int(equation[0])
			b = int(equation[1])

		try:
			res_dict = {
				'+': a+b,
				'-': a-b,
				'*': a*b,
				'/': a/b,
				'**': a**b,
			}
		except ZeroDivisionError:
			return 'Деление на "0" не допустимо!'

		return res_dict.get(op)


if __name__ == '__main__':
	operations: List = ['+', '-', '*', '/', '**']
	calc = Result()

	while True:
		print('Доступны такие операций вычисления: +, -, *, /, **\nДля выхода введите "q"', end='\n\n')
		op = input('Выберите операцию: ')

		if op in operations:
			a = input('Введите первое число: ')
			b = input('Введите второе число: ')
			print('\n', calc.get_result((a, b, op)), end='\n')

		if op.lower() == 'q':
			break
