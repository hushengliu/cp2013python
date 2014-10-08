#encoding:utf-8
import collections
class Myclass(object):
    def __init__(self, employee_id, name, address, payment, union_id, work_mode, union_rate, no_salary, salary_rate):
        self.employee_id = employee_id
        self.name = name
        self.address = address
        self.payment = payment
        self.union_id = union_id
        self.work_mode = work_mode
        self.union_rate = union_rate
        self.no_salary = no_salary
        self.salary_rate = salary_rate
#   将employee类型转换成一个有序的dictionary类型
    def get(self):
        d=collections.OrderedDict()
        d['employee_id']=self.employee_id
        d['name']=self.name
        d['address']=self.address
        d['payment']=self.payment
        d['union_id']=self.union_id
        d['work_mode']=self.work_mode
        d['union_rate']=self.union_rate
        d['no_salary']=self.no_salary
        d['salary_rate']=self.salary_rate
        return d
