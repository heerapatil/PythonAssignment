
import sqlite3
conn=sqlite3.connect("first.db")
cursor=conn.cursor()
sql = """create table employee(first_name char(20) not null,last_name char(20),age int,income float)"""
cursor.execute(sql)
print "table created successfully"
cursor.executemany("insert into employee(first_name,last_name,age,income)/values(%s,%s,%s,%s),
[
("heera","patil",21,25000),
("ajay","musham",22,25000),
]
print "insertion done"
cursor.execute("select * from employee")
for x in cursor:
  print "FIRST_NAME = ", x[0] 
  print "LAST_NAME = ", x[1] 
  print "AGE = ", x[2]
  print "INCOME= ", x[3],"\n" 
conn.commit()
print "record updated"
cursor.execute("insert into employee(first_name,last_name,age,income)/ values("prachi","chikshe",24,25000)")
print "insertion done"
cursor.execute("delete from employee where age=24")
conn.commit()
print "record deleted"
cursor.execute("select * from employee")
for x in cursor:
  print "FIRST_NAME = ", x[0] 
  print "LAST_NAME = ", x[1] 
  print "AGE = ", x[2]
  print "INCOME= ", x[3],"\n" 
conn.commit()
conn.close()

