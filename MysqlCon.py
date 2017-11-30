
import pymysql
from MyObject import *

#       根据所传内容填充数据库
def fillCoTable(yline,time,fren,dbtable):
    # 打开数据库连接
    db = pymysql.connect("localhost" ,"root" ,"root123","testDb")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 如果数据表已经存在使用 execute() 方法删除表。
    sql_drop = "DROP TABLE IF EXISTS testDb." + dbtable
    cursor.execute(sql_drop)

    # 创建数据表SQL语句
    sql_createTable =""" 
         CREATE TABLE testDb.""" + dbtable +\
         """
         (
         id INT NOT NULL AUTO_INCREMENT,
         c_value  FLOAT ,
         c_time  INT,
         c_fren INT,  
         PRIMARY KEY (id)
          )
          """
    cursor.execute(sql_createTable)

    for index in range(len(yline)):
        insert = "INSERT INTO testDb."+dbtable+"(c_value,c_time,c_fren) value (" + str(yline[index]) + "," + str(time) +","+str(fren)+")"
        cursor.execute(insert)
    try:
       # 执行sql语句
       # 提交到数据库执行
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    # 关闭数据库连接
    db.close()
    pass
#       获取所有列表名称
def getListOfTable(dbName):
    db = pymysql.connect("localhost", "root", "root123", dbName)
    cursor = db.cursor()
    sql = "select TABLE_NAME from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA = '"+dbName+"'"
    # 使用 cursor() 方法创建一个游标对象 cursor
    tableNames = cursor.execute(sql)
    try:
       # 执行sql语句
       # 提交到数据库执行
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    # 关闭数据库连接
    db.close()
    tables = list(cursor.fetchmany(tableNames))
    tableList = []

    for x in tables:
        tableList.append(str(x).replace('(\'','').replace(',','').replace('\')',''))

    return tableList
    pass

#       通过数据库名和表名获取数据
def getDataOfTable(dbName,tbName):
    db = pymysql.connect("localhost", "root", "root123", dbName)
    cursor = db.cursor()

    sql = "select * from " + dbName + "." + tbName
    index = cursor.execute(sql)
    db.close()
    data = list(cursor.fetchmany(index))
    data_list = []

    for x in data:
        data_list.append(SingleData(x[0],x[1],x[2],x[3]))

    # print(len(data_list))
    # for x in data_list:
    #     print(x.id)
    #     print(x.value)
    #     print(x.time)
    #     print(x.fren)
    return data_list
    pass