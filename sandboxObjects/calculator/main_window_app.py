from PyQt5 import QtWidgets

from ui_main_window import Ui_MainWindow
from buttons_calculator import ButtonsCalculator
from res_calculations import ResCalculations
from res_screen_calculations import ResScreenCalculations


class MainWindowApp(QtWidgets.QMainWindow):
	def __init__(self, parent=None) -> None:
		QtWidgets.QWidget.__init__(self, parent)

		self.operation: str = ''
		self.number_one: str = ''
		self.number_two: str = ''

		self.ui_main_window = Ui_MainWindow()
		self.ui_main_window.setupUi(self)

		self.buttons = ButtonsCalculator(self)
		self.screen = ResScreenCalculations(self.ui_main_window)

	def action_result(self, value: str) -> None:
		if value == '=':
			result = ResCalculations([self.number_one, self.operation, self.number_two])
			self.screen.screen_upgrade(result.mathematical_action())

		if value == 'c':
			self.screen.screen_upgrade('0')

		self.operation = ''
		self.number_one = ''
		self.number_two = ''

	def setting_values(self, values: str) -> None:
		if isinstance(values, int) and self.number_two == '' and self.operation == '':
			self.number_one += str(values)
			self.screen.screen_upgrade(self.number_one)
		elif isinstance(values, int) and self.operation != '':
			self.number_two += str(values)
			self.screen.screen_upgrade(self.number_two)
		elif isinstance(values, str) and values == 'sin' or values == 'cos' or values == 'tan':
			self.operation = values
			self.action_result('=')
		elif isinstance(values, str) and self.number_two == '':
			self.operation = values
