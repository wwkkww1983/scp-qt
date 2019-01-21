#! /usr/bin/env python3
import os,sys
import time
class config_init:
    def __init__(self,parent):
        self.parent=parent

    #history_file="history.json"
    #path="."
    #backhistory="back_history"
    #maxSize=1024**2

    def newcfg(self,file):
        with open(file,'w') as hist:
                hist.write('{}')

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
