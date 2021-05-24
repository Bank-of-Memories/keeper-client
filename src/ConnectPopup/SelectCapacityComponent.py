from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QFrame, QSlider
from core.Component import Component

class SelectCapacityComponent(Component):
	def __init__(self, parent = None):
		super(SelectCapacityComponent, self).__init__(parent)
		self.setObjectName("select-capacity-component")

		self.basedLayout = QHBoxLayout()
		self.basedLayout.setSpacing(0)
		self.basedLayout.setContentsMargins(0, 0, 0, 0)
		self.basedLayout.setAlignment(Qt.AlignLeft | Qt.AlignHCenter)

		frameLayout = QHBoxLayout()
		frameLayout.setSpacing(0)
		frameLayout.setContentsMargins(0, 0, 0, 0)
		frameLayout.setAlignment(Qt.AlignLeft | Qt.AlignHCenter)
		slider_frame = QFrame()
		slider_frame.setObjectName("margin-helper-capasity-slider")

		self.capacity_slider = QSlider(Qt.Horizontal, self)
		self.capacity_slider.setObjectName("capacity-slider")
		self.capacity_slider.setRange(0, self._parent.page2.free_gb_value)
		self.capacity_slider.setFocusPolicy(Qt.NoFocus)
		self.capacity_slider.valueChanged.connect(self.updateValue)

		frameLayout.addWidget(self.capacity_slider)
		slider_frame.setLayout(frameLayout)

		self.capacity_value = QLabel("0 GB")
		self.capacity_value.setObjectName("capacity-value")
		self.capacity_value.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

		self.basedLayout.addWidget(slider_frame)
		self.basedLayout.addWidget(self.capacity_value)

		self.setLayout(self.basedLayout)

	def updateValue(self, value):
		self.capacity_value.setText(str(value) + " GB")