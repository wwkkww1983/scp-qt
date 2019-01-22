import os,stat,engfmt
from PyQt5 import QtWidgets
class itemize:
    def total_transfer_send(self,p,gui=None):
        size=0
        #p='/home/carl/Downloads'
        for root,dirs,fnames in os.walk(p,topdown=True):
            if gui != None:
                if gui.stopTRX['send'] == True:
                    break
            for fname in fnames:
                if gui != None:
                    if gui.stopTRX['send'] == True:
                        break
                path=os.path.join(root,fname)
                path=os.path.abspath(os.path.realpath(path))
                if os.path.exists(path):
                    size+=os.stat(path).st_size
                    size_eng=engfmt.quant_to_eng(size,prec=2)
                    if gui != None:
                        QtWidgets.QApplication.processEvents()
                        gui.statusBar().showMessage(size_eng)
                    print(('\b'*len(str(size_eng)))+str(size_eng),end='')

        print(('\b'*len(str(size)))+engfmt.quant_to_eng(size,prec=2)+' ',end='')
        print()
        return size
