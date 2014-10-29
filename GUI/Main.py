import wx
import time
import Employee
import EmployeeDaoImpl
import Account
import AccountDaoImpl
import Workload
import WorkLoadDaoImpl
import EmployeeServiceImpl
import wx.grid
import Record
from Tix import Grid


#encoding:utf-8
#MainPanel
class MainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)  
        self.SetSize(wx.Size(700, 500)) 
        self.ll = wx.StaticText(self, -1, "PayRoll", size=wx.Size(150, 40), pos=(300, 40))
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.ll.SetForegroundColour("red")
        self.ll.SetFont(font)
        
        
        self.button = wx.Button(self, -1, "PostUnion", pos=(120, 100))
        self.button.SetSize(wx.Size(150, 40))
        self.Bind(wx.EVT_BUTTON, self.OnClick_1, self.button)
        self.button.SetDefault()
        
        self.button_1 = wx.Button(self, -1, "New", pos=(120, 200))
        self.button_1.SetSize(wx.Size(150, 40))
        self.Bind(wx.EVT_BUTTON, self.OnClick_2, self.button_1)
        self.button_1.SetDefault()
         
        self.button_2 = wx.Button(self, -1, "PostSale", pos=(120, 300))
        self.button_2.SetSize(wx.Size(150, 40))
        self.Bind(wx.EVT_BUTTON, self.OnClick_3, self.button_2)
        self.button_2.SetDefault()
         
        self.button_3 = wx.Button(self, -1, "PostCardTime", pos=(400, 100))
        self.button_3.SetSize(wx.Size(150, 40))
        self.Bind(wx.EVT_BUTTON, self.OnClick_4, self.button_3)
        self.button_3.SetDefault()
        
        self.button_4 = wx.Button(self, -1, "View/Edit", pos=(400, 200))
        self.button_4.SetSize(wx.Size(150, 40))
        self.Bind(wx.EVT_BUTTON, self.OnClick_5, self.button_4)
        self.button_4.SetDefault()
        
        self.button_5 = wx.Button(self, -1, "RunPayRoll", pos=(400, 300))
        self.button_5.SetSize(wx.Size(150, 40))
        self.Bind(wx.EVT_BUTTON, self.OnClick_6, self.button_5)
        self.button_5.SetDefault()      
    def OnClick_1(self, event):
        self.Destroy()
        UpdateRatePanel(frame)
        frame.Refresh()
    def OnClick_2(self, event):
        self.Destroy()
        self.ee2=New_Employee(frame)
        frame.Refresh()
    def OnClick_3(self, event):
        self.Destroy()
        self.ee3=PostSalePanel(frame)
        frame.Refresh()
    def OnClick_4(self, event):
        self.Destroy()
        self.ee4=TimeCardPanel(frame)
        frame.Refresh()
    def OnClick_5(self, event):
        self.Destroy()
        self.ee4=ListOfEmplPanel(frame)
        frame.Refresh()
    def OnClick_6(self, event):
        self.Destroy()
        self.ee5=PayRollDetailPanel(frame)
        frame.Refresh()
        


#New_EmployeePanel       
class New_Employee(wx.Panel):
    name=""
    address=""
    payment=""
    e_id=""
    u_id=""
    mode=""
    msg_eid=''
    msg_uid=''
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)  
        self.SetSize(wx.Size(700,500)) 
        self.ll=wx.StaticText(self, -1,"New Employee Detail", size=wx.Size(150,40),pos=(220,40))
        font = wx.Font(18,wx.DECORATIVE,wx.ITALIC,wx.NORMAL)
        self.ll.SetForegroundColour("red")
        self.ll.SetFont(font)
        
        self.name=wx.StaticText(self, -1,"Name:", size=wx.Size(150,40),pos=(150,100))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.name.SetFont(font)
        self.e_name = wx.TextCtrl(self,-1,size=wx.Size(200,25),pos=(220,95),name="e_name");
          
        self.address=wx.StaticText(self, -1,"Address:", size=wx.Size(150,40),pos=(120,150))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.address.SetFont(font)
        self.e_address = wx.TextCtrl(self,-1,size=wx.Size(200,25),pos=(220,145),name="e_address");
        
        self.payment=wx.StaticText(self, -1,"Method of Payment:", size=wx.Size(150,40),pos=(20,200))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.payment.SetFont(font)
#         self.e_payment= wx.TextCtrl(self,-1,size=wx.Size(200,25),pos=(220,195),name="e_payment");
        sampleList = ['email','pickup','bankaccout']
        self.e_payment=wx.Choice(self, -1, (220, 195), choices=sampleList,name="e_payment")
        self.e_payment.SetSize(wx.Size(200,25))
        self.e_payment.Bind(wx.EVT_CHOICE, self.choice_payment, self.e_payment)
        
        self.e_id=wx.StaticText(self, -1,"Employee ID:", size=wx.Size(150,40),pos=(80,250))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.e_id.SetFont(font)
        self.ee_id= wx.TextCtrl(self,-1,size=wx.Size(200,25),pos=(220,245),name="ee_id");
        self.Bind(wx.EVT_TEXT, self.judgeE_ID, self.ee_id)
         
        self.u_id=wx.StaticText(self, -1,"Union ID:", size=wx.Size(150,40),pos=(110,300))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.u_id.SetFont(font)
        self.uu_id= wx.TextCtrl(self,-1,size=wx.Size(200,25),pos=(220,295),name="uu_id");
        self.Bind(wx.EVT_TEXT, self.judgeU_ID, self.uu_id)
         
        self.ll=wx.StaticText(self, -1,"Working mode:", size=wx.Size(150,40),pos=(70,350))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.ll.SetFont(font)
        sampleList = ['Hourly','Commission','Salary']
        self.ch=wx.Choice(self, -1, (220, 345), choices=sampleList,name="e_mode")
        self.ch.SetSize(wx.Size(200,25))
        self.ch.Bind(wx.EVT_CHOICE, self.choice, self.ch)
        
        self.submit = wx.Button(self, -1, "submit", pos=(480, 400))
        self.submit.SetSize(wx.Size(80,30))
        self.submit.Bind(wx.EVT_BUTTON, self.ok, self.submit)
        self.submit.SetDefault()
        
        self.btnback = wx.Button(self, -1, "back", pos=(580, 400))
        self.btnback.SetSize(wx.Size(80,30))
        self.btnback.Bind(wx.EVT_BUTTON, self.back, self.btnback)
        self.btnback.SetDefault()
    def judgeE_ID(self,event):
        New_Employee.msg_eid=wx.StaticText(self, -1, size=wx.Size(150,60),pos=(450,250))
        self.ju_eid=self.ee_id.GetValue()
        if self.ju_eid=="":
            pass;
        else:
            if EmployeeServiceImpl.MyClass().judgeE_id(self.ee_id.GetValue()):
                New_Employee.msg_eid=wx.StaticText(self, -1,"E_ID is exist", size=wx.Size(150,60),pos=(450,250))
    def judgeU_ID(self,event):
        New_Employee.msg_uid=wx.StaticText(self, -1,"",size=wx.Size(150,60),pos=(450,300))
        self.ju_uid=self.uu_id.GetValue()
        if self.ju_uid=="":
            pass;
        else:
            if EmployeeServiceImpl.MyClass().judgeU_id(self.uu_id.GetValue()):
                New_Employee.msg_uid=wx.StaticText(self, -1,"U_ID is exist",size=wx.Size(150,60),pos=(450,300))   
    def ok(self,event):
        New_Employee.name=self.e_name.GetValue()
        New_Employee.address=self.e_address.GetValue()
        New_Employee.e_id=self.ee_id.GetValue()
        if(self.uu_id.GetValue()==""):
            New_Employee.u_id="0"
        else:
            New_Employee.u_id=self.uu_id.GetValue()
        if self.value=="Hourly":
            self.em=Employee.Myclass(self.ee_id.GetValue(),self.e_name.GetValue(),self.e_address.GetValue(),
                                  New_Employee.payment,New_Employee.u_id,self.value,"0","0","0.6")
        if self.value=="Commission":
            self.em=Employee.Myclass(self.ee_id.GetValue(),self.e_name.GetValue(),self.e_address.GetValue(),
                                  New_Employee.payment,New_Employee.u_id,self.value,"0","0","0")
        if self.value=="Salary":
            self.em=Employee.Myclass(self.ee_id.GetValue(),self.e_name.GetValue(),self.e_address.GetValue(),
                                  New_Employee.payment,New_Employee.u_id,self.value,"0","2000","0")
        self.emdao=EmployeeDaoImpl.MyClass()
        self.emdao.addEmpl(self.em)
        if self.e_account.Name=="e_account":
            self.acc=Account.MyClass(self.ee_id.GetValue(),self.e_account.GetValue())
        else:
            self.acc=Account.MyClass(self.ee_id.GetValue(),"")
        self.accdao=AccountDaoImpl.MyClass()
        self.accdao.addAcc(self.acc)
        self.Destroy()
        New_Employee_Detail(frame)
        frame.Refresh() 
    def choice(self,event):
        self.value=event.GetEventObject().GetStringSelection()
        New_Employee.mode=self.value
    def choice_payment(self,event):
        New_Employee.payment=event.GetEventObject().GetStringSelection()
        if New_Employee.payment=="email":
            self.e_account = wx.TextCtrl(self,-1,size=wx.Size(150,25),pos=(450,195),name="e_account");
        if New_Employee.payment=="pickup":
            self.e_account = wx.StaticText(self,-1,size=wx.Size(150,25),pos=(450,195),name="www")
        if New_Employee.payment=="bankaccout":
            self.e_account = wx.TextCtrl(self,-1,size=wx.Size(150,25),pos=(450,195),name="e_account");
    def back(self,event):
        self.Destroy()
        MainPanel(frame)
        frame.Refresh()
#New_Employee Panel    
class New_Employee_Detail(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)  
        self.SetSize(wx.Size(700,500)) 
        self.ll=wx.StaticText(self, -1,"Congraulation", size=wx.Size(150,40),pos=(250,20))
        font = wx.Font(18,wx.DECORATIVE,wx.ITALIC,wx.NORMAL)
        self.ll.SetForegroundColour("red")
        self.ll.SetFont(font)
        
        self.msg=wx.StaticText(self, -1,"You are success enroll to system", size=wx.Size(150,40),pos=(150,50))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.msg.SetFont(font)
        
        self.name=wx.StaticText(self, -1,"Name:", size=wx.Size(150,40),pos=(150,100))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.name.SetFont(font)
        self.e_name=wx.StaticText(self, -1,New_Employee.name,size=wx.Size(200,25),pos=(220,100))
        self.e_name.SetFont(font)
        
        self.address=wx.StaticText(self, -1,"Address:", size=wx.Size(150,40),pos=(120,150))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.address.SetFont(font)
        self.e_address=wx.StaticText(self, -1,New_Employee.address,size=wx.Size(200,25),pos=(220,150))
        self.e_address.SetFont(font)
          
        self.payment=wx.StaticText(self, -1,"Method of Payment:", size=wx.Size(150,40),pos=(20,200))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.payment.SetFont(font)  
        self.e_payment=wx.StaticText(self, -1,New_Employee.payment,size=wx.Size(200,25),pos=(220,200))
        self.e_payment.SetFont(font)
        
        self.e_id=wx.StaticText(self, -1,"Employee ID:", size=wx.Size(150,40),pos=(80,250))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.e_id.SetFont(font)
        self.ee_id=wx.StaticText(self, -1,New_Employee.e_id,size=wx.Size(200,25),pos=(220,250))
        self.ee_id.SetFont(font)
    
        self.u_id=wx.StaticText(self, -1,"Union ID:", size=wx.Size(150,40),pos=(110,300))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.u_id.SetFont(font)
        if New_Employee.u_id=="0":
            self.uuid=""
        else:
            self.uuid=New_Employee.u_id
        self.uu_id=wx.StaticText(self, -1,self.uuid,size=wx.Size(200,25),pos=(220,300))
        self.uu_id.SetFont(font)
         
        self.ll=wx.StaticText(self, -1,"Working mode:", size=wx.Size(150,40),pos=(70,350))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.ll.SetFont(font)
        self.mode=wx.StaticText(self, -1,New_Employee.mode,size=wx.Size(200,25),pos=(220,350))
        self.mode.SetFont(font)
        
        self.backbtn = wx.Button(self, -1, "back", pos=(500, 400))
        self.backbtn.SetSize(wx.Size(80,30))
        self.Bind(wx.EVT_BUTTON, self.back, self.backbtn)
        self.backbtn.SetDefault()
    def back(self,event):
        self.Destroy()
        MainPanel(frame)
        frame.Refresh()
        
#PostSale Panel
class PostSalePanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)  
        self.SetSize(wx.Size(700,500)) 
        self.ll=wx.StaticText(self, -1,"PostSale", size=wx.Size(150,40),pos=(270,20))
        font = wx.Font(18,wx.DECORATIVE,wx.ITALIC,wx.NORMAL)
        self.ll.SetForegroundColour("red")
        self.ll.SetFont(font)
        
        self.e_id=wx.StaticText(self, -1,"E_ID:", size=wx.Size(150,40),pos=(30,80))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.e_id.SetFont(font)
        self.E_ID = wx.TextCtrl(self,-1,size=wx.Size(70,25),pos=(30,110),name="E_ID");
        self.Bind(wx.EVT_TEXT, self.judgeE_ID, self.E_ID)
        
        self.date=wx.StaticText(self, -1,"Date:", size=wx.Size(150,40),pos=(30,150))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.date.SetFont(font)
        self.Date = wx.TextCtrl(self,-1,size=wx.Size(70,25),pos=(30,180),name="Date");
        
        self.amount=wx.StaticText(self, -1,"Amount:", size=wx.Size(150,40),pos=(30,220))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.amount.SetFont(font)
        self.Amount = wx.TextCtrl(self,-1,size=wx.Size(70,25),pos=(30,250),name="Amount");
        
        self.submit = wx.Button(self, -1, "submit", pos=(30, 300))
        self.submit.SetSize(wx.Size(70,30))
        self.Bind(wx.EVT_BUTTON, self.ok, self.submit)
        self.submit.SetDefault()
        
        self.backbtn = wx.Button(self, -1, "back", pos=(30, 350))
        self.backbtn.SetSize(wx.Size(70,30))
        self.Bind(wx.EVT_BUTTON, self.back, self.backbtn)
        self.backbtn.SetDefault() 
        
        self.wldao=WorkLoadDaoImpl.MyClass()
        self.wls=self.wldao.getByType("Amount")
        self.grid = wx.grid.Grid(self,pos=(200,80))
        self.grid.CreateGrid(30,3)
        self.grid.SetRowLabelSize(0)
        self.grid.SetColLabelValue(0, "E_ID")
        self.grid.SetColLabelValue(1, "Date")
        self.grid.SetColLabelValue(2, "Amount")
        self.grid.SetSize(wx.Size(260,300))        
        for row in range(self.wls.__len__()):
            for col in range(3):
                self.grid.SetReadOnly(row,col,True)
                if not isinstance(self.wls[row][col], str):
                    self.grid.SetCellValue(row, col,str(self.wls[row][col]))
                else:
                    self.grid.SetCellValue(row, col,self.wls[row][col])  
    def judgeE_ID(self,event):
        New_Employee.msg_eid=wx.StaticText(self, -1,"", size=wx.Size(150,60),pos=(20,20))
        self.ju_eid=self.E_ID.GetValue()
        if self.ju_eid=="":
            pass;
        else:
            if EmployeeServiceImpl.MyClass().judgeE_id(self.E_ID.GetValue())==False:
                New_Employee.msg_eid=wx.StaticText(self, -1,"E_ID is error", size=wx.Size(150,60),pos=(20,20))         
    def ok(self,event):
        if self.E_ID.GetValue()=="" or self.Date.GetValue()=="" or self.Amount.GetValue()=="" or New_Employee.msg_eid.GetLabel()=="E_ID is error":
            self.E_ID.SetValue("")
            self.Date.SetValue("")
            self.Amount.SetValue("")
            New_Employee.msg_eid=wx.StaticText(self, -1,"", size=wx.Size(150,60),pos=(20,20))
        else: 
            self.wl=Workload.Workload(self.E_ID.GetValue(),self.Date.GetValue(),self.Amount.GetValue(),None)
            EmployeeServiceImpl.MyClass().addAmount(self.wl)
            self.Destroy()
            PostSalePanel(frame)
            frame.Refresh()
    def back(self,event):
        self.Destroy()
        MainPanel(frame)
        frame.Refresh()
     
        
#TimeCard Panel
class TimeCardPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)  
        self.SetSize(wx.Size(700,500)) 
        self.ll=wx.StaticText(self, -1,"Time Card", size=wx.Size(150,40),pos=(270,20))
        font = wx.Font(18,wx.DECORATIVE,wx.ITALIC,wx.NORMAL)
        self.ll.SetForegroundColour("red")
        self.ll.SetFont(font)
        
        self.e_id=wx.StaticText(self, -1,"E_ID:", size=wx.Size(150,40),pos=(30,80))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.e_id.SetFont(font)
        self.E_ID = wx.TextCtrl(self,-1,size=wx.Size(70,25),pos=(30,110),name="E_ID");
        self.Bind(wx.EVT_TEXT, self.judgeE_ID, self.E_ID)
        
        
        self.date=wx.StaticText(self, -1,"Date:", size=wx.Size(150,40),pos=(30,150))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.date.SetFont(font)
        self.Date = wx.TextCtrl(self,-1,size=wx.Size(70,25),pos=(30,180),name="Date");
        
        self.amount=wx.StaticText(self, -1,"Hours:", size=wx.Size(150,40),pos=(30,220))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.amount.SetFont(font)
        self.Hours = wx.TextCtrl(self,-1,size=wx.Size(70,25),pos=(30,250),name="Hours");
        
        self.submit = wx.Button(self, -1, "submit", pos=(30, 300))
        self.submit.SetSize(wx.Size(70,30))
        self.Bind(wx.EVT_BUTTON, self.ok, self.submit)
        self.submit.SetDefault()
        
        self.backbtn = wx.Button(self, -1, "back", pos=(30, 350))
        self.backbtn.SetSize(wx.Size(70,30))
        self.Bind(wx.EVT_BUTTON, self.back, self.backbtn)
        self.backbtn.SetDefault() 
        
        self.wldao=WorkLoadDaoImpl.MyClass()
        self.wls=self.wldao.getByType("Hours")
        self.grid = wx.grid.Grid(self,pos=(200,80))
        self.grid.CreateGrid(30,4)
        self.grid.SetRowLabelSize(0)
        self.grid.SetColLabelValue(0, "E_ID")
        self.grid.SetColLabelValue(1, "Name")
        self.grid.SetColLabelValue(2, "Date")
        self.grid.SetColLabelValue(3, "Hours")
        self.grid.SetSize(wx.Size(340,300))      
        for row in range(self.wls.__len__()):
            self.ser=EmployeeServiceImpl.MyClass().getEmplById(str(self.wls[row][0]))
            self.grid.SetCellValue(row, 0,self.wls[row][0])
            self.grid.SetCellValue(row, 1,self.ser[0][1])
            self.grid.SetCellValue(row, 2,str(self.wls[row][1])) 
            self.grid.SetCellValue(row, 3,self.wls[row][3]) 
            for col in range(4):
                self.grid.SetReadOnly(row,col,True) 
    def judgeE_ID(self,event):
        New_Employee.msg_eid=wx.StaticText(self, -1,"", size=wx.Size(150,60),pos=(20,20))
        self.ju_eid=self.E_ID.GetValue()
        if self.ju_eid=="":
            pass;
        else:
            if EmployeeServiceImpl.MyClass().judgeE_id(self.E_ID.GetValue())==False:
                New_Employee.msg_eid=wx.StaticText(self, -1,"E_ID is error", size=wx.Size(150,60),pos=(20,20))         
    def ok(self,event):
        if self.E_ID.GetValue()=="" or self.Date.GetValue()=="" or self.Hours.GetValue()=="" or New_Employee.msg_eid.GetLabel()=="E_ID is error":
            self.E_ID.SetValue("")
            self.Date.SetValue("")
            self.Hours.SetValue("")
            New_Employee.msg_eid=wx.StaticText(self, -1,"", size=wx.Size(150,60),pos=(20,20))
        else:
            self.wl=Workload.Workload(self.E_ID.GetValue(),self.Date.GetValue(),None,self.Hours.GetValue())
            EmployeeServiceImpl.MyClass().addHours(self.wl)
            self.Destroy()
            TimeCardPanel(frame)
            frame.Refresh()
    def back(self,event):
        self.Destroy()
        MainPanel(frame)
        frame.Refresh()  
        
#PayRoll Detail
class PayRollDetailPanel(wx.Panel):
    week=''
    month=''
    number=1
    weeknum=0
    monthnum=0
    num=''
    grid=''
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)  
        self.SetSize(wx.Size(700,500)) 
        self.ll=wx.StaticText(self, -1,"PayRoll Detail", size=wx.Size(150,40),pos=(270,20))
        font = wx.Font(18,wx.DECORATIVE,wx.ITALIC,wx.NORMAL)
        self.ll.SetForegroundColour("red")
        self.ll.SetFont(font) 
        
        wx.StaticText(self, -1,"week:", size=wx.Size(50,40),pos=(500,30))
        PayRollDetailPanel.week=wx.StaticText(self, -1,str(PayRollDetailPanel.weeknum), size=wx.Size(50,40),pos=(550,30))
        PayRollDetailPanel.week.SetForegroundColour("red")
        wx.StaticText(self, -1,"month:", size=wx.Size(50,40),pos=(600,30))
        PayRollDetailPanel.month=wx.StaticText(self, -1,str(PayRollDetailPanel.monthnum), size=wx.Size(50,40),pos=(650,30))
        PayRollDetailPanel.month.SetForegroundColour("red")
        PayRollDetailPanel.num=wx.StaticText(self, -1,str(PayRollDetailPanel.number), size=wx.Size(50,40),pos=(580,70))
        PayRollDetailPanel.num.SetForegroundColour("red")
        
        
        
        
        PayRollDetailPanel.grid = wx.grid.Grid(self,pos=(200,70))
        PayRollDetailPanel.grid.CreateGrid(40,3)
        PayRollDetailPanel.grid.SetRowLabelSize(0)
        PayRollDetailPanel.grid.SetColLabelValue(0, "Name")
        PayRollDetailPanel.grid.SetColLabelValue(1, "E_ID")
        PayRollDetailPanel.grid.SetColLabelValue(2, "Amount")
        PayRollDetailPanel.grid.SetSize(wx.Size(260,300))
        self.ems=EmployeeServiceImpl.MyClass().getAllEmpl()
        for row in range(self.ems.__len__()):
            PayRollDetailPanel.grid.SetCellValue(row, 0,self.ems[row][1]) 
            PayRollDetailPanel.grid.SetCellValue(row, 1,self.ems[row][0]) 
            self.salary=float(self.ems[row][7])*(1-float(self.ems[row][6]))
            PayRollDetailPanel.grid.SetCellValue(row, 2,str(self.salary))
            for col in range(3):
                PayRollDetailPanel.grid.SetReadOnly(row,col,True)
            
        self.backbtn = wx.Button(self, -1, "back", pos=(350, 400))
        self.backbtn.SetSize(wx.Size(70,30))
        self.Bind(wx.EVT_BUTTON, self.back, self.backbtn)
        self.backbtn.SetDefault()
        
        self.loadbtn = wx.Button(self, -1, "load", pos=(430, 400))
        self.loadbtn.SetSize(wx.Size(70,30))
        self.Bind(wx.EVT_BUTTON, self.load, self.loadbtn)
        self.loadbtn.SetDefault()
        
        self.savebtn = wx.Button(self, -1, "Run", pos=(510, 400))
        self.savebtn.SetSize(wx.Size(70,30))
        self.Bind(wx.EVT_BUTTON, self.save, self.savebtn)
        self.savebtn.SetDefault()
        
        self.resetbtn = wx.Button(self, -1, "Reset", pos=(590, 400))
        self.resetbtn.SetSize(wx.Size(70,30))
        self.Bind(wx.EVT_BUTTON, self.reset, self.resetbtn)
        self.resetbtn.SetDefault()
        
    def reset(self,event):
        PayRollDetailPanel.number=0
        PayRollDetailPanel.weeknum=0
        PayRollDetailPanel.monthnum=0
        wx.StaticText(self, -1,str(PayRollDetailPanel.number), size=wx.Size(50,40),pos=(580,70))
        wx.StaticText(self, -1,str(PayRollDetailPanel.weeknum), size=wx.Size(50,40),pos=(550,30))
        wx.StaticText(self, -1,str(PayRollDetailPanel.monthnum), size=wx.Size(50,40),pos=(650,30))
    def back(self,event):
        self.Destroy()
        MainPanel(frame)
        frame.Refresh() 
    def load(self,event):
        self.Destroy()
        ReecordPanel(frame)
        frame.Refresh()
    def save(self,event):
        PayRollDetailPanel.number=PayRollDetailPanel.number+1
        PayRollDetailPanel.num=wx.StaticText(self, -1,str(PayRollDetailPanel.number), size=wx.Size(50,40),pos=(580,70))
        PayRollDetailPanel.num.SetForegroundColour("red")
        if PayRollDetailPanel.number%5==0 and PayRollDetailPanel.number%10!=0:
            PayRollDetailPanel.weeknum=PayRollDetailPanel.weeknum+1
            PayRollDetailPanel.week=wx.StaticText(self, -1,str(PayRollDetailPanel.weeknum), size=wx.Size(50,40),pos=(550,30))
            PayRollDetailPanel.week.SetForegroundColour("red")
            self.emshour=EmployeeServiceImpl.MyClass().getEmplByWork("Hourly")
            PayRollDetailPanel.grid.ClearGrid()
            for row in range(self.emshour.__len__()):
                PayRollDetailPanel.grid.SetCellValue(row, 0,self.ems[row][1]) 
                PayRollDetailPanel.grid.SetCellValue(row, 1,self.ems[row][0]) 
                self.hsalary=float(self.emshour[row][7])*(1-float(self.emshour[row][6]))
                PayRollDetailPanel.grid.SetCellValue(row, 2,str(self.hsalary))
            self.dlg = wx.MessageDialog(None, 'Hourly can get Salary!',
                          'MessageDialog', wx.YES_NO | wx.ICON_QUESTION)
            self.result = self.dlg.ShowModal()
            self.dlg.Destroy()
            if self.result==5103:
                self.addRecord()
                for row in range(self.emshour.__len__()):
                    PayRollDetailPanel.grid.SetCellValue(row, 2,"0.0")
                EmployeeServiceImpl.MyClass().clearSalary("Hourly")
                EmployeeServiceImpl.MyClass().deleteByType("hours")
        if  PayRollDetailPanel.number%10==0 and PayRollDetailPanel.number!=30:
            PayRollDetailPanel.weeknum=PayRollDetailPanel.weeknum+1
            PayRollDetailPanel.week=wx.StaticText(self, -1,str(PayRollDetailPanel.weeknum), size=wx.Size(50,40),pos=(550,30))
            PayRollDetailPanel.week.SetForegroundColour("red")
            self.emshour=EmployeeServiceImpl.MyClass().getCommHourEmpl("Hourly", "Commission")
            PayRollDetailPanel.grid.ClearGrid()
            for row in range(self.emshour.__len__()):
                PayRollDetailPanel.grid.SetCellValue(row, 0,self.ems[row][1]) 
                PayRollDetailPanel.grid.SetCellValue(row, 1,self.ems[row][0]) 
                self.hsalary=float(self.emshour[row][7])*(1-float(self.emshour[row][6]))
                PayRollDetailPanel.grid.SetCellValue(row, 2,str(self.hsalary))
            self.dlg = wx.MessageDialog(None, 'Hourly Commission can get Salary!!',
                          'MessageDialog', wx.YES_NO | wx.ICON_QUESTION)
            self.result = self.dlg.ShowModal()
            self.dlg.Destroy()
            if self.result==5103:
                self.addRecord()
                for row in range(self.emshour.__len__()):
                    PayRollDetailPanel.grid.SetCellValue(row, 2,"0.0")
                EmployeeServiceImpl.MyClass().clearSalary("Hourly")
                EmployeeServiceImpl.MyClass().deleteByType("hours")
                EmployeeServiceImpl.MyClass().clearSalary("Commission")
                EmployeeServiceImpl.MyClass().deleteByType("amount")  
        if  PayRollDetailPanel.number==30:
            PayRollDetailPanel.monthnum=PayRollDetailPanel.monthnum+1
            PayRollDetailPanel.month=wx.StaticText(self, -1,str(PayRollDetailPanel.monthnum), size=wx.Size(50,40),pos=(650,30))
            PayRollDetailPanel.month.SetForegroundColour("red")
            self.emshour=EmployeeServiceImpl.MyClass().getAllEmpl()
            PayRollDetailPanel.grid.ClearGrid()
            for row in range(self.emshour.__len__()):
                PayRollDetailPanel.grid.SetCellValue(row, 0,self.ems[row][1]) 
                PayRollDetailPanel.grid.SetCellValue(row, 1,self.ems[row][0]) 
                self.hsalary=float(self.emshour[row][7])*(1-float(self.emshour[row][6]))
                PayRollDetailPanel.grid.SetCellValue(row, 2,str(self.hsalary))
            self.dlg = wx.MessageDialog(None, 'Hourly Commission Salary can get Salary!',
                          'MessageDialog', wx.YES_NO | wx.ICON_QUESTION)
            self.result = self.dlg.ShowModal()
            self.dlg.Destroy()
            if self.result==5103:
                self.addRecord()
                for row in range(self.emshour.__len__()):
                    PayRollDetailPanel.grid.SetCellValue(row, 2,"0.0")
                EmployeeServiceImpl.MyClass().clearSalary("Salary")
            PayRollDetailPanel.number=0
    def addRecord(self):
        self.n=0
        for row in range(40):
            if PayRollDetailPanel.grid.GetCellValue(row,0)=="" or PayRollDetailPanel.grid.GetCellValue(row,0)==None:
                pass
            else:
                self.n=self.n+1
        for row in range(self.n):
            self.r_name=PayRollDetailPanel.grid.GetCellValue(row,0)
            self.r_eid=PayRollDetailPanel.grid.GetCellValue(row,1)
            self.r_amount=PayRollDetailPanel.grid.GetCellValue(row,2)
            self.rtime=time.strftime('%Y-%m-%d',time.localtime(time.time()))
            self.re=Record.MyClass(self.r_name,self.r_eid,self.r_amount,self.rtime)
            EmployeeServiceImpl.MyClass().addRecord(self.re)
            
            
            
#RecordPanel
class ReecordPanel(wx.Panel):
    re=''
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)  
        self.SetSize(wx.Size(700,500)) 
        self.ll=wx.StaticText(self, -1,"Record", size=wx.Size(150,40),pos=(290,20))
        font = wx.Font(18,wx.DECORATIVE,wx.ITALIC,wx.NORMAL)
        self.ll.SetForegroundColour("red")
        self.ll.SetFont(font) 
        
        self.datelb=wx.StaticText(self, -1,"Date:", size=wx.Size(150,40),pos=(30,70))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.datelb.SetFont(font)
        self.date = wx.TextCtrl(self,-1,size=wx.Size(100,25),pos=(30,100),name="date");
        
        self.delete = wx.Button(self, -1, "delete", pos=(30, 210))
        self.delete.SetSize(wx.Size(80,30))
        self.Bind(wx.EVT_BUTTON, self.de, self.delete)
        self.delete.SetDefault() 
       
        self.submit = wx.Button(self, -1, "search", pos=(30, 270))
        self.submit.SetSize(wx.Size(80,30))
        self.Bind(wx.EVT_BUTTON, self.search, self.submit)
        self.submit.SetDefault()
        
        self.bk= wx.Button(self, -1, "back", pos=(30, 330))
        self.bk.SetSize(wx.Size(80,30))
        self.Bind(wx.EVT_BUTTON, self.back, self.bk)
        self.bk.SetDefault()
        
        
        
        ReecordPanel.re = wx.grid.Grid(self,pos=(180,70))
        self.res=EmployeeServiceImpl.MyClass().getRecords()
        ReecordPanel.re.SetSize(wx.Size(340,320))
        ReecordPanel.re.CreateGrid(20+self.res.__len__(),4)
        ReecordPanel.re.SetRowLabelSize(0)
        ReecordPanel.re.SetColLabelValue(0, "Name")
        ReecordPanel.re.SetColLabelValue(1, "E_ID")
        ReecordPanel.re.SetColLabelValue(2, "Amount")
        ReecordPanel.re.SetColLabelValue(3, "Date")
        for row in range(self.res.__len__()):
            ReecordPanel.re.SetCellValue(row,0,self.res[row][0])
            ReecordPanel.re.SetCellValue(row,1,self.res[row][1])
            ReecordPanel.re.SetCellValue(row,2,self.res[row][2])
            ReecordPanel.re.SetCellValue(row,3,self.res[row][3])
            for col in range(4):
                ReecordPanel.re.SetReadOnly(row,col,True)
    def de(self,event):
        self.time=self.date.GetValue()
        if self.time=="":
            pass
        else:
            EmployeeServiceImpl.MyClass().deleteRecord(self.time)
            self.lookres=EmployeeServiceImpl.MyClass().getRecords()
            ReecordPanel.re.ClearGrid()
            for row in range(self.lookres.__len__()):
                ReecordPanel.re.SetCellValue(row,0,self.lookres[row][0])
                ReecordPanel.re.SetCellValue(row,1,self.lookres[row][1])
                ReecordPanel.re.SetCellValue(row,2,self.lookres[row][2])
                ReecordPanel.re.SetCellValue(row,3,self.lookres[row][3])
            self.date.SetValue("")
    def search(self,event):
        self.time=self.date.GetValue()
        if self.time=="":
            pass
        else:
            self.lookres=EmployeeServiceImpl.MyClass().getRecordByTime(self.time)
            ReecordPanel.re.ClearGrid()
            for row in range(self.lookres.__len__()):
                ReecordPanel.re.SetCellValue(row,0,self.lookres[row][0])
                ReecordPanel.re.SetCellValue(row,1,self.lookres[row][1])
                ReecordPanel.re.SetCellValue(row,2,self.lookres[row][2])
                ReecordPanel.re.SetCellValue(row,3,self.lookres[row][3])
    def back(self,event):
        self.Destroy()
        MainPanel(frame)
        frame.Refresh()
      
#List of Empyolee Panel
class ListOfEmplPanel(wx.Panel):
    listofempl=''
    E_Name=''
    E_ID=''
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)  
        self.SetSize(wx.Size(700,500)) 
        self.ll=wx.StaticText(self, -1,"List of Employees", size=wx.Size(150,40),pos=(270,20))
        font = wx.Font(18,wx.DECORATIVE,wx.ITALIC,wx.NORMAL)
        self.ll.SetForegroundColour("red")
        self.ll.SetFont(font) 
        
        self.e_name=wx.StaticText(self, -1,"Name:", size=wx.Size(150,40),pos=(30,80))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.e_name.SetFont(font)
        self.E_Name = wx.TextCtrl(self,-1,size=wx.Size(70,25),pos=(30,110),name="E_Name");
        
        self.e_id=wx.StaticText(self, -1,"E_ID:", size=wx.Size(150,40),pos=(30,150))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.e_id.SetFont(font)
        self.E_ID = wx.TextCtrl(self,-1,size=wx.Size(70,25),pos=(30,180),name="E_ID");
        self.Bind(wx.EVT_TEXT, self.judgeE_ID, self.E_ID)
        
        self.submit = wx.Button(self, -1, "change", pos=(30, 270))
        self.submit.SetSize(wx.Size(80,30))
        self.Bind(wx.EVT_BUTTON, self.search, self.submit)
        self.submit.SetDefault()
        
        self.backbtn = wx.Button(self, -1, "back", pos=(30, 320))
        self.backbtn.SetSize(wx.Size(80,30))
        self.Bind(wx.EVT_BUTTON, self.back, self.backbtn)
        self.backbtn.SetDefault()
        
        self.delete = wx.Button(self, -1, "delete", pos=(30, 370))
        self.delete.SetSize(wx.Size(80,30))
        self.Bind(wx.EVT_BUTTON, self.dele, self.delete)
        self.delete.SetDefault()  
        
        ListOfEmplPanel.listofempl = wx.grid.Grid(self,pos=(140,70))
        self.ems=EmployeeServiceImpl.MyClass().getAllEmpl()
        ListOfEmplPanel.listofempl.CreateGrid(30+self.ems.__len__(),6)
        ListOfEmplPanel.listofempl.SetRowLabelSize(0)
        ListOfEmplPanel.listofempl.SetColLabelValue(0, "Name")
        ListOfEmplPanel.listofempl.SetColLabelValue(1, "Address")
        ListOfEmplPanel.listofempl.SetColLabelValue(2, "E_ID")
        ListOfEmplPanel.listofempl.SetColLabelValue(3, "Union")
        ListOfEmplPanel.listofempl.SetColLabelValue(4, "Working Mode")
        ListOfEmplPanel.listofempl.SetColLabelValue(5, "Method of Payment")
        ListOfEmplPanel.listofempl.SetSize(wx.Size(500,350))
        for row in range(self.ems.__len__()):
            ListOfEmplPanel.listofempl.SetCellValue(row, 0,self.ems[row][1]) 
            ListOfEmplPanel.listofempl.SetCellValue(row, 1,self.ems[row][2]) 
            ListOfEmplPanel.listofempl.SetCellValue(row, 2,self.ems[row][0])
            if self.ems[row][4]=="0":
                ListOfEmplPanel.listofempl.SetCellValue(row, 3,"null")
            else:
                ListOfEmplPanel.listofempl.SetCellValue(row, 3,str(self.ems[row][4]))
            ListOfEmplPanel.listofempl.SetCellValue(row, 4,self.ems[row][5])
            ListOfEmplPanel.listofempl.SetCellValue(row, 5,self.ems[row][3])
            for col in range(5):
                ListOfEmplPanel.listofempl.SetReadOnly(row,col,True)
    def judgeE_ID(self,event):
        New_Employee.msg_eid=wx.StaticText(self, -1,"", size=wx.Size(150,60),pos=(20,20))
        self.ju_eid=self.E_ID.GetValue()
        if self.ju_eid=="":
            pass;
        else:
            if EmployeeServiceImpl.MyClass().judgeE_id(self.E_ID.GetValue())==False:
                New_Employee.msg_eid=wx.StaticText(self, -1,"E_ID is error", size=wx.Size(150,60),pos=(20,20))
    def search(self,event):
        if New_Employee.msg_eid.GetLabel()=="E_ID is error":
            self.E_Name.SetValue("")
            self.E_ID.SetValue("")
        else:
            ListOfEmplPanel.E_Name=self.E_Name.GetValue()
            ListOfEmplPanel.E_ID=self.E_ID.GetValue()
            self.Destroy()
            ChangeDetailPanel(frame)
            frame.Refresh()
    def back(self,event):
        self.Destroy()
        MainPanel(frame)
        frame.Refresh()
    def dele(self,event):
        self.id=self.E_ID.GetValue()
        if self.id=="":
            pass
        else:
            self.dlg = wx.MessageDialog(None, 'Are you sure!',
                          'MessageDialog', wx.YES_NO|wx.ICON_QUESTION)
            self.result = self.dlg.ShowModal()
            self.dlg.Destroy()
            if self.result==5103:
                if self.id=="":
                    pass
                else:
                    EmployeeServiceImpl.MyClass().delEmpl(self.id)
                    AccountDaoImpl.MyClass().delAccById(self.id)
                    self.repaint()
    def repaint(self):
        ListOfEmplPanel.listofempl.ClearGrid()
        self.ems=EmployeeServiceImpl.MyClass().getAllEmpl()
        for row in range(self.ems.__len__()):
            ListOfEmplPanel.listofempl.SetCellValue(row, 0,self.ems[row][1]) 
            ListOfEmplPanel.listofempl.SetCellValue(row, 1,self.ems[row][2]) 
            ListOfEmplPanel.listofempl.SetCellValue(row, 2,self.ems[row][0])
            if self.ems[row][4]=="0":
                ListOfEmplPanel.listofempl.SetCellValue(row, 3,"null")
            else:
                ListOfEmplPanel.listofempl.SetCellValue(row, 3,str(self.ems[row][4]))
            ListOfEmplPanel.listofempl.SetCellValue(row, 4,self.ems[row][5])
            ListOfEmplPanel.listofempl.SetCellValue(row, 5,self.ems[row][3])
            for col in range(5):
                ListOfEmplPanel.listofempl.SetReadOnly(row,col,True)
#Change Detail Panel
class ChangeDetailPanel(wx.Panel):
    mode=''
    payment=''
    def __init__(self,parent):
        self.ems=EmployeeServiceImpl.MyClass().getFind(ListOfEmplPanel.E_Name,ListOfEmplPanel.E_ID)
        wx.Panel.__init__(self, parent)  
        self.SetSize(wx.Size(700,500)) 
        self.ll=wx.StaticText(self, -1,"Detail Change", size=wx.Size(150,40),pos=(270,20))
        font = wx.Font(18,wx.DECORATIVE,wx.ITALIC,wx.NORMAL)
        self.ll.SetForegroundColour("red")
        self.ll.SetFont(font)
        
        self.name=wx.StaticText(self, -1,"Name:", size=wx.Size(150,40),pos=(150,100))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.name.SetFont(font)
        self.e_name = wx.TextCtrl(self,-1,self.ems[0][1],size=wx.Size(200,25),pos=(220,95),name="e_name");
          
        self.address=wx.StaticText(self, -1,"Address:", size=wx.Size(150,40),pos=(120,150))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.address.SetFont(font)
        self.e_address = wx.TextCtrl(self,-1,self.ems[0][2],size=wx.Size(200,25),pos=(220,145),name="e_address");
       
        self.e_id=wx.StaticText(self, -1,"E_ID:", size=wx.Size(150,40),pos=(150,200))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.e_id.SetFont(font)
        self.ee_id= wx.TextCtrl(self,-1,self.ems[0][0],size=wx.Size(200,25),pos=(220,195),name="ee_id");
        self.Bind(wx.EVT_TEXT, self.judgeE_ID, self.ee_id)
        
         
        self.u_id=wx.StaticText(self, -1,"Union:", size=wx.Size(150,40),pos=(140,250))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.u_id.SetFont(font)
        if self.ems[0][4]=="0":
            self.uid="null"
        else:
            self.uid=self.ems[0][4]
        self.uu_id= wx.TextCtrl(self,-1,self.uid,size=wx.Size(200,25),pos=(220,245),name="uu_id");
        self.Bind(wx.EVT_TEXT, self.judgeU_ID, self.uu_id)
        
        self.ll=wx.StaticText(self, -1,"Working mode:", size=wx.Size(150,40),pos=(70,300))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.ll.SetFont(font)
#         self.mode= wx.TextCtrl(self,-1,self.ems[0][5],size=wx.Size(200,25),pos=(220,295),name="mode");
        ChangeDetailPanel.mode=self.ems[0][5]
        sampleList = ['Hourly','Commission','Salary']
        self.m=0
        for k in range(3):
            if sampleList[k]==self.ems[0][5]:
                self.m=k
        self.ch=wx.Choice(self, -1, (220, 295), choices=sampleList,name="e_mode")
        self.ch.Select(self.m)
        self.ch.SetSize(wx.Size(200,25))
        self.ch.Bind(wx.EVT_CHOICE, self.choice, self.ch)
        
        self.payment=wx.StaticText(self, -1,"Method of Payment:", size=wx.Size(150,40),pos=(20,350))
        font = wx.Font(13,wx.SWISS, wx.NORMAL, wx.BOLD)
        self.payment.SetFont(font)
#         self.e_payment= wx.TextCtrl(self,-1,self.ems[0][3],size=wx.Size(200,25),pos=(220,345),name="payment");
        ChangeDetailPanel.payment=self.ems[0][3]
        sampleList1 = ['email','pickup','bankaccount']
        self.mu=0
        for k in range(3):
            if sampleList1[k]==self.ems[0][3]:
                self.mu=k
        self.e_payment=wx.Choice(self, -1, (220, 345), choices=sampleList1,name="e_payment")
        self.e_payment.Select(self.mu)
        self.e_payment.SetSize(wx.Size(200,25))
        self.e_payment.Bind(wx.EVT_CHOICE, self.choice_payment, self.e_payment)
       
        if sampleList1[self.mu]=="pickup":
            pass
        else:
            self.accdao=AccountDaoImpl.MyClass()
            self.acc=self.accdao.getAccById(self.ems[0][0])
            self.account=wx.TextCtrl(self,-1,self.acc[0][1],size=wx.Size(150,25),pos=(460,345),name="e_account");
        
        self.subbtn = wx.Button(self, -1, "submit", pos=(480, 400))
        self.subbtn.SetSize(wx.Size(80,30))
        self.Bind(wx.EVT_BUTTON, self.submit, self.subbtn)
        self.subbtn.SetDefault()
        
        self.backbtn = wx.Button(self, -1, "back", pos=(580, 400))
        self.backbtn.SetSize(wx.Size(80,30))
        self.Bind(wx.EVT_BUTTON, self.back, self.backbtn)
        self.backbtn.SetDefault()
        
        
    def judgeE_ID(self,event):
        New_Employee.msg_eid=wx.StaticText(self, -1,"", size=wx.Size(150,60),pos=(450,195))
        self.ju_eid=self.ee_id.GetValue()
        if self.ju_eid=="":
            pass;
        else:
            if EmployeeServiceImpl.MyClass().judgeE_id(self.ee_id.GetValue()):
                New_Employee.msg_eid=wx.StaticText(self, -1,"E_ID is exist", size=wx.Size(150,60),pos=(450,195))
    def judgeU_ID(self,event):
        New_Employee.msg_uid=wx.StaticText(self, -1,"",size=wx.Size(150,60),pos=(450,245))
        self.ju_uid=self.uu_id.GetValue()
        if self.ju_uid=="":
            pass;
        else:
            if EmployeeServiceImpl.MyClass().judgeU_id(self.uu_id.GetValue()):
                New_Employee.msg_uid=wx.StaticText(self, -1,"U_ID is exist",size=wx.Size(150,60),pos=(450,245))   
    def submit(self,event):
        if self.uu_id.GetValue()=="" or self.uu_id.GetValue()=="null":
            self.uuid="0"
        else:
            self.uuid=self.uu_id.GetValue()
        self.em=Employee.Myclass(self.ee_id.GetValue(),self.e_name.GetValue(),self.e_address.GetValue(),
                                 ChangeDetailPanel.payment,self.uuid,ChangeDetailPanel.mode,self.ems[0][6],self.ems[0][7],self.ems[0][8])
        self.emdao=EmployeeDaoImpl.MyClass()
        self.emdao.delEmpl(self.ems[0][0])
        self.emdao.addEmpl(self.em)
        
        if  ChangeDetailPanel.payment=="pickup":
            pass
        else:
            if self.account.Name=="e_account":
                self.acc=Account.MyClass(self.ee_id.GetValue(),self.account.GetValue())
                self.accdao=AccountDaoImpl.MyClass()
                self.accdao.delAccById(self.ee_id.GetValue())
                self.accdao.addAcc(self.acc)
        
        self.Destroy()
        ListOfEmplPanel(frame)
        frame.Refresh()
        
    def back(self,event):
        self.Destroy()
        ListOfEmplPanel(frame)
        frame.Refresh()
    def choice(self,event):
        self.value=event.GetEventObject().GetStringSelection()
        ChangeDetailPanel.mode=self.value
    def choice_payment(self,event):
        ChangeDetailPanel.payment=event.GetEventObject().GetStringSelection()
        if self.ems[0][3]!="pickup":
            self.account.Destroy()
        if ChangeDetailPanel.payment=="email":
            self.account=wx.TextCtrl(self,-1,"",size=wx.Size(150,25),pos=(460,345),name="e_account");
        if ChangeDetailPanel.payment=="pickup":
            self.account=wx.StaticText(self,-1,"",size=wx.Size(150,25),pos=(460,345),name="www")
        if ChangeDetailPanel.payment=="bankaccount":
            self.account=wx.TextCtrl(self,-1,"",size=wx.Size(150,25),pos=(460,345),name="e_account");
        
#UpdateRatePanel

class UpdateRatePanel(wx.Panel):
    listofrate=''
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)  
        self.SetSize(wx.Size(700,500)) 
        self.ll=wx.StaticText(self, -1,"List of Employees", size=wx.Size(150,40),pos=(270,20))
        font = wx.Font(18,wx.DECORATIVE,wx.ITALIC,wx.NORMAL)
        self.ll.SetForegroundColour("red")
        self.ll.SetFont(font) 
        
        self.submit = wx.Button(self, -1, "submit", pos=(550, 400))
        self.submit.SetSize(wx.Size(70,30))
        self.Bind(wx.EVT_BUTTON, self.update, self.submit)
        self.submit.SetDefault()
        
        self.backbtn = wx.Button(self, -1, "back", pos=(450, 400))
        self.backbtn.SetSize(wx.Size(70,30))
        self.Bind(wx.EVT_BUTTON, self.back, self.backbtn)
        self.backbtn.SetDefault()
        
        UpdateRatePanel.listofrate = wx.grid.Grid(self,pos=(150,70))
        self.ems=EmployeeServiceImpl.MyClass().getUnionEmpl()
        UpdateRatePanel.listofrate.CreateGrid(20+self.ems.__len__(),4)
        UpdateRatePanel.listofrate.SetRowLabelSize(0)
        UpdateRatePanel.listofrate.SetSize(wx.Size(340,300))
        UpdateRatePanel.listofrate.SetColLabelValue(0, "Name")
        UpdateRatePanel.listofrate.SetColLabelValue(1, "U_ID")
        UpdateRatePanel.listofrate.SetColLabelValue(2, "Charges")
        UpdateRatePanel.listofrate.SetColLabelValue(3, "rate")
        for row in range(self.ems.__len__()):
            UpdateRatePanel.listofrate.SetCellValue(row,0,self.ems[row][1])
            UpdateRatePanel.listofrate.SetReadOnly(row,0,True)
            if self.ems[row][4]=="0":
                self.uuid="null"
            else:
                self.uuid=self.ems[row][4]
            UpdateRatePanel.listofrate.SetCellValue(row,1,self.uuid)
            UpdateRatePanel.listofrate.SetReadOnly(row,1,True)
            self.rate=float(self.ems[row][6])*float(self.ems[row][7])
            UpdateRatePanel.listofrate.SetCellValue(row,2,str(self.rate))
            UpdateRatePanel.listofrate.SetReadOnly(row,2,True)
            UpdateRatePanel.listofrate.SetCellValue(row,3,self.ems[row][6]) 
             
    def update(self,event):
        self.ems=EmployeeServiceImpl.MyClass().getUnionEmpl()
        for row in range(self.ems.__len__()):
            self.rate=UpdateRatePanel.listofrate.GetCellValue(row,3) 
            if self.rate=="":
                pass
            else:
                if UpdateRatePanel.listofrate.GetCellValue(row,1)=="null":
                    pass
                else:
                    self.u_id=UpdateRatePanel.listofrate.GetCellValue(row,1)
                    self.ems=EmployeeServiceImpl.MyClass().changeUnionRate(self.u_id, self.rate)
                    self.repaint()
    def back(self,event):
        self.Destroy()
        MainPanel(frame)
        frame.Refresh()
    def repaint(self):
        self.ems=EmployeeServiceImpl.MyClass().getUnionEmpl()
        for row in range(self.ems.__len__()):
            UpdateRatePanel.listofrate.SetCellValue(row,0,self.ems[row][1])
            if self.ems[row][4]=="0":
                self.uuid="null"
            else:
                self.uuid=self.ems[row][4]
            UpdateRatePanel.listofrate.SetCellValue(row,1,self.uuid)
            self.rate=float(self.ems[row][6])*float(self.ems[row][7])
            UpdateRatePanel.listofrate.SetCellValue(row,2,str(self.rate))
#Main Frame
class Main(wx.Frame):
    def __init__(self):  
        wx.Frame.__init__(self, None, size=(700, 500)) 
        self.MainPanel = MainPanel(self)
                
#Start
app=wx.App()
frame=Main()
frame.Show()
app.MainLoop()
