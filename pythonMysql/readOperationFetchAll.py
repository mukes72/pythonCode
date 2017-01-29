#!/usr/bin/python

import MySQLdb

# Open database connection
conn = MySQLdb.connect("localhost","mukesh","mk$423","mydb" )

# prepare a cursor object using cursor() method
cursor = conn.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM customer \
       WHERE customerid > '%d'" % (1003)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   print "Total count :"+str(cursor.rowcount)
   for row in results:
      customerid = row[0]
      customername = row[1]
      emailid = row[2]
      accountno = row[3]
      # Now print fetched result
      print "customerid=%s,customername=%s,emailid=%s,accountno=%d" % \
             (customerid, customername, emailid, accountno )
except :
   print "Error: unable to fecth data"

# Close the cursur and disconnect from server
finally:
	cursor.close()
	conn.close()
