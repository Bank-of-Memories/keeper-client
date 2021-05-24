import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from core.FramedComponent import FramedComponent
from core.Component import Component
from src.WebView import WebView

class PickerButton(QLabel):
	def __init__(self, text):
		super(PickerButton, self).__init__(text)
		self.active = False
		self.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

		self.neighbors = []

		self.setObjectName("picker-button")

	def setNeighbors(self, arr):
		self.neighbors = arr

	def mousePressEvent(self, evt):
		self.active = not self.active
		self.redrawStyles()

	def redrawStyles(self):
		if self.active == True:
			self.setStyleSheet("background: #FFFFFF; margin-top: 1px; margin-left: 1px; min-width: 25px; min-height: 20px; max-width: 25px; max-height: 20px; border-radius: 5px;")
			for neighb in self.neighbors:
				neighb.active = False
				neighb.setStyleSheet("margin-top: 1px; margin-left: 1px; min-width: 25px; min-height: 20px; max-width: 25px; max-height: 20px; border-radius: 5px;")
		else:
			self.setStyleSheet("margin-top: 1px; margin-left: 1px; min-width: 25px; min-height: 20px; max-width: 25px; max-height: 20px; border-radius: 5px;")


class Picker(QFrame):
	def __init__(self, parent = None):
		super(Picker, self).__init__(parent)

		self.setObjectName("day-picker-body")

		self.mainLayout = QHBoxLayout()
		self.mainLayout.setSpacing(0)
		self.mainLayout.setAlignment(Qt.AlignLeft | Qt.AlignHCenter | Qt.AlignVCenter)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)

		self.day_button = PickerButton("D")
		self.day_button.active = True
		self.day_button.redrawStyles()

		self.week_button = PickerButton("W")
		self.month_button = PickerButton("M")

		self.day_button.setNeighbors([self.week_button, self.month_button])
		self.week_button.setNeighbors([self.day_button, self.month_button])
		self.month_button.setNeighbors([self.week_button, self.day_button])

		self.mainLayout.addWidget(self.day_button)
		self.mainLayout.addWidget(self.week_button)
		self.mainLayout.addWidget(self.month_button)

		self.setLayout(self.mainLayout)

class _Item(Component):
	def __init__(self, title, value_title, title_top_margin = False, percent_item = False, with_chart=False, with_border=True, with_picker=False, parent = None):
		super(_Item, self).__init__(parent)

		self.vLayout = QVBoxLayout()
		self.vLayout.setAlignment(Qt.AlignTop)
		self.vLayout.setSpacing(0)
		self.vLayout.setContentsMargins(0, 0, 0, 0)

		self.hLayout = QHBoxLayout()
		self.hLayout.setSpacing(0)
		self.hLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
		self.hLayout.setContentsMargins(0, 0, 0, 0)

		self.hLayoutValue = QHBoxLayout()
		self.hLayoutValue.setSpacing(0)
		self.hLayoutValue.setAlignment(Qt.AlignLeft | Qt.AlignTop)
		self.hLayoutValue.setContentsMargins(0, 0, 0, 0)

		self.title = QLabel(title)
		if title_top_margin == False:
			self.title.setObjectName("item-title")
		else:
			self.title.setObjectName("item-title-with-top-margin")

		self.title.setAlignment(Qt.AlignLeft | Qt.AlignTop)



		self.value = QLabel(value_title)
		self.value.setObjectName("item-value")
		self.value.setAlignment(Qt.AlignLeft | Qt.AlignTop)

		self.vLayout.addLayout(self.hLayout)
		self.vLayout.addLayout(self.hLayoutValue)
		self.vLayout.addStretch()

		self.hLayout.addWidget(self.title)

		if with_picker:
			self.day_picker = Picker()
			self.hLayout.addWidget(self.day_picker)

		self.hLayoutValue.addWidget(self.value)

		if percent_item == True:
			self.value.setObjectName("item-value-usd")

			self.percent_value = QLabel("+0,70%")
			self.percent_value.setObjectName("item-percent-value")
			self.percent_value.setAlignment(Qt.AlignLeft | Qt.AlignTop)
			self.hLayoutValue.addWidget(self.percent_value)

		if with_chart == True:
			self.chart = WebView(os.path.abspath("static/html/lineChart.html"))
			self.chart.setFixedWidth(350)
			self.chart.setFixedHeight(110)
			self.vLayout.addWidget(self.chart)

		if with_border == True:
			self.pseudo_border = QLabel()
			self.pseudo_border.setObjectName("item-pseudo-border")
			self.pseudo_border.setAlignment(Qt.AlignLeft | Qt.AlignTop)
			self.vLayout.addWidget(self.pseudo_border)



		# self.vLayout.addWidget(self.pseudo_border)

		self.setLayout(self.vLayout)

class TokenStatusComponent(FramedComponent):
	def __init__(self, parent = None):
		super(TokenStatusComponent, self).__init__(parent)
		self.setObjectName("token-status-component")
		self.basedLayout = QVBoxLayout()
		self.basedLayout.setSpacing(0)
		self.basedLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
		self.basedLayout.setContentsMargins(0, 0, 0, 0)

		self.balance_item = _Item("YOUR CURRENT TOKEN BALANCE", "GBM 0.0", True)
		self.mining_dynamics_item = _Item("MINING DYNAMICS", "- / -", with_picker=True)
		self.stock_dynamics_item = _Item("STOCK DYNAMICS", "USD 0.65", False, True, True, False, with_picker=True)

		self.basedLayout.addWidget(self.balance_item, 0)
		self.basedLayout.addWidget(self.mining_dynamics_item, 0)
		self.basedLayout.addWidget(self.stock_dynamics_item, 1)

		self.frame.setLayout(self.basedLayout)