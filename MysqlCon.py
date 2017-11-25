
import pymysql

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