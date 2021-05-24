from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel
from core.Component import Component

class Footer(Component):
	def __init__(self, parent = None):
		super(Footer, self).__init__(parent)
		self.setObjectName("connect-popup-footer")

		self.basedLayout = QVBoxLayout()
		self.basedLayout.setSpacing(0)
		self.basedLayout.setContentsMargins(0, 0, 0, 0)
		self.basedLayout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

		self.hLayout = QHBoxLayout()
		self.hLayout.setSpacing(0)
		self.hLayout.setContentsMargins(0, 0, 0, 0)
		self.hLayout.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

		self.pseudo_border = QLabel()
		self.pseudo_border.setObjectName("cp-item-pseudo-border")
		self.pseudo_border.setAlignment(Qt.AlignLeft | Qt.AlignTop)

		self.cancel_button = QLabel("cancel")
		self.cancel_button.mousePressEvent = self.closePopup
		self.cancel_button.setObjectName("cp-cancel-button")
		self.cancel_button.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
		self.start_button = QLabel("start")
		self.start_button.setObjectName("cp-start-button")
		self.start_button.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
		self.start_button.mousePressEvent = self.startLease

		self.basedLayout.addWidget(self.pseudo_border)

		self.hLayout.addWidget(self.cancel_button)
		self.hLayout.addWidget(self.start_button)

		self.basedLayout.addLayout(self.hLayout)

		self.setLayout(self.basedLayout)

	def startLease(self, evt):
		self._parent._parent.page2.connect_status_component.hide()
		self._parent._parent.page2.lease_controller.show()
		self._parent.lease_settings_component.hide()
		self._parent.footer.hide()
		self._parent.ok_message.show()

	def closePopup(self, evt):
		self._parent.title.closePopup(evt)