from os import chmod
import os,io
from Crypto.PublicKey import RSA
import paramiko

class generator:
    def __init__(self):
        self.key = RSA.generate(2048)

    def genPrivate(self,path,file,encrypt=False,passphrase=None):
        with open(os.path.join(path,file), 'wb') as content_file:
            chmod(os.path.join(path,file),0o600)
            if encrypt == False:
                content_file.write(self.key.exportKey('PEM'))
            else:
                content_file.write(self.key.exportKey(
                    passphrase=passphrase,
                    pkcs=8,
                    protection='scryptAndAES128-CBC'
                    )
                    )
    def genPublic(self,path,file):
        pubkey = self.key.publickey()
        with open(os.path.join(path,file), 'wb') as content_file:
            content_file.write(pubkey.exportKey('OpenSSH'))

    def dumpKey(self,privateKeyString,passphrase=None):
        return RSA.import_key(privateKeyString,passphrase).export_key().decode()

    def paramikoRSA(self,keyString):
        keyIO=io.StringIO(keyString)
        param=paramiko.RSAKey.from_private_key(keyIO)
        return param

if __name__ == "__main__":
    app=generator()
    app.genPrivate('/home/carl/genkey/','private1.key',encrypt=True,passphrase='password123')
    app.genPublic('/home/carl/genkey/','public1.key')
    k=app.dumpKey(open('/home/carl/genkey/private1.key','rb').read(),passphrase='password123')
    r=app.paramikoRSA(k)
    print(k)
