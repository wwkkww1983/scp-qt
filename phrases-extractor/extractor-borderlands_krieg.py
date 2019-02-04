import os,json,time,sqlite3
from bs4 import BeautifulSoup as bs
import string

class extractor:
    def __ini__(self):
        pass
    html=''
    settings={
            'file':'krieg_src.html',
            'tag':'krieg',
            'db':'statements.db'
            }
    data={}
    def krieg(self):
        scrubChars=['\n']
        with open(self.settings['file'],'r') as src:
            self.html=src.read()
        
        soup=bs(self.html,'html.parser')
        trim=soup.find_all('article')[0].find_all('li')
        count=0
        for i in trim:
            res=i.find_all(['div','a'])
            if res == []:
                if not i.has_attr('class'):
                    self.data[str(count)]=i.text
                    for char in scrubChars:
                        self.data[str(count)]=self.data[str(count)].replace(char,'')
                    count+=1
        
    def save(self):
        db=sqlite3.connect(self.settings['db'])
        cursor=db.cursor()
        sql='''insert into statements(phrase,tag) values(?,?);'''
        for i in self.data.keys():
            cursor.execute(sql,(self.data[i],self.settings['tag']))
        db.commit()
        db.close()

if __name__ == "__main__":
    app=extractor()
    app.krieg()
    app.save()

