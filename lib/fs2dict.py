import os
import collections

class fs2dict:
    fs={}
    master=None
    def __init__(self):
        pass


    def readdict(self,model=None,dic=None,parent=None):
        for k, v in dic.items():
            if isinstance(v,dict):
                if model != None:
                    item=QtGui.QStandardItem(k)
                    model.appendRow(item)
                if v != {}:
                    if model != None:
                        self.readdict(model=item,dic=v,parent=k)
                    else:
                        pass
                else:
                    dic[k]=None
                #self.guicall(k,parent)
            else:
                print(k,v)


    def main(self,path):
        counter=0
        DynamicDict=lambda: collections.defaultdict(
                lambda: collections.defaultdict(DynamicDict)
                )
        dd=DynamicDict()
        fs='dd'
        for root,dirnames,fnames in os.walk(path):
            counter+=1
            for fname in fnames:
                dpath=os.path.join(root,fname)
                dlist=dpath.split('/')
                dlist=[i for i in dlist if i != '']
                for key in dlist:
                    fs='{}[{}]'.format(fs,repr(key))
                fs+=' = {}'
                if (counter % 100) == 0:
                    print("getting remote drive status: {}".format(counter))
                exec(fs)
                fs='dd'
                #print(dd)
        #print(dd['home']['carl']['devel']['scp-qt'].keys())            
        return dd

    def guicall(self,key,parent):
        print(key,parent)
        if self.master != None:
            self.master.addItems(parent,key)


    

if __name__ == "__main__":
    app=fs2dict()
    d=app.main()
    dd=app.readdict(d)
    print(dd)
