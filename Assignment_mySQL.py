##############################################################################
'''Q1. What is a database? Differentiate between SQL and NoSQL databases.'''
''' Answer - A database is an organized collection of structured information, or data, 
typically stored electronically in a computer system.
It can be classified broadly as a)SQL DBs b)noSQL DBs
SQL dbs - mySQL, MS SQL, DB2, Oracle etc - 
works only with sturctured data.
data stored in rows and columns.

NoSQL dbs - MongoDB , Cassandra, Hbase, influx, Neo4j etc- 
works with unstructured data - text files,audio files, video files, rows/column data too.

'''

######################################################################################
'''Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.'''

'''Answer - 
## DDL -
DDL or Data Definition Language actually consists of the SQL commands that can be used to define the database schema.
 It simply deals with descriptions of the database schema and is used to create and modify the structure of
  database objects in the database. DDL is a set of SQL commands used to create, modify, and delete database structures
   but not data. These commands are normally not used by a general user, who should be accessing the database via an application.

List of DDL commands: 
List of DDL commands: 

CREATE: This command is used to create the database or its objects (like table, index, function, views, store procedure, and triggers).
DROP: This command is used to delete objects from the database.
ALTER: This is used to alter the structure of the database.
TRUNCATE: This is used to remove all records from a table, including all spaces allocated for the records are removed.
COMMENT: This is used to add comments to the data dictionary.
RENAME: This is used to rename an object existing in the database.
'''

try:
    import mysql.connector
    # import mysql.connector
    #create user 'user'@'%' identified by 'password'
    mydb = mysql.connector.connect(
    host="localhost",
    user="abc",
    password="password"
    )
    print(mydb)
    mycursor = mydb.cursor()
    mycursor.execute("create database if not exists personal")
    mycursor.execute("create table if not exists personal.person(social_id integer,first_name varchar(500),last_name varchar(500),contact varchar(200),city varchar(200),info varchar(1000))")
    mycursor.execute("create table if not exists personal.testdb(col1 varchar(200))")
    mycursor.execute("describe personal.testdb")
    for i in mycursor.fetchall():
        print(i)
    mycursor.execute("alter table  personal.testdb add col2 varchar(200)")  
    mycursor.execute("alter table  personal.testdb add col3 varchar(200)")  
    #mycursor.execute("describe personal.testdb")
    #for j in mycursor.fetchall():
    #    print(j)
    mycursor.execute("insert into personal.testdb values('THIS','IS','FUN')")  
    mydb.commit()
    mycursor.execute("select * from personal.testdb")  
    for k in mycursor.fetchall():
        print(k)
    mycursor.execute("truncate table personal.testdb")  
    mycursor.execute("select * from personal.testdb")  
    print("Table personal.testdb is trunacted now ==============================================")
    for m in mycursor.fetchall():
        print(m) 
    mycursor.execute("drop table personal.testdb") 
    print("now below no results are received")
    mycursor.execute("select * from personal.testdb")  
    for m in mycursor.fetchall():
        print(m) 
    mydb.close()
except Exception as e:
    print(e)
    
#################################################################################################################
'''
Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.
The SQL INSERT, UPDATE, and DELETE commands enable SQL users to manipulate and modify data:
The INSERT statement introduces new rows into an existing table.
The DELETE statement removes a row or combination of rows from a table.
The UPDATE statement enables users to update a row or group of rows in a table.
'''
import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("insert into personal.person values(10113,'ADIKRAH','TAMBANI','9811177777','DELHI','HR dept')")   ## this will give outcome in iterable mode, s need to use for loop
mydb.commit()
mycursor.execute("insert into personal.person values(10114,'KALRAJ','MISHRA','6811177777','NOIDA','FInance dept')")
mydb.commit()
mycursor.execute("update personal.person set city='GURGAON' where social_id=10114")
mydb.commit()
mycursor.execute("delete from personal.person where social_id=10114")
mydb.commit()
mycursor.execute("select * from personal.person")
for i in mycursor.fetchall():
    print(i)
mydb.close()

#########################################################################################
'''Q4. What is DQL? Explain SELECT with an example.
Ans - Data Query Language (DQL) is one of the basic sub-languages of SQL statements. 
There are generally four categories in SQL languages which are data query language (DQL), data definition language (DDL),
 data control language (DCL), and data manipulation language(DML). 
It is also occasionally suggested that a transaction control language (TCL) belongs in the sub-language set.
'''
import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("select * from personal.person")
for i in mycursor.fetchall():
    print(i)
mydb.close()

########################################################################
'''
Q5. Explain Primary Key and Foreign Key.
A primary key is used to ensure that data in the specific column is unique. A column cannot have NULL values.
 It is either an existing table column or a column that is specifically generated 
 by the database according to a defined sequence. 

A foreign key is a column or group of columns in a relational database table that provides a link between data in two tables. 
It is a column (or columns) that references a column (most often the primary key) of another table. 
'''

####################################################################################
'''
Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.
'''
## connection to python , since python & mySQL are on same AWS server localhost is used.
import mysql.connector
# import mysql.connector
#create user 'user abc' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
##### Cursors are created by the connection. cursor() method: they are bound to the connection for the
#  entire lifetime and all the commands are executed in the context of the database session wrapped by the connection.
mycursor = mydb.cursor()
## execute method takes queries given to it & executes them in DB.
mycursor.execute("select * from personal.person")
for i in mycursor.fetchall():
    print(i)
mydb.close()

##################################################################
'''
Q7. Give the order of execution of SQL clauses in an SQL query
Ans - order of execution is below -
The order in which the clauses in queries are executed is as follows:

1. FROM/JOIN: The FROM and/or JOIN clauses are executed first to determine the data of interest.

2. WHERE: The WHERE clause is executed to filter out records that do not meet the constraints.

3. GROUP BY: The GROUP BY clause is executed to group the data based on the values in one or more columns.

4. HAVING: The HAVING clause is executed to remove the created grouped records that don’t meet the constraints.

5. SELECT: The SELECT clause is executed to derive all desired columns and expressions.

6. ORDER BY: The ORDER BY clause is executed to sort the derived values in ascending or descending order. 
'''
