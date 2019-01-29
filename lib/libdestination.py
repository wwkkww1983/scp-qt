#! /usr/bin/python3

from PyQt5 import QtCore,QtGui,QtWidgets
from PIL import ImageDraw,Image
import cv2,numpy,os,json

class dest:
    statusColorObj={
            'send':{},
            'get':{},
            }
    in_config={
            'send':{
                'host':None,
                'port':None,
                'user':None,
                'password':None,
                'destination':None,
                'hostKey':None,
                'useHostKey':False,
                'sources':[],
            },
            'get':{
                'host':None,
                'port':None,
                'user':None,
                'password':None,
                'destination':None,
                'hostKey':None,
                'useHostKey':False,
                'sources':[],
                }
            }
    con={
            'send':0,
            'get':0
            }
    tabs=['get','send']
    #historyFile='./history.json'
    def __init__(self):
        pass
    
    def newLog(self,log):
        log['0']=self.connection['cfg']
        for tab in self.tabs:
            log['0'][tab]['password']=None

        with open(self.configJson['historyFile'],'w') as cnf:
            print('{} : log: {}'.format(self.sayit(self.vul),log))
            json.dump(log,cnf)
    
    def transHistory_save(self):
        log={}
        if os.path.exists(self.configJson['historyFile']):
            with open(self.configJson['historyFile'],'r') as cnf:
                log=json.load(cnf)
            print('{} : loaded: {}'.format(self.sayit(tag=self.vul),log))
            try:
                countLast=sorted([int(i) for i in log.keys()])[-1]
                countLast+=1
                log[str(countLast)]=self.connection['cfg']
                #passwords are not to be stored in the history log
                for tab in self.tabs:
                    log[str(countLast)][tab]['password']=None
                with open(self.configJson['historyFile'],'w') as cnf:
                    json.dump(log,cnf)
            except:
                self.newLog(log)
        else:
            self.newLog(log)
            
            '''
            log['0']=self.connection['cfg']
            for tab in self.tabs:
                log['0'][tab]['password']=None

            with open(self.historyFile,'w') as cnf:
                print('log: {}'.format(log))
                json.dump(log,cnf)
            '''

    def fields(self,cnf,host,port,user,password,destination,hostKey,useKeys,sources):
        if cnf['host'] != None:
            host.setText(cnf['host'])
        if cnf['port'] != None:
            port.setValue(cnf['port'])
        if cnf['user'] != None:
            user.setText(cnf['user'])
        if cnf['password'] != None:
            password.setText(cnf['password'])
        if cnf['destination'] != None:
            destination.setText(cnf['destination'])
        if cnf['hostKey'] != None:
            hostKey.setText(cnf['hostKey'])
        if cnf['useHostKey'] != None:
            print(useKeys.objectName())
            useKeys.setChecked(cnf['useHostKey'])
        if cnf['sources'] not in [[""],None]:
            sources.setText('\n'.join(cnf['sources']))

    def loadFields(self,tab):
        cnf=self.in_config[tab]
        if tab == 'send':
            self.fields(
                    cnf=cnf,
                    host=self.host_address,
                    port=self.port_remote,
                    user=self.user_remote,
                    password=self.password_remote,
                    destination=self.destination,
                    hostKey=self.hostKey,
                    useKeys=self.useKeys,
                    sources=self.sources,
                    )
        elif tab == 'get':
            self.fields(
                    cnf=cnf,
                    host=self.host_address_get,
                    port=self.port_remote_get,
                    user=self.user_remote_get,
                    password=self.password_remote_get,
                    destination=self.destination_get_le,
                    hostKey=self.hostKey_get,
                    useKeys=self.useKeys_get,
                    sources=self.source_le,
                    )

    def transHistory_loadLast(self):
        log={}
        if os.path.exists(self.configJson['historyFile']):
            with open(self.configJson['historyFile'],'r') as cnf:
                log=json.load(cnf)
        try:
            countLast=sorted([int(i) for i in log.keys()])[-1]
            self.in_config=log[str(countLast)]
            for tab in self.tabs:
                self.loadFields(tab=tab)
        except:
            self.statusBar().showMessage('No Last History to use!')

    def openFile(self,mode='file',windowTitle='Open',defaultDir='~',Filter='All Files (*)'):
        home=os.path.expandvars(os.path.expanduser(defaultDir))
        stringMode=False
        if mode == 'file':
            files=QtWidgets.QFileDialog.getOpenFileName(self,windowTitle,home,Filter,options=QtWidgets.QFileDialog.DontUseNativeDialog)
        if mode == 'files':
            files=QtWidgets.QFileDialog.getOpenFileNames(self,windowTitle,home,Filter,options=QtWidgets.QFileDialog.DontUseNativeDialog)
        if mode == 'dirs':
            files=QtWidgets.QFileDialog.getExistingDirectory(self,windowTitle,home,options=QtWidgets.QFileDialog.DontUseNativeDialog)
            if files != None:
                files=([files],)
        if mode == 'dir':
            files=QtWidgets.QFileDialog.getExistingDirectory(self,windowTitle,home,options=QtWidgets.QFileDialog.DontUseNativeDialog,)
            stringMode=True

        if files != None:
            if stringMode == False:
                return files[0]
            else:
                return files
        else:
            return False

    def get_rsa(self,hostKey,tab='send'):
        key=self.openFile(mode='file',windowTitle='Open Host Key',defaultDir=self.configJson['ssh-dir'])
        if key != False:
            hostKey.setText(key)

    def destination_checkbox_toggle(self,checkBox,lineEdit,label,tab='send'):
        print('{} : {}'.format(self.sayit(tag=self.vul),self.con))
        if checkBox.isChecked():
            lineEdit.setEnabled(True)
            label.setEnabled(True)
            if tab == 'send':
                self.connect.setEnabled(False)
                self.send.setEnabled(False)
            elif tab == 'get':
                self.check_connection_get.setEnabled(False)
                self.get_btn.setEnabled(False)
            self.con[tab]+=1
            if checkBox.objectName() in ['hostKeyEdit','hostKeyEdit_get']:
                if checkBox.objectName() == 'hostKeyEdit':
                    self.hostKeyBrowse.setEnabled(True)
                elif checkBox.objectName() == 'hostKeyEdit_get':
                    self.hostKeyBrowse_get.setEnabled(True)
        else:
            self.con[tab]-=1
            lineEdit.setEnabled(False)
            label.setEnabled(False)
            if self.con[tab] < 1:
                if tab == 'send':
                    self.connect.setEnabled(True)
                    self.send.setEnabled(True)
                elif tab == 'get':
                    self.check_connection_get.setEnabled(True)
                    self.get_btn.setEnabled(True)
            if checkBox.objectName() in ['hostKeyEdit','hostKeyEdit_get']:
                if checkBox.objectName() == 'hostKeyEdit':
                    self.hostKeyBrowse.setEnabled(False)
                elif checkBox.objectName() == 'hostKeyEdit_get':
                    self.hostKeyBrowse_get.setEnabled(False)

    def untilComplete(self,tab,enable_state):
        self.fileGet=''
        self.fileSend=''
        if tab == 'send':
            self.send.setEnabled(enable_state)
            self.connect.setEnabled(enable_state)
            self.hostEdit.setEnabled(enable_state)
            self.portEdit.setEnabled(enable_state)
            self.userEdit.setEnabled(enable_state)
            self.passwordEdit.setEnabled(enable_state)
            self.destinationEdit.setEnabled(enable_state)
            self.useKeys.setEnabled(enable_state)
            self.sources.setEnabled(enable_state)
            self.browse.setEnabled(enable_state)
            self.sendDirectory.setEnabled(enable_state)
            self.appendSource.setEnabled(enable_state)
            self.clearSources.setEnabled(enable_state)
            self.hostKeyEdit.setEnabled(enable_state)
        if tab == 'get':
            self.get_btn.setEnabled(enable_state)
            self.check_connection_get.setEnabled(enable_state)
            self.hostEdit_get.setEnabled(enable_state)
            self.portEdit_get.setEnabled(enable_state)
            self.userEdit_get.setEnabled(enable_state)
            self.passwordEdit_get.setEnabled(enable_state)
            self.sourceEdit_get.setEnabled(enable_state)
            self.useKeys_get.setEnabled(enable_state)
            self.destination_get_le.setEnabled(enable_state)
            self.browse_get.setEnabled(enable_state)
            self.hostKeyEdit_get.setEnabled(enable_state)

    def statusColor(self,status=False,tab='send',obj=None):
        im=Image.new('RGB',(320,200))
        draw=ImageDraw.Draw(im)
        if status == False:
            draw.rectangle([(0,0),(320,200)],self.configJson['statusColor-bad']['ring']['rgb'])
            draw.rectangle([(10,10),(310,190)],self.configJson['statusColor-bad']['core']['rgb'])
        elif status == True:
            draw.rectangle([(0,0),(320,200)],self.configJson['statusColor-good']['core']['rgb'])
            draw.rectangle([(10,10),(310,190)],self.configJson['statusColor-good']['ring']['rgb'])
        else:
            draw.rectangle([(0,0),(320,200)],fill=self.configJson['statusColor-inprogress']['core']['rgb'])
            draw.rectangle([(10,10),(310,190)],fill=self.configJson['statusColor-inprogress']['ring']['rgb'])
        nim=numpy.array(im,dtype=numpy.uint8)
        ##this returns None... why?
        #cimTest=cv2.imdecode(nim,cv2.IMREAD_COLOR)
        #print(cimTest)
        cim=cv2.cvtColor(nim,cv2.COLOR_RGB2BGR,nim)
        cim=cv2.cvtColor(cim,cv2.COLOR_RGB2BGR,cim)
        self.statusColorObj[tab]['img']=cim
        h,w,c=cim.shape
        self.statusColorObj[tab]['qImg']=QtGui.QImage(self.statusColorObj[tab]['img'],w,h,w*c,QtGui.QImage.Format_RGB888)
        self.statusColorObj[tab]['pixmap']=QtGui.QPixmap(self.statusColorObj[tab]['qImg'])
        
        #self.status.setPixmap(self.statusColorObj[key]['pixmap'])
        obj.setPixmap(self.statusColorObj[tab]['pixmap'])

    def get_creds(self,tab='send'):
        cnf={}
        cnf['host']=self.host_address.text()
        cnf['port']=self.port_remote.value()
        cnf['user']=self.user_remote.text()
        cnf['password']=self.password_remote.text()
        cnf['destination']=self.destination.text()
        cnf['hostKey']=self.hostKey.text()
        cnf['useHostKey']=self.useKeys.isChecked()
        cnf['sources']=self.sources.toPlainText().split(',\n')
        self.in_config[tab]=cnf

    def get_creds_v2(self,tab,host_address,port_remote,user_remote,password_remote,destination,hostKey,useKeys,sources):
        cnf={}
        cnf['host']=host_address.text()
        cnf['port']=port_remote.value()
        cnf['user']=user_remote.text()
        cnf['password']=password_remote.text()
        cnf['destination']=destination.text()
        cnf['hostKey']=hostKey.text()
        cnf['useHostKey']=useKeys.isChecked()
        cnf['sources']=sources.toPlainText().split('\n')
        self.in_config[tab]=cnf
 
    def set_in_cfg(self,tab,edit,key,value):
        if edit.isChecked() == True:
            self.in_config[tab][key]=value

    def destination_buttons(self):
        self.hostKeyBrowse.clicked.connect(lambda: self.get_rsa(
            tab='send',
            hostKey=self.hostKey
            ))

    def source_get_buttons(self):
        self.hostKeyBrowse_get.clicked.connect(lambda: self.get_rsa(
            tab='get',
            hostKey=self.hostKey_get
            ))

    def source_get_fields(self):
        self.port_remote_get.valueChanged.connect(lambda: self.set_in_cfg(
            'get',
            self.portEdit_get,
            'port',
            self.port_remote_get.value()))
        self.host_address_get.textChanged.connect(lambda: self.set_in_cfg(
            'get',
            self.hostEdit_get,
            'host',
            self.host_address_get.text()))
        self.user_remote_get.textChanged.connect(lambda: self.set_in_cfg(
            'get',
            self.userEdit_get,
            'user',
            self.user_remote_get.text()))
        self.password_remote_get.textChanged.connect(lambda: self.set_in_cfg(
            'get',
            self.passwordEdit_get,
            'password',
            self.password_remote_get.text()))
        self.source_le.textChanged.connect(lambda: self.set_in_cfg(
            'get',
            self.sourceEdit_get,
            'sources',
            self.source_le.toPlainText().split('\n')))
        self.hostKey_get.textChanged.connect(lambda: self.set_in_cfg(
            'get',
            self.hostKeyEdit_get,
            'hostKey',
            self.hostKey_get.text()))

    def destination_fields(self):
        self.port_remote.valueChanged.connect(lambda: self.set_in_cfg(
            'send',
            self.portEdit,
            'port',
            self.port_remote.value()))
        self.host_address.textChanged.connect(lambda: self.set_in_cfg(
            'send',
            self.hostEdit,
            'host',
            self.host_address.text()))
        self.user_remote.textChanged.connect(lambda: self.set_in_cfg(
            'send',
            self.userEdit,
            'user',
            self.user_remote.text()))
        self.password_remote.textChanged.connect(lambda: self.set_in_cfg(
            'send',
            self.passwordEdit,
            'password',
            self.password_remote.text()))
        self.destination.textChanged.connect(lambda: self.set_in_cfg(
            'send',
            self.destinationEdit,
            'destination',
            self.destination.text()))
        self.hostKey.textChanged.connect(lambda: self.set_in_cfg(
            'send',
            self.hostKeyEdit,
            'hostKey',
            self.hostKey.text()))
        self.source_fields()

    def enableHostKeys(self,tab):
        self.in_config[tab]['useHostKey']=self.useKeys.isChecked()
        if self.useKeys.isChecked():
            self.hostKeyEdit.setEnabled(True)
            #self.connect.setEnabled(False)
        else:
            #self.connect.setEnabled(True)
            self.hostKeyEdit.setEnabled(False)
            self.hostKey.setEnabled(False)
            self.hostKeyLabel.setEnabled(False)
            self.hostKeyBrowse.setEnabled(False)
    

    def enableHostKeys_v2(self,tab,useKeys,label,button,hostKeyEdit,hostKey):
        self.in_config[tab]['useHostKey']=useKeys.isChecked()
        print('{} : using enableHostKeys_v2()!'.format(self.sayit(tag=self.vul)))
        if useKeys.isChecked():
            hostKeyEdit.setEnabled(True)
        else:
            hostKeyEdit.setEnabled(False)
            hostKey.setEnabled(False)
            label.setEnabled(False)
            button.setEnabled(False)
            
    def source_get_init(self):
        self.source_get_checkboxes()
        self.source_get_fields()
        self.source_get_buttons()

    def destination_init(self):
        self.destination_checkboxes()
        self.destination_fields()
        self.destination_buttons()

        self.source_get_init()

    def source_get_checkboxes(self):
        self.hostEdit_get.toggled.connect(
                lambda: self.destination_checkbox_toggle(
                    self.hostEdit_get,
                    self.host_address_get,
                    label=self.hostLabel_get,
                    tab='get'
                    )
                )
        self.portEdit_get.toggled.connect(
                lambda: self.destination_checkbox_toggle(
                    self.portEdit_get,
                    self.port_remote_get,
                    label=self.portLabel_get,
                    tab='get',
                    )
                )
        self.userEdit_get.toggled.connect(
                lambda: self.destination_checkbox_toggle(
                    self.userEdit_get,
                    self.user_remote_get,
                    label=self.userLabel_get,
                    tab='get',
                    )
                )
        self.passwordEdit_get.toggled.connect(
                lambda: self.destination_checkbox_toggle(
            self.passwordEdit_get,
            self.password_remote_get,
            label=self.passwordLabel_get,
            tab='get',
            )
                )
        self.sourceEdit_get.toggled.connect(
                lambda: self.destination_checkbox_toggle(
                    self.sourceEdit_get
                    ,self.source_le
                    ,label=self.sourceLabel_get,
                    tab='get'
                    )
                )
        self.hostKeyEdit_get.toggled.connect(
                lambda: self.destination_checkbox_toggle(
                    self.hostKeyEdit_get,
                    self.hostKey_get,
                    label=self.hostKeyLabel_get,
                    tab='get',
                    )
                )
        self.useKeys_get.toggled.connect(
                lambda: self.enableHostKeys_v2(
                    tab='get',
                    useKeys=self.useKeys_get,
                    label=self.hostKeyLabel_get,
                    button=self.hostKeyBrowse_get,
                    hostKeyEdit=self.hostKeyEdit_get,
                    hostKey=self.hostKey_get
                    )
                )

    def destination_checkboxes(self):
        self.hostEdit.toggled.connect(
                lambda: self.destination_checkbox_toggle(
                    self.hostEdit,
                    self.host_address,
                    label=self.hostLabel,
                    tab='send'
                    )
                )
        self.portEdit.toggled.connect(
                lambda: self.destination_checkbox_toggle(
                    self.portEdit,
                    self.port_remote,
                    label=self.portLabel,
                    tab='send',
                    )
                )
        self.userEdit.toggled.connect(
                lambda: self.destination_checkbox_toggle(
                    self.userEdit,
                    self.user_remote,
                    label=self.userLabel,
                    tab='send',
                    )
                )
        self.passwordEdit.toggled.connect(
                lambda: self.destination_checkbox_toggle(
            self.passwordEdit,
            self.password_remote,
            label=self.passwordLabel,
            tab='send',
            )
                )
        self.destinationEdit.toggled.connect(
                lambda: self.destination_checkbox_toggle(
                    self.destinationEdit
                    ,self.destination
                    ,label=self.destinationLabel,
                    tab='send'
                    )
                )
        self.hostKeyEdit.toggled.connect(
                lambda: self.destination_checkbox_toggle(
                    self.hostKeyEdit,
                    self.hostKey,
                    label=self.hostKeyLabel,
                    tab='send',
                    )
                )
        self.useKeys.toggled.connect(
                lambda: self.enableHostKeys(tab='send')
                )
