from PyQt5 import QtGui


class ResScreenCalculations:
	def __init__(self, ui) -> None:
		self.ui_main_window = ui

	def screen_upgrade(self, text: str):
		if len(text) <= 8:
			self.ui_main_window.label_number.setFont(self.font_size_screen(len(text)))
			self.ui_main_window.label_number.setText(text)
		else:
			self.ui_main_window.label_number.setFont(self.font_size_screen(5))
			self.ui_main_window.label_number.setText('Error')

	def font_size_screen(self, size: int) -> QtGui:
		default_size: int = 0

		if size <= 5:
			default_size = 70
		elif size >= 6:
			default_size = 50
		elif size >= 7:
			default_size = 30
		elif size >= 8:
			default_size = 20

		font = QtGui.QFont()
		font.setFamily("Yu Gothic UI Semilight")
		font.setPointSize(default_size)
		font.setBold(False)
		font.setWeight(50)
		font.setKerning(True)
		font.setStyleStrategy(QtGui.QFont.PreferDefault)

		return font
