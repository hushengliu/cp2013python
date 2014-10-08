# encoding:utf-8
import mysql.connector
class MyClass(object):
#   初始化连接数据库
    def __init__(self):
        self.conn = mysql.connector.connect(host='50.87.115.118', user='cptwozer_remote', password='8BHdwDYu', database='cptwozer_payroll', port=3306, use_unicode=True)
        self.cur = self.conn.cursor()
#   关闭数据库连接
    def close(self):
        self.conn.close()
        self.cur.close()
#   执行数据库insert操作，传入的table为table名，dict为一个包含了数据库列名对应值的dictionary类型
    def insert(self, table, dict):
        for i in dict:
            if dict[i] != None:
                dict[i] = "'" + dict[i] + "'"
            else:
                dict.pop(i)
        key = ",".join(dict.keys())
        str = ",".join(dict.values())
        sql = "insert into " + table + "(" + key + ") values(" + str + ")"
        self.cur.execute(sql)
        if self.cur.rowcount > 0:
            self.conn.commit()
            self.close()
            return True
        else:
            self.close()
            return False
#   执行数据库update操作，dict是传进来的dictionary,judge为sql语句中where后的条件的列名
    def update(self, table, dict, judge):
        value = dict[judge]
        dict.pop(judge)
        sql = []
        for i in dict:
            if dict[i] != None:
                if dict[i].find("+")!=-1 or dict[i]=="null":
                    sql.append(i + "=" + dict[i])
                else:
                    sql.append(i + "='" + dict[i] + "'")
        str = ",".join(sql)
        str = "update " + table + " set " + str + " where " + judge + "='" + value+"'"
        print str

        
