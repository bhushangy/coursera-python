import sqlite3

conn = sqlite3.connect('emaildb.sqlite') #create a new db named emaildb
cur = conn.cursor()

cur.execute("SELECT * FROM Counts")
for row in cur:
  print(row)

#See this row is a tuple/triple/quadruple
#This is how u iterate through the tables in a databse

#pls refer emaildb.py for ur future projects regarding writing to a database