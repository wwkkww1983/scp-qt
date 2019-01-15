#! /usr/bin/python3
from PyQt5 import QtWidgets
import sys
class controls:
    def __init__(self):
        pass

    def quitApp(self):
        print('quitting application')
        sys.exit()

    def actions_shortcuts(self):
        print('setting up actions!')
        self.actionQuit.triggered.connect(self.quitApp),   
        self.actionUse_Last_Transaction.triggered.connect(self.transHistory_loadLast)
        self.actionHistory.triggered.connect(self.loadHistory)
        print('settings up actions done!')

    def buttons(self):
        self.check_connection_get.clicked.connect(lambda: self.check_connection(tab='get',obj=self.status_get))
        self.get_btn.clicked.connect(lambda: self.get_sources(tab='get',status_obj=self.status_get))
        
        self.get_transfer_cancel.clicked.connect(lambda: self.stopTransfer(tab='get'))
        self.send_transfer_cancel.clicked.connect(lambda: self.stopTransfer(tab='send'))

        self.connect.clicked.connect(lambda: self.check_connection(tab='send',obj=self.status))
        self.send.clicked.connect(lambda: self.send_sources(tab='send',status_obj=self.status))

    def controls_init(self):
        self.actions_shortcuts()
        self.buttons()
