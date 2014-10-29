#encoding:utf-8
import db
import IEmployeeDao


class MyClass(IEmployeeDao.MyClass):
    
    def __init__(self):
        pass
#   添加�?��新雇员，em为传入的employee类实�?
    def addEmpl(self,em):
        dbconn=db.MyClass()
        table="employee"
        if dbconn.insert(table, em.get()):
            return True
        else:
            return False
#   修改雇员资料，em为传入的employee类实�?
    def changeEmpl(self,em):
        dbconn=db.MyClass()
        table="employee"
        judge="employee_id"
        if dbconn.update(table, em.get(),judge)>0:
            return True
        else:
            return False
#   删除指定的雇员，emid为传入的employee_id(字符串型)
    def delEmpl(self,emid):
        dbconn=db.MyClass()
        str="where employee_id="+emid
        table ="employee"
        if dbconn.delete(table, str):
            return True
        else:
            return False
#   改变指定公会会员的会费率，em为传入的employee类实�?
    def changeUnionRate(self,em):
        dbconn=db.MyClass()
        table ="employee"
        if dbconn.update(table, em.get(),"union_id"):
            return True
        else:
            return False
#   获取�?��雇员信息
    def getAllEmpl(self):
        dbconn=db.MyClass()
        table="employee"
        l=dbconn.get(table, "")           
        return l
#   获取�?��加了公会的雇员的信息
    def getUnionEmpl(self):
        dbconn=db.MyClass()
        table="employee"
        str=" where union_id>0"
        l=dbconn.get(table, str)
        return l
#   为指定雇员添加薪�?还未扣除会费�?，em为传入的employee类实�?
    def addSalary(self,em):
        dbconn=db.MyClass()
        table="employee"
        d=em.get()
        d["no_salary"]="no_salary+"+d["no_salary"]
        if dbconn.update(table, d, "employee_id"):
            return True
        else:
            return False
#   结算日清零，em为传入的employee类实�?
    def clearSalary(self,em):
        dbconn=db.MyClass()
        table="employee"
        if dbconn.update(table, em.get(), "work_mode"):
            return True
        else:
            return False
#   得到指定雇员的信息，emid为传入的employee_id(字符串型)
    def getEmplById(self,emid):
        dbconn=db.MyClass()
        table="employee"
        str="where employee_id="+emid
        l=dbconn.get(table, str)
        return l
#   根据工作类型得到雇员的信息，work_mode为传入的工作类型
    def getEmplByWork(self,work_mode): 
        dbconn=db.MyClass()
        table="employee"
        str="where work_mode='"+work_mode+"'"
        l=dbconn.get(table, str)
        return l
#   根据工作类型得到雇员的信息，work_mode为传入的工作类型
    def getCommHourEmpl(self,work_mode,work_mode1): 
        dbconn=db.MyClass()
        table="employee"
        str="where work_mode='"+work_mode+"' or work_mode='"+work_mode1+"'"
        l=dbconn.get(table, str)
        return l
#   根据条件查询对应的雇�?
    def getFind(self,str):
        dbconn=db.MyClass()
        table="employee"
        l=dbconn.get(table, str)
        return l
#   根据传入的会员id判断会员是否存在
    def judgeU_id(self,union_id):
        dbconn=db.MyClass()
        table="employee"
        str="where union_id="+union_id
        if len(dbconn.get(table, str))!=0:
            return True
        else:
            return False
#   根据传入的e_id判断会员是否存在
    def judgeE_id(self,e_id):
        dbconn=db.MyClass()
        table="employee"
        str="where employee_id="+e_id
        if len(dbconn.get(table, str))!=0:
            return True
        else:
            return False