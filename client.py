import sys
from PyQt5.QtWidgets import QApplication
from chatroom import ChatroomWindow
from time import sleep

app = QApplication(sys.argv)

chatroomInst = ChatroomWindow()

sys.exit(app.exec_())