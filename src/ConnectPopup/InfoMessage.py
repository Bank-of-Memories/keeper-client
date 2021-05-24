from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from core.Component import Component

class InfoMessage(Component):
	def __init__(self, parent = None):
		super(InfoMessage, self).__init__(parent)

		self.basedLayout = QVBoxLayout()
		self.basedLayout.setSpacing(0)
		self.basedLayout.setContentsMargins(0, 0, 0, 0)
		self.basedLayout.setAlignment(Qt.AlignLeft | Qt.AlignHCenter)

		self.label = QLabel("Please note that you need to pay a deposit of $35 to\nstart the lease. It will be returned after the trial period\nof 30 days")
		self.label.setObjectName("cp-info-message-label")
		self.label.setAlignment(Qt.AlignLeft)

		self.basedLayout.addWidget(self.label)

		self.setLayout(self.basedLayout)