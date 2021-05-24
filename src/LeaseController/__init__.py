from PyQt5.QtWidgets import QFrame, QHBoxLayout
from PyQt5.QtCore import Qt

from src.LeaseController.LeaseTimeWidget import LeaseTimeWidget
from src.LeaseController.LeaseControlls import LeaseControlls

class LeaseController(QFrame):
	def __init__(self, parent = None):
		super(LeaseController, self).__init__(parent)
		self.setObjectName("lease-controller-body")
		self.mainLayout = QHBoxLayout()
		self.mainLayout.setSpacing(0)
		self.mainLayout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)

		self.lease_time = LeaseTimeWidget()
		self.lease_controlls = LeaseControlls()

		self.mainLayout.addWidget(self.lease_time)
		self.mainLayout.addWidget(self.lease_controlls)

		self.setLayout(self.mainLayout)