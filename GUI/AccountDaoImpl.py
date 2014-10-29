import db
import IAccountDao


class MyClass(IAccountDao.MyClass):
    def __init__(self):
        pass
    def addAcc(self,acc):
        dbconn=db.MyClass()
        table="account"
        if dbconn.insert(table, acc.get()):
            return True
        else:
            return False
    def getAccById(self,e_id):
        dbconn=db.MyClass()
        table="account"
        self.str="where e_id="+e_id
        l=dbconn.get(table, self.str)
        return l
    def delAccById(self,e_id):
        dbconn=db.MyClass()
        self.str="where e_id="+e_id
        table ="account"
        if dbconn.delete(table, self.str):
            return True
        else:
            return False
        