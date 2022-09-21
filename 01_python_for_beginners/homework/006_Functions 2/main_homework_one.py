# Создайте программу, которая проверяет, является ли палиндромом введённая фраза.

def text_reversed(text: str) -> str:
	text_join: str = ''

	for i in reversed(text):
		text_join += ''.join(i)

	return text_join


if __name__ == '__main__':
	while True:
		text_input: str = input('Для завершения введите exit \nВведите фразу для проверки на "Палиндром": ')
		print('='*45, end='\n\n')

		if text_input == 'exit':
			break

		text_pol: str = text_reversed(text_input)

		if text_pol == text_input:
			print(f'Это истиный "Палиндром: {text_input} = {text_pol}\n')
		else:
			print(f'Это слово не является "Палиндромом: {text_input} != {text_pol}\n')
