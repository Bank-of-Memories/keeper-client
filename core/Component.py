from PyQt5.QtWidgets import QWidget

class Component(QWidget):
	def __init__(self, parent = None, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self._parent = parent