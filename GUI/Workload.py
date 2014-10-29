#encoding:utf-8
import collections


class Workload(object):
    
    def __init__(self, employee_id,workdate,amount,hours):
        self.employee_id=employee_id
        self.workdate=workdate
        self.amount=amount
        self.hours=hours    
    def get(self):
        d=collections.OrderedDict()
        d['employee_id']=self.employee_id
        d['workdate']=self.workdate
        d['amount']=self.amount
        d['hours']=self.hours
        return d