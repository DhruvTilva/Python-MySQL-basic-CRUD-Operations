# **************************************************************************************************************************
#*****************Connection establishment**********
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='admin')
print(mydb.connection_id) # to check our pc is make connection to sql or not?

# **************Create Database ******************name=db1
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='admin')
cur=mydb.cursor()
cur.execute("CREATE DATABASE db1")

# ***************Create Table *********************table create in db1
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='admin',database='db1')
cur=mydb.cursor()
s="CREATE TABLE book(bookid integer(4),title varchar(20),price float(5,2))"
cur.execute(s)

#****************inserting data into table************insert in db1
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='admin',database='db1')
cur=mydb.cursor()
a="INSERT INTO book (bookid,title,price) VALUES(%s,%s,%s)"
b1=(1,'Pythonbook,234')
cur.execute(s,b1)
mydb.commit() #for save changes

#***************inserting multiple Rows**************** in table db1
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='admin',database='db1')
cur=mydb.cursor()
a="INSERT INTO book (bookid,title,price) VALUES(%s,%s,%s)"
books=[(2,'PHPbook,24'),(3,'C++',567),(4,'HTML CSS JS',764)] #make list and add multiple tuples and then
cur.executemany(s,books) #write command insertmany to add multiple tuple at one time
mydb.commit()# to save changes

#***************Extracting Data from table**************detail from db1
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='admin',database='db1')
cur=mydb.cursor()
s= "SELECT * FROM book"
cur.execute(s)
result=cur.fetchall() #all data fech and store result variable #it is multiple tupules list
for rec in result: #for obtaining one one tupules from the result print
    print(rec)

#***************Update Table Record*******************any data there is stored in table updation
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='admin',database='db1')
cur=mydb.cursor()
s="UPDATE book SET price=price+10 WHERE price>200" #updation where 200 higher increase by 10 set
cur.execute(s)
mydb.commit()#for permenently change data

#****************Delete Record from Table*************delet 2nd PHP row
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='admin',database='db1')
cur=mydb.cursor()
s="DELET FROM book WHERE title='PHP'"
cur.execute(s)
mydb.commit()

# *************************************************************************************************************************

'''first daunload MYSQL and then install connector module in python (you can also install via pip install mysql-connector)


connection.cursor()- it method return object we can execute SQL querys


&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&  Author:Dhruv Tilva       &
&  time:10:44  <5 Aug 2022> &
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&             '''