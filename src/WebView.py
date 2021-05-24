from PyQt5.QtCore import QObject, pyqtSlot, QUrl, QVariant
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel

from core.Component import Component

class CallHandler(QObject):
	def __init__(self, datastore):
		super(CallHandler, self).__init__()
		self.datastore = datastore

	@pyqtSlot(result=QVariant)
	def test(self):
		return QVariant({ "value": self.datastore.download_value, "color": "#cecece" })

	@pyqtSlot(result=QVariant)
	def test2(self):
		return QVariant({ "value": self.datastore.upload_value, "color": "#cecece" })

	# take an argument from javascript - JS:  handler.test1('hello!')
	@pyqtSlot(QVariant, result=QVariant)
	def test1(self, args):
		return "ok"

class WebView(QWebEngineView, Component):
	def __init__(self, f_path, parent = None):
		super(WebView, self).__init__(parent)

		self.setObjectName("chart-view")

		self.setFixedWidth(64)
		self.setFixedHeight(72)
		# self.setContentsMargins(16, 8, 0, 16)
		self.setContentsMargins(0, 0, 0, 0)

		self.channel = QWebChannel()
		self.handler = CallHandler(self._parent)
		self.channel.registerObject('handler', self.handler)
		self.page().setWebChannel(self.channel)

		file_path = f_path
		local_url = QUrl.fromLocalFile(file_path)

		self.load(local_url)