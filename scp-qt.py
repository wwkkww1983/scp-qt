#! /usr/bin/env python3
from PyQt5 import QtWidgets,QtCore,QtGui
import sys,os,tarfile,gzip,json
lib=['./lib','./lib_widget']
for l in lib:
    sys.path.insert(0,l)
import scp_qt
import libssh,libcontrols
import libdestination
import libsource
import libsftp_getdirs
import scp_qt_tray
import libhistory
import json

class scp(QtWidgets.QMainWindow,scp_qt.Ui_scp_qt,libssh.ssh,libcontrols.controls,libdestination.dest,libsource.source,libsftp_getdirs.sftp_get):
    iconPathTray='./icons/icon-tray.png'
    tray_menu=None
    tray_maximize=None
    tray_minimize=None
    tray_show=None
    hist=None
    hist_d=None

    def tray_actions_setup(self):
        self.tray_maximize=QtWidgets.QAction('&Maximize')
        self.tray_maximize.triggered.connect(lambda: self.setWindowState(QtCore.Qt.WindowMaximized))
        self.tray_minimize=QtWidgets.QAction('M&inimize')
        self.tray_minimize.triggered.connect(lambda: self.setWindowState(QtCore.Qt.WindowMinimized))
        self.tray_show=QtWidgets.QAction('&Show Window')
        self.tray_show.triggered.connect(lambda: self.setWindowState(QtCore.Qt.WindowActive))

    def tray_context_menu(self):
        self.tray_actions_setup()
        self.tray_menu=QtWidgets.QMenu(self)
        self.tray_menu.addAction(self.tray_maximize)
        self.tray_menu.addAction(self.tray_minimize)
        self.tray_menu.addAction(self.tray_show)


    def tray_message(self,tray,reason):
        if self.fileGet != '' and self.fileSend != '':
            msg='Total Completed\nTx: {}% - {} \n Rx: {}% - {}'.format(
                        self.totalProgress_send.value(),
                        self.fileSend,
                        self.totalProgress_get.value(),
                        self.fileGet,
                        )
        elif self.fileGet != '':
            msg='Total Completed\nRx: {}% - {}'.format(self.totalProgress_get.value(),self.fileGet)
        elif self.fileSend != '':
            msg='Total Completed\nTx: {}% - {}'.format(self.totalProgress_send.value(),self.fileSend)
        else:
            msg='Idle!'

        if reason == QtWidgets.QSystemTrayIcon.Trigger:
            tray.showMessage(
                msg, 
                'Information',
                25,
                )
                    
    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self) 
        self.controls_init()
        self.destination_init()
        self.source_init()
        for k,o in [['send',self.status],['get',self.status_get]]:
            self.statusColor(status=False,tab=k,obj=o)
        
        qdialog=QtWidgets.QDialog(self)
        dialog=scp_qt_tray.Ui_tray()
        dialog.setupUi(qdialog)

        tray=QtWidgets.QSystemTrayIcon(QtGui.QIcon(self.iconPathTray),self)
        tray.activated.connect(lambda reason: self.tray_message(tray,reason) )
        self.tray_context_menu()
        tray.setContextMenu(self.tray_menu)
        tray.show()

    def loadHistory(self):
        self.hist=libhistory.history()
        self.hist_d=self.hist.viewer_setup(self)
        self.hist_d['viewer']['0']['dialog'].show() 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    cp=scp()
    cp.show()
    app.exec_()
