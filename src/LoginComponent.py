import requests
import hashlib
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QLineEdit, QCheckBox, QLabel, QVBoxLayout, QHBoxLayout
from core.Component import Component
from constants import SIGN_IN_URL

class LoginComponent(Component):
	def __init__(self, parent = None):
		super(LoginComponent, self).__init__(parent)
		self.setObjectName("login-component")

		self.pageLayout = QHBoxLayout()
		self.pageLayout.setAlignment(Qt.AlignCenter)
		self.vPageLayout = QVBoxLayout()
		self.vPageLayout.setAlignment(Qt.AlignCenter)

		self.title = QLabel("Sign in to Bank of Memories")
		self.title.setObjectName("login-title")
		self.title.setAlignment(Qt.AlignCenter)

		self.username = QLineEdit()
		self.username.setAttribute(Qt.WA_MacShowFocusRect, 0)

		self.username.setObjectName("input-form")
		self.username.setAlignment(Qt.AlignLeft)

		self.username.setPlaceholderText("Email")

		self.password = QLineEdit()
		self.password.setAttribute(Qt.WA_MacShowFocusRect, 0)

		self.password.setObjectName("input-form")
		self.password.setEchoMode(QLineEdit.Password)
		self.password.setAlignment(Qt.AlignLeft)

		self.password.setPlaceholderText("Password")

		self.keep_cbox = QCheckBox("Keep me signed in")
		self.keep_cbox.setObjectName("keep-cbox")
		self.keep_cbox.clicked.connect(self.keepSignIn)

		self.button_login = QPushButton("Sign in")
		self.button_login.setObjectName("login-button")
		self.button_login.clicked.connect(self.trySignin)

		self.forgot_pass = QPushButton("Forgot password?")
		self.forgot_pass.setObjectName("forgot-button")

		self.vPageLayout.addWidget(self.title)
		self.vPageLayout.addWidget(self.username)
		self.vPageLayout.addWidget(self.password)
		self.vPageLayout.addWidget(self.keep_cbox)
		self.vPageLayout.addWidget(self.button_login)
		self.vPageLayout.addWidget(self.forgot_pass)

		self.pageLayout.addLayout(self.vPageLayout)
		self.setLayout(self.pageLayout)

	def keepSignIn(self):
		self._parent.store.keepSignIn = self.keep_cbox.isChecked()

	def trySignin(self):
		hash_object = hashlib.sha1(str(self.password.text()).encode())

		data = {
			"email": str(self.username.text()),
			"password": hash_object.hexdigest()
		}

		out = requests.post(SIGN_IN_URL, json=data).json()

		if out["result"] == True:
			self._parent.store.token = out["data"]["token"]

			self._parent.updateCentralWidgetIndex(2)
			self._parent.switchPage()
		else:
			self._parent.showAlertMessage(out["error"]["msg"])
