from PySide6.QtWidgets import QPushButton, QWidget, QGridLayout, QDialog, QSizePolicy, QLineEdit, QLabel, QFormLayout, QHBoxLayout, QVBoxLayout, \
	QGroupBox
from PySide6.QtGui import QFont


class CustomButton(QPushButton):
	def __init__(self, parent=None):
		super().__init__(parent)
		font = QFont("Helvetia", 13)
		font.setBold(True)
		self.setFont(font)


class CustomLineEdit(QLineEdit):
	def __init__(self, parent=None):
		super().__init__(parent)
		font = QFont("Helvetia", 13)
		font.setBold(True)
		self.setFont(font)


class CalculatorMain(QWidget):
	def __init__(self):
		super().__init__()

		with open("style.qss", 'r') as f:
			self.setStyleSheet(f.read())

		self.expression = CustomLineEdit()

		self.buttons_operation = [CustomButton(str(operator_)) for operator_ in ["+", "-", "*", "/"]]
		self.buttons_number = []

		layout = QVBoxLayout(self)
		number_layout = QGridLayout()

		backspace_button = CustomButton("<<")
		backspace_button.setProperty("class", "PinkRose")
		backspace_button.clicked.connect(self.backspace_button_clicked)

		for number in range(10):
			self.buttons_number.append(CustomButton(str(number)))

			self.buttons_number[number].setMinimumSize(50, 50)
			self.buttons_number[number].setProperty("class", 'Aqua')
			self.buttons_number[number].clicked.connect(lambda state, num=number: self.number_button_clicked(num))

			# row = (9 - number) // 3
			# col = (9 - number) % 3
			row = (9 - number) // 3
			col = (2 + number) % 3
			print(f"number: {number}, row: {row}, col: {col}")

			number_layout.addWidget(self.buttons_number[number], row, col)

		for i in self.buttons_operation:
			i.setProperty("class", 'Sunflower')
			i.clicked.connect(lambda state, operation=i.text(): self.operation_button_clicked(operation))
			layout.addWidget(i)

		layout.addWidget(self.expression)
		layout.addWidget(backspace_button)
		layout.addLayout(number_layout, 3)

		self.show()

	def number_button_clicked(self, number):
		# print(f"{number}")
		expression = self.expression.text()
		expression += str(number)
		self.expression.setText(expression)

	def operation_button_clicked(self, operator_):
		# print(f"{operator_}")
		if self.expression.text() == "":
			return
		else:
			expression = self.expression.text()
			expression += str(operator_)
			self.expression.setText(expression)

	def backspace_button_clicked(self):
		expression = self.expression.text()
		expression = expression[:-1]
		self.expression.setText(expression)
