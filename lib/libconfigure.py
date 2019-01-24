#! /usr/bin/env python3
import os,time,json
from PyQt5 import QtWidgets,QtGui

class configure:
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
        class_self.config_temp=class_self.parent.configJson
        class_self.connect_buttons_colors()
        class_self.setDefaultsColorView()
        #class_self.connect_buttons_main()
        
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
            #color.setRed(obj[1][0])
            #color.setBlue(obj[1][1])
            #color.setGreen(obj[1][2])
            label=viewer.findChild(QtWidgets.QLabel,obj[0])
            label.setAutoFillBackground(True)
            pal=QtGui.QPalette()
            pal.setColor(QtGui.QPalette.Background,color)
            label.setPalette(pal)
            label.setText('')
            print('init : {} {}'.format(obj[0],label))

    def colorChanged(self,label,color):
        color_as_tuple=color.getRgb()
        pal=QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Background,color)
        self.parent.conf_d['dialog'].findChild(QtWidgets.QLabel,label).setAutoFillBackground(True)
        self.parent.conf_d['dialog'].findChild(QtWidgets.QLabel,label).setPalette(pal)
        self.parent.conf_d['dialog'].findChild(QtWidgets.QLabel,label).setText('')
        parts=label.split('_')
        key1='{}-{}'.format(parts[0],parts[2])
        self.config_temp[key1][parts[1]]=color.getRgb()[:3]
        print(self.config_temp[key1][parts[1]])
        
    def colors(self):
        label=self.parent.sender().objectName().replace("select_","")
        print('selecting color: {}'.format(label))
        dialog=QtWidgets.QColorDialog() 
        #dialog.setStandardColor(0,self.parent.conf_d['dialog'].findChild(QtWidgets.QLabel,label).palette().color(QtGui.QPalette.Background))
        dialog.setCustomColor(0,self.parent.conf_d['dialog'].findChild(QtWidgets.QLabel,label).palette().color(QtGui.QPalette.Background))
        initial=self.parent.conf_d['dialog'].findChild(QtWidgets.QLabel,label).palette().color(QtGui.QPalette.Background)
        color=dialog.getColor(initial)
        if color.isValid() == True:
            self.colorChanged(label,color)

    def p(self):
        print(self.parent.sender())

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
            print(obj)

        #.clicked.connect(lambda: self.colors(obj[0]))
        #print(button,obj[0])

        #self.parent.conf_d['obj'].select_statusColor_core_bad.clicked.connect(lambda: self.colors(self.parent.conf_d['obj'].select_statusColor_core_bad.objectName()))
