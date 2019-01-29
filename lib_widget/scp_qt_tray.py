# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/scp_qt_tray.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_tray(object):
    def setupUi(self, tray):
        tray.setObjectName("tray")
        tray.resize(400, 300)
        self.gridLayout_2 = QtWidgets.QGridLayout(tray)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(tray)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.get_transfer_cancel = QtWidgets.QPushButton(self.frame)
        self.get_transfer_cancel.setObjectName("get_transfer_cancel")
        self.gridLayout_5.addWidget(self.get_transfer_cancel, 0, 2, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.totalProgress_get = QtWidgets.QProgressBar(self.frame)
        self.totalProgress_get.setProperty("value", 0)
        self.totalProgress_get.setObjectName("totalProgress_get")
        self.gridLayout_4.addWidget(self.totalProgress_get, 0, 0, 1, 1)
        self.current_progress_get = QtWidgets.QProgressBar(self.frame)
        self.current_progress_get.setProperty("value", 0)
        self.current_progress_get.setObjectName("current_progress_get")
        self.gridLayout_4.addWidget(self.current_progress_get, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(tray)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.send_transfer_cancel = QtWidgets.QPushButton(self.frame_2)
        self.send_transfer_cancel.setObjectName("send_transfer_cancel")
        self.gridLayout_7.addWidget(self.send_transfer_cancel, 0, 2, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.current_progress_send = QtWidgets.QProgressBar(self.frame_2)
        self.current_progress_send.setProperty("value", 0)
        self.current_progress_send.setObjectName("current_progress_send")
        self.gridLayout_3.addWidget(self.current_progress_send, 3, 0, 1, 1)
        self.totalProgress_send = QtWidgets.QProgressBar(self.frame_2)
        self.totalProgress_send.setProperty("value", 0)
        self.totalProgress_send.setObjectName("totalProgress_send")
        self.gridLayout_3.addWidget(self.totalProgress_send, 2, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(tray)
        QtCore.QMetaObject.connectSlotsByName(tray)

    def retranslateUi(self, tray):
        _translate = QtCore.QCoreApplication.translate
        tray.setWindowTitle(_translate("tray", "Dialog"))
        self.get_transfer_cancel.setText(_translate("tray", "Cancel"))
        self.label_2.setText(_translate("tray", "Rx"))
        self.send_transfer_cancel.setText(_translate("tray", "Cancel"))
        self.label.setText(_translate("tray", "Tx."))

