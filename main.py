import sys
from PyQt5.QtWidgets import QApplication
from chatroom import ChatroomWindow
from threading import _start_new_thread
import select

app = QApplication(sys.argv)

chatroomInst = ChatroomWindow()


def message_sender(chatroom, nothingLMAO):
	while True:
		server = chatroom.server
		if (server):
			# maintains a list of possible input streams 
			sockets_list = [server]  #sys.stdin

			""" There are two possible input situations. Either the 
			user wants to give manual input to send to other people, 
			or the server is sending a message to be printed on the 
			screen. Select returns from sockets_list, the stream that 
			is reader for input. So for example, if the server wants 
			to send a message, then the if condition will hold true 
			below.If the user wants to send a message, the else 
			condition will evaluate as true"""
			read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 

			for socks in read_sockets: 
				if socks == chatroomInst.server: 
					message = socks.recv(2048) 
					chatroomInst.display_message(message)
				# else: 
				# 	message = sys.stdin.readline() 
				# 	server.send(message) 
				# 	sys.stdout.write("<You>") 
				# 	sys.stdout.write(message) 
				# 	sys.stdout.flush() 
	server.close() 

_start_new_thread(message_sender, (chatroomInst, 0))

sys.exit(app.exec_())