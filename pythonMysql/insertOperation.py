#!/usr/bin/python

import MySQLdb

# Open database connection
conn = MySQLdb.connect("localhost","mukesh","mk$423","mydb" )

# prepare a cursor object using cursor() method
cursor = conn.cursor()

# Prepare SQL query to INSERT a record into the database.
#sql = """INSERT INTO customer(customerid,
#         customername, emailid, accountno)
 #        VALUES ('1006', 'Mohan', 'mohan@reddif.com', '30009')"""
		 
# Prepare dynamic SQL query to INSERT a record into the database.
sql = "INSERT INTO customer(customerid,\
         customername, emailid, accountno) \
		 VALUES('%s','%s','%s','%d')" \
         %('1006', 'Mohan', 'mohan@reddif.com', 30009)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   conn.commit()
except:
   # Rollback in case there is any error
   conn.rollback()

# Close cursor and disconnect from server
conn.close()
cursor.close()
