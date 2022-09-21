class ButtonsNumbers:
	def __init__(self, window) -> None:
		self.main_window = window

		self.main_window.ui_main_window.button_0.clicked.connect(self.button_zero)
		self.main_window.ui_main_window.button_1.clicked.connect(self.button_one)
		self.main_window.ui_main_window.button_2.clicked.connect(self.button_two)
		self.main_window.ui_main_window.button_3.clicked.connect(self.button_tree)
		self.main_window.ui_main_window.button_4.clicked.connect(self.button_four)
		self.main_window.ui_main_window.button_5.clicked.connect(self.button_five)
		self.main_window.ui_main_window.button_6.clicked.connect(self.button_six)
		self.main_window.ui_main_window.button_7.clicked.connect(self.button_seven)
		self.main_window.ui_main_window.button_8.clicked.connect(self.button_eight)
		self.main_window.ui_main_window.button_9.clicked.connect(self.button_nine)

	def button_zero(self) -> None:
		self.main_window.setting_values(0)

	def button_one(self) -> None:
		self.main_window.setting_values(1)

	def button_two(self) -> None:
		self.main_window.setting_values(2)

	def button_tree(self) -> None:
		self.main_window.setting_values(3)

	def button_four(self) -> None:
		self.main_window.setting_values(4)

	def button_five(self) -> None:
		self.main_window.setting_values(5)

	def button_six(self) -> None:
		self.main_window.setting_values(6)

	def button_seven(self) -> None:
		self.main_window.setting_values(7)

	def button_eight(self) -> None:
		self.main_window.setting_values(8)

	def button_nine(self) -> None:
		self.main_window.setting_values(9)


class ButtonsCalculations:
	def __init__(self, window) -> None:
		self.main_window = window

		self.main_window.ui_main_window.button_plus.clicked.connect(self.button_plus)
		self.main_window.ui_main_window.button_minus.clicked.connect(self.button_minus)
		self.main_window.ui_main_window.button_multiply.clicked.connect(self.button_multiply)
		self.main_window.ui_main_window.button_share.clicked.connect(self.button_share)
		self.main_window.ui_main_window.button_percent.clicked.connect(self.button_percent)
		self.main_window.ui_main_window.button_sin.clicked.connect(self.button_sin)
		self.main_window.ui_main_window.button_cos.clicked.connect(self.button_cos)
		self.main_window.ui_main_window.button_tan.clicked.connect(self.button_tan)

	def button_plus(self) -> None:
		self.main_window.setting_values('+')

	def button_minus(self) -> None:
		self.main_window.setting_values('-')

	def button_multiply(self) -> None:
		self.main_window.setting_values('*')

	def button_share(self) -> None:
		self.main_window.setting_values('/')

	def button_percent(self) -> None:
		self.main_window.setting_values('%')

	def button_sin(self) -> None:
		self.main_window.setting_values('sin')

	def button_cos(self) -> None:
		self.main_window.setting_values('cos')

	def button_tan(self) -> None:
		self.main_window.setting_values('tan')


class ButtonsAction:
	def __init__(self, window) -> None:
		self.main_window = window

		self.main_window.ui_main_window.button_res.clicked.connect(self.button_res)
		self.main_window.ui_main_window.button_del.clicked.connect(self.button_del)

	def button_res(self) -> None:
		self.main_window.action_result('=')

	def button_del(self) -> None:
		self.main_window.action_result('c')


class ButtonsCalculator:
	def __init__(self, window) -> None:
		self.action = ButtonsAction(window)
		self.numbers = ButtonsNumbers(window)
		self.calculations = ButtonsCalculations(window)
