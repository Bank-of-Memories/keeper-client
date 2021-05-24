from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QFrame

class ComboBox(QFrame):
	def __init__(self, values, parent = None):
		super(ComboBox, self).__init__(parent)
		self.setObjectName("combo-box")

		self.options_open = False

		self.values = values
		self.selectedIndex = 0

		self.mainLayout = QHBoxLayout()
		self.mainLayout.setSpacing(0)
		self.mainLayout.setAlignment(Qt.AlignLeft | Qt.AlignHCenter)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)

		self.current_value = QLabel(self.getCurrentValue())
		self.current_value.setObjectName("combo-box-value")

		self.open_button = QLabel()
		self.open_button.setObjectName("combo-box-open-button")
		self.open_button.setAlignment(Qt.AlignRight)


		self.mainLayout.addWidget(self.current_value)
		self.mainLayout.addWidget(self.open_button)

		self.setLayout(self.mainLayout)

	def getCurrentValue(self):
		return self.values[self.selectedIndex]