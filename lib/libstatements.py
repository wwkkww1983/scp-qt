import os,sys,sqlite3,random

class statements:
    def __init__(self):
        pass
    dbname="statements.db"
    path="."

    def sayit(self,tag):
        randomColor=random.randint(30,37)
        
        db=sqlite3.connect(os.path.join(self.path,self.dbname))
        cursor=db.cursor()

        sql='select count(rowid) from statements;'
        cursor.execute(sql)
        top=cursor.fetchone()
        if top not in [(),None]:
            top=top[0]

        randomStatementAddr=random.randint(1,top)

        sql='select phrase from statements where rowid = {} and tag = ?;'.format(randomStatementAddr)
        cursor.execute(sql,(tag,))
        statement=cursor.fetchone()
        if statement not in [(),None,(None,)]:
            statement=statement[0]
        db.close()

        if statement != None:
            phrase_color='''\033[1;{0};40m{1}\033[1;40;m'''.format(randomColor,statement)
            print(phrase_color)
            return phrase_color
        else:
            return False

if __name__ == "__main__":
    app = statements()
    tags=['friendly','fiendish']
    for t in tags:
        app.sayit(tag=t)
        
