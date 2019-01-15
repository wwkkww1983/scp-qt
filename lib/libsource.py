#! /usr/bin/env python3

from PyQt5 import QtWidgets,QtGui,QtCore
import os,sys

class source:
    def __init__(self):
        pass
    def setDestination(self):
        files=self.openFile(mode='dirs',windowTitle='Set Your Destination')
        if os.path.exists(files[0]):
            self.destination_get_le.setText(files[0])

    def setSource(self):
        if not self.sendDirectory.isChecked():
            files=self.openFile(mode='files',windowTitle='Open')
        if self.sendDirectory.isChecked():
            files=self.openFile(mode='dirs',windowTitle='Open Directory')
        self.sources.setText('\n'.join(files))
        print(self.in_config['sources'])

    def append_source(self):
        if not self.sendDirectory.isChecked():
            files=self.openFile(mode='files',windowTitle='Open')
        if self.sendDirectory.isChecked():
            files=self.openFile(mode='dirs',windowTitle='Open Directory')
        oldList=self.in_config['sources']
        print(oldList)
        if files != False:
            oldList.extend(files)
        self.sources.setText('\n'.join(oldList))
        print(self.in_config['sources'])

    def clear_sources(self):
        self.sources.setText('')
        self.in_config['sources']=[]

    def get_destination_buttons(self):
        self.browse_get.clicked.connect(self.setDestination)

    def source_buttons(self):
        self.browse.clicked.connect(self.setSource)
        self.appendSource.clicked.connect(self.append_source)
        self.clearSources.clicked.connect(self.clear_sources)
        self.get_destination_buttons()

    def saveFields(self):
        self.in_config['sources']=self.sources.toPlainText().split('\n')

    def source_fields(self):
        self.sources.textChanged.connect(self.saveFields)

    def source_init(self):
        self.source_buttons()
        self.source_fields()
