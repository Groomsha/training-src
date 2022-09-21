# Создайте словарь с ключами-строками и значениями-числами. Создайте функцию, которая принимает произвольное
# количество именованных параметров. Вызовите её с созданным словарём и явно указывая параметры.


if __name__ == '__main__':
	dict_temp = {
		"@context": "http://schema.org",
		"@type": "NewsArticle",
		"headline": "Зінченко зацікавив Вест Хем та Арсенал",
		"datePublished": "2022-06-06T11:57:00",
		"dateModified": "2022-06-06T11:57:00",
	}

	def temp_def(**kwargs):
		for key, val in kwargs.items():
			print(f'Ключ: {key} - Значение: {val}')

	temp_def(schema=dict_temp)
