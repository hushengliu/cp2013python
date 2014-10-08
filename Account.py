import collections
class MyClass(object):
    def __init__(self, e_id,e_account):
        self.e_id=e_id
        self.e_account=e_account
    def get(self):
        d=collections.OrderedDict()
        d['e_id']=self.e_id
        d['e_account']=self.e_account
        return d
        