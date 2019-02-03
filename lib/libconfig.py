#! /usr/bin/env python3
import os,sys
import time
from PyQt5 import QtWidgets

class config_init:
    def __init__(self,parent):
        self.parent=parent

    #history_file="history.json"
    #path="."
    #backhistory="back_history"
    #maxSize=1024**2

    def newcfg(self,file):
        try:
            with open(file,'w') as hist:
                hist.write('{}')
        except FileNotFoundError as e:
            text='you need to set a valid history file! : {}\nDo it Now?'.format(e)
            print(text)
            msg=QtWidgets.QMessageBox(self.parent)
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setStandardButtons(QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
            msg.setText(text)
            msg.show()
            status=msg.exec()
            if status == QtWidgets.QMessageBox.Yes:
                self.parent.conf_d['controls'].show()
            self.parent.statusBar().showMessage(text)


    def configurator(self):
        tname=time.strftime(self.parent.configJson['dateformat'],time.localtime())
        bh=self.parent.configJson['historyCache']
        file=self.parent.configJson['historyFile']
        h=os.path.splitext(self.parent.configJson['historyFile'])
        newname=os.path.join(bh,h[0]+'_'+tname+h[1])
        size=0
        if os.path.exists(file):
            if os.path.isfile(file):
                size=os.path.getsize(file)
            else:
                print("{} : not a file {}".format(self.sayit(tag=self.vul),file))
                return False
        else:
            self.newcfg(file)
            return True 
        if size >= self.parent.configJson['maxHistorySize']:
            print('{} : {} exceeds recommended size ({})... moving to {}'.format(
                self.sayit(
                    tag=self.vul
                    ),
                file,
                self.parent.configJson['maxHistorySize'],
                newname
                )
                )
            if os.path.exists(bh):
                if not os.path.isdir(bh):
                    print(bh,": {} : not a directory".format(self.sayit(tag=self.vul)))
                    return False
            else:
                os.mkdir(bh)    
            os.rename(file,newname)
            self.newcfg(file)
            return True
        else:
            return True

if __name__ == "__main__":
    app=config_init()
    app.configurator()
