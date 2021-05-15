################################################################

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mcadb")



##############################################################
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#"
)
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)



###################################################################
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE student (name VARCHAR(25), address VARCHAR(25))")



#####################################################################
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE employee (name VARCHAR(25), address VARCHAR(25))")

# will show the list of already create tables
for x in mycursor:
  print(x)



####################################################################
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE student2 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(25), address VARCHAR(25))")
# will show the list of already create tables
mycursor.execute("show tables")
for x in mycursor:
  print(x)



#################################################################

#Alter Table 

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE student ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")



###################################################################
#INSERT INTO TABLE

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()

sql= "INSERT INTO student(name,address)VALUES(%s,%s)"
val=("Devesh","Doon")
mycursor.execute(sql,val)

mydb.commit()
print(mycursor.rowcount, "record inserted.", mycursor.lastrowid)



##################################################################
#SELECT COMMAND
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM student")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



##################################################################
#SELECT COMMAND2
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT name FROM student")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



##################################################################
#SELECT COMMAND2
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM student")

myresult = mycursor.fetchone()

print(myresult)



##################################################################
#WHERE STATEMENT
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM student WHERE address='doon' ")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)




################################################################
#Where_With_Like
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM student WHERE address LIKE '%wala'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)



###############################################################
#DELETE STATEMENT

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()
sql = "DELETE FROM student WHERE id =5"

mycursor.execute(sql)

mydb.commit()
print(mycursor.rowcount, "record(s) delete")



###################################################################
#UPDATE STATEMENT
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()

sql="UPDATE student SET address='premnagar' WHERE id =4"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount,"record updated")

################################################################

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mcadb")



##############################################################
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#"
)
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)



###################################################################
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE student (name VARCHAR(25), address VARCHAR(25))")



#####################################################################
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE employee (name VARCHAR(25), address VARCHAR(25))")

# will show the list of already create tables
for x in mycursor:
  print(x)



####################################################################
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE student2 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(25), address VARCHAR(25))")
# will show the list of already create tables
mycursor.execute("show tables")
for x in mycursor:
  print(x)



#################################################################

#Alter Table 

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE student ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")



###################################################################
#INSERT INTO TABLE

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()

sql= "INSERT INTO student(name,address)VALUES(%s,%s)"
val=("Devesh","Doon")
mycursor.execute(sql,val)

mydb.commit()
print(mycursor.rowcount, "record inserted.", mycursor.lastrowid)



##################################################################
#SELECT COMMAND
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM student")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



##################################################################
#SELECT COMMAND2
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT name FROM student")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



##################################################################
#SELECT COMMAND2
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM student")

myresult = mycursor.fetchone()

print(myresult)



##################################################################
#WHERE STATEMENT
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM student WHERE address='doon' ")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)




################################################################
#Where_With_Like
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM student WHERE address LIKE '%wala'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)



###############################################################
#DELETE STATEMENT

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()
sql = "DELETE FROM student WHERE id =5"

mycursor.execute(sql)

mydb.commit()
print(mycursor.rowcount, "record(s) delete")



###################################################################
#UPDATE STATEMENT
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#yourpassword#",
  database="mcadb"
)
mycursor = mydb.cursor()

sql="UPDATE student SET address='premnagar' WHERE id =4"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount,"record updated")









