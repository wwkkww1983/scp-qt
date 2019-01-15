from PyQt5 import QtWidgets,QtCore
import json,os,sys

libs=('./lib','./lib_widget')
for p in libs:
    sys.path.insert(0,p)

import historyView,entryView

class history:
    history_file='history.json'
    path='.'
    def open_history(class_self):
        keys={}
        with open(os.path.join(class_self.path,class_self.history_file),'r') as c:
            keys=json.load(c)
        return keys

    def create_viewer(class_self,self):
        viewer={}
        viewer['0']={}
        viewer['0']['dialog']=QtWidgets.QDialog(self)
        viewer['0']['obj']=historyView.Ui_configView()
        viewer['0']['obj'].setupUi(viewer['0']['dialog'])
        return viewer

    def reload_history(class_self,self):
            #this will need to be converted to work specifically on the already existing gui in self
            keys=class_self.open_history()

            self.hist_d['entry']={}
            #viewer=class_self.create_viewer(self)
            #need to make children accessible by dict
            for em in keys.keys():
                self.hist_d['entry'][em]={}
                
                self.hist_d['entry'][em]['dialog']=QtWidgets.QDialog(self)
                self.hist_d['entry'][em]['obj']=entryView.Ui_entryView()
                self.hist_d['entry'][em]['obj'].setupUi(self.hist_d['entry'][em]['dialog'])
                self.hist_d['entry'][em]['cfg']=keys[em] 
                tree=self.hist_d['entry'][em]['obj'].treeWidget
                for mode in self.hist_d['entry'][em]['cfg'].keys():
                    if mode != 'date':
                        item=self.hist_d['entry'][em]['obj'].treeWidget.findItems(mode,QtCore.Qt.MatchExactly)[0]
                        #item_parts=[getattr(item,i) for i in dir(item)]
                        children=item.childCount()
                        self.hist_d['entry'][em]['num']=str(em)
                        class_self.entry_buttons_connect(self,self.hist_d['entry'][em],self.hist_d['entry'],mode,self.hist_d['viewer'])
                        item=class_self.countConf(self.hist_d['entry'][em]['cfg'][mode],item,tree,mode)
                        for cnf in self.hist_d['entry'][em]['cfg'][mode].keys():
                            for i in range(children):
                                subChild=item.child(i)
                                n=subChild.text(0)
                                if n == cnf:
                                    print(n,self.hist_d['entry'][em]['cfg'][mode][cnf],mode)
                                    if n != 'sources':
                                       subChild.setData(1,QtCore.Qt.EditRole,self.hist_d['entry'][em]['cfg'][mode][cnf])
                                    else:
                                        if self.hist_d['entry'][em]['cfg'][mode][cnf] != None:
                                            for src in self.hist_d['entry'][em]['cfg'][mode][cnf]:
                                                if src not in [None,'']:
                                                    print(src,mode,'srcs')
                                                    newChild=QtWidgets.QTreeWidgetItem(subChild)
                                                    newChild.setData(1,QtCore.Qt.EditRole,src)
                                                    subChild.addChild(newChild)
                                                else:
                                                    break
                                        #need to add treewidgetitem as child for sources list elements
                                        pass
    
                    #problem ended beeing that i was overwriting previous declared widget leaving only half the cfg to display
                    if 'date' in self.hist_d['entry'][em]['cfg'].keys():
                        self.hist_d['entry'][em]['obj'].groupBox.setTitle('{}'.format(self.hist_d['entry'][em]['cfg']['date']))
                    else:
                        self.hist_d['entry'][em]['obj'].groupBox.setTitle('{}'.format(self.mkDate())) 
                    self.hist_d['viewer']['0']['obj'].gridLayout_6.addWidget(self.hist_d['entry'][em]['dialog'],int(em),0,1,1)
            class_self.viewer_buttons_connect(self,self.hist_d['viewer'],self.hist_d['entry'])
            #viewer['0']['dialog'].show()
            '''
            historyViewer_dict={}
            historyViewer_dict['viewer']=viewer
            historyViewer_dict['entry']=entry
            return historyViewer_dict
            '''

    def viewer_setup(class_self,self):
            keys=class_self.open_history()

            entry={}
            viewer=class_self.create_viewer(self)
            #need to make children accessible by dict
            for em in keys.keys():
                entry[em]={}
                entry[em]['dialog']=QtWidgets.QDialog(self)
                entry[em]['obj']=entryView.Ui_entryView()
                entry[em]['obj'].setupUi(entry[em]['dialog'])
                entry[em]['cfg']=keys[em] 
                tree=entry[em]['obj'].treeWidget
                for mode in entry[em]['cfg'].keys():
                    if mode != 'date':
                        item=entry[em]['obj'].treeWidget.findItems(mode,QtCore.Qt.MatchExactly)[0]
                        item_parts=[getattr(item,i) for i in dir(item)]
                        children=item.childCount()
                        entry[em]['num']=str(em)
                        class_self.entry_buttons_connect(self,entry[em],entry,mode,viewer)
                        item=class_self.countConf(entry[em]['cfg'][mode],item,tree,mode)
                        for cnf in entry[em]['cfg'][mode].keys():
                            for i in range(children):
                                subChild=item.child(i)
                                n=subChild.text(0)
                                if n == cnf:
                                    print(n,entry[em]['cfg'][mode][cnf],mode)
                                    if n != 'sources':
                                       subChild.setData(1,QtCore.Qt.EditRole,entry[em]['cfg'][mode][cnf])
                                    else:
                                        if entry[em]['cfg'][mode][cnf] != None:
                                            for src in entry[em]['cfg'][mode][cnf]:
                                                if src not in [None,'']:
                                                    print(src,mode,'srcs')
                                                    newChild=QtWidgets.QTreeWidgetItem(subChild)
                                                    newChild.setData(1,QtCore.Qt.EditRole,src)
                                                    subChild.addChild(newChild)
                                                else:
                                                    break
                                        #need to add treewidgetitem as child for sources list elements
                                        pass
    
                    #problem ended beeing that i was overwriting previous declared widget leaving only half the cfg to display
                    if 'date' in entry[em]['cfg'].keys():
                        entry[em]['obj'].groupBox.setTitle('{}'.format(entry[em]['cfg']['date']))
                    else:
                        entry[em]['obj'].groupBox.setTitle('{}'.format(self.mkDate())) 
                    viewer['0']['obj'].gridLayout_6.addWidget(entry[em]['dialog'],int(em),0,1,1)
            class_self.viewer_buttons_connect(self,viewer,entry)
            #viewer['0']['dialog'].show()
            historyViewer_dict={}
            historyViewer_dict['viewer']=viewer
            historyViewer_dict['entry']=entry
            return historyViewer_dict

    def loadEntry(class_self,self,cfg,mode):
        self.in_config=cfg
        print(self.in_config,cfg,sep='\n')
        self.loadFields(tab=mode)
        self.get_creds_wrapped(tab=mode,updateHistory=False)

    def removeEntry(class_self,self,entry_bottom,entry_top,viewer):
        entry_bottom['dialog'].hide()
        viewer['0']['obj'].gridLayout_6.removeWidget(entry_bottom['dialog'])
        entry_bottom['dialog'].deleteLater()
       
        keys=class_self.open_history()
        print(keys.keys())
        #keys.pop(entry_bottom['num'])

        newCfg={}

        for num,i in enumerate(entry_top.keys()):
            if entry_bottom['num'] != entry_top[i]['num']:
                newCfg[str(num)]=entry_top[i]['cfg']
        
        with open(os.path.join(class_self.path,class_self.history_file),'w') as cnf:
            json.dump(newCfg,cnf)

        class_self.removeAll(self,self.hist_d['viewer'],self.hist_d['entry'])
        #self.hist_d['viewer']['0']['dialog'].hide()

        class_self.reload_history(self)
        
        #self.hist_d=class_self.viewer_setup(self)
        #self.hist_d['viewer']['0']['dialog'].show()

    def entry_buttons_connect(class_self,self,entry_bottom,entry_top,mode,viewer):
        entry_bottom['obj'].load.clicked.connect(lambda: class_self.loadEntry(self,entry_bottom['cfg'],mode))
        entry_bottom['obj'].remove.clicked.connect(lambda: class_self.removeEntry(self,entry_bottom,entry_top,viewer))

    def viewer_destroy(class_self,self,viewer):
        viewer['0']['dialog'].destroy()
        self.hist=None
        self.hist_d=None

    def removeAll(class_self,self,viewer,entry):
        for i in entry.keys():
            entry[i]['dialog'].hide()
            viewer['0']['obj'].gridLayout_6.removeWidget(entry[i]['dialog'])
            entry[i]['dialog'].deleteLater()


    def history_clear(class_self,self,viewer,entry):
        class_self.removeAll(self,viewer,entry)
        cfg={}
        with open(os.path.join(class_self.path,class_self.history_file),'w') as cnf:
            json.dump(cfg,cnf)

    def viewer_buttons_connect(class_self,self,viewer,entry):
        viewer['0']['obj'].close.clicked.connect(lambda: class_self.viewer_destroy(self,viewer))
        viewer['0']['obj'].clear.clicked.connect(lambda: class_self.history_clear(self,viewer,entry))

    def countConf(self,cfg,item,tree,mode):
        count=0
        for key in cfg.keys():
            if key != 'port':
                if cfg[key] == None:
                    count+=1
                if cfg[key] == False:
                    count+=1
                if cfg[key] == ['']:
                    count+=1
                if cfg[key] == '':
                    count+=1
            elif key == 'port':
                if cfg[key] == 22:
                    count+=1
        print(count)
        if count >= len(cfg.keys())-1:
            item.setHidden(True)
        return item

