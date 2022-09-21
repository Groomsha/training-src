# Напишите программу, которая вводит с клавиатуры текст и выводит отсортированные по алфавиту слова данного текста.


if __name__ == '__main__':
	input_text = input('text: ')

	sorted_text = sorted(input_text.lower().split())
	print(sorted_text)
