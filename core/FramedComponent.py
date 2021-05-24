from PyQt5.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout
from core.Component import Component

class FramedComponent(Component):
  def __init__(self, parent = None):
    super(FramedComponent, self).__init__(parent)

    self._layout = QVBoxLayout()
    self._layout.setContentsMargins(0, 0, 0, 0)

    self.frame = QFrame()
    self.frame.setObjectName("framed-component")

    self._layout.addWidget(self.frame)
    self.setLayout(self._layout)