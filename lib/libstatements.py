import os,sys,sqlite3,random

class statements:
    def __init__(self):
        pass
    dbname="statements.db"
    path="."
    vul='fiendish'
    enable_statements=True
    db={'db':None,'cursor':None}
    fails=[None,[],()]
    def db_init(self):
        self.db['db']=sqlite3.connect(self.configJson['beColorfulDB'])
        self.db['cursor']=self.db['db'].cursor()

    def getTag(self):
        sql='''select tag from statements group by tag;'''
        self.db['cursor'].execute(sql)
        tags=self.db['cursor'].fetchall()
        tag=tags[random.randint(0,len(tags)-1)]
        if tag not in [None,[],()]:
            tag=tag[0]
        return tag

    def getRowID(self,tag):
        sql='''select rowid from statements where tag=?;'''
        self.db['cursor'].execute(sql,(tag,))
        ids=self.db['cursor'].fetchall()
        ID=ids[random.randint(0,len(ids)-1)][0]
        return ID

    def getAllTags(self):
        sql='''select tag from statements group by tag;'''
        db=sqlite3.connect(self.dbname)
        cursor=db.cursor()
        cursor.execute(sql)
        tags=cursor.fetchall()

        tags=[i[0] for i in tags if i not in self.fails]
        return tags

    def sayit(self,tag,noPrint=True):
        self.db_init()
        all_temp=tag
        if tag == 'disable':
            return ''
        if tag == 'All':
            tag=self.getTag()
            all_temp='All'
            
        randomColor=random.randint(30,37)
        
        sql='select count(rowid) from statements;'
        self.db['cursor'].execute(sql)
        top=self.db['cursor'].fetchone()
        if top not in [(),None]:
            top=top[0]
        #the line below has issues where rowid was not matched to tag, resulting in NoneType output
        #using the new line, fixes this
        #randomStatementAddr=random.randint(1,top)
        randomStatementAddr=self.getRowID(tag)
        
        statement=self.getStatement(randomStatementAddr,tag)        
        self.db['db'].close()
        
        if all_temp == 'All':
            statement='[{}] {}'.format(tag,statement)
        if statement != None:
            phrase_color='''\033[1;{0};40m{1}\033[1;40;m'''.format(randomColor,statement)
            if noPrint == False:
                print(phrase_color)
            return phrase_color
        else:
            return ''
        
    def getStatement(self,randomStatementAddr,tag):
        sql='select phrase from statements where rowid = {} and tag = ?;'.format(randomStatementAddr)
        self.db['cursor'].execute(sql,(tag,))
        statement=self.db['cursor'].fetchone()
        if statement not in [(),None,(None,)]:
            statement=statement[0]
        return statement

if __name__ == "__main__":
    app = statements()
    tags=['friendly','fiendish']
    for t in tags:
        app.sayit(tag=t,noPrint=False)
        
