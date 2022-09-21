import sys

from PyQt5.QtWidgets import QApplication
from main_window_app import MainWindowApp


if __name__ == '__main__':
	app = QApplication(sys.argv)

	qt_main = MainWindowApp()
	qt_main.show()

	sys.exit(app.exec_())
