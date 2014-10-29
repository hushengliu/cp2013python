# encoding:utf-8
import Employee, RecordDao
import WorkLoadDaoImpl, IHoursService, IAmountService, IEmployeeService
import EmployeeDaoImpl


class MyClass(IHoursService.MyClass,IAmountService.MyClass,IEmployeeService.MyClass):
    emdao = EmployeeDaoImpl.MyClass()
    wdao = WorkLoadDaoImpl.MyClass() 
    def __init__(self):
        pass
#   添加�?��新雇�?
    def addEmpl(self, em):
        return self.emdao.addEmpl(em)
#   修改雇员资料
    def changeEmpl(self, em):
        return self.emdao.changeEmpl(em)
#   删除指定的雇员及其工作量信息
    def delEmpl(self, emid):
        flag=False
        if self.emdao.delEmpl(emid) and self.wdao.delWorkByEmId(emid):
            flag=True
        return flag
#   改变指定公会会员的会费率
    def changeUnionRate(self, union_id, union_rate):
        em = Employee.Myclass(None, None, None, None, union_id, None, union_rate, None, None)
        return self.emdao.changeUnionRate(em)
#   获取�?��雇员信息
    def getAllEmpl(self):
        return self.emdao.getAllEmpl()
#   通过雇员工作类型获取雇员信息
    def getEmplByWork(self, work_mode):
        return self.emdao.getEmplByWork(work_mode)
#   通过id查询雇员信息
    def getEmplById(self, emid):
        return self.emdao.getEmplById(emid)
#   获取�?��加了公会的雇员的信息
    def getUnionEmpl(self):
        return self.emdao.getUnionEmpl()
#   为按业绩算薪水的雇员添加工作量信�?
    def addAmount(self, w):
        num = float(w.amount)
        em = Employee.Myclass(w.employee_id, None, None, None, None, None, None, str(num * 10), None)
        if self.wdao.add(w) and self.emdao.addSalary(em):
            return True
        else:
            return False
#   为按小时得薪水的雇员添加工作量信�?
    def addHours(self, w):
        flag = False
        num = float(w.hours)
        em1 = self.emdao.getEmplById(w.employee_id)
        rate = float(em1[0][8])
        if self.wdao.add(w):
            if num > 8:
                em2 = Employee.Myclass(w.employee_id, None, None, None, None, None, None, str((rate * 1.5 * (num - 8) + 8 * rate) * 10), None)
            else:
                em2 = Employee.Myclass(w.employee_id, None, None, None, None, None, None, str(num * rate * 10), None)
            if self.emdao.addSalary(em2):
                flag = True
        return flag
#   根据雇员编号获取其工作量信息
    def getWorkById(self, emid):
        return self.wdao.getById(emid)
#   删除指定类型�?��雇员工作量信息，type为传入的字符�?amount或�?hours)
    def deleteByType(self, type):
        return self.wdao.deleteByType(type)
#   结算日指定类型员工清�?type为传入的字符�?
    def clearSalary(self, type):
        em = Employee.Myclass(None, None, None, None, None, type, None, "0", None)
        return self.emdao.clearSalary(em)
#   得到指定类型�?��雇员工作量信息，type为传入的字符�?amount或�?hours)
    def getByType(self, type):
        return self.wdao.getByType(type)
#   判断u_id是否存在
    def judgeU_id(self, union_id):
        return self.emdao.judgeU_id(union_id)
    #   判断e_id是否存在
    def judgeE_id(self, e_id):
        return self.emdao.judgeE_id(e_id)
#   根据条件查询对应的雇�?
    def getFind(self, name, emid):
        if name == "" and emid == "":
            str = ""
        else:
            if name != "" and emid == "":
                name = "name like '%" + name + "%'"
            if name != "" and emid != "":
                name = "name like '%" + name + "%' and"
            if emid != "":
                emid = "employee_id=" + emid
            str = "where " + name + " " + emid
        return self.emdao.getFind(str)
    def getCommHourEmpl(self,work_mode,work_mode1):
        return self.emdao.getCommHourEmpl(work_mode, work_mode1)
    def addRecord(self,re):
        return RecordDao.MyClass().addRecord(re)
    def getRecords(self):
        return RecordDao.MyClass().getRecords()
    def getRecordByTime(self,time):
        return RecordDao.MyClass().getRecordByTime(time)
    def deleteRecord(self,time):
        return RecordDao.MyClass().deleteRecord(time)
