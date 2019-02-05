#! /usr/bin/env python3
import os,time,json,sys
from PyQt5 import QtWidgets,QtGui,QtCore
import copy,hashlib

path='.'
lib=('{}/lib','{}/lib_widget')
for i in lib:
    sys.path.insert(0,i.format(path))

from libdestination import dest 
openFile=dest.openFile

class configure:
    supportedImgs='PNG (*.png);;JPG (*.jpg);;JPEG (*.jpeg)'
    config='config.json'
    config_temp={
        "app-icon-path":"./icons/scp-qt.png",
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
        for i in self.getAllTags():
            self.conf_d['obj'].statements_tag.addItem(i)       
        #load config defaults
        class_self.load_config()

        #set buttons for color selection
        class_self.connect_buttons_colors()
        
        #class_self.connect_buttons_main() below
        class_self.buttons_connect()
        #non-button connections
        class_self.setConnections()
        class_self.timed()

    def setConnections(self):
        self.parent.conf_d['obj'].defaultDir_send.textChanged.connect(lambda: self.assignVal(self.parent.conf_d['obj'].defaultDir_send,self.parent.conf_d['obj'].defaultDir_send.text()))
        self.parent.conf_d['obj'].defaultDir_get.textChanged.connect(lambda: self.assignVal(self.parent.conf_d['obj'].defaultDir_get,self.parent.conf_d['obj'].defaultDir_get.text()))
        self.parent.conf_d['obj'].statementsDB.textChanged.connect(lambda: self.assignVal(self.parent.conf_d['obj'].statementsDB,self.parent.conf_d['obj'].statementsDB.text()))

        self.parent.conf_d['obj'].statements_tag.currentIndexChanged.connect(lambda: self.assignVal(self.parent.conf_d['obj'].statements_tag,self.parent.conf_d['obj'].statements_tag.currentText()))
        
        self.parent.conf_d['obj'].beColorful.toggled.connect(lambda: self.assignVal(self.parent.conf_d['obj'].beColorful,self.parent.conf_d['obj'].beColorful.isChecked()))
        self.parent.conf_d['obj'].useChecksum.toggled.connect(lambda: self.assignVal(self.parent.conf_d['obj'].useChecksum,self.parent.conf_d['obj'].useChecksum.isChecked()))
        self.parent.conf_d['obj'].checksumType.currentIndexChanged.connect(lambda: self.assignVal(self.parent.conf_d['obj'].checksumType,self.parent.conf_d['obj'].checksumType.currentText()))
        self.parent.conf_d['obj'].icon_tray_path.textChanged.connect(lambda: self.assignVal(self.parent.conf_d['obj'].icon_tray_path,self.parent.conf_d['obj'].icon_tray_path.text()))
        self.parent.conf_d['obj'].dateformat.textChanged.connect(lambda: self.assignVal(self.parent.conf_d['obj'].dateformat,self.parent.conf_d['obj'].dateformat.text()))
        self.parent.conf_d['obj'].maxHistorySize.valueChanged.connect(lambda: self.assignVal(self.parent.conf_d['obj'].maxHistorySize,self.parent.conf_d['obj'].maxHistorySize.value()))
        self.parent.conf_d['obj'].historyCache.textChanged.connect(lambda: self.assignVal(self.parent.conf_d['obj'].historyCache,self.parent.conf_d['obj'].historyCache.text()))
        self.parent.conf_d['obj'].historyFile.textChanged.connect(lambda: self.assignVal(self.parent.conf_d['obj'].historyFile,self.parent.conf_d['obj'].historyFile.text()))
        self.parent.conf_d['obj'].ssh_dir.textChanged.connect(lambda: self.assignVal(self.parent.conf_d['obj'].ssh_dir,self.parent.conf_d['obj'].ssh_dir.text()))
        self.parent.conf_d['obj'].known_hosts.textChanged.connect(lambda: self.assignVal(self.parent.conf_d['obj'].known_hosts,self.parent.conf_d['obj'].known_hosts.text()))
        self.parent.conf_d['obj'].app_icon_path.textChanged.connect(lambda: self.assignVal(self.parent.conf_d['obj'].app_icon_path,self.parent.conf_d['obj'].app_icon_path.text()))
        self.parent.conf_d['obj'].history_icon_path.textChanged.connect(lambda: self.assignVal(self.parent.conf_d['obj'].history_icon_path,self.parent.conf_d['obj'].history_icon_path.text()))

    def assignVal(self,widget,val=None):
        #print(widget,val)
        conv=[
                [
                    'defaultDir_send',
                    ['default-dirs','send']
                ],
                [
                    'defaultDir_get',
                    ['default-dirs','get']    
                ],
                [
                    'statementsDB',
                    'beColorfulDB'
                ],
                [
                    'statements_tag',
                    'beColorful-tag'
                ],
                [
                    'beColorful',
                    'beColorful'
                ],
                [
                    'useChecksum',
                    'skipChecksumLog'
                ],
                [
                    'checksumType',
                    'checksumType'
                ],
                [
                    'icon_tray_path',
                    'icon-tray-path'
                ],
                [
                    'dateformat',
                    'dateformat'
                ],
                [
                    'maxHistorySize',
                    'maxHistorySize'
                ],
                [
                    'historyCache',
                    'historyCache'
                ],
                [
                    'historyFile',
                    'historyFile'
                ],
                [
                    'ssh_dir',
                    'ssh-dir'
                ],
                [
                    'known_hosts',
                    'known-hosts'
                ],
                [
                    'app_icon_path',
                    'app-icon-path'
                ],
                [
                    'history_icon_path',
                    'history-icon-path'
                ]
            ]
        for field in conv: 
            if widget.objectName() == field[0]:
                #print(field,widget,val)
                if type(field[1]) == type(str()):
                    self.config_temp[field[1]]=val
                if type(field[1]) == type(list()):
                    self.config_temp[field[1][0]][field[1][1]]=val
                break

    def setChecksumTypes(self):
        available=hashlib.algorithms_available
        for t in available:
            cb=self.parent.conf_d['dialog'].findChild(QtWidgets.QComboBox,'checksumType')
            if cb != None:
                cb.addItem(t)

    def load_config(self):
        #print(self.parent.configJson)
        self.config_temp=copy.deepcopy(self.parent.configJson)
        self.setDefaultsColorView()
        self.setChecksumTypes()
        self.load_fields()
        #print(id(self.config_temp),id(self.parent.configJson))

    def setDefaultsColorView(self):
        viewer=self.parent.conf_d['dialog']
        objects=[
        ['statusColor_ring_bad',self.config_temp["statusColor-bad"]["ring"]["rgb"]],
        ['statusColor_core_bad',self.config_temp["statusColor-bad"]["core"]["rgb"]],
        ['statusColor_ring_good',self.config_temp["statusColor-good"]["ring"]["rgb"]],
        ['statusColor_core_good',self.config_temp["statusColor-good"]["core"]["rgb"]],
        ['statusColor_ring_inProgress',self.config_temp["statusColor-inprogress"]["ring"]["rgb"]],
        ['statusColor_core_inProgress',self.config_temp["statusColor-inprogress"]["core"]["rgb"]],
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
        print(self.parent.getAllTags())

    def reset_config(self):
        print('reset clicked')
        #read config-default.json
        with open(os.path.join(path,'defaults/config.json'),'r') as default:
            self.config_temp=json.load(default)
        self.load_fields()
        self.setDefaultsColorView()
        #adjust config-default for current user
        #save new config

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
                    QtWidgets.QComboBox,
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
                    self.config_temp['ChecksumLog']
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
                [
                    'app_icon_path',
                    QtWidgets.QLineEdit,
                    self.config_temp['app-icon-path']
                ],
                [
                    'history_icon_path',
                    QtWidgets.QLineEdit,
                    self.config_temp['history-icon-path']
                ]
            ]
        for obj in fields:
            obj.append(self.parent.conf_d['dialog'].findChild(obj[1],obj[0]))
            if obj[1] == QtWidgets.QLineEdit:
                obj[-1].setText(obj[2])
            if obj[1] == QtWidgets.QCheckBox:
                if obj[0] in ['useChecksum']:
                    state=obj[2]
                else:
                    state=obj[2]
                obj[-1].setChecked(state)

            if obj[1] == QtWidgets.QSpinBox:
                obj[-1].setValue(obj[2])
            if obj[1] == QtWidgets.QComboBox:
                index=obj[-1].findText(obj[2],QtCore.Qt.MatchExactly)
                if index != None:
                    obj[-1].setCurrentIndex(index)
                elif obj[0] == 'statements_tag':
                    if index == None:
                        index=obj[-1].findText('All',QtCore.Qt.MatchExactly)
                        obj[-1].setCurrentIndex(index)
                
        #print(fields)

    def save_config(self):
        print('save clicked : {}'.format(self.config_temp))
        self.parent.configJson=copy.deepcopy(self.config_temp)
        with open(self.config,'w') as cnf:
            json.dump(self.parent.configJson,cnf)
        python=sys.executable
        os.execl(python,python,* sys.argv)

    def op(self,fmethod,setMethod):
        #print(fmethod)
        if fmethod not in [False,'']:
            setMethod(fmethod)

    def buttons_connect(self):
        supportedImgs=self.supportedImgs
        buttons=[
                ['reset',self.reset_config],
                ['close',self.close_config],
                ['save',self.save_config],
                ]
        for obj in buttons:
            obj.append(self.parent.conf_d['dialog'].findChild(QtWidgets.QPushButton,obj[0]))
            obj[2].clicked.connect(obj[1])

        dialog=self.parent.conf_d['obj']
        #automate this option later
        dialog.browse_iconTrayPath.clicked.connect(lambda: self.op(openFile(None,mode='file',Filter="{0};;All Files (*)".format(supportedImgs),defaultDir=path),dialog.icon_tray_path.setText))
        dialog.browse_statementsDB.clicked.connect(lambda: self.op(openFile(None,mode='file',Filter="sqliteDB (*.db);;All Files (*)",defaultDir=path),dialog.statementsDB.setText))
        dialog.browse_historyCache.clicked.connect(lambda: self.op(openFile(None,mode='dir',defaultDir=path),dialog.historyCache.setText))
        dialog.browse_historyFile.clicked.connect(lambda: self.op(openFile(None,mode='file',Filter='JSON (*.json);;All Files (*)',defaultDir=path),dialog.historyFile.setText))
        dialog.browse_app_icon_path.clicked.connect(lambda: self.op(openFile(None,mode='file',Filter=supportedImgs,defaultDir=path),dialog.app_icon_path.setText))
        dialog.browse_sshDir.clicked.connect(lambda: self.op(openFile(None,mode='dir',defaultDir=os.environ['HOME']),dialog.ssh_dir.setText))
        dialog.browse_knownHosts.clicked.connect(lambda: self.op(openFile(None,mode='file',defaultDir=os.path.join(os.environ['HOME'],'.ssh')),dialog.known_hosts.setText))
        dialog.browse_get.clicked.connect(lambda: self.op(openFile(None,mode='dir',defaultDir=os.environ['HOME']),dialog.defaultDir_get.setText))
        dialog.browse_history_icon_path.clicked.connect(lambda: self.op(openFile(None,mode='file',defaultDir=path,Filter=supportedImgs),dialog.history_icon_path.setText))

    def timerActions(self):
        dialog=self.parent.conf_d['obj']
        f=dialog.dateformat.text()
        try:
            dialog.dateformat_view.setText(time.strftime(f,time.localtime()))
        except:
            dialog.dateFormat_view.setText('Invalid Date Format!')

    def timed(self):
        dialog=self.parent.conf_d['obj']
        self.timer=QtCore.QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.timerActions)
        self.timer.start(100)

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
