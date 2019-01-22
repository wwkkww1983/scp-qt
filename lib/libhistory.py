from PyQt5 import QtWidgets,QtCore
import json,os,sys

libs=('./lib','./lib_widget')
for p in libs:
    sys.path.insert(0,p)

import historyView,entryView
import libstatements as state
class history(state.statements):
    #history_file=None
    #path='.'

    def open_history(class_self,self):
        keys={}
        with open(self.configJson['historyFile'],'r') as c:
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
            keys=class_self.open_history(self)

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

                modes=class_self.modesUseable(self,self.hist_d['entry'][em]['cfg'])
                class_self.entry_buttons_connect(self,self.hist_d['entry'][em],self.hist_d['entry'],modes,self.hist_d['viewer'])
                
                for mode in self.hist_d['entry'][em]['cfg'].keys():
                    if mode != 'date':
                        item=self.hist_d['entry'][em]['obj'].treeWidget.findItems(mode,QtCore.Qt.MatchExactly)[0]
                        #item_parts=[getattr(item,i) for i in dir(item)]
                        children=item.childCount()
                        self.hist_d['entry'][em]['num']=str(em)
                        
                        item=class_self.countConf(self,self.hist_d['entry'][em]['cfg'][mode],item,tree,mode)
                        for cnf in self.hist_d['entry'][em]['cfg'][mode].keys():
                            for i in range(children):
                                subChild=item.child(i)
                                n=subChild.text(0)
                                if n == cnf:
                                    print('{} : {} {} {}'.format(
                                        self.sayit(tag=self.vul),
                                        n,
                                        self.hist_d['entry'][em]['cfg'][mode][cnf]
                                        ,mode
                                        )
                                        )
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
            class_self.setClearState(self)
    
    def modesUseable(class_self,self,cfg):
        modes=[]
        print(cfg)
        for keys in cfg.keys():
            count=0
            if keys != 'date':
                for skeys in cfg[keys].keys():
                    if skeys != 'port' or skeys != 'useHostKey':
                        if cfg[keys][skeys] in ['',None]:
                            count+=1
                    if skeys == 'port':
                        if cfg[keys][skeys] in [22,None]:
                            count+=1
                    if skeys == 'useHostKey':
                        if cfg[keys][skeys] in [False,None]:
                            count+=1
                if count < len(cfg[keys].keys()):
                    modes.append(keys)
        return modes    

    def viewer_setup(class_self,self):
            keys=class_self.open_history(self)

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
                modes=class_self.modesUseable(self,entry[em]['cfg'])
                class_self.entry_buttons_connect(self,entry[em],entry,modes,viewer)
                for mode in entry[em]['cfg'].keys():
                    if mode != 'date':
                        item=entry[em]['obj'].treeWidget.findItems(mode,QtCore.Qt.MatchExactly)[0]
                        item_parts=[getattr(item,i) for i in dir(item)]
                        children=item.childCount()
                        entry[em]['num']=str(em)
                        #here is the problem 
                        #class_self.entry_buttons_connect(self,entry[em],entry,mode,viewer)
                        item=class_self.countConf(self,entry[em]['cfg'][mode],item,tree,mode)
                        for cnf in entry[em]['cfg'][mode].keys():
                            for i in range(children):
                                subChild=item.child(i)
                                n=subChild.text(0)
                                if n == cnf:
                                    print('{}: {} {} {}'.format(
                                        self.sayit(tag=self.vul),
                                        n,
                                        entry[em]['cfg'][mode][cnf],
                                        mode
                                        )
                                        )
                                    if n != 'sources':
                                       subChild.setData(1,QtCore.Qt.EditRole,entry[em]['cfg'][mode][cnf])
                                    else:
                                        if entry[em]['cfg'][mode][cnf] != None:
                                            for src in entry[em]['cfg'][mode][cnf]:
                                                if src not in [None,'']:
                                                    print('{} : {} {} {}'.format(
                                                        self.sayit(tag=self.vul),
                                                        src,
                                                        mode,
                                                        'srcs'
                                                        )
                                                        )
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
        #this is gettings run 2x not suposed to be. why?!
        self.in_config=cfg
        print('{} : {} {}'.format(
            self.sayit(tag=self.vul),
            self.in_config,
            cfg),
            sep='\n'
            )
        for m in mode:
            self.loadFields(tab=m)
            self.get_creds_wrapped(tab=m,updateHistory=False)

    def removeEntry(class_self,self,entry_bottom,entry_top,viewer):
        entry_bottom['dialog'].hide()
        viewer['0']['obj'].gridLayout_6.removeWidget(entry_bottom['dialog'])
        entry_bottom['dialog'].deleteLater()
       
        keys=class_self.open_history(self)
        print(keys.keys())
        #keys.pop(entry_bottom['num'])

        newCfg={}

        for num,i in enumerate(entry_top.keys()):
            if entry_bottom['num'] != entry_top[i]['num']:
                newCfg[str(num)]=entry_top[i]['cfg']
        
        with open(self.configJson['historyFile'],'w') as cnf:
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
            try:
                entry[i]['dialog'].hide()
                viewer['0']['obj'].gridLayout_6.removeWidget(entry[i]['dialog'])
                entry[i]['dialog'].deleteLater()
            except Exception as e:
                print(e)


    def history_clear_warn(class_self,self):
        warn={}
        warn['box']=QtWidgets.QMessageBox()
        warn['box'].setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        warn['box'].setWindowTitle('Warning')
        warn['box'].setText('You are about to clear your transaction History. Are You sure')
        warn['box'].setIcon(QtWidgets.QMessageBox.Warning)
        warn['box'].setDefaultButton(QtWidgets.QMessageBox.Yes)
        warn['box'].setEscapeButton(QtWidgets.QMessageBox.No)
        warn['box'].buttonClicked.connect(lambda arg: class_self.historyWarn(self,arg))
        return warn['box'].exec_()

    def historyWarn(class_self,self,arg):
        print('{} : user selected history clear : {} '.format(self.sayit(tag=self.vul),arg.text()))

    def history_clear(class_self,self,viewer,entry):
        warn=class_self.history_clear_warn(self)
        if warn == 16384:
            class_self.removeAll(self,viewer,entry)
            cfg={} 
            mode='w'
            with open(self.configJson['historyFile'],mode) as cnf:
                json.dump(cfg,cnf)
            self.hist_d['entry']={}
        else:
            msg='User cancelled clearing history!'
            print(msg)
            self.statusBar().showMessage(msg)
        class_self.setClearState(self)

    def setClearState(class_self,self):
        h=class_self.historyLen(self)
        if h < 1:
            class_self.clearEnable(self,False)
        else:
            class_self.clearEnable(self,True)

    def historyLen(class_self,self):
        if self.hist_d == None:
            return 0
        else:
            return len(self.hist_d['entry'].keys())

    def clearEnable(class_self,self,state):
        self.hist_d['viewer']['0']['obj'].clear.setEnabled(state)

    def viewer_buttons_connect(class_self,self,viewer,entry):
        viewer['0']['obj'].close.clicked.connect(lambda: class_self.viewer_destroy(self,viewer))
        viewer['0']['obj'].clear.clicked.connect(lambda: class_self.history_clear(self,viewer,entry))

    def countConf(class_self,self,cfg,item,tree,mode,returnItem=True):
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
        print('{} : {}'.format(self.sayit(tag=self.vul),count))
        if count >= len(cfg.keys())-1:
            if returnItem == True:
                item.setHidden(True)
        if returnItem == True:
            return item

