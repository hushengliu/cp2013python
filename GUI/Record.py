import collections


class MyClass(object):
    def __init__(self, name,e_id,amount,time):
        self.name=name
        self.e_id=e_id
        self.amount=amount
        self.time=time
    def get(self):
        d=collections.OrderedDict()
        d['name']=self.name
        d['e_id']=self.e_id
        d['amount']=self.amount
        d['time']=self.time
        return d