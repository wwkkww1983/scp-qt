#! /usr/bin/env python3
import os,time,json,sys
from PyQt5 import QtWidgets,QtGui,QtCore
import copy,hashlib

class configure:
    config='config.json'
    config_temp={
	"default-dirs":{
		"get":"~/scp-qt-GET",
		"send":"~/scp-qt-SEND"
	},
	"beColorfulDB":"./statements.db",
	"beColorful":True,
	"beColorful-tag":"fiendish",
	"skipChecksumLog":False,
	"checksumType":"sha512",
	"icon-tray-path":"./icons/icon-tray.png",
	"dateformat":"%S.%M.%H-%d.%m.%Y",
	"maxHistorySize":1048576,
	"historyCache":"./back_history",
	"historyFile":"./history.json",
	"ssh-dir":"~/.ssh",
	"statusColor-bad":{
		"core":{
			"rgb":[255,0,20],
			"alpha":255
		},
		"ring":{
			"rgb":[200,10,0],
			"alpha":255
		}
	},
	"statusColor-inprogress":{
		"core":{
			"rgb":[255,0,0],
			"alpha":255
		},
		"ring":{
			"rgb":[255,120,0],
			"alpha":255
		}
	},
	"statusColor-good":{
		"core":{
			"rgb":[73,73,73],
			"alpha":255
		},
		"ring":{
			"rgb":[10,190,20],
			"alpha":255
		}
	},
	"known-hosts":"~/.ssh/known_hosts"
    }
    def __init__(class_self,self):
        class_self.parent=self
        
        #load config defaults
        class_self.load_config()

        #set buttons for color selection
        class_self.connect_buttons_colors()
        
        #class_self.connect_buttons_main() below
        class_self.buttons_connect()
  
    def setChecksumTypes(self):
        available=hashlib.algorithms_available
        for t in available:
            cb=self.parent.conf_d['dialog'].findChild(QtWidgets.QComboBox,'checksumType')
            if cb != None:
                cb.addItem(t)

    def load_config(self):
        #print(self.parent.configJson)
        self.setDefaultsColorView()
        self.config_temp=copy.deepcopy(self.parent.configJson)
        self.setChecksumTypes()

        self.load_fields()
        #print(id(self.config_temp),id(self.parent.configJson))

    def setDefaultsColorView(self):
        viewer=self.parent.conf_d['dialog']
        objects=[
        ['statusColor_ring_bad',self.parent.configJson["statusColor-bad"]["ring"]["rgb"]],
        ['statusColor_core_bad',self.parent.configJson["statusColor-bad"]["core"]["rgb"]],
        ['statusColor_ring_good',self.parent.configJson["statusColor-good"]["ring"]["rgb"]],
        ['statusColor_core_good',self.parent.configJson["statusColor-good"]["core"]["rgb"]],
        ['statusColor_ring_inProgress',self.parent.configJson["statusColor-inprogress"]["ring"]["rgb"]],
        ['statusColor_core_inProgress',self.parent.configJson["statusColor-inprogress"]["core"]["rgb"]],
        ]
        for obj in objects:
            color=QtGui.QColor(obj[1][0],obj[1][1],obj[1][2])
            label=viewer.findChild(QtWidgets.QLabel,obj[0])
            label.setAutoFillBackground(True)
            pal=QtGui.QPalette()
            pal.setColor(QtGui.QPalette.Background,color)
            label.setPalette(pal)
            label.setText('')
            #print('init : {} {}'.format(obj[0],label))

    def show(self):
        self.load_config()
        self.parent.conf_d['dialog'].show()

    def reset_config(self):
        print('reset clicked')

    def close_config(self):
        print('close clicked')
        self.parent.conf_d['dialog'].close()

    def load_fields(self):
        fields=[
                [
                    'defaultDir_send',
                    QtWidgets.QLineEdit,
                    self.config_temp['default-dirs']['send']
                ],
                [
                    'defaultDir_get',
                    QtWidgets.QLineEdit,
                    self.config_temp['default-dirs']['get']    
                ],
                [
                    'statementsDB',
                    QtWidgets.QLineEdit,
                    self.config_temp['beColorfulDB']
                ],
                [
                    'statements_tag',
                    QtWidgets.QLineEdit,
                    self.config_temp['beColorful-tag']
                ],
                [
                    'beColorful',
                    QtWidgets.QCheckBox,
                    self.config_temp['beColorful']
                ],
                [
                    'useChecksum',
                    QtWidgets.QCheckBox,
                    self.config_temp['skipChecksumLog']
                ],
                [
                    'checksumType',
                    QtWidgets.QComboBox,
                    self.config_temp['checksumType']
                ],
                [
                    'icon_tray_path',
                    QtWidgets.QLineEdit,
                    self.config_temp['icon-tray-path']
                ],
                [
                    'dateformat',
                    QtWidgets.QLineEdit,
                    self.config_temp['dateformat']
                ],
                [
                    'maxHistorySize',
                    QtWidgets.QSpinBox,
                    self.config_temp['maxHistorySize']
                ],
                [
                    'historyCache',
                    QtWidgets.QLineEdit,
                    self.config_temp['historyCache']
                ],
                [
                    'historyFile',
                    QtWidgets.QLineEdit,
                    self.config_temp['historyFile']
                ],
                [
                    'ssh_dir',
                    QtWidgets.QLineEdit,
                    self.config_temp['ssh-dir']
                ],
                [
                    'known_hosts',
                    QtWidgets.QLineEdit,
                    self.config_temp['known-hosts']
                ],
            ]
        for obj in fields:
            obj.append(self.parent.conf_d['dialog'].findChild(obj[1],obj[0]))
            if obj[1] == QtWidgets.QLineEdit:
                obj[-1].setText(obj[2])
            if obj[1] == QtWidgets.QCheckBox:
                if obj[0] in ['useChecksum']:
                    state=not obj[2]
                else:
                    state=obj[2]
                obj[-1].setChecked(state)

            if obj[1] == QtWidgets.QSpinBox:
                obj[-1].setValue(obj[2])
            if obj[1] == QtWidgets.QComboBox:
                index=obj[-1].findText(obj[2],QtCore.Qt.MatchExactly)
                if index != None:
                    obj[-1].setCurrentIndex(index)
                
        #print(fields)

    def save_config(self):
        print('save clicked : {}'.format(self.config_temp))
        self.parent.configJson=copy.deepcopy(self.config_temp)
        with open(self.config,'w') as cnf:
            json.dump(self.parent.configJson,cnf)
        python=sys.executable
        os.execl(python,python,* sys.argv)

    def buttons_connect(self):
        buttons=[
                ['reset',self.reset_config],
                ['close',self.close_config],
                ['save',self.save_config],
                ]
        for obj in buttons:
            obj.append(self.parent.conf_d['dialog'].findChild(QtWidgets.QPushButton,obj[0]))
            obj[2].clicked.connect(obj[1])

    def colorChanged(self,label,color):
        color_as_tuple=color.getRgb()
        pal=QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Background,color)
        self.parent.conf_d['dialog'].findChild(QtWidgets.QLabel,label).setAutoFillBackground(True)
        self.parent.conf_d['dialog'].findChild(QtWidgets.QLabel,label).setPalette(pal)
        self.parent.conf_d['dialog'].findChild(QtWidgets.QLabel,label).setText('')
        parts=label.split('_')
        key1='{}-{}'.format(parts[0],parts[2].lower())
        self.config_temp[key1][parts[1]]['rgb']=color.getRgb()[:3]
        self.config_temp[key1][parts[1]]['alpha']=color.getRgb()[-1]
        #print(id(self.parent.configJson),id(self.config_temp))
        
    def colors(self):
        label=self.parent.sender().objectName().replace("select_","")
        #print('selecting color: {}'.format(label))
        dialog=QtWidgets.QColorDialog() 
        #dialog.setStandardColor(0,self.parent.conf_d['dialog'].findChild(QtWidgets.QLabel,label).palette().color(QtGui.QPalette.Background))
        dialog.setCustomColor(0,self.parent.conf_d['dialog'].findChild(QtWidgets.QLabel,label).palette().color(QtGui.QPalette.Background))
        initial=self.parent.conf_d['dialog'].findChild(QtWidgets.QLabel,label).palette().color(QtGui.QPalette.Background)
        color=dialog.getColor(initial)
        if color.isValid() == True:
            self.colorChanged(label,color)
 
    def connect_buttons_colors(self):
        objects=[
        ['select_statusColor_ring_bad'],
        ['select_statusColor_core_bad'],
        ['select_statusColor_ring_good'],
        ['select_statusColor_core_good'],
        ['select_statusColor_ring_inProgress'],
        ['select_statusColor_core_inProgress'],
        ]
        for obj in objects:
            obj.append(self.parent.conf_d['dialog'].findChild(QtWidgets.QPushButton,obj[0]))
            obj.append(self.parent.conf_d['dialog'].findChild(QtWidgets.QLabel,obj[0].replace('select_','')))
            obj[1].clicked.connect(self.colors)
            #print(obj)

        #.clicked.connect(lambda: self.colors(obj[0]))
        #print(button,obj[0])

        #self.parent.conf_d['obj'].select_statusColor_core_bad.clicked.connect(lambda: self.colors(self.parent.conf_d['obj'].select_statusColor_core_bad.objectName()))
