#! /usr/bin/env python3
import os,sys
import time
class config_init:
    def __init__(self):
        pass

    history_file="history.json"
    path="."
    backhistory="back_history"
    maxSize=1024**2

    def newcfg(self,file):
        with open(file,'w') as hist:
                hist.write('{}')

    def configurator(self):
        tname=time.strftime('%H.%M.%S-%m.%d.%Y',time.localtime())
        bh=os.path.join(self.path,self.backhistory)
        file=os.path.join(self.path,self.history_file)
        h=os.path.splitext(self.history_file)
        newname=os.path.join(bh,h[0]+'_'+tname+h[1])
        size=0
        if os.path.exists(file):
            if os.path.isfile(file):
                size=os.path.getsize(file)
            else:
                print(file,"not a file")
                return False
        else:
            self.newcfg(file)
            return True 
        if size >= self.maxSize:
            print('{} exceeds recommended size ({})... moving to {}'.format(file,self.maxSize,newname))
            if os.path.exists(bh):
                if not os.path.isdir(bh):
                    print(bh,"not a directory")
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
