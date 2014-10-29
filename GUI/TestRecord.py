
import unittest
import Record
import RecordDao


class Test(unittest.TestCase):
    re=Record.MyClass('123','213','123','123')
    redao=RecordDao.MyClass()

    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testName(self):
        pass
    def testAddRecord(self):
        self.assertEqual(self.redao.addRecord(self.re), True)
   
    def testGetRecords(self):
        self.assertIsNotNone(self.redao.getRecords(), True)
    def testGetRecordByTime(self):
        self.assertIsNotNone(self.redao.getRecordByTime("123"), True)
    def testDel(self):
        self.assertEqual(self.redao.deleteRecord("123"), True)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()