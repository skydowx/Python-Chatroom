from PyQt5 import QtWidgets
from chatroomgui import Ui_ChatRoom
import threading
import socket 
import select 
import sys 
import random
import re
from time import sleep

"""
Main Class that renders the GUI and handles the messaging logic

"""

class ChatroomWindow(QtWidgets.QMainWindow, Ui_ChatRoom):
	def __init__(self):

		# GUI Initialization
		super().__init__()
		self.setupUi(self)
		self.show()

		# Client data initialization
		self.server = None
		self.useralias = "Anon"
		self.aliascolor = f"rgb({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)})"	

		# connecting different buttons to the respective functions that they perform
		self.connect.clicked.connect(self.connect_to_server)
		self.disconnect.clicked.connect(self.disconnect_from_server)
		self.send.clicked.connect(self.send_message)
		self.setalias.clicked.connect(self.set_alias)

		# Some QoL connections that'll trigger the respective function if 
		# the user presses return in the respective text box
		self.message.returnPressed.connect(self.send_message)
		self.hostname.returnPressed.connect(self.connect_to_server)
		self.port.returnPressed.connect(self.connect_to_server)
		self.aliasinput.returnPressed.connect(self.set_alias)

	# Connects the user to the server and starts the message receiving thread
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
		port_no = self.port.text()
		if (not port_no.isnumeric()):
			self.port.setText("8000")
			self.messagedisplay.insertHtml(f"<div style='color: red'>Invalid port number.<div>")
			return

		self.Port = int(port_no)

		# Finally initialize and connect to server
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			ret = self.server.connect((self.IP_address, self.Port))
			self.messagedisplay.insertHtml(f"<div style='color: green'>Connection Successful<div>")
			# self.server.send(f"<div style='color: green'>{self.useralias} has joined the chat.<div>".encode())

			# Run the receive message thread

			thread = threading.Thread(target=self.receive_message_thread)
			# thread.setDaemon(True)
			thread.start()
		except:
			self.server = None
			self.messagedisplay.insertHtml(f"<div style='color: red'>Connection to the server failed. Is the server running?.<div>")

	# Disconnect from the server
	def disconnect_from_server(self):
		
		# If we're connected to a server
		if(self.server):
			# self.server.send(f"<div style='color: green'>{self.useralias} has left the chat.<div>".encode())
			self.server.close()
			self.server = None
			self.messagedisplay.insertHtml(f"<div style='color: green'>Disconnected<div>")
		# else display error message
		else:
			self.messagedisplay.insertHtml(f"<div style='color: red'>You are not connected to any server.<div>")

	# Used to send messages to the server
	def send_message(self):
		# self.messagedisplay.insertHtml("<div style='color: red'>Implement the message sending logic<div>")
		if (self.server):
			msg = self.message.text()
			self.message.setText("")
			toWrite = f"<inline style='color: {self.aliascolor}'>&lt;{self.useralias}&gt;</inline> " + msg + "<br>"
			if (msg == ""):
				return
			else:
				self.server.send(toWrite.encode())
				self.messagedisplay.insertHtml(toWrite)
		else:
			self.messagedisplay.insertHtml(f"<div style='color: red'>You are not connected to any server.<div>")

	# Used to receive messages from the server
	def receive_message_thread(self):
		while self.server:
			try:
				message = self.server.recv(2048).decode()
				self.messagedisplay.insertHtml(message)
				sleep(.1)
			except Exception:
				self.messagedisplay.insertHtml("<div style='color: red'>Unable to get data from the server.<div>")
	
	# Used to set alias
	def set_alias(self):
		# self.messagedisplay.insertHtml("<div style='color: red'>Implement the alias setting logic<div>")
		newalias = self.aliasinput.text()
		if (newalias==""):
			return
		# self.server.send(f"<div style='color: green'>{self.useralias} => {newalias}<div>".encode())
		self.useralias = newalias
		self.aliascolor = f"rgb({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)})"



