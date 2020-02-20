import sqlite3
import re

conn = sqlite3.connect('mbox.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '): continue
    lst_line = line.split()
    email = lst_line[1]
    #print (email)

    pieces = re.findall('@([^ ]*)',email)
    org = pieces[0]
    #print(org)

    #need to fetch the domain name of the emails (part after @)
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
    conn.commit()


# display the top 10 emails in descending order
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()