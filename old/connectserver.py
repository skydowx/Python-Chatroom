from PyQt5 import QtWidgets
from connectservergui import Ui_ConnectServer

class ConnectServerWindow(QtWidgets.QMainWindow, Ui_ConnectServer):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()