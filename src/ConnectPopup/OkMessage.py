from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout
from core.Component import Component

class OkMessage(Component):
	def __init__(self, parent = None):
		super(OkMessage, self).__init__(parent)

		self.mainLayout = QVBoxLayout()
		self.mainLayout.setSpacing(0)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)
		self.mainLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

		self.title = QLabel("You have been successfully connected to the\nBank of Memories System")
		self.title.setObjectName("ok-message-title")
		self.title.setAlignment(Qt.AlignHCenter)

		self.image = QLabel()
		pixmap = QPixmap("static/User_profile_intro.png")
		pixmap.scaledToHeight(238)
		self.image.setMinimumWidth(368)
		self.image.setMinimumHeight(218)
		self.image.setPixmap(pixmap)
		# self.image.setObjectName("ok-message-image")
		# self.image.setFixedHeight(360)

		self.mainLayout.addWidget(self.title)
		self.mainLayout.addWidget(self.image)
		# self.mainLayout.addStretch(1)

		self.setLayout(self.mainLayout)