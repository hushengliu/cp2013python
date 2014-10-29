import Employee
import EmployeeDaoImpl
import unittest


class Test(unittest.TestCase):
    em=Employee.Myclass('100','yyyy','chongqing','email','0','Hourly','0.1','0', '0')
    emdao=EmployeeDaoImpl.MyClass()
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testName(self):
        pass
    def testAddEmpl(self):
        self.assertEqual(self.emdao.addEmpl(self.em),True)
#     def testChangeEmpl(self):
#         self.assertEqual(self.emdao.changeEmpl(self.em), True)
#     def testaddSalary(self):
#         self.assertEqual(self.emdao.addSalary(self.em), True)
    def clearSalary(self):
        self.assertEqual(self.emdao.clearSalary(self.em), True)
    def jugdejudgeE_id(self):
        self.assertEqual(self.emdao.judgeE_id("100"), True)
    def jugdejudgeU_id(self):
        self.assertEqual(self.emdao.judgeU_id("0"),True)   
   
    def testGetAllEmpl(self):
        self.assertIsNotNone(self.emdao.getAllEmpl(), True)
    def testGetUnionEmpl(self):
        self.assertIsNotNone(self.emdao.getUnionEmpl(), True)
    def testGetEmplByWork(self):
        self.assertIsNotNone(self.emdao.getEmplByWork("Hourly"),True)
    def testGetFind(self):
        self.assertIsNotNone(self.emdao.getFind("Hourly"), True)
    
    def testDelEmpl(self):
        self.assertEqual(self.emdao.delEmpl("100"), True)
    
if __name__ == "__main__":
    unittest.main()