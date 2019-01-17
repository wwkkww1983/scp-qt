import paramiko,engfmt
import time,sys,os
from PyQt5 import QtWidgets
class ssh:
    def __init__(self):
        pass
    statusBarMessage={
            'send':'',
            'get':''
            }
    connection_good={
            'send':True,
            'get':True,
            }
    transfer_log='transfer_{}'
    transfer_dir='./transfer_logs'
    logname={
            'send':None,
            'get':None
            }
    connection={
            'cfg':{
                'date':time.strftime('%S:%M:%H-%d/%m/%Y',time.localtime()),
                'send':{
                    'host':None,
                    'password':None,
                    'port':None,
                    'hostKey':None,
                    'useHostKey':False,
                    'sources':None,
                    'destination':None,
                    'remote_home':None,
                    'user':None,
                    },
                'get':{
                    'host':None,
                    'password':None,
                    'port':None,
                    'hostKey':None,
                    'useHostKey':False,
                    'sources':None,
                    'destination':None,
                    'remote_home':None,
                    'user':None,
                    }
                },
            'connect':{
                'send':{
                    'clientSSH':None,
                    'clientSCP':None,
                },
                'get':{
                        'clientSSH':None,
                        'clientSCP':None,
                    }
                }
            }
    fileSend=''
    mkdir_script='./scripts/mkdir.sh'

    def get_sources(self,tab,status_obj=None):
        self.create_transfer_log(tab)
        self.untilComplete(tab,False)
        #to ease with removal of duplicates
        sources=[]
        defaultDest='~/scp-qt-get'
        status=self.check_connection(tab=tab,obj=status_obj)
        if status == True:
            if not self.connection['cfg'][tab]['sources'] in [[],['']]:
                for source in self.connection['cfg'][tab]['sources']:
                    if os.path.exists(source):
                        if source not in sources:
                            sources.append(source)
                            print(sources)
            else:
                print('sources list is empty... not getting anything from the mothership!')
        else:
            self.untilComplete(tab,True)
            return False
        #need to rm none printable/control chars from sources list
        try:
            if self.in_config[tab]['useHostKey'] == True:
                self.rsa_client(tab=tab)
            else:
                self.password_client(tab=tab)
            self.transferClient(tab='get')
        except OSError as e:
            print(sys.exc_info())
            self.untilComplete(tab,True)
            return False
        #more to come
        if self.connection['cfg'][tab]['destination'] in [None,'']:
            print('setting default destination to "{}" since destination is blank!'.format(os.path.expanduser(defaultDest)))
            self.destination_get_le.setText(os.path.expanduser(defaultDest))
            if not os.path.exists(os.path.expanduser(defaultDest)):
                os.mkdir(os.path.expanduser(defaultDest))
            self.get_creds_wrapped(tab=tab) 
        #more to come
        self.get_list(
                self.connection['cfg'][tab]['destination'],
                self.connection['cfg'][tab]['sources'],
                self.connection['connect'][tab]['clientSCP']
                )
        self.progressBar_get.setValue(0)
        self.progressBar_get.setFormat('%p%')
        self.totalProgress_get.setValue(0)
        self.statusBar().showMessage('Done!')
        self.untilComplete(tab,True)

    def stopTransfer(self,tab):
        if tab == 'get':
            self.totalProgress_get.setValue(0)
            self.progressBar_get.setValue(0)
            self.totalProgress_get.setFormat('%p%')
            self.progressBar_get.setFormat('%p%')
            self.get_transfer_cancel.setEnabled(False)
        if tab == 'send':
            self.progressBar.setValue(0)
            self.totalProgress_send.setValue(0)
            self.progressBar.setFormat('%p%')
            self.totalProgress_send.setFormat('%p%')
            self.send_transfer_cancel.setEnabled(False)
        if self.connection['connect'][tab]['clientSCP'] != None:
            self.statusBar().showMessage('Transfer Stopped!')
            try:
                self.connection['connect'][tab]['clientSCP'].close()
            except:
                pass
            #self.connection['connect'][tab]['clientSCP']=None
        self.totalTransfer[tab]=0
        self.totalTransferred[tab]=0

    def checkExists(self,remote,sftp):
        try:
            res=sftp.lstat(remote)
            return res
        except:
            return False

    def create_transfer_log(self,tab):
        name=os.path.join(self.transfer_dir,self.transfer_log.format(tab))
        if not os.path.exists(self.transfer_dir):
            os.mkdir(self.transfer_dir)
        elif os.path.exists(self.transfer_dir) and not os.path.isdir(self.transfer_dir):
            exit('transfer_dir is not a dir')
        self.logname[tab]=name+"_"+time.strftime('%S.%M.%H-%m.%d.%Y',time.localtime())+".log"

    def send_sources(self,tab,status_obj=None):
        self.create_transfer_log(tab)
        self.totalTransferred['send']=0
        self.totalTransfer['send']=0
        self.untilComplete(tab,False)
        sources=[]
        status=self.check_connection(tab=tab,obj=status_obj)
        if status == True:
            if not self.connection['cfg'][tab]['sources'] in [[],['']]:
                for source in self.connection['cfg'][tab]['sources']:
                    if os.path.exists(source):
                        if source not in sources:
                            sources.append(source)
                            print(source)
            else:
                print('sources list is empty... not sending anything!')
        else:
            self.untilComplete(tab,True)
            return False
        #send from sources as sources should be duplicate and invalid free
        #setup client
        try:
            if self.in_config[tab]['useHostKey'] == True: 
                self.rsa_client(tab=tab)
            else: 
                self.password_client(tab=tab)
            self.transferClient(tab='send')
        except OSError as e:
            print(sys.exc_info())
            self.untilComplete(tab,True)
            return False
        if self.connection['cfg'][tab]['destination'] in ['',None]:
            #needs to be moved to more global location
            remote_alt=os.path.join(self.connection['cfg'][tab]['remote_home'],'scp-qt-send')
            print('destination cannot be empty! creating "{}" on remote host so file can be transfered!'.format(remote_alt))
            self.connection['cfg'][tab]['destination']=remote_alt
            self.destination.setText(remote_alt)
            if self.connection['connect'][tab]['clientSCP'].sock.closed != True:
                try:
                    res=self.checkExists(remote_alt,self.connection['connect'][tab]['clientSCP'])
                    if res == False:
                        self.connection['connect'][tab]['clientSCP'].mkdir(remote_alt)
                except OSError as e:
                    print('{} : {}'.format(remote_alt,str(e)))
            
            '''
            chan=self.connection['connect'][tab]['clientSSH'].get_transport().open_session()
            chan.exec_command(self.remote_script())
            status=chan.recv_exit_status()
            chan.close()
            if status == 0:
                self.statusColor(status=True,tab=tab,obj=status_obj)
            else:
                self.statusColor(status=False,tab=tab,obj=status_obj)
                if status == 1:
                    print('could not mkdir "{}"'.format(remote_alt))
                elif status == 2:
                    print('something already exists as "{}" that is not a directory!'.format(remote_alt))
                else:
                    print("something went wrong and I do not know what that may be!")
                self.untilComplete(tab,True)
                return False
            '''
        self.totalProgress_send.setMaximum(100)
        #total=0
        
        self.send_transfer_cancel.setEnabled(False)
        for source in sources:
            self.transfer_total_send(source)
        self.send_transfer_cancel.setEnabled(True)

        for source in sources:
            self.statusBarMessage['send']=source
            srcRoot=source.replace(os.path.basename(source),'')
            if os.path.isdir(source):
                dest=os.path.join(
                            self.connection['cfg'][tab]['destination'],
                            source.replace(srcRoot,
                                ''
                                )
                            )
                print(dest)
                res=self.sendData(source,self.connection['cfg'][tab]['destination'],srcRoot=srcRoot,tab=tab)
                if res == False:
                    break
                for root,dirs,fnames in os.walk(source,topdown=True):
                    for d in dirs:
                        res=self.sendData(os.path.join(root,d),self.connection['cfg'][tab]['destination'],srcRoot=srcRoot,tab=tab)
                        if res == False:
                            break
                    for fname in fnames:
                        res=self.sendData(os.path.join(root,fname),self.connection['cfg'][tab]['destination'],srcRoot=srcRoot,tab=tab)
                        if res == False:
                            break
            if os.path.isfile(source):
                res=self.sendData(source,self.connection['cfg'][tab]['destination'],srcRoot=srcRoot,tab=tab)
                if res == False:
                    break
            #total+=1
            #self.totalProgress_send.setValue(total)
            QtWidgets.QApplication.processEvents()
        
        self.statusBar().showMessage('Done!')
        self.progressBar.setFormat('%p%')
        self.totalProgress_send.setFormat('%p%')
        self.progressBar.setValue(0)
        self.totalTransferred['send']=0
        self.totalTransfer['send']=0
        self.totalProgress_send.setValue(0)
        #get a responce
        self.untilComplete(tab,True)
        return True
   
    def progressUpdateSend(self,transferred,toBeTransferred):
        self.progressBar.setFormat('{}/{} {} - %p%'.format(engfmt.quant_to_eng(transferred,prec=2),engfmt.quant_to_eng(toBeTransferred,prec=2),self.fileSend))
        p=int((transferred/toBeTransferred)*100)
        self.progressBar.setValue(p)
        self.statusBar().showMessage(self.statusBarMessage['send'])

        self.print_terminal_updates(
                engfmt.quant_to_eng(transferred,prec=2),
                engfmt.quant_to_eng(toBeTransferred,prec=2),
                self.fileSend,self.fileSend
                )

        QtWidgets.QApplication.processEvents()

    def remote_script(self):
        script_str=''
        with open(self.mkdir_script,'r') as script:
            script_str=script.read()
        return script_str
    def write_log_send(self,src,dest,tab):
        with open(self.logname[tab],'a') as log:
            log.write('{} -> {}@{}:{}\n'.format(
                src,
                self.connection['cfg'][tab]['user'],
                self.connection['cfg'][tab]['host'],
                dest
                ))

    def sendData(self,src,dest,srcRoot,tab):
        self.write_log_send(src,dest,tab=tab)
        #print(self.connection['connect'][tab]['clientSCP'].sock.closed)
        if self.connection['connect'][tab]['clientSCP'].sock.closed == True:
            return False
        try:
            if self.connection['connect'][tab]['clientSCP'].sock.closed != True:
                self.connection['connect'][tab]['clientSCP'].stat(dest)
            else:
                return False
        except FileNotFoundError as e:
            if self.connection['connect'][tab]['clientSCP'].sock.closed != True:
                print('{0} : mkdir({1})'.format(e,dest))
                self.connection['connect'][tab]['clientSCP'].mkdir(dest)
            else:
                return False

        print('[start] {} -> {}'.format(src,os.path.join(src,os.path.join(dest,src.replace(srcRoot,'')))))
        if os.path.isdir(src):
            try:
                if self.connection['connect'][tab]['clientSCP'].sock.closed != True:
                    self.connection['connect'][tab]['clientSCP'].stat(os.path.join(dest,src.replace(srcRoot,'')))
                else:
                    return False
            except FileNotFoundError as e:
                if self.connection['connect'][tab]['clientSCP'].sock.closed != True:
                    self.connection['connect'][tab]['clientSCP'].mkdir(os.path.join(dest,src.replace(srcRoot,'')))
                else:
                    return False
        if os.path.isfile(src):
            #self.statusBar().showMessage(src)
            self.fileSend=os.path.basename(src)
            if len(self.fileSend) > 10:
                self.fileSend=self.fileSend[:10]+'...'
            self.progressBar.setMinimum(0)
            self.progressBar.setMaximum(100)
            if self.connection['connect'][tab]['clientSCP'].sock.closed != True:
                try:
                    self.connection['connect'][tab]['clientSCP'].put(src,os.path.join(dest,src.replace(srcRoot,'')),callback=self.progressUpdateSend)
                    self.send_transfer_update_total(src)
                except:
                    print(sys.exc_info())
            else:
                return False
        print('[stop] {} -> {}'.format(src,dest))


    def rsa_client(self,tab='send'):
        try:
            self.connection['connect'][tab]['clientSSH']=paramiko.SSHClient()
            self.connection['connect'][tab]['clientSSH'].load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))                    
            self.connection['connect'][tab]['clientSSH'].set_missing_host_key_policy(paramiko.AutoAddPolicy())
            #self.connection['connect']['clientSSH'].load_system_host_keys(self.connection['cfg']['hostKey']) 
            
            self.connection['connect'][tab]['clientSSH'].connect(
                    hostname=self.connection['cfg'][tab]['host'],
                    username=self.connection['cfg'][tab]['user'],
                    password=self.connection['cfg'][tab]['password'],
                    port=self.connection['cfg'][tab]['port'],
                    key_filename=self.connection['cfg'][tab]['hostKey']
                    )
            return True
        except:
            print(sys.exc_info())
            return False
    
    def transferClient(self,tab):
        self.connection['connect'][tab]['clientSCP']=self.connection['connect'][tab]['clientSSH'].open_sftp()


    def password_client(self,tab='send'):
        try:
            self.connection['connect'][tab]['clientSSH']=paramiko.SSHClient()
            self.connection['connect'][tab]['clientSSH'].load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))                    
            self.connection['connect'][tab]['clientSSH'].set_missing_host_key_policy(paramiko.AutoAddPolicy())
            #self.connection['connect']['clientSSH'].load_system_host_keys(self.connection['cfg']['hostKey']) 
            
            self.connection['connect'][tab]['clientSSH'].connect(
                    hostname=self.connection['cfg'][tab]['host'],
                    username=self.connection['cfg'][tab]['user'],
                    password=self.connection['cfg'][tab]['password'],
                    port=self.connection['cfg'][tab]['port'],
                    look_for_keys=False,
                    allow_agent=False
                    )
            #self.connection['connect'][tab]['clientSCP']=self.connection['connect'][tab]['clientSSH'].open_sftp()
            return True
        except:
            print(sys.exc_info())
            return False

    def mkDate(self):
        return time.strftime('%S:%M:%H-%d/%m/%Y',time.localtime())

    def get_creds_wrapped(self,tab,updateHistory=True):
        self.connection['cfg']['date']=self.mkDate()
        if tab == 'send':
            self.get_creds_v2(
                tab=tab,
                host_address=self.host_address,
                port_remote=self.port_remote,
                user_remote=self.user_remote,
                password_remote=self.password_remote,
                destination=self.destination,
                hostKey=self.hostKey,
                useKeys=self.useKeys,
                sources=self.sources)
        if tab == 'get':
            self.get_creds_v2(
                tab=tab,
                host_address=self.host_address_get,
                port_remote=self.port_remote_get,
                user_remote=self.user_remote_get,
                password_remote=self.password_remote_get,
                destination=self.destination_get_le,
                hostKey=self.hostKey_get,
                useKeys=self.useKeys_get,
                sources=self.source_le)
        self.update_cnf(tab=tab)
        if updateHistory == True:
            self.transHistory_save()

    def update_cnf(self,tab):
        self.connection['cfg'][tab]['host']=self.in_config[tab]['host']
        self.connection['cfg'][tab]['port']=self.in_config[tab]['port']
        self.connection['cfg'][tab]['user']=self.in_config[tab]['user']
        self.connection['cfg'][tab]['password']=self.in_config[tab]['password']
        self.connection['cfg'][tab]['hostKey']=self.in_config[tab]['hostKey']
        self.connection['cfg'][tab]['useHostKey']=self.in_config[tab]['useHostKey']
        self.connection['cfg'][tab]['destination']=self.in_config[tab]['destination']
        self.connection['cfg'][tab]['sources']=self.in_config[tab]['sources']

        for key in self.in_config[tab].keys():
            if key in self.in_config[tab].keys():
                if self.in_config[tab][key] == None:
                    self.get_creds_wrapped(tab=tab)

    def check_connection(self,tab,obj=None):
        print('checking connection!')
        #self.get_creds(tab=tab)
        self.get_creds_wrapped(tab=tab)
        print(self.in_config[tab])
        '''
        self.connection['cfg'][tab]['host']=self.in_config[tab]['host']
        self.connection['cfg'][tab]['port']=self.in_config[tab]['port']
        self.connection['cfg'][tab]['user']=self.in_config[tab]['user']
        self.connection['cfg'][tab]['password']=self.in_config[tab]['password']
        self.connection['cfg'][tab]['hostKey']=self.in_config[tab]['hostKey']
        self.connection['cfg'][tab]['useHostKey']=self.in_config[tab]['useHostKey']
        self.connection['cfg'][tab]['destination']=self.in_config[tab]['destination']
        self.connection['cfg'][tab]['sources']=self.in_config[tab]['sources']

        for key in self.in_config[tab].keys():
            if key in self.in_config[tab].keys():
                if self.in_config[tab][key] == None:
                    self.get_creds_wrapped(tab=tab)
        '''
        self.update_cnf(tab=tab)
        self.connection_good[tab]=self.connect_init_test(tab)
        self.statusColor(status=self.connection_good[tab],obj=obj) 
        return self.connection_good[tab]
        '''
        for i in range(0,30000
            QtWidgets.QApplication.processEvents()
            print(i)
        '''
        '''
        if self.connection_good == True:
            self.statusColor(status=self.connection_good)
        else:
            self.statusColor(status=self.connection_good)
        print(self.in_config)
        '''
    def connect_init_test(self,tab): 
        try:
            print(self.in_config[tab]['useHostKey'])
            if self.in_config[tab]['useHostKey'] == True: 
                return self.rsa_test_connection(tab=tab)
            else: 
                return self.password_test_connection(tab=tab)
        except OSError as e:
            print(sys.exc_info())
            return False
        #get a responce
        return True

    def rsa_test_connection(self,tab):
        print('using host key!')
        skipNext=False
        try:
            self.connection['connect'][tab]['clientSSH']=paramiko.SSHClient()
            self.connection['connect'][tab]['clientSSH'].load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))                    
            self.connection['connect'][tab]['clientSSH'].set_missing_host_key_policy(paramiko.AutoAddPolicy())
            #self.connection['connect']['clientSSH'].load_system_host_keys(self.connection['cfg']['hostKey']) 
            
            self.connection['connect'][tab]['clientSSH'].connect(
                    hostname=self.connection['cfg'][tab]['host'],
                    username=self.connection['cfg'][tab]['user'],
                    password=self.connection['cfg'][tab]['password'],
                    port=self.connection['cfg'][tab]['port'],
                    key_filename=self.connection['cfg'][tab]['hostKey']
                    )
        except paramiko.ssh_exception.AuthenticationException as e:
            print(e)
            skipNext=True
        except:
            print(self.connection['cfg'][tab]['host'])
            print(sys.exc_info())
            skipNext=True
            
        if skipNext == True:
            return False
        try:
            stdin,stdout,stderr=self.connection['connect'][tab]['clientSSH'].exec_command('echo $HOME')
            response=stdout.readlines()
            if response:
                response=response[0]
                self.connection['cfg'][tab]['remote_home']=response.replace('\n','')
                print('remote_home: {}'.format(self.connection['cfg'][tab]['remote_home']))
            self.connection['connect'][tab]['clientSSH'].close()
            self.connection['connect'][tab]['clientSSH']=None
        except:
            return False
        return True

    def password_test_connection(self,tab):
        print('using password')
        skipNext=False
        try:
            print(self.connection['cfg'])
            self.connection['connect'][tab]['clientSSH']=paramiko.SSHClient()
            self.connection['connect'][tab]['clientSSH'].load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
            self.connection['connect'][tab]['clientSSH'].set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.connection['connect'][tab]['clientSSH'].connect(
                    hostname=self.connection['cfg'][tab]['host'],
                    port=self.connection['cfg'][tab]['port'],
                    username=self.connection['cfg'][tab]['user'],
                    password=self.connection['cfg'][tab]['password'],
                    look_for_keys=False,
                    allow_agent=False
                    )
        except:
            skipNext=True
            print(sys.exc_info())
        if skipNext == True:
            return False
        try:
            stdin,stdout,stderr=self.connection['connect'][tab]['clientSSH'].exec_command('echo $HOME')
            response=stdout.readlines()
            if response:
                response=response[0]
                self.connection['cfg'][tab]['remote_home']=response.replace('\n','')
                print('remote_home: {}'.format(self.connection['cfg'][tab]['remote_home']))
            self.connection['connect'][tab]['clientSSH'].close()
            self.connection['connect'][tab]['clientSSH']=None
        except:
            return False
        return True


'''
if __name__ == '__main__':
    app=ssh()
    app.connection['cfg']['host']='localhost'
    app.connection['cfg']['port']=22
    app.connection['cfg']['user']='carl'
    app.connection['cfg']['password']=''
    app.connection['cfg']['hostKey']='/home/carl/.ssh/id_rsa'
    app.connection['cfg']['useHostKey']=True
    app.connect_init_test()
'''
