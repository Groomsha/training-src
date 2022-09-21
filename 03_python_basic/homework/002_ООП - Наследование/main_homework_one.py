# Создайте класс Editor, который содержит методы view_document и edit_document. Пусть метод edit_document
# выводит на экран информацию о том, что редактирование документов недоступно для бесплатной версии.
# Создайте подкласс ProEditor, в котором данный метод будет переопределён. Введите с клавиатуры лицензионный
# ключ и, если он корректный, создайте экземпляр класса ProEditor, иначе Editor.
# Вызовите методы просмотра и редактирования документов.


class Editor:
	def view_document(self) -> None:
		pass

	def edit_document(self) -> None:
		print('\nредактирование документов недоступно для бесплатной версии')
		print('*'*60)


class ProEditor(Editor):
	def edit_document(self) -> None:
		print('\nредактирование документов доступно')
		print('*'*40)


if __name__ in '__main__':
	editor = None

	while True:
		print(f'\nлицензионный ключ: LTXT\n')

		editor_check = str(input('Введите Free для обычной версий.\nВведите лицензионный ключ для Pro.\nИли Exit\n->'))

		if editor_check.upper() == 'LTXT':
			editor = ProEditor().edit_document()
		elif editor_check.lower() == 'free':
			editor = Editor().edit_document()
		elif editor_check.lower() == 'exit':
			break
