from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from core.FramedComponent import FramedComponent

class ConnectStatusComponent(FramedComponent):
	def __init__(self, parent = None):
		super(ConnectStatusComponent, self).__init__(parent)
		self.setObjectName("connect-status-component")
		self.basedLayout = QHBoxLayout()
		self.basedLayout.setSpacing(0)
		self.basedLayout.setContentsMargins(0, 0, 0, 0)
		self.basedLayout.setAlignment(Qt.AlignLeft)

		self.icon = QLabel()
		self.icon.setObjectName("status-icon")
		self.icon.setAlignment(Qt.AlignVCenter)

		self.label = QLabel("You haven’t been connected to the data transmission system yet")
		self.label.setObjectName("connect-status-label")
		self.label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

		# self.connect_popup = ConnectPopup()

		self.button = QPushButton("Connect to Bank")
		self.button.setObjectName("connect-btn")
		self.button.clicked.connect(self.openPopup)

		self.basedLayout.addWidget(self.icon)
		self.basedLayout.addWidget(self.label)
		self.basedLayout.addStretch()
		self.basedLayout.addWidget(self.button)
		# self.basedLayout.addWidget(self.connect_popup)

		self.frame.setLayout(self.basedLayout)

	def openPopup(self):
		popup_is_open = self._parent.store.connectPopupOpen
		popup_is_open = not popup_is_open

		if popup_is_open:
			self._parent._foreground.show()
			self._parent.connect_popup.show()

		print("Open!")