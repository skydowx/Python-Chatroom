from PyQt5 import QtWidgets
from chatroomgui import Ui_ChatRoom
from connectserver import Ui_connectServer
import socket 
import select 
import sys 
import random
import re

class ChatroomWindow(QtWidgets.QMainWindow, Ui_ChatRoom):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()
		self.server = None
		self.useralias = "Anon"
		self.aliascolor = f"rgb({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)})"	

		# connecting different buttons to the respective functions that they perform
		self.connect.clicked.connect(self.connect_to_server)
		self.disconnect.clicked.connect(self.disconnect_from_server)
		self.send.clicked.connect(self.send_message)
		self.setalias.clicked.connect(self.set_alias)
		self.actionExit.triggered.connect(self.exit_handler)
		
		self.actionConnectServer.triggered.connect(self.connect_server_window)

	def connect_server_window(self):
		connectServer = QtWidgets.QWidget()
		ui = Ui_connectServer()
		ui.setupUi(connectServer)
		connectServer.show()

	def connect_to_server(self):

		# If we're already connected to a server
		if (self.server):
			self.messagedisplay.insertHtml(f"<div style='color: red'>You're already connected, disconnect first.<div>")
			return
		
		# Get IP address and check if it's valid
		IP = self.hostname.text() 
		match_res = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", IP)
		if (not match_res):
			self.messagedisplay.insertHtml(f"<div style='color: red'>Invalid IP address.<div>")
			return

		self.IP_address = IP

		# Get port no. and check if it's valid 
		port_no = int(self.port.text())
		if not (1023 < port_no <= 65535):
			self.messagedisplay.insertHtml(f"<div style='color: red'>Invalid port number.<div>")
			return

		self.Port = port_no

		# Finally initialize and connect to server
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			ret = self.server.connect((self.IP_address, self.Port))
			self.messagedisplay.insertHtml(f"<div style='color: green'>Connection Successful<div>")
		except:
			self.server = None
			self.messagedisplay.insertHtml(f"<div style='color: red'>Connection to the server failed. Is the server running?.<div>")

	def disconnect_from_server(self):
		
		# If we're connected to a server
		if(self.server):
			self.server.close()
			self.server = None
			self.messagedisplay.insertHtml(f"<div style='color: green'>Disconnected<div>")
		# else display error message
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
