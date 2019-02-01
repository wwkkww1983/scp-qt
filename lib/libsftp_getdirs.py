#!/usr/bin/env python3
import paramiko, os,sys
paramiko.util.log_to_file('/tmp/paramiko.log')
from stat import S_ISDIR,S_ISREG
from PyQt5 import QtWidgets
import pathlib
import libtotal_progress_send

sys.path.insert(0,'./lib')
OS=os.uname().sysname
if OS == 'windows':
    from libengformat_wrapper import engfmt
    engfmt=engfmt()
else:
    import engfmt


class sftp_get:
    fileGet=''
    state={
            'get':True,
            'send':True
            }
    totalTransfer={
            'get':0,
            'send':0
            }
    totalTransferred={
            'get':0,
            'send':0
            }
    def sftp_walk(self,remotepath,sftp):
        #this bit of code is dominantly not mine
        #just needed something quick
        #the code can found at the url below
        #https://techtalkontv.wordpress.com/2016/11/05/python-pramiko-sftp-copydownload-all-files-in-a-folder-recursively-from-remote-server/
        path=remotepath
        files=[]
        folders=[]
        try:
            if sftp.sock.closed != True:
                for f in sftp.listdir_attr(remotepath):
                    if self.stopTRX['get'] == True:
                        break
                    if sftp.sock.closed != True:
                        if S_ISDIR(f.st_mode):
                            folders.append(f.filename)
                        else:
                            if S_ISREG(f.st_mode):
                                files.append(f.filename)
            if files:
                yield path, files
            for folder in folders:
                if self.stopTRX['get'] == True:
                    break
                new_path=os.path.join(remotepath,folder)
                if sftp.sock.closed != True:
                    for x in self.sftp_walk(new_path,sftp):
                        if self.stopTRX['get'] == True:
                            break
                        yield x
                else:
                    break
        except PermissionError as e:
            self.statusBar().showMessage(str(e))


    def get_remote_total(self,remotepath,sftp):
        self.state['get']=True
        try:
            if not S_ISDIR(sftp.lstat(remotepath).st_mode) and S_ISREG(sftp.lstat(remotepath).st_mode):
                self.totalTransfer['get']+=sftp.lstat(remotepath).st_size
                self.statusBar().showMessage(engfmt.quant_to_eng(self.totalTransfer['get'],prec=2))
                QtWidgets.QApplication.processEvents()
            else:
                for path,files in self.sftp_walk(remotepath,sftp):
                    for file in files:
                        if self.stopTRX['get'] == True:
                            break
                        self.totalTransfer['get']+=sftp.lstat(os.path.join(path,file)).st_size
                        self.statusBar().showMessage(engfmt.quant_to_eng(self.totalTransfer['get'],prec=2))
                        QtWidgets.QApplication.processEvents()
        except FileNotFoundError as e:
            print(e)
            self.state['get']=False
            self.statusBar().showMessage("no such source")

    def mkLocal_path(self,local_p):
        if not os.path.exists(local_p):
            pathlib.Path(local_p).mkdir(parents=True,exist_ok=True)

    def print_terminal_updates(self,transferred,toBeTransferred,fileTruncated,fileNotTruncated):
        msg='{}/{} TRUNCATED_NAME:"{}..." FULL:"{}"'.format(transferred,toBeTransferred,fileTruncated,fileNotTruncated)
        msg_len=len(msg)
        screen_len=os.get_terminal_size().columns
        screen='\b'*screen_len
        print(screen,end='')
        print(msg_len*'\b'+msg,end='')

    def progressUpdateGet(self,transferred,toBeTransferred):
        '''
        self.totalTransferred['get']+=transferred
        tp=int(self.totalTransferred['get']/self.totalTransfer['get'])*100
        self.totalProgress_get.setValue(tp)
        print(tp,self.totalTransferred['get'],self.totalTransfer['get'])
        '''
        try:
            p=int((transferred/toBeTransferred)*100)
        except:
            pass
        transferred=engfmt.quant_to_eng(transferred,prec=2)
        toBeTransferred=engfmt.quant_to_eng(toBeTransferred,prec=2)
        
        self.print_terminal_updates(transferred,toBeTransferred,self.fileGet,self.fileGetNotTruncated)
        
        '''
        msg='{}/{} TRUNCATED_NAME:"{}..." FULL:"{}"'.format(transferred,toBeTransferred,self.fileGet,self.fileGetNotTruncated)
        msg_len=len(msg)
        screen_len=os.get_terminal_size().columns
        screen='\b'*screen_len
        print(screen,end='')
        
        print(msg_len*'\b'+msg,end='')
        '''
        #print('')
        try:
            self.progressBar_get.setFormat('{}/{} {} - %p%'.format(transferred,toBeTransferred,self.fileGet))
            self.progressBar_get.setValue(p)
            self.statusBar().showMessage(self.statusBarMessage['get'])
            QtWidgets.QApplication.processEvents()
        except:
            if __name__ != "__main__":
                print(sys.exc_info())
            pass


    def write_log(self,remote,local_p,tab): 
        with open(self.logname['get'],'a') as log:
            log.write('{}@{}:{} -> {} : {}\n'.format(
                    self.connection['cfg'][tab]['user'],
                    self.connection['cfg'][tab]['host'],
                    remote,
                    local_p,
                    self.checksum(local_p,tab='get')
                    ))

    def get_list(self,local_p,remote_list,sftp):
        self.totalProgress_get.setMaximum(100)
        self.totalTransfer['get']=0
        self.totalTransferred['get']=0
        self.get_transfer_cancel.setEnabled(False)
        for remote in remote_list:
            if self.stopTRX['get'] == True:
                break
            self.statusBar().showMessage('Getting total to Transfer!')
            self.get_remote_total(remote,sftp)
        self.get_transfer_cancel.setEnabled(True)
        #print(self.totalTransfer['get'])
        #exit()
        for remote in remote_list:  
            if self.stopTRX['get'] == True:
                break
            self.statusBarMessage['get']=remote
            try:
                self.get_items(local_p,remote,sftp)
            except FileNotFoundError as e:
                print(e)
                self.statusBar().showMessage('no such source')

            #total+=1
            #self.totalProgress_get.setValue(total)
            #QtWidgets.QApplication.processEvents()
        self.totalTransfer['get']=0
        self.totalProgress_get.setFormat('%p%')
        self.totalProgress_get.setValue(0)
        self.totalTransferred['get']=0

    def transfer_total_send(self,local):
        progress=libtotal_progress_send.itemize()
        self.totalTransfer['send']+=progress.total_transfer_send(local,gui=self)

    def send_transfer_update_total(self,file):
        self.totalTransferred['send']+=os.stat(file).st_size
        tp=int((self.totalTransferred['send']/self.totalTransfer['send'])*100)
        self.totalProgress_send.setFormat('{}/{} - %p%'.format(
            engfmt.quant_to_eng(self.totalTransferred['send'],prec=2),
            engfmt.quant_to_eng(self.totalTransfer['send'],prec=2)))
        self.totalProgress_send.setValue(tp)
        print(tp,self.totalTransferred['send'],self.totalTransfer['send'])
        QtWidgets.QApplication.processEvents()

    def get_transfer_update_total(self,remote,sftp):
        try:
            if sftp.sock.closed != True:
                self.totalTransferred['get']+=sftp.lstat(remote).st_size
                tp=int((self.totalTransferred['get']/self.totalTransfer['get'])*100)
                self.totalProgress_get.setFormat('{}/{} - %p%'.format(
                    engfmt.quant_to_eng(self.totalTransferred['get'],prec=2),
                    engfmt.quant_to_eng(self.totalTransfer['get'],prec=2)))
    
                self.totalProgress_get.setValue(tp)
                #print(tp,self.totalTransferred['get'],self.totalTransfer['get'])
                QtWidgets.QApplication.processEvents()
            else:
                return False
        except:
            return False

    def getFileStatus(self,remote):
        self.fileGet=os.path.basename(remote)
        self.fileGetNotTruncated=self.fileGet
        if len(self.fileGet) > 10:
            self.fileGet=self.fileGet[:10]

    def get_items(self,local_p,remote,sftp):
        self.mkLocal_path(local_p)
        remote_root=os.path.split(remote)[0]
        
        if remote_root in ['/']:
            remote_root='/'
        else:
            remote_root=remote_root
        
        print(remote_root,remote)
        if sftp.sock.closed != True:
            if not S_ISDIR(sftp.lstat(remote).st_mode) and S_ISREG(sftp.lstat(remote).st_mode):
                self.getFileStatus(remote)
                print(remote_root,local_p)
                lroot=remote.replace(remote_root,'')
                if lroot[0] == '/':
                    lroot=lroot[1:]
                where=os.path.join(local_p,lroot)
                try:
                    if sftp.sock.closed != True:
                        sftp.get(remote,where,callback=self.progressUpdateGet)
                        self.write_log(remote,where,tab='get')
                        self.get_transfer_update_total(remote,sftp)
                    else:
                        return True
                except Exception as e:
                    print(e)
                    pass
            else:
                if sftp.sock.closed != True:
                    for path,files  in self.sftp_walk(remote,sftp):
                        if self.stopTRX['get'] == True:
                            break
                        for file in files:
                            if self.stopTRX['get']  == True:
                                break
                            #sftp.get(remote, local) line for dowloading.
                            if remote_root != '/':
                                stripped=path.replace(remote_root,'')[1:]
                            else:
                                stripped=path[1:]
                            new_path=os.path.join(local_p,stripped)
                            newPath_withFile=os.path.join(new_path,file)
                            directions={
                                    'remote':{
                                    'path':path,
                                        'file':file,
                                        'path+file':os.path.join(path,file)
                                    },
                                    'local':{
                                        'path':new_path,
                                        'file':file,
                                        'path+file':newPath_withFile
                                        }
                                    }
                    
                            print(directions)
                            if not os.path.exists(directions['local']['path']):
                                pathlib.Path(directions['local']['path']).mkdir(parents=True,exist_ok=True)
                            self.getFileStatus(directions['remote']['path+file'])
                            try:
                                if sftp.sock.closed != True:
                                    sftp.get(directions['remote']['path+file'],directions['local']['path+file'],self.progressUpdateGet)
                                    self.write_log(directions['remote']['path+file'],directions['local']['path+file'],'get')
                                    res=self.get_transfer_update_total(directions['remote']['path+file'],sftp)
                                    print('line 197: {}'.format(res))
                                    if res == False:
                                        return False
                                else:
                                    return False
                            except TypeError as e:
                                print(e)
                            except:
                                print(sys.exc_info())
                                return False
        else:
            return False
#test code to ensure working operation
if __name__ == "__main__":
    host = "localhost"
    port = 22
    password = ""
    username = ""

    client=paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh=client.connect(
            hostname=host,
            port=port,
            username=username,
            password=password,
            allow_agent=False,look_for_keys=False
            )
    sftp=client.open_sftp()


    local_p='/home/carl/test-ssh-drops'
    remote=['/home/carl/newpc.json','/home/carl/Documents','/etc']
    app=sftp_get()
    app.get_list(local_p,remote,sftp)
