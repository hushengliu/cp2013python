#encoding:utf-8
import db
import IWorkLoadDao


class MyClass(IWorkLoadDao.MyClass):
    def __init__(self):
        pass
#   添加雇员工作量信�?w为传入的workload类实�?
    def add(self,w):
        dbconn=db.MyClass()
        table="workload"
        if dbconn.insert(table, w.get()):
            return True
        else:
            return False
#   根据雇员id取得该雇员所有的工作量信�?
    def getById(self,emid):
        dbconn=db.MyClass()
        table="workload"
        str="where employee_id="+emid
        l=dbconn.get(table, str)
        return l
#   根据类型删除该类型下�?��的雇员工作量信息
    def deleteByType(self,type):
        dbconn=db.MyClass()
        table="workload"
        str="where "+type+" is not null"
        if dbconn.delete(table, str):
            return True
        else:
            return False
#   根据雇员id删除该雇员所有的工作量信�?
    def delWorkByEmId(self,emid):
        dbconn=db.MyClass()
        table="workload"
        str="where employee_id="+emid
        if dbconn.delete(table, str):
            return True
        else:
            return False
#   根据类型取得�?��该类型雇员的工作量信�?
    def getByType(self,type):
        dbconn=db.MyClass()
        table="workload"
        str="where "+type+" is not null"
        l=dbconn.get(table, str)
        return l