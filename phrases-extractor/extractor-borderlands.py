from bs4 import BeautifulSoup as bs
import json,os
import sqlite3

class extract:
    fname={
            'bandit':'./psycho_src.html'
            }
    text={
            'fiendish':[]
            }
    textRefined={
            'fiendish':[]
            }
    polished={
            'fiendish':[]
            }
    def bandit(self):
        with open(os.path.expanduser(self.fname['bandit']),'r') as html:
            self.soup=bs(html,'html.parser')
            uls=self.soup.find_all('ul')
            endtarget='''Killing a psycho contributes to the Mama's Boys'''
            starttarget='''I can still taste her lovely sweat box'''
            ulsRange=[]
            for num,i in enumerate(uls):
                if starttarget in i.text:
                    ulsRange.append(num)
                    break
            for num,i in enumerate(uls):
                if endtarget in i.text:
                    ulsRange.append(num)
                    break
            
            ulsNew=uls[ulsRange[0]:ulsRange[1]]
            for i in ulsNew:
                if i.b == None:
                    if 'Reference' not in i.text:
                        self.text['fiendish'].append(i.text)
                    else:
                        self.text['fiendish'].append(i.text.split('(Reference')[0])
            for num,i in enumerate(self.text['fiendish']):
                self.textRefined['fiendish'].extend(i.split('\n'))
            for i in self.textRefined['fiendish']:
                if i != '':
                    self.polished['fiendish'].append(i)

            for i in self.polished['fiendish']:
                self.save('fiendish',i)
        self.db.commit()
        self.db.close()

    def __init__(self):
        skip=False
        columns=[
                    ['phrase', 'text'],
                    ['tag', 'text'],
                    ['rowid', 'integer'],
                ]
        self.db=sqlite3.connect('statements.db')
        self.cursor=self.db.cursor()
        #check for statements table
        sql='''pragma table_info(statements);'''
        self.cursor.execute(sql)
        res=self.cursor.fetchall()
        if res in [None,[],()]:
            sql='''create table statements(phrase text,tag text,rowid integer primary key autoincrement);'''
            self.cursor.execute(sql)
            self.db.commit()
            skip = True
        
        if skip == False:
            #check for valid table
            if res != None:
                if len(res) == 3:
                    print('table exists... checking for valid table')
                    for i in res:
                        des=[i[1],i[2]]
                        if des not in columns:
                            exit('invalid table detected... please re-initialize "statements.db"')
                    print('valid table detected!')

    def save(self,tag,line):
        sql='''insert into statements(phrase,tag) values(?,?);'''
        self.cursor.execute(sql,(line,tag,))

if __name__ == "__main__":
    app=extract()
    app.bandit()

