# encoding:utf-8
import mysql.connector
class MyClass(object):

    def __init__(self):
        self.conn = mysql.connector.connect(host='50.87.115.118', user='cptwozer_remote', password='8BHdwDYu', database='cptwozer_payroll', port=3306, use_unicode=True)
        self.cur = self.conn.cursor()

    def close(self):
        self.conn.close()
        self.cur.close()

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
        self.cur.execute(str)
        if self.cur.rowcount > 0:
            self.conn.commit()
            self.close()
            return True
        else:
            self.close()
            return False

    def get(self, table, data):
        sql = "select *from " + table + " " + data
        self.cur.execute(sql)
        info = self.cur.fetchall()
        l = []
        for i in info:
            t = []
            for j in i:
                if isinstance(j, (int, float)) :
                    t.append(str(j))
                else:
                    t.append(j)
            l.append(t)
        self.close()
        return l

    def delete(self, table, data):
        sql = "delete from " + table + " " + data
        self.cur.execute(sql)
        if self.cur.rowcount > 0:
            self.conn.commit()
            self.close()
            return True
        else:
            self.close()
            return False
        


        
