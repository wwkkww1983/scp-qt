# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/scp_qt.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_scp_qt(object):
    def setupUi(self, scp_qt):
        scp_qt.setObjectName("scp_qt")
        scp_qt.resize(859, 693)
        self.centralwidget = QtWidgets.QWidget(scp_qt)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName("tabWidget")
        self.send_tab = QtWidgets.QWidget()
        self.send_tab.setEnabled(True)
        self.send_tab.setObjectName("send_tab")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.send_tab)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(self.send_tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 799, 576))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 200))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.browse = QtWidgets.QPushButton(self.groupBox)
        self.browse.setObjectName("browse")
        self.gridLayout_6.addWidget(self.browse, 0, 1, 1, 1)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 253, 121))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.gridLayout_21 = QtWidgets.QGridLayout()
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.sources = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_3)
        self.sources.setTabChangesFocus(True)
        self.sources.setObjectName("sources")
        self.gridLayout_21.addWidget(self.sources, 0, 0, 1, 1)
        self.gridLayout_22.addLayout(self.gridLayout_21, 1, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_6.addWidget(self.scrollArea_3, 2, 1, 1, 1)
        self.sendDirectory = QtWidgets.QCheckBox(self.groupBox)
        self.sendDirectory.setObjectName("sendDirectory")
        self.gridLayout_6.addWidget(self.sendDirectory, 0, 2, 1, 1)
        self.gridLayout_24 = QtWidgets.QGridLayout()
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.appendSource = QtWidgets.QPushButton(self.groupBox)
        self.appendSource.setObjectName("appendSource")
        self.gridLayout_24.addWidget(self.appendSource, 1, 0, 1, 1)
        self.clearSources = QtWidgets.QPushButton(self.groupBox)
        self.clearSources.setObjectName("clearSources")
        self.gridLayout_24.addWidget(self.clearSources, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_24.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_24, 2, 2, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 1, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_15.addWidget(self.frame_2, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setMinimumSize(QtCore.QSize(390, 350))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.groupBox_2)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 401, 302))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.status = QtWidgets.QLabel(self.frame)
        self.status.setMinimumSize(QtCore.QSize(320, 200))
        self.status.setObjectName("status")
        self.gridLayout_11.addWidget(self.status, 0, 0, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_11, 0, 0, 1, 1)
        self.gridLayout_12.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.send = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.send.setObjectName("send")
        self.gridLayout_17.addWidget(self.send, 0, 0, 1, 1)
        self.connect = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.connect.setObjectName("connect")
        self.gridLayout_17.addWidget(self.connect, 0, 1, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_17, 1, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_9.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.gridLayout_15.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_15, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.frame_3 = QtWidgets.QFrame(self.groupBox_3)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.host_address = QtWidgets.QLineEdit(self.frame_3)
        self.host_address.setEnabled(False)
        self.host_address.setDragEnabled(True)
        self.host_address.setClearButtonEnabled(True)
        self.host_address.setObjectName("host_address")
        self.gridLayout_3.addWidget(self.host_address, 1, 1, 1, 1)
        self.passwordLabel = QtWidgets.QLabel(self.frame_3)
        self.passwordLabel.setEnabled(False)
        self.passwordLabel.setObjectName("passwordLabel")
        self.gridLayout_3.addWidget(self.passwordLabel, 4, 0, 1, 1)
        self.port_remote = QtWidgets.QSpinBox(self.frame_3)
        self.port_remote.setEnabled(False)
        self.port_remote.setMaximum(65535)
        self.port_remote.setProperty("value", 22)
        self.port_remote.setObjectName("port_remote")
        self.gridLayout_3.addWidget(self.port_remote, 2, 1, 1, 1)
        self.hostLabel = QtWidgets.QLabel(self.frame_3)
        self.hostLabel.setEnabled(False)
        self.hostLabel.setObjectName("hostLabel")
        self.gridLayout_3.addWidget(self.hostLabel, 1, 0, 1, 1)
        self.userLabel = QtWidgets.QLabel(self.frame_3)
        self.userLabel.setEnabled(False)
        self.userLabel.setObjectName("userLabel")
        self.gridLayout_3.addWidget(self.userLabel, 3, 0, 1, 1)
        self.portLabel = QtWidgets.QLabel(self.frame_3)
        self.portLabel.setEnabled(False)
        self.portLabel.setObjectName("portLabel")
        self.gridLayout_3.addWidget(self.portLabel, 2, 0, 1, 1)
        self.user_remote = QtWidgets.QLineEdit(self.frame_3)
        self.user_remote.setEnabled(False)
        self.user_remote.setDragEnabled(True)
        self.user_remote.setClearButtonEnabled(True)
        self.user_remote.setObjectName("user_remote")
        self.gridLayout_3.addWidget(self.user_remote, 3, 1, 1, 1)
        self.password_remote = QtWidgets.QLineEdit(self.frame_3)
        self.password_remote.setEnabled(False)
        self.password_remote.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.password_remote.setDragEnabled(True)
        self.password_remote.setClearButtonEnabled(True)
        self.password_remote.setObjectName("password_remote")
        self.gridLayout_3.addWidget(self.password_remote, 4, 1, 1, 1)
        self.destination = QtWidgets.QLineEdit(self.frame_3)
        self.destination.setEnabled(False)
        self.destination.setDragEnabled(True)
        self.destination.setClearButtonEnabled(True)
        self.destination.setObjectName("destination")
        self.gridLayout_3.addWidget(self.destination, 5, 1, 1, 1)
        self.destinationLabel = QtWidgets.QLabel(self.frame_3)
        self.destinationLabel.setEnabled(False)
        self.destinationLabel.setObjectName("destinationLabel")
        self.gridLayout_3.addWidget(self.destinationLabel, 5, 0, 1, 1)
        self.hostEdit = QtWidgets.QCheckBox(self.frame_3)
        self.hostEdit.setObjectName("hostEdit")
        self.gridLayout_3.addWidget(self.hostEdit, 1, 2, 1, 1)
        self.portEdit = QtWidgets.QCheckBox(self.frame_3)
        self.portEdit.setObjectName("portEdit")
        self.gridLayout_3.addWidget(self.portEdit, 2, 2, 1, 1)
        self.userEdit = QtWidgets.QCheckBox(self.frame_3)
        self.userEdit.setObjectName("userEdit")
        self.gridLayout_3.addWidget(self.userEdit, 3, 2, 1, 1)
        self.passwordEdit = QtWidgets.QCheckBox(self.frame_3)
        self.passwordEdit.setObjectName("passwordEdit")
        self.gridLayout_3.addWidget(self.passwordEdit, 4, 2, 1, 1)
        self.destinationEdit = QtWidgets.QCheckBox(self.frame_3)
        self.destinationEdit.setObjectName("destinationEdit")
        self.gridLayout_3.addWidget(self.destinationEdit, 5, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 6, 1, 1, 1)
        self.gridLayout_20.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_16.addWidget(self.frame_3, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 150))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.hostKeyLabel = QtWidgets.QLabel(self.groupBox_4)
        self.hostKeyLabel.setEnabled(False)
        self.hostKeyLabel.setMaximumSize(QtCore.QSize(16777215, 25))
        self.hostKeyLabel.setObjectName("hostKeyLabel")
        self.gridLayout_18.addWidget(self.hostKeyLabel, 1, 0, 1, 1)
        self.hostKey = QtWidgets.QLineEdit(self.groupBox_4)
        self.hostKey.setEnabled(False)
        self.hostKey.setMaximumSize(QtCore.QSize(16777215, 25))
        self.hostKey.setDragEnabled(True)
        self.hostKey.setClearButtonEnabled(True)
        self.hostKey.setObjectName("hostKey")
        self.gridLayout_18.addWidget(self.hostKey, 1, 1, 1, 1)
        self.hostKeyEdit = QtWidgets.QCheckBox(self.groupBox_4)
        self.hostKeyEdit.setEnabled(False)
        self.hostKeyEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.hostKeyEdit.setObjectName("hostKeyEdit")
        self.gridLayout_18.addWidget(self.hostKeyEdit, 1, 2, 1, 1)
        self.useKeys = QtWidgets.QCheckBox(self.groupBox_4)
        self.useKeys.setMaximumSize(QtCore.QSize(16777215, 25))
        self.useKeys.setObjectName("useKeys")
        self.gridLayout_18.addWidget(self.useKeys, 0, 0, 1, 1)
        self.hostKeyBrowse = QtWidgets.QPushButton(self.groupBox_4)
        self.hostKeyBrowse.setEnabled(False)
        self.hostKeyBrowse.setObjectName("hostKeyBrowse")
        self.gridLayout_18.addWidget(self.hostKeyBrowse, 0, 1, 1, 1)
        self.gridLayout_19.addLayout(self.gridLayout_18, 0, 0, 1, 1)
        self.gridLayout_16.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 1, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_5.addWidget(self.scrollArea, 2, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 2, 2, 1, 1)
        self.gridLayout_25.addLayout(self.gridLayout, 1, 1, 1, 1)
        self.gridLayout_50 = QtWidgets.QGridLayout()
        self.gridLayout_50.setObjectName("gridLayout_50")
        self.send_transfer_cancel = QtWidgets.QPushButton(self.send_tab)
        self.send_transfer_cancel.setEnabled(False)
        self.send_transfer_cancel.setObjectName("send_transfer_cancel")
        self.gridLayout_50.addWidget(self.send_transfer_cancel, 0, 1, 1, 1)
        self.gridLayout_49 = QtWidgets.QGridLayout()
        self.gridLayout_49.setObjectName("gridLayout_49")
        self.totalProgress_send = QtWidgets.QProgressBar(self.send_tab)
        self.totalProgress_send.setProperty("value", 0)
        self.totalProgress_send.setObjectName("totalProgress_send")
        self.gridLayout_49.addWidget(self.totalProgress_send, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.send_tab)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_49.addWidget(self.progressBar, 1, 0, 1, 1)
        self.gridLayout_50.addLayout(self.gridLayout_49, 0, 0, 1, 1)
        self.gridLayout_25.addLayout(self.gridLayout_50, 0, 1, 1, 1)
        self.tabWidget.addTab(self.send_tab, "")
        self.get_tab = QtWidgets.QWidget()
        self.get_tab.setEnabled(True)
        self.get_tab.setObjectName("get_tab")
        self.gridLayout_47 = QtWidgets.QGridLayout(self.get_tab)
        self.gridLayout_47.setObjectName("gridLayout_47")
        self.gridLayout_23 = QtWidgets.QGridLayout()
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.gridLayout_26 = QtWidgets.QGridLayout()
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.get_tab)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, -66, 799, 576))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.gridLayout_28 = QtWidgets.QGridLayout()
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.destination_get = QtWidgets.QGroupBox(self.frame_4)
        self.destination_get.setMinimumSize(QtCore.QSize(0, 200))
        self.destination_get.setObjectName("destination_get")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.destination_get)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.gridLayout_31 = QtWidgets.QGridLayout()
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.destination_get_le = QtWidgets.QLineEdit(self.destination_get)
        self.destination_get_le.setDragEnabled(True)
        self.destination_get_le.setClearButtonEnabled(True)
        self.destination_get_le.setObjectName("destination_get_le")
        self.gridLayout_31.addWidget(self.destination_get_le, 0, 2, 1, 1)
        self.browse_get = QtWidgets.QPushButton(self.destination_get)
        self.browse_get.setObjectName("browse_get")
        self.gridLayout_31.addWidget(self.browse_get, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_31.addItem(spacerItem2, 1, 1, 1, 1)
        self.gridLayout_30.addLayout(self.gridLayout_31, 1, 0, 1, 1)
        self.gridLayout_29.addWidget(self.destination_get, 0, 0, 1, 1)
        self.gridLayout_28.addWidget(self.frame_4, 1, 0, 1, 1)
        self.source_get = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_4)
        self.source_get.setMinimumSize(QtCore.QSize(390, 350))
        self.source_get.setObjectName("source_get")
        self.gridLayout_35 = QtWidgets.QGridLayout(self.source_get)
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.gridLayout_36 = QtWidgets.QGridLayout()
        self.gridLayout_36.setObjectName("gridLayout_36")
        self.scrollArea_6 = QtWidgets.QScrollArea(self.source_get)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 362, 302))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.gridLayout_37 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_37.setObjectName("gridLayout_37")
        self.gridLayout_38 = QtWidgets.QGridLayout()
        self.gridLayout_38.setObjectName("gridLayout_38")
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents_6)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_39 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_39.setObjectName("gridLayout_39")
        self.gridLayout_40 = QtWidgets.QGridLayout()
        self.gridLayout_40.setObjectName("gridLayout_40")
        self.status_get = QtWidgets.QLabel(self.frame_5)
        self.status_get.setMinimumSize(QtCore.QSize(320, 200))
        self.status_get.setObjectName("status_get")
        self.gridLayout_40.addWidget(self.status_get, 0, 0, 1, 1)
        self.gridLayout_39.addLayout(self.gridLayout_40, 0, 0, 1, 1)
        self.gridLayout_38.addWidget(self.frame_5, 0, 0, 1, 1)
        self.gridLayout_37.addLayout(self.gridLayout_38, 0, 0, 1, 1)
        self.gridLayout_41 = QtWidgets.QGridLayout()
        self.gridLayout_41.setObjectName("gridLayout_41")
        self.get_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.get_btn.setObjectName("get_btn")
        self.gridLayout_41.addWidget(self.get_btn, 0, 0, 1, 1)
        self.check_connection_get = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.check_connection_get.setObjectName("check_connection_get")
        self.gridLayout_41.addWidget(self.check_connection_get, 0, 1, 1, 1)
        self.gridLayout_37.addLayout(self.gridLayout_41, 1, 0, 1, 1)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout_36.addWidget(self.scrollArea_6, 0, 0, 1, 1)
        self.gridLayout_35.addLayout(self.gridLayout_36, 0, 0, 1, 1)
        self.gridLayout_28.addWidget(self.source_get, 0, 0, 1, 1)
        self.gridLayout_27.addLayout(self.gridLayout_28, 1, 0, 1, 1)
        self.source_info_get = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_4)
        self.source_info_get.setObjectName("source_info_get")
        self.gridLayout_42 = QtWidgets.QGridLayout(self.source_info_get)
        self.gridLayout_42.setObjectName("gridLayout_42")
        self.frame_6 = QtWidgets.QFrame(self.source_info_get)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_43 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_43.setObjectName("gridLayout_43")
        self.gridLayout_44 = QtWidgets.QGridLayout()
        self.gridLayout_44.setObjectName("gridLayout_44")
        self.host_address_get = QtWidgets.QLineEdit(self.frame_6)
        self.host_address_get.setEnabled(False)
        self.host_address_get.setDragEnabled(True)
        self.host_address_get.setClearButtonEnabled(True)
        self.host_address_get.setObjectName("host_address_get")
        self.gridLayout_44.addWidget(self.host_address_get, 1, 1, 1, 1)
        self.passwordLabel_get = QtWidgets.QLabel(self.frame_6)
        self.passwordLabel_get.setEnabled(False)
        self.passwordLabel_get.setObjectName("passwordLabel_get")
        self.gridLayout_44.addWidget(self.passwordLabel_get, 4, 0, 1, 1)
        self.port_remote_get = QtWidgets.QSpinBox(self.frame_6)
        self.port_remote_get.setEnabled(False)
        self.port_remote_get.setMaximum(65535)
        self.port_remote_get.setProperty("value", 22)
        self.port_remote_get.setObjectName("port_remote_get")
        self.gridLayout_44.addWidget(self.port_remote_get, 2, 1, 1, 1)
        self.hostLabel_get = QtWidgets.QLabel(self.frame_6)
        self.hostLabel_get.setEnabled(False)
        self.hostLabel_get.setObjectName("hostLabel_get")
        self.gridLayout_44.addWidget(self.hostLabel_get, 1, 0, 1, 1)
        self.userLabel_get = QtWidgets.QLabel(self.frame_6)
        self.userLabel_get.setEnabled(False)
        self.userLabel_get.setObjectName("userLabel_get")
        self.gridLayout_44.addWidget(self.userLabel_get, 3, 0, 1, 1)
        self.portLabel_get = QtWidgets.QLabel(self.frame_6)
        self.portLabel_get.setEnabled(False)
        self.portLabel_get.setObjectName("portLabel_get")
        self.gridLayout_44.addWidget(self.portLabel_get, 2, 0, 1, 1)
        self.user_remote_get = QtWidgets.QLineEdit(self.frame_6)
        self.user_remote_get.setEnabled(False)
        self.user_remote_get.setDragEnabled(True)
        self.user_remote_get.setClearButtonEnabled(True)
        self.user_remote_get.setObjectName("user_remote_get")
        self.gridLayout_44.addWidget(self.user_remote_get, 3, 1, 1, 1)
        self.password_remote_get = QtWidgets.QLineEdit(self.frame_6)
        self.password_remote_get.setEnabled(False)
        self.password_remote_get.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.password_remote_get.setDragEnabled(True)
        self.password_remote_get.setClearButtonEnabled(True)
        self.password_remote_get.setObjectName("password_remote_get")
        self.gridLayout_44.addWidget(self.password_remote_get, 4, 1, 1, 1)
        self.sourceLabel_get = QtWidgets.QLabel(self.frame_6)
        self.sourceLabel_get.setEnabled(False)
        self.sourceLabel_get.setObjectName("sourceLabel_get")
        self.gridLayout_44.addWidget(self.sourceLabel_get, 5, 0, 1, 1)
        self.hostEdit_get = QtWidgets.QCheckBox(self.frame_6)
        self.hostEdit_get.setObjectName("hostEdit_get")
        self.gridLayout_44.addWidget(self.hostEdit_get, 1, 2, 1, 1)
        self.userEdit_get = QtWidgets.QCheckBox(self.frame_6)
        self.userEdit_get.setObjectName("userEdit_get")
        self.gridLayout_44.addWidget(self.userEdit_get, 3, 2, 1, 1)
        self.passwordEdit_get = QtWidgets.QCheckBox(self.frame_6)
        self.passwordEdit_get.setObjectName("passwordEdit_get")
        self.gridLayout_44.addWidget(self.passwordEdit_get, 4, 2, 1, 1)
        self.sourceEdit_get = QtWidgets.QCheckBox(self.frame_6)
        self.sourceEdit_get.setObjectName("sourceEdit_get")
        self.gridLayout_44.addWidget(self.sourceEdit_get, 5, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_44.addItem(spacerItem3, 6, 1, 1, 1)
        self.portEdit_get = QtWidgets.QCheckBox(self.frame_6)
        self.portEdit_get.setObjectName("portEdit_get")
        self.gridLayout_44.addWidget(self.portEdit_get, 2, 2, 1, 1)
        self.scrollArea_5 = QtWidgets.QScrollArea(self.frame_6)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 212, 187))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.gridLayout_33 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.gridLayout_32 = QtWidgets.QGridLayout()
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.source_le = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_5)
        self.source_le.setEnabled(False)
        self.source_le.setTabChangesFocus(True)
        self.source_le.setObjectName("source_le")
        self.gridLayout_32.addWidget(self.source_le, 0, 0, 1, 1)
        self.gridLayout_33.addLayout(self.gridLayout_32, 0, 0, 1, 1)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout_44.addWidget(self.scrollArea_5, 5, 1, 1, 1)
        self.gridLayout_43.addLayout(self.gridLayout_44, 0, 0, 1, 1)
        self.gridLayout_42.addWidget(self.frame_6, 0, 0, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(self.source_info_get)
        self.groupBox_8.setMinimumSize(QtCore.QSize(0, 150))
        self.groupBox_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_45 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_45.setObjectName("gridLayout_45")
        self.gridLayout_46 = QtWidgets.QGridLayout()
        self.gridLayout_46.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_46.setObjectName("gridLayout_46")
        self.hostKeyLabel_get = QtWidgets.QLabel(self.groupBox_8)
        self.hostKeyLabel_get.setEnabled(False)
        self.hostKeyLabel_get.setMaximumSize(QtCore.QSize(16777215, 25))
        self.hostKeyLabel_get.setObjectName("hostKeyLabel_get")
        self.gridLayout_46.addWidget(self.hostKeyLabel_get, 1, 0, 1, 1)
        self.hostKey_get = QtWidgets.QLineEdit(self.groupBox_8)
        self.hostKey_get.setEnabled(False)
        self.hostKey_get.setMaximumSize(QtCore.QSize(16777215, 25))
        self.hostKey_get.setDragEnabled(True)
        self.hostKey_get.setClearButtonEnabled(True)
        self.hostKey_get.setObjectName("hostKey_get")
        self.gridLayout_46.addWidget(self.hostKey_get, 1, 1, 1, 1)
        self.hostKeyEdit_get = QtWidgets.QCheckBox(self.groupBox_8)
        self.hostKeyEdit_get.setEnabled(False)
        self.hostKeyEdit_get.setMaximumSize(QtCore.QSize(16777215, 25))
        self.hostKeyEdit_get.setObjectName("hostKeyEdit_get")
        self.gridLayout_46.addWidget(self.hostKeyEdit_get, 1, 2, 1, 1)
        self.useKeys_get = QtWidgets.QCheckBox(self.groupBox_8)
        self.useKeys_get.setMaximumSize(QtCore.QSize(16777215, 25))
        self.useKeys_get.setObjectName("useKeys_get")
        self.gridLayout_46.addWidget(self.useKeys_get, 0, 0, 1, 1)
        self.hostKeyBrowse_get = QtWidgets.QPushButton(self.groupBox_8)
        self.hostKeyBrowse_get.setEnabled(False)
        self.hostKeyBrowse_get.setObjectName("hostKeyBrowse_get")
        self.gridLayout_46.addWidget(self.hostKeyBrowse_get, 0, 1, 1, 1)
        self.gridLayout_45.addLayout(self.gridLayout_46, 0, 0, 1, 1)
        self.gridLayout_42.addWidget(self.groupBox_8, 1, 0, 1, 1)
        self.gridLayout_27.addWidget(self.source_info_get, 1, 1, 1, 1)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_26.addWidget(self.scrollArea_4, 2, 1, 1, 1)
        self.gridLayout_23.addLayout(self.gridLayout_26, 2, 2, 1, 1)
        self.gridLayout_47.addLayout(self.gridLayout_23, 2, 0, 1, 1)
        self.gridLayout_34 = QtWidgets.QGridLayout()
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.gridLayout_48 = QtWidgets.QGridLayout()
        self.gridLayout_48.setObjectName("gridLayout_48")
        self.progressBar_get = QtWidgets.QProgressBar(self.get_tab)
        self.progressBar_get.setProperty("value", 0)
        self.progressBar_get.setTextVisible(True)
        self.progressBar_get.setInvertedAppearance(False)
        self.progressBar_get.setObjectName("progressBar_get")
        self.gridLayout_48.addWidget(self.progressBar_get, 1, 0, 1, 1)
        self.totalProgress_get = QtWidgets.QProgressBar(self.get_tab)
        self.totalProgress_get.setProperty("value", 0)
        self.totalProgress_get.setObjectName("totalProgress_get")
        self.gridLayout_48.addWidget(self.totalProgress_get, 0, 0, 1, 1)
        self.gridLayout_34.addLayout(self.gridLayout_48, 1, 1, 1, 1)
        self.get_transfer_cancel = QtWidgets.QPushButton(self.get_tab)
        self.get_transfer_cancel.setEnabled(False)
        self.get_transfer_cancel.setObjectName("get_transfer_cancel")
        self.gridLayout_34.addWidget(self.get_transfer_cancel, 1, 2, 1, 1)
        self.gridLayout_47.addLayout(self.gridLayout_34, 0, 0, 1, 1)
        self.tabWidget.addTab(self.get_tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        scp_qt.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(scp_qt)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 859, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        scp_qt.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(scp_qt)
        self.statusbar.setObjectName("statusbar")
        scp_qt.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(scp_qt)
        self.actionQuit.setObjectName("actionQuit")
        self.actionUse_Last_Transaction = QtWidgets.QAction(scp_qt)
        self.actionUse_Last_Transaction.setObjectName("actionUse_Last_Transaction")
        self.actionHistory = QtWidgets.QAction(scp_qt)
        self.actionHistory.setObjectName("actionHistory")
        self.action_Configure = QtWidgets.QAction(scp_qt)
        self.action_Configure.setObjectName("action_Configure")
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addAction(self.actionUse_Last_Transaction)
        self.menuFile.addAction(self.actionHistory)
        self.menuFile.addAction(self.action_Configure)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(scp_qt)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(scp_qt)

    def retranslateUi(self, scp_qt):
        _translate = QtCore.QCoreApplication.translate
        scp_qt.setWindowTitle(_translate("scp_qt", "scp-qt"))
        self.groupBox.setTitle(_translate("scp_qt", "Source"))
        self.browse.setText(_translate("scp_qt", "Browse"))
        self.sendDirectory.setText(_translate("scp_qt", "Send Directory"))
        self.appendSource.setText(_translate("scp_qt", "&Append To List"))
        self.clearSources.setText(_translate("scp_qt", "&Clear List"))
        self.groupBox_2.setTitle(_translate("scp_qt", "Destination"))
        self.status.setText(_translate("scp_qt", "Status"))
        self.send.setText(_translate("scp_qt", "Send"))
        self.connect.setText(_translate("scp_qt", "Check Connection"))
        self.groupBox_3.setTitle(_translate("scp_qt", "Destination Information"))
        self.passwordLabel.setText(_translate("scp_qt", "Password"))
        self.hostLabel.setText(_translate("scp_qt", "Host"))
        self.userLabel.setText(_translate("scp_qt", "User"))
        self.portLabel.setText(_translate("scp_qt", "Port"))
        self.destinationLabel.setText(_translate("scp_qt", "Destination"))
        self.hostEdit.setText(_translate("scp_qt", "edit"))
        self.portEdit.setText(_translate("scp_qt", "edit"))
        self.userEdit.setText(_translate("scp_qt", "edit"))
        self.passwordEdit.setText(_translate("scp_qt", "edit"))
        self.destinationEdit.setText(_translate("scp_qt", "edit"))
        self.groupBox_4.setTitle(_translate("scp_qt", "HostKey"))
        self.hostKeyLabel.setText(_translate("scp_qt", "HostKey"))
        self.hostKeyEdit.setText(_translate("scp_qt", "Edit"))
        self.useKeys.setText(_translate("scp_qt", "Use Host Key"))
        self.hostKeyBrowse.setText(_translate("scp_qt", "Browse"))
        self.send_transfer_cancel.setText(_translate("scp_qt", "Cancel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.send_tab), _translate("scp_qt", "Send"))
        self.destination_get.setTitle(_translate("scp_qt", "Destination"))
        self.browse_get.setText(_translate("scp_qt", "Browse"))
        self.source_get.setTitle(_translate("scp_qt", "Source"))
        self.status_get.setText(_translate("scp_qt", "Status"))
        self.get_btn.setText(_translate("scp_qt", "Get"))
        self.check_connection_get.setText(_translate("scp_qt", "Check Connection"))
        self.source_info_get.setTitle(_translate("scp_qt", "Source Information"))
        self.passwordLabel_get.setText(_translate("scp_qt", "Password"))
        self.hostLabel_get.setText(_translate("scp_qt", "Host"))
        self.userLabel_get.setText(_translate("scp_qt", "User"))
        self.portLabel_get.setText(_translate("scp_qt", "Port"))
        self.sourceLabel_get.setText(_translate("scp_qt", "Source"))
        self.hostEdit_get.setText(_translate("scp_qt", "edit"))
        self.userEdit_get.setText(_translate("scp_qt", "edit"))
        self.passwordEdit_get.setText(_translate("scp_qt", "edit"))
        self.sourceEdit_get.setText(_translate("scp_qt", "edit"))
        self.portEdit_get.setText(_translate("scp_qt", "edit"))
        self.groupBox_8.setTitle(_translate("scp_qt", "HostKey"))
        self.hostKeyLabel_get.setText(_translate("scp_qt", "HostKey"))
        self.hostKeyEdit_get.setText(_translate("scp_qt", "Edit"))
        self.useKeys_get.setText(_translate("scp_qt", "Use Host Key"))
        self.hostKeyBrowse_get.setText(_translate("scp_qt", "Browse"))
        self.get_transfer_cancel.setText(_translate("scp_qt", "Cancel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.get_tab), _translate("scp_qt", "Get"))
        self.menuFile.setTitle(_translate("scp_qt", "&File"))
        self.actionQuit.setText(_translate("scp_qt", "&Quit"))
        self.actionQuit.setShortcut(_translate("scp_qt", "Ctrl+Q"))
        self.actionUse_Last_Transaction.setText(_translate("scp_qt", "Use &Last Transaction"))
        self.actionHistory.setText(_translate("scp_qt", "&History"))
        self.action_Configure.setText(_translate("scp_qt", "&Configure"))

