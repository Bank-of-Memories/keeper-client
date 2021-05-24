from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel
from core.Component import Component

class Title(Component):
	def __init__(self, parent = None):
		super(Title, self).__init__(parent)
		self.setObjectName("connect-popup-title")

		self.basedLayout = QVBoxLayout()
		self.basedLayout.setSpacing(0)
		self.basedLayout.setContentsMargins(0, 0, 0, 0)
		self.basedLayout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

		self.hLayout = QHBoxLayout()
		self.hLayout.setSpacing(0)
		self.hLayout.setContentsMargins(0, 0, 0, 0)
		self.hLayout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

		self.label = QLabel("Connect to Bank")
		self.label.setObjectName("connect-popup-label")
		self.label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

		self.close_button = QLabel()
		self.close_button.mouseReleaseEvent = self.closePopup

		self.close_button.setFixedWidth(232)

		self.close_button.setObjectName("connect-popup-close-button")
		self.close_button.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

		self.pseudo_border = QLabel()
		self.pseudo_border.setObjectName("cp-item-pseudo-border")
		self.pseudo_border.setAlignment(Qt.AlignLeft | Qt.AlignBottom)

		self.hLayout.addWidget(self.label)
		self.hLayout.addWidget(self.close_button)

		self.basedLayout.addLayout(self.hLayout)

		self.basedLayout.addWidget(self.pseudo_border)

		self.setLayout(self.basedLayout)

	def closePopup(self, event):
		self._parent.hide()