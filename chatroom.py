from PyQt5 import QtWidgets
from chatroomgui import Ui_ChatRoom
import socket 
import select 
import sys 
import random

class ChatroomWindow(QtWidgets.QMainWindow, Ui_ChatRoom):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()
		self.server = None
		self.useralias = "Anon"
		self.aliascolor = f"rgb({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)})"

		# Implement the connect server logic
		self.connect.clicked.connect(self.connect_to_server)
		self.disconnect.clicked.connect(self.disconnect_from_server)
		self.send.clicked.connect(self.send_message)
		self.setalias.clicked.connect(self.set_alias)
		self.actionExit.triggered.connect(self.exit_handler)

	def connect_to_server(self):
		# self.messagedisplay.insertHtml("<div style='color: red'>Implement the server connection logic<div>")
		if (self.server):
			self.messagedisplay.insertHtml(f"<div style='color: red'>You're already connected, disconnect first.<div>")
			return
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		#if len(sys.argv) != 3: 
		#	print("Correct usage: script, IP address, port number")
		#	exit() 
		self.IP_address = self.hostname.text() #TODO: ERROR HANDLING
		self.Port = int(self.port.text()) #TODO: ERROR HANDLING
		ret = self.server.connect((self.IP_address, self.Port))
		self.messagedisplay.insertHtml(f"<div style='color: green'>Connection Successful<div>")


	def disconnect_from_server(self):
		# self.messagedisplay.insertHtml("<div style='color: red'>Implement the server disconnection logic<div>")
		# todo
		if(self.server):
			self.server.close()
			self.server = None
			self.messagedisplay.insertHtml(f"<div style='color: green'>Disconnected<div>")
		else:
			self.messagedisplay.insertHtml(f"<div style='color: red'>You are not connected to any server.<div>")


	def exit_handler(self):
		print("Implement the server exit handler")
		# todo
		exit()

	def send_message(self):
		# self.messagedisplay.insertHtml("<div style='color: red'>Implement the message sending logic<div>")
		if (self.server):
			msg = self.message.text()
			toWrite = f"<inline style='color: {self.aliascolor}'>&lt;{self.useralias}&gt;</inline> " + msg + "<br>"
			if (msg == ""):
				return
			else:
				self.server.send(toWrite.encode())
				self.messagedisplay.insertHtml(toWrite)
		else:
			self.messagedisplay.insertHtml(f"<div style='color: red'>You are not connected to any server.<div>")


	def set_alias(self):
		# self.messagedisplay.insertHtml("<div style='color: red'>Implement the alias setting logic<div>")
		newalias = self.aliasinput.text()
		if (newalias==""):
			return
		self.useralias = newalias

	def display_message(self, message):
		self.messagedisplay.insertHtml(message.decode())
