# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/historyView.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_configView(object):
    def setupUi(self, configView):
        configView.setObjectName("configView")
        configView.resize(591, 539)
        self.gridLayout_2 = QtWidgets.QGridLayout(configView)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.clear = QtWidgets.QPushButton(configView)
        self.clear.setObjectName("clear")
        self.gridLayout_3.addWidget(self.clear, 1, 1, 1, 1)
        self.close = QtWidgets.QPushButton(configView)
        self.close.setObjectName("close")
        self.gridLayout_3.addWidget(self.close, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(configView)
        self.frame.setMinimumSize(QtCore.QSize(0, 450))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 547, 462))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(configView)
        QtCore.QMetaObject.connectSlotsByName(configView)

    def retranslateUi(self, configView):
        _translate = QtCore.QCoreApplication.translate
        configView.setWindowTitle(_translate("configView", "Dialog"))
        self.clear.setText(_translate("configView", "Clear"))
        self.close.setText(_translate("configView", "Close"))

