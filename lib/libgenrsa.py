import os,sys,json,time
from PyQt5 import QtWidgets,QtCore,QtGui
lib=('./lib','./lib_widget')
for i in lib:
    sys.path.insert(0,i)
import librsa
from Crypto.PublicKey import RSA

class genRSA_controls:
    parent=None
    settings={
            'passphrase':None,
            'size':2048,
            'pathPrivate':None,
            'pathPublic':None,
            'privateKey':None,
            'publicKey':None,
            'keyEncrypted':False,
            }
    def __init__(self,parent):
        self.parent=parent
        self.base_controls_connect()

    def show(self):
        self.parent.genrsa['dialog'].show()
    
    def progress(self,stage,stages):
        state=int((stage/stages)*100)
        QtWidgets.QApplication.processEvents()
        return state

    def sameNames(self):
        private=os.path.join(self.settings['pathPrivate'],self.settings['privateKey'])
        public=os.path.join(self.settings['pathPublic'],self.settings['publicKey'])
        msgbox=QtWidgets.QMessageBox(self.parent)
        msgbox.setIcon(QtWidgets.QMessageBox.Critical)
        msgbox.setText('private key cannot be the same as the public key!')
        if private == public:
            msgbox.show()
            self.parent.genrsa['obj'].generate.setEnabled(False)
        else:
            self.parent.genrsa['obj'].generate.setEnabled(True)

    def generateKeys(self):
        progressbar=self.parent.genrsa['obj'].progressBar
        for key in self.settings.keys():
            print('{} - {} : {}: {}'.format('genRSA Dialog',self.parent.sayit(tag=self.parent.vul),key,self.settings[key]))
        rsa=librsa.generator()
        rsa.keysize=self.settings['size']
        rsa.__init__()
        if self.settings['keyEncrypted'] == True:
            passphrase=self.settings['passphrase']
        else:
            passphrase=None

        progressbar.setValue(self.progress(0,3))
        rsa.genPrivate(self.settings['pathPrivate'],self.settings['privateKey'],encrypt=self.settings['keyEncrypted'],passphrase=passphrase)
        progressbar.setValue(self.progress(1,3))

        rsa.genPublic(self.settings['pathPublic'],self.settings['publicKey'])
        progressbar.setValue(self.progress(2,3))
        
        check=self.checkKeys(rsa,passphrase)
        progressbar.setValue(self.progress(3,3))

        msgbox=QtWidgets.QMessageBox(self.parent)
        
        if check == True:
            msg='RSA key creation successful!'
            self.parent.statusBar().showMessage(msg)
            msgbox.setText(msg)
            msgbox.setIcon(QtWidgets.QMessageBox.Information)
        else:
            msg='keys failed to generate: {}'.format(check[1])
            print(msg)
            self.parent.statusBar().showMessage(msg)
            msgbox.setText(msg+' Retry?')
            msgbox.setStandardButtons(QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
            msgbox.setIcon(QtWidgets.QMessageBox.Critical)
        msgbox.show()
        progressbar.reset()

        if check == True:
            if msgbox.exec() == QtWidgets.QMessageBox.Ok:
                self.parent.genrsa['dialog'].hide()
        else:
            if msgbox.exec() == QtWidgets.QMessageBox.No:
                self.parent.genrsa['dialog'].hide()
            
    def checkKeys(self,rsa,passphrase,testTrigger=False):
        key=''
        if not os.path.exists(os.path.join(self.settings['pathPublic'],self.settings['publicKey'])):
            return False,'MissingPublic'

        if not os.path.exists(os.path.join(self.settings['pathPrivate'],self.settings['privateKey'])):
            return False,'MissingPrivate'

        try:
            print(passphrase)
            key=rsa.dumpKey(
                    open(
                        os.path.join(
                            self.settings['pathPrivate'],
                            self.settings['privateKey']),
                        'rb').read(),
                    passphrase=passphrase
                    )
        except ValueError as e:
            return False,'InvalidPrivate:Crypto.PublicKey.RSA.import_key(open(KEYNAME,"rb")): {}'.format(e)

        try:
            rsa.paramikoRSA(key)
        except paramiko.ssh_exception.SSHException as e:
            return False,'InvalidPrivate:Paramiko.RSAKey.from_private_key(io.StringIO(KEY_STRING)): {}'.format(e)
        
        try:
            pkey=RSA.importKey(open(os.path.join(self.settings['pathPublic'],self.settings['publicKey']),'rb').read())
        except ValueError as e:
            return False,'InvalidPublic:Crypto.PublicKey.RSA.importKey(open(KEYNAME,"rb")): {}'.format(e)
        #fail error
        #issue a dialog to letuser know keys are created at location
        if testTrigger == True:
            return False,'"test fail triggered!"' 
        return True

    def keyEncrypted(self,gen):
        self.settings['keyEncrypted']=gen['obj'].encrypted.isChecked()
        gen['obj'].passphrase.setEnabled(self.settings['keyEncrypted'])

    def setSize(self,gen):
        self.settings['size']=gen['obj'].keysize.value()

    def setPassphrase(self,gen):
        self.settings['passphrase']=gen['obj'].passphrase.text()
    
    def setKeyNames(self,gen):
        splotePrivate=os.path.split(gen['obj'].privateKey.text())
        self.settings['privateKey']=splotePrivate[1]
        self.settings['pathPrivate']=splotePrivate[0]

        splotePublic=os.path.split(gen['obj'].publicKey.text())
        self.settings['publicKey']=splotePublic[1]
        self.settings['pathPublic']=splotePublic[0]
        self.sameNames()

    def setPaths(self,gen,objname):
        if objname == 'browse_privateKey':
            if self.settings['pathPrivate'] == None:
                fname=self.saveFile(title='Save Private Key')
            else:
                fname=self.saveFile(title='Save Private Key',defaultdir=self.settings['pathPrivate'],fname=self.settings['privateKey'])
            if fname != False:
                gen['obj'].privateKey.setText(fname)
                open(fname,'wb').write(b'')
        elif objname == 'browse_publicKey':
            if self.settings['pathPublic'] == None:
                fname=self.saveFile(title='Save Public Key')
            else:
                fname=self.saveFile(title='Save Public Key',defaultdir=self.settings['pathPublic'],fname=self.settings['publicKey'])
            if fname != False:
                gen['obj'].publicKey.setText(fname)
                open(fname,'wb').write(b'')

    def saveFile(self,title,defaultdir=os.environ['HOME'],fname='',_filter='key (*.key);;All Files (*)'):
        out=''
        file=QtWidgets.QFileDialog.getSaveFileName(self.parent.genrsa['dialog'],title,os.path.join(defaultdir,fname),_filter,options=QtWidgets.QFileDialog.DontUseNativeDialog)
        if file[0] != '':
            if os.path.splitext(file[0])[1] != '.key':
                out='{}.{}'.format(file[0],'key')
            else:
                out=file[0]
        else:
            return False
        return out

    def base_controls_connect(self):
        gen=self.parent.genrsa
        gen['obj'].close.clicked.connect(gen['dialog'].close)
        gen['obj'].generate.clicked.connect(self.generateKeys)
        gen['obj'].encrypted.toggled.connect(lambda: self.keyEncrypted(gen))
        gen['obj'].keysize.valueChanged.connect(lambda: self.setSize(gen))
        gen['obj'].passphrase.textChanged.connect(lambda: self.setPassphrase(gen))
        gen['obj'].privateKey.textChanged.connect(lambda: self.setKeyNames(gen))
        gen['obj'].publicKey.textChanged.connect(lambda: self.setKeyNames(gen))
        gen['obj'].browse_publicKey.clicked.connect(lambda: self.setPaths(gen,'browse_publicKey'))
        gen['obj'].browse_privateKey.clicked.connect(lambda: self.setPaths(gen,'browse_privateKey'))
