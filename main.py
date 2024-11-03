import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout
from calculator_ui import CalculatorMain


class Test(QWidget):
	def __init__(self):
		super().__init__()
		button1 = QPushButton("1")
		button2 = QPushButton("2")

		layout = QGridLayout()
		layout.addWidget(button1)
		layout.addWidget(button2)

		self.setLayout(layout)

		self.show()


def main():
	app = QApplication(sys.argv)

	window = QMainWindow()
	# window.setCentralWidget(Test())
	window.setCentralWidget(CalculatorMain())

	window.show()
	sys.exit(app.exec())


if __name__ == "__main__":
	main()
