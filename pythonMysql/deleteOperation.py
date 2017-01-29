#!/usr/bin/python

import MySQLdb

# Open database connection
conn = MySQLdb.connect("localhost","mukesh","mk$423","mydb" )

# prepare a cursor object using cursor() method
cursor = conn.cursor()

# Prepare SQL query to DELETE required records
sql = "DELETE FROM customer WHERE customerid = '%s'" % ('1006')
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   conn.commit()
except:
   # Rollback in case there is any error
   conn.rollback()

# disconnect from server
conn.close()
