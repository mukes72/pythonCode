#!/usr/bin/python

import MySQLdb

# Open database connection
conn = MySQLdb.connect("localhost","mukesh","mk$423","mydb" )

# prepare a cursor object using cursor() method
cursor = conn.cursor()

# Prepare SQL query to UPDATE required records
sql = "UPDATE customer SET emailid = 'mohan.kumar@reddif.com'\
                          WHERE customername = '%s'" % ('Mohan')
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
