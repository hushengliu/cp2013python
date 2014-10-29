
import Workload
import WorkLoadDaoImpl
import unittest


class Test(unittest.TestCase):
    wl=Workload.Workload('12','2012-12-12','21','21')
    wldao=WorkLoadDaoImpl.MyClass()
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testName(self):
        pass
    def testAdd(self):
        self.assertEqual(self.wldao.add(self.wl),True)
    def testgetWorkLoad(self):
        self.assertIsNotNone(self.wldao.getById('12'),True)
    def testGetByType(self):
        self.assertIsNotNone(self.wldao.getByType("21"), True)
    def testdelWorkLoad(self):
        self.assertEqual(self.wldao.delWorkByEmId('12'), True)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()