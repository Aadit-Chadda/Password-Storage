import sqlite3
from tkinter import *
import tkinter as tkinter
from encrypting import *

db = sqlite3.connect('pass_word_lib.sqlite')
db.execute("CREATE TABLE IF NOT EXISTS pass(title TEXT ,password BYTES, description TEXT)")

pass_show = []

cursor = db.cursor()
cursor.execute('SELECT *, oid FROM pass')
records = cursor.fetchall()

print_record = ''
for r in records:
    string = str(r[1])
    print(string)
    pa = string.lstrip("(b'")
    pa = pa.rstrip("', <class 'bytes'>)")
    pa = decryption(pa)
    pa = pa.lstrip('b')
    print_record += str(r[0]) + '\n' + str(pa) + '\n' + str(r[2]) + '\n\n'

cursor.close()
db.close()

root = tkinter.Tk()
root.title('TEST')

query_label = tkinter.Label(root, text=print_record)
query_label.pack()

root.mainloop()
