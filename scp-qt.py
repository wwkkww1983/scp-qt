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
import libconfig
import libstatements as state
import config,libconfigure

class scp(QtWidgets.QMainWindow,scp_qt.Ui_scp_qt,libssh.ssh,libcontrols.controls,libdestination.dest,libsource.source,libsftp_getdirs.sftp_get,state.statements):
    iconPathTray='./icons/icon-tray.png'
    tray_menu=None
    tray_maximize=None
    tray_minimize=None
    tray_show=None
    hist=None
    hist_d=None
    configJson={}
    #needs a path other than .
    configJsonFile='./config.json'
    dateformat='%S.%M.%H-%d.%m.%Y'
    conf_d={}
    def load_config(self):
        if os.path.exists(self.configJsonFile) and os.path.isfile(self.configJsonFile):
            with open(self.configJsonFile,'r') as cfg:
                self.configJson=json.load(cfg)

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

    def init_config(self):
        fails=[False,None,'',0]
        if 'icon-tray-path' in self.configJson.keys():
            if self.configJson['icon-tray-path'] not in [False,None,'']:
                iconPathConfig=os.path.abspath(
                        os.path.expanduser(
                            os.path.expandvars(
                                self.configJson['icon-tray-path']
                                )
                            )
                        )
            if os.path.exists(iconPathConfig):
                self.IconPathTray=iconPathConfig

        if self.configJson['beColorful'] == False:
            #this is the tag that is used in the db to pull the phrases set
            self.vul='disable'
        else:
            self.vul=self.configJson['beColorful-tag']
        if 'dateformat' in self.configJson.keys():
            if self.configJson['dateformat'] in [False,None,'']:
                self.configJson['dateformat']=self.dateformat
        if 'maxHistorySize' in self.configJson.keys():
            if self.configJson['maxHistorySize'] in [False,None,'',0]:
                self.configJson['maxHistorySize']=1024**2
        else:
            self.configJson['maxHistorySize']=1024**2

        if 'beColorfulDB' in self.configJson.keys():
            if self.configJson['beColorfulDB'] in fails:
                self.configJson['beColorfulDB']='./statements.db'
        else:
            self.configJson['beColorfulDB']='./statements.db'


        if 'historyCache' in self.configJson.keys():
            if self.configJson['historyCache'] in fails:
                self.configJson['historyCache']='./back_history'
        else:
            self.configJson['historyCache']='./back_history'

        if 'historyFile' in self.configJson.keys():
            if self.configJson['historyFile'] in fails:
                self.configJson['historyFile']='./history.json'
        else:
            self.configJson['historyFile']='./history.json'
        
        if 'ssh-dir' in self.configJson.keys():
            if self.configJson['ssh-dir'] in fails:
                self.configJson['ssh-dir']='~/.ssh'
        else:
            self.configJson['ssh-dir']='~/.ssh'
        
        if 'known-hosts' in self.configJson.keys():
            if self.configJson['known-hosts'] in fails:
                self.configJson['known-hosts']='~/.ssh/known-hosts'
        else:
            self.configJson['known-hosts']='~/.ssh/known-hosts'

        if 'app-icon-path' in self.configJson.keys():
            if self.configJson['app-icon-path'] in fails:
                self.configJson['app-icon-path']='./icons/scp-qt.png'
        else:
            self.configJson['app-icon-path']='./icons/scp-qt.png'

        parts=[
                [
                    'statusColor-bad',
                    [255,10,0],
                    [255,10,0]],
                [
                    'statusColor-inprogress',
                    [255,0,0],
                    [255,120,0],
                    ],
                [
                    'statusColor-good',
                    [73,73,73],
                    [10,190,20],
                    ],
            ]
        for t,r,c in parts:
            self.setColors(t,r,c,fails)

        for key in self.configJson.keys():
            print('{} : {} = {}'.format(self.sayit(tag=self.vul),key,self.configJson[key]))

    def setColors(self,Type,r,c,fails):
        if Type in self.configJson.keys():
            if self.configJson[Type] in fails:
                self.configJson[Type]['ring']['rgb']=tuple(r)
                self.configJson[Type]['core']['rgb']=tuple(c)
            else:
                self.configJson[Type]['ring']['rgb']=tuple(
                        self.configJson[Type]['ring']['rgb']
                        )
                self.configJson[Type]['core']['rgb']=tuple(
                        self.configJson[Type]['core']['rgb']
                        )
        else:
            self.configJson[Type]={}
            self.configJson[Type]['ring']['rgb']=tuple(r)
            self.configJson[Type]['core']['rgb']=tuple(c)


    def __init__(self):
        super(self.__class__,self).__init__()
        self.load_config()
        self.init_config()
        
        self.conf_d['dialog']=QtWidgets.QDialog(self)
        self.conf_d['obj']=config.Ui_configure()
        self.conf_d['obj'].setupUi(self.conf_d['dialog'])
        self.conf_d['controls']=libconfigure.configure(self)

        print('{} : starting scp-qt.py'.format(self.sayit(tag=self.vul)))
        cnf=libconfig.config_init(self)
        res=cnf.configurator()
        if res == False:
            exit(1)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(self.configJson['app-icon-path']))
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

    def closeAll(self):
        print('SCREAM! : User is Quitting!')
        self.stopTRX['get']=True
        self.stopTRX['send']=True

    def loadHistory(self):
        self.hist=libhistory.history()
        self.hist_d=self.hist.viewer_setup(self)
        self.hist.setClearState(self)
        self.hist_d['viewer']['0']['dialog'].show() 

    def closeEvent(self,event):
        for tab in ['get','send']:
            self.stopTransfer(tab)
        self.closeAll()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    cp=scp()
    cp.show()
    app.exec_()
