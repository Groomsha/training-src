import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets, Qt


class PyQT5EventInfo(QtWidgets.QWidget):
	def __init__(self, parent=None) -> None:
		QtWidgets.QWidget.__init__(self, parent)

	def keyPressEvent(self, e):
		if e.key() == Qt.Qt.Key_E:
			print(e.key())

	def mousePressEvent(self, event):
		print('Щелчок мышью. -> mousePressEvent')

	def event(self, event: Qt.QEvent) -> bool:
		if event.type() == Qt.QEvent.KeyPress:
			print("Нажата клавиша на клавиатуре")
			print("Код:", event.key(), ", текст:", event.text())
		elif event.type() == Qt.QEvent.Close:
			print("Окно закрыто")
		elif event.type() == Qt.QEvent.MouseButtonPress:
			print("Щелчок мышью. Координаты:", event.x(), event.y())
		return QtWidgets.QWidget.event(self, event)


if __name__ == '__main__':
	app = QApplication(sys.argv)

	qt_main = PyQT5EventInfo()
	qt_main.show()

	sys.exit(app.exec_())
