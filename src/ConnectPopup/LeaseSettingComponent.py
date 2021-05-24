from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QComboBox
from core.Component import Component

from src.ConnectPopup.InfoMessage import InfoMessage
from src.ConnectPopup.SelectCapacityComponent import SelectCapacityComponent

class LeaseSettingComponent(Component):
	def __init__(self, parent = None):
		super(LeaseSettingComponent, self).__init__(parent)

		self.mainLayout = QVBoxLayout()
		self.mainLayout.setSpacing(0)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)
		self.mainLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

		self.info_message = InfoMessage()

		self.set_capacity_title = QLabel("Select the capacity of storage you want to allocate")
		self.set_capacity_title.setObjectName("set-capacity-title")
		self.set_capacity_title.setAlignment(Qt.AlignLeft)

		self.select_capacity_component = SelectCapacityComponent(parent=self._parent)

		self.set_lease_time_title = QLabel("Select the time you want to lease your data")
		self.set_lease_time_title.setObjectName("set-lease-time-title")
		self.set_lease_time_title.setAlignment(Qt.AlignLeft)

		# self.lease_time_value = ComboBox(["2 months", "3 months", "6 months",
		# 																	"1 year", "2 years", "5 years", "Unlimited lease"])
		self.lease_time_value = QComboBox()
		# self.lease_time_value.setFixedWidth(200)
		# self.lease_time_value.setFixedHeight(32)
		self.lease_time_value.setObjectName("lease-value-box")
		self.lease_time_value.addItem("2 months")
		self.lease_time_value.addItem("3 months")
		self.lease_time_value.addItem("6 months")
		self.lease_time_value.addItem("1 year")
		self.lease_time_value.addItem("2 years")
		self.lease_time_value.addItem("5 years")
		self.lease_time_value.addItem("Unlimited lease")

		self.mainLayout.addWidget(self.info_message)
		self.mainLayout.addWidget(self.set_capacity_title)
		self.mainLayout.addWidget(self.select_capacity_component)
		self.mainLayout.addWidget(self.set_lease_time_title)
		self.mainLayout.addWidget(self.lease_time_value)

		self.setLayout(self.mainLayout)