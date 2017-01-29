#!/usr/bin/python

import MySQLdb

# Open database connection
conn = MySQLdb.connect("localhost","mukesh","mk$423","mydb" )

# prepare a cursor object using cursor() method
cursor = conn.cursor()
# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data

# Close the cursor and disconnect from server
if cursor:
	print "Cursor is open"
	cursor.close()

if cursor:
	print "cursor is open"
	cursor.close()
else:
	print "cursor is closed"

#cursor.open()
conn.close()
