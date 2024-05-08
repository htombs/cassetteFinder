import sqlite3

mydb = sqlite3.connect()
cursor = mydb.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS cassette_finder.db")

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

#for x in mycursor:
#  print(x)