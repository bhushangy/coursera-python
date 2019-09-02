import sqlite3

conn = sqlite3.connect('emaildb.sqlite') #create a new db named emaildb
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts') #if there existes prev db then drop that'

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    organl = pieces[1].split('.')
    org    = organl[0]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,)) #here ? is palceholder that cud be anything like email or name or any other
    row = cur.fetchone() #searching for the row with specified email
    if row is None: #if that is not der insert it and set count to 1
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else: #if its der already then increase its count by 1 in the count clumn
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))

conn.commit()
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
#so uptill here its gonna write to the database

#here we are reading from the database
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])  #here row is a tuple so row[0] is email and row[1] is count....(email,count) -->tuple

cur.close()
