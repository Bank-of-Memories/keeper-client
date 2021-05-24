import os.path
import json

from PyQt5.QtWidgets import *
from src.LoginComponent import LoginComponent
from src.OtpComponent import OtpComponent
from src.MonitoringComponent import MonitoringComponent
from src.IpfsController import IpfsController

from core.Store import Store

from src.ConnectPopup import ConnectPopup

class MainWindow(QWidget):
	central_widget_index = 0
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
		self.resolution = QDesktopWidget().screenGeometry(-1)

		self.store = Store()
		self.ipfs_controller = IpfsController(self)

		self.setWindowTitle("Bank of Memories")

		self.frame = QFrame()
		self.frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.frame.setObjectName("background")
		
		layout = QVBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)
		layout.addStretch()

		self.setLayout(layout)

		self.stackedLayout = QStackedLayout()
		self.frame.setLayout(self.stackedLayout)
		
		self.page1 = LoginComponent(self)
		self.page2 = MonitoringComponent(self)
		self.page3 = OtpComponent(self)

		self.stackedLayout.addWidget(self.page1)
		self.stackedLayout.addWidget(self.page2)
		self.stackedLayout.addWidget(self.page3)

		layout.addWidget(self.frame)

		self._foreground = QFrame(parent=self)
		self._foreground.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self._foreground.setObjectName("foreground-popup")

		self.connect_popup = ConnectPopup(parent=self)

		self._foreground.hide()

		self.moveToCenter()

		if os.path.isfile(".profile"):
			with open(".profile", "r") as f:
				out = json.loads(f.read())
				self.store.accessToken = out["access_token"]
				self.store.refreshToken = out["refresh_token"]
				self.store.userProfile = out["user"]
				self.updateCentralWidgetIndex(1)
				self.switchPage()
		else:
			pass

	def switchPage(self):
		self.stackedLayout.setCurrentIndex(self.central_widget_index)

	def updateCentralWidgetIndex(self, index):
		self.central_widget_index = index

	def showAlertMessage(self, err):
		msg = QMessageBox()
		msg.setIcon(QMessageBox.Warning)
		msg.setInformativeText(err)
		msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
		msg.exec_()

	def moveAppToTopCorner(self):
		self.move(self.resolution.width() / 2, 0)

	def moveToCenter(self):
		# geometry of the main window
		qr = self.frameGeometry()
		# center point of screen
		cp = QDesktopWidget().availableGeometry().center()
		# move rectangle's center point to screen's center point
		qr.moveCenter(cp)
		# top left of rectangle becomes top left of window centering it
		self.move(qr.topLeft())

	def closeEvent(self, evt):
		self.ipfs_controller.daemon_proc.kill()
		evt.accept()
