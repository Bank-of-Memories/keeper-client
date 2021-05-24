import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from core.FramedComponent import FramedComponent
from core.Component import Component
from src.WebView import WebView

class NSItem(Component):
	def __init__(self, title_string, value_string, chart, parent = None):
		super(NSItem, self).__init__(parent)
		self.vLayout = QVBoxLayout()
		self.vLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
		self.vLayout.setSpacing(0)
		self.vLayout.setContentsMargins(0, 0, 0, 0)

		self.hLayout = QHBoxLayout()
		self.hLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
		self.hLayout.setSpacing(0)
		self.hLayout.setContentsMargins(0, 0, 0, 0)

		self.chart_view = chart

		self.title = QLabel(title_string)
		self.title.setObjectName("download-title")
		self.title.setAlignment(Qt.AlignLeft | Qt.AlignTop)

		self.value = QLabel(value_string)
		self.value.setObjectName("download-value")
		self.value.setAlignment(Qt.AlignLeft | Qt.AlignTop)

		self.hLayout.addWidget(self.chart_view)

		self.vLayout.addWidget(self.title)
		self.vLayout.addWidget(self.value)

		self.hLayout.addLayout(self.vLayout)

		self.setLayout(self.hLayout)

class NetworkStatsComponent(FramedComponent):
	def __init__(self, parent = None):
		super(NetworkStatsComponent, self).__init__(parent)
		self.setObjectName("network-stats-component")

		self.basedLayout = QVBoxLayout()
		self.basedLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
		self.basedLayout.setSpacing(0)
		self.basedLayout.setContentsMargins(0, 0, 0, 0)

		self.hLayout = QHBoxLayout()
		self.hLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
		self.hLayout.setContentsMargins(0, 0, 0, 0)
		self.hLayout.setSpacing(0)

		self.speedStatsLayout = QVBoxLayout()
		self.speedStatsLayout.setAlignment(Qt.AlignRight | Qt.AlignTop)
		self.speedStatsLayout.setContentsMargins(0, 0, 0, 0)
		self.speedStatsLayout.setSpacing(0)

		self.download_value = 0
		self.upload_value = 0

		self.title = QLabel("INTERNET SPEED")
		self.title.setObjectName("speed-title")
		self.title.setAlignment(Qt.AlignLeft | Qt.AlignTop)

		self.download_stats = NSItem("Download speed", "0.0 Mbs", WebView(os.path.abspath("static/html/downloadChart.html"), self), parent=self)
		self.upload_stats = NSItem("Upload speed", "0.0 Mbs", WebView(os.path.abspath("static/html/uploadChart.html"), self), parent=self)

		self.basedLayout.addWidget(self.title)

		self.speedStatsLayout.addWidget(self.download_stats)
		self.speedStatsLayout.addWidget(self.upload_stats)

		self.hLayout.addLayout(self.speedStatsLayout)
		self.basedLayout.addLayout(self.hLayout)

		self.frame.setLayout(self.basedLayout)