import os
import time
import shutil
import requests
import pyspeedtest

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from core.Worker import Worker
from core.Component import Component

from src.ConnectStatusComponent import ConnectStatusComponent
from src.TokenStatusComponent import TokenStatusComponent
from src.NetworkStatsComponent import NetworkStatsComponent
from src.StorageStatsComponent import StorageStatsComponent

from src.LeaseController import LeaseController

from constants import WALLET_URL, SPEED_TEST_URL

class MonitoringComponent(Component):
	def __init__(self, parent = None):
		super(MonitoringComponent, self).__init__(parent)

		self.checkNetwork = True

		self.pageLayout = QVBoxLayout()

		self.pageLayout.setContentsMargins(0, 0, 0, 0)
		self.pageLayout.setSpacing(0)
		self.pageLayout.setAlignment(Qt.AlignTop)

		self.hLayout = QHBoxLayout()
		self.hLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
		self.hLayout.setSpacing(0)
		self.hLayout.setContentsMargins(0, 0, 0, 0)

		self.vLayoutRight = QVBoxLayout()
		self.vLayoutRight.setAlignment(Qt.AlignLeft | Qt.AlignTop)
		self.vLayoutRight.setContentsMargins(0, 0, 0, 0)
		self.vLayoutRight.setSpacing(0)

		self.worker = Worker(self.updateNetworkStats)
		self.speed_test = pyspeedtest.SpeedTest(SPEED_TEST_URL)

		self.connect_status_component = ConnectStatusComponent(parent=self._parent)
		self.lease_controller = LeaseController(parent=self._parent)
		self.lease_controller.hide()

		self.token_status_component = TokenStatusComponent()
		self.network_stats_component = NetworkStatsComponent(parent=self._parent)
		self.storage_stats_component = StorageStatsComponent()

		self.vLayoutRight.addWidget(self.network_stats_component)
		self.vLayoutRight.addWidget(self.storage_stats_component)

		self.hLayout.addWidget(self.token_status_component)
		self.hLayout.addLayout(self.vLayoutRight)

		self.pageLayout.addWidget(self.connect_status_component)
		self.pageLayout.addWidget(self.lease_controller)
		self.pageLayout.addLayout(self.hLayout)

		self.pageLayout.addStretch()
		self.pageLayout.setContentsMargins(0, 0, 0, 0)

		self.setLayout(self.pageLayout)

		self.free_gb_value = 0
		self.total_gb_value = 0

		self.updateStorageStats()

	def getWalletStats(self):
		out = requests.get(WALLET_URL, headers={"Authorization": "Bearer %s" % self._parent.store.accessToken}).json()
		walletData = out["data"]

		balance = str(walletData["balances"][0]["balance"])

		self.token_status_component.balance_item.value.setText("GBM " + balance)

	def updateStorageStats(self):
		total, used, free = shutil.disk_usage("/")

		self.free_gb_value = free // (2 ** 30)
		self.total_gb_value = total // (2 ** 30)
		# ipfs_gb = self._parent.ipfs_controller.getStorageSize()

		self.storage_stats_component.active_used.value.setText(str(self.free_gb_value) + " GB")
		self.storage_stats_component.available_storage.value.setText(str(self.total_gb_value) + " GB")

	def updateNetworkStats(self):
		while self.checkNetwork:
			time.sleep(2)

			download_mb = round(round(self.speed_test.download()) / 1e+6, 2)
			upload_mb = round(round(self.speed_test.upload()) / 1e+6, 2)

			self.network_stats_component.download_value = download_mb
			self.network_stats_component.upload_value = upload_mb

			self.network_stats_component.download_stats.value.setText(str(self.network_stats_component.download_value) + " Mbs")
			self.network_stats_component.upload_stats.value.setText(str(self.network_stats_component.upload_value) + " Mbs")

	def showEvent(self, ev):
		try:
			self.getWalletStats()
		except:
			os.remove(".profile")
			self._parent.updateCentralWidgetIndex(0)
			self._parent.switchPage()

		if not self.checkNetwork:
			self.checkNetwork = True

		self.worker.start()

	def hideEvent(self, ev):
		self.checkNetwork = False
		self.worker.quit()