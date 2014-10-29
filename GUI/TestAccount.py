
import Account
import AccountDaoImpl
import unittest


class Test(unittest.TestCase):
    acc=Account.MyClass('100','2342342@qq.com')
    accdao=AccountDaoImpl.MyClass()

    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testName(self):
        pass
    def testAddAcc(self):
        self.assertEqual(self.accdao.addAcc(self.acc), True)
    def testgetAcc(self):
        self.assertIsNotNone(self.accdao.getAccById("100"), True)
    def testDelAcc(self):
        self.assertEqual(self.accdao.delAccById("100"), True)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()