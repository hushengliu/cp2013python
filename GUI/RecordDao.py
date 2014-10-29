#encoding:utf-8
import db
import IRecordDao


class MyClass(IRecordDao.MyClass):
    def __init__(self):
        pass
    def addRecord(self,re):
        dbconn=db.MyClass()
        table="record"
        if dbconn.insert(table, re.get()):
            return True
        else:
            return False
    def getRecords(self):
        dbconn=db.MyClass()
        table="record"
        l=dbconn.get(table,"")           
        return l
    def getRecordByTime(self,time):
        dbconn=db.MyClass()
        table="record"
        self.str="where time='"+time+"'"
        l=dbconn.get(table,self.str)           
        return l
    def deleteRecord(self,time):
        dbconn=db.MyClass()
        table="record"
        self.str="where time='"+time+"'"
        l=dbconn.delete(table, self.str)
        return l