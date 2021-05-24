from PyQt5.QtWidgets import QHBoxLayout, QFrame, QLabel
from PyQt5.QtCore import Qt
from core.Component import Component

class StopLeaseButton(Component):
	def __init__(self, parent = None):
		super(StopLeaseButton, self).__init__(parent)
		self.mainLayout = QHBoxLayout()
		self.mainLayout.setSpacing(0)
		self.mainLayout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)

		self.button = QLabel()
		self.button.setObjectName("stop-lease-button")

		self.title = QLabel("Stop")
		self.title.setObjectName("stop-lease-button-title")

		self.mainLayout.addWidget(self.button)
		self.mainLayout.addWidget(self.title)

		self.setLayout(self.mainLayout)

	def mousePressEvent(self, evt):
		print("StopLeaseButton is pressed")

class LeaseControlButton(Component):
	def __init__(self, parent = None):
		super(LeaseControlButton, self).__init__(parent)

		self.pause_styles = "min-width: 24px; min-height: 24px; background-image: url(\"static/Pause.png\"); background-attachment: local; background-repeat: no-repeat; margin-left: 16px;"
		self.play_styles = "min-width: 24px; min-height: 24px; background-image: url(\"static/play.png\"); background-attachment: local; background-repeat: no-repeat; margin-left: 16px;"

		self.is_leasing = False

		self.mainLayout = QHBoxLayout()
		self.mainLayout.setSpacing(0)
		self.mainLayout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)

		self.button = QLabel()
		self.button.setObjectName("pause-lease-button")
		self.button.mousePressEvent = self._mousePressEvent

		self.title = QLabel("Pause")
		self.title.setObjectName("pause-lease-button-title")

		self.mainLayout.addWidget(self.button)
		self.mainLayout.addWidget(self.title)

		self.setLayout(self.mainLayout)

	def updateStyles(self):
		if self.is_leasing:
			self.button.setStyleSheet(self.play_styles)
		else:
			self.button.setStyleSheet(self.pause_styles)

	def _mousePressEvent(self, evt):
		self.is_leasing = not self.is_leasing
		print("PauseLeaseButton is pressed")

		# TODO: Start timer?

		self.updateStyles()

class ReleaseMoreButton(QFrame):
	def __init__(self, parent = None):
		super(ReleaseMoreButton, self).__init__(parent)
		self.setObjectName("release-button")

		self.mainLayout = QHBoxLayout()
		self.mainLayout.setSpacing(0)
		self.mainLayout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)

		self.title = QLabel("Release more storage")
		self.title.setObjectName("release-button-title")

		self.mainLayout.addWidget(self.title)

		self.setLayout(self.mainLayout)

	def mousePressEvent(self, evt):
		print("ReleaseMoreButton is pressed")

class LeaseControlls(Component):
	def __init__(self, parent = None):
		super(LeaseControlls, self).__init__(parent)
		self.mainLayout = QHBoxLayout()
		self.mainLayout.setSpacing(0)
		self.mainLayout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)

		self.stop_button = StopLeaseButton()
		self.pause_button = LeaseControlButton()
		self.more_button = ReleaseMoreButton()

		self.mainLayout.addWidget(self.stop_button)
		self.mainLayout.addWidget(self.pause_button)
		self.mainLayout.addWidget(self.more_button)

		self.setLayout(self.mainLayout)