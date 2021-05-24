from PyQt5.QtCore import QThread, pyqtSlot

class Worker(QThread):
	def __init__(self, fn, *args, **kwargs):
		super(Worker, self).__init__()

		self.fn = fn
		self.args = args
		self.kwargs = kwargs

	@pyqtSlot()
	def run(self):
		self.fn(*self.args, **self.kwargs)