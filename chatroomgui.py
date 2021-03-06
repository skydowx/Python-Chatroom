# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatroom.ui'
# Omer: Automatically created GUI file by Qtcreator
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChatRoom(object):
    def setupUi(self, ChatRoom):
        ChatRoom.setObjectName("ChatRoom")
        ChatRoom.setEnabled(True)
        ChatRoom.resize(532, 425)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ChatRoom.sizePolicy().hasHeightForWidth())
        ChatRoom.setSizePolicy(sizePolicy)
        ChatRoom.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        ChatRoom.setTabShape(QtWidgets.QTabWidget.Rounded)
        ChatRoom.setDockNestingEnabled(False)
        ChatRoom.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtWidgets.QWidget(ChatRoom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.hostname = QtWidgets.QLineEdit(self.centralWidget)
        self.hostname.setObjectName("hostname")
        self.horizontalLayout_3.addWidget(self.hostname)
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.port = QtWidgets.QLineEdit(self.centralWidget)
        self.port.setObjectName("port")
        self.horizontalLayout_3.addWidget(self.port)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.connect = QtWidgets.QPushButton(self.centralWidget)
        self.connect.setObjectName("connect")
        self.horizontalLayout_3.addWidget(self.connect)
        self.disconnect = QtWidgets.QPushButton(self.centralWidget)
        self.disconnect.setObjectName("disconnect")
        self.horizontalLayout_3.addWidget(self.disconnect)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.aliasinput = QtWidgets.QLineEdit(self.centralWidget)
        self.aliasinput.setObjectName("aliasinput")
        self.horizontalLayout_4.addWidget(self.aliasinput)
        self.setalias = QtWidgets.QPushButton(self.centralWidget)
        self.setalias.setObjectName("setalias")
        self.horizontalLayout_4.addWidget(self.setalias)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.messagedisplay = QtWidgets.QTextEdit(self.centralWidget)
        self.messagedisplay.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.messagedisplay.setReadOnly(True)
        self.messagedisplay.setObjectName("messagedisplay")
        self.verticalLayout_3.addWidget(self.messagedisplay)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.message = QtWidgets.QLineEdit(self.centralWidget)
        self.message.setObjectName("message")
        self.horizontalLayout.addWidget(self.message)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.send = QtWidgets.QPushButton(self.centralWidget)
        self.send.setObjectName("send")
        self.verticalLayout.addWidget(self.send)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        ChatRoom.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(ChatRoom)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 532, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        ChatRoom.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(ChatRoom)
        self.mainToolBar.setObjectName("mainToolBar")
        ChatRoom.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(ChatRoom)
        self.statusBar.setObjectName("statusBar")
        ChatRoom.setStatusBar(self.statusBar)
        self.actionConnect = QtWidgets.QAction(ChatRoom)
        self.actionConnect.setObjectName("actionConnect")
        self.actionExit = QtWidgets.QAction(ChatRoom)
        self.actionExit.setObjectName("actionExit")
        self.actionConnectServer = QtWidgets.QAction(ChatRoom)
        self.actionConnectServer.setCheckable(False)
        self.actionConnectServer.setObjectName("actionConnectServer")
        self.actionDisconnectServer = QtWidgets.QAction(ChatRoom)
        self.actionDisconnectServer.setObjectName("actionDisconnectServer")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionConnectServer)
        self.menuFile.addAction(self.actionDisconnectServer)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(ChatRoom)
        QtCore.QMetaObject.connectSlotsByName(ChatRoom)
        ChatRoom.setTabOrder(self.messagedisplay, self.send)

    def retranslateUi(self, ChatRoom):
        _translate = QtCore.QCoreApplication.translate
        ChatRoom.setWindowTitle(_translate("ChatRoom", "ChatRoom"))
        self.label_3.setText(_translate("ChatRoom", "Hostname:"))
        self.label_4.setText(_translate("ChatRoom", "Port:"))
        self.connect.setText(_translate("ChatRoom", "Connect"))
        self.disconnect.setText(_translate("ChatRoom", "Disconnect"))
        self.label.setText(_translate("ChatRoom", "Alias:"))
        self.setalias.setText(_translate("ChatRoom", "Set Alias"))
        self.label_2.setText(_translate("ChatRoom", "Message:"))
        self.send.setText(_translate("ChatRoom", "Send"))
        self.menuFile.setTitle(_translate("ChatRoom", "File"))
        self.actionConnect.setText(_translate("ChatRoom", "Connect"))
        self.actionExit.setText(_translate("ChatRoom", "Exit"))
        self.actionConnectServer.setText(_translate("ChatRoom", "Connect"))
        self.actionDisconnectServer.setText(_translate("ChatRoom", "Disconnect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChatRoom = QtWidgets.QMainWindow()
    ui = Ui_ChatRoom()
    ui.setupUi(ChatRoom)
    ChatRoom.show()
    sys.exit(app.exec_())
