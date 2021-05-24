from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QLabel
from core.Component import Component

DAYS_LIMIT = 35

class LeaseTimeWidget(Component):
	def __init__(self, parent = None):
		super(LeaseTimeWidget, self).__init__(parent)
		self.setObjectName("lease-time-widget")
		self.mainLayout = QHBoxLayout()
		self.mainLayout.setSpacing(0)
		self.mainLayout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)

		self.title = QLabel("Lease time: ")
		self.value = QLabel("0 days")

		self.message = QLabel("%d days left to return your deposit" % DAYS_LIMIT)
		self.message.setObjectName("lease-time-message")

		self.mainLayout.addWidget(self.title)
		self.mainLayout.addWidget(self.value)
		self.mainLayout.addWidget(self.message)

		self.setLayout(self.mainLayout)