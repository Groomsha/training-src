# Пусть на каждую ступеньку лестницы можно стать с предыдущей или переступив через одну.
# Определите, сколькими способами можно подняться на заданную ступеньку.

from typing import List


def stairs(steps: int):
	return [(steps // 2), (steps // 4) + 1]


if __name__ == '__main__':
	number_step: int = int(input('Введите число задуманой ступеньки: '))
	print('*' * 40)

	step: List = stairs(number_step)
	print(f'\nс предыдущей {step[0]}, a переступив через одну {step[1]}')
