from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from core.FramedComponent import FramedComponent
from core.Component import Component


class SSItem(Component):
	def __init__(self, icon_object_name, title_string, value_string, parent = None):
		super(SSItem, self).__init__(parent)

		self.setObjectName("storage-status-component")

		self.hLayout = QHBoxLayout()
		self.hLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
		self.hLayout.setSpacing(0)
		self.hLayout.setContentsMargins(0, 0, 0, 0)

		self.icon = QLabel()
		self.icon.setObjectName(icon_object_name)
		self.icon.setAlignment(Qt.AlignLeft | Qt.AlignTop)

		self.vLayout = QVBoxLayout()
		self.vLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
		self.vLayout.setSpacing(0)
		self.vLayout.setContentsMargins(0, 0, 0, 0)

		self.title = QLabel(title_string)
		self.title.setObjectName("active-used-title")
		self.title.setAlignment(Qt.AlignLeft | Qt.AlignTop)

		self.value = QLabel(value_string)
		self.value.setObjectName("active-used-value")
		self.value.setAlignment(Qt.AlignLeft | Qt.AlignTop)

		self.hLayout.addWidget(self.icon)

		self.vLayout.addWidget(self.title)
		self.vLayout.addWidget(self.value)

		self.hLayout.addLayout(self.vLayout)

		self.setLayout(self.hLayout)

class StorageStatsComponent(FramedComponent):
	def __init__(self, parent = None):
		super(StorageStatsComponent, self).__init__(parent)
		self.setObjectName("storage-stats-component")

		self.basedLayout = QVBoxLayout()
		self.basedLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
		self.basedLayout.setContentsMargins(0, 0, 0, 0)
		self.basedLayout.setSpacing(0)

		self.title = QLabel("STORAGE CAPACITY")
		self.title.setObjectName("storage-title")
		self.title.setAlignment(Qt.AlignLeft | Qt.AlignTop)

		self.active_used = SSItem("active-used-icon", "Active used storage", "0 Gb")
		self.available_storage = SSItem("available-storage-icon", "Available storage", "0 Gb")

		self.basedLayout.addWidget(self.title)
		self.basedLayout.addWidget(self.active_used)
		self.basedLayout.addWidget(self.available_storage)

		self.frame.setLayout(self.basedLayout)