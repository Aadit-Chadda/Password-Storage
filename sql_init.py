import sqlite3

db = sqlite3.connect('pass_word_lib.sqlite')
db.execute("CREATE TABLE IF NOT EXISTS pass(title TEXT ,password TEXT, description TEXT)")

e_title = 'test.test.com'
a_password = 'test123'
e_description = 'test'

db.execute("INSERT INTO pass VALUES(?, ?, ?)", (e_title, a_password, e_description))
db.commit()

cursor = db.cursor()
cursor.execute("SELECT * FROM pass")

for title, password, description in cursor:
    print(title, '\t', password, '\t', description)
    print()

cursor.close()
db.close()
