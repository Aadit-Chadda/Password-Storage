import sqlite3
import tkinter as tkinter
import pandas as pd
from encrypting import *
from secureHash import *


def add_pass():
    def input_data():
        db = sqlite3.connect('pass_word_lib.sqlite')
        db.execute("CREATE TABLE IF NOT EXISTS pass(title TEXT ,password TEXT, description TEXT)")

        e_title = title.get()
        e_password = password.get()
        a_password = encryption(e_password)
        e_description = description.get()

        t = str(e_title)
        p = str(a_password)
        d = str(e_description)

        db.execute("INSERT INTO pass VALUES(?, ?, ?)", (t, p, d))
        db.commit()
        db.close()

        win1.destroy()

    win1 = tkinter.Toplevel()
    win1.title('Add Password')

    todo = tkinter.Label(win1, text="Please fill in the following field and then press Enter")
    todo.pack()

    label1 = tkinter.Label(win1, text='Title/ID: ')
    label1.pack()

    title = tkinter.Entry(win1, width=50)
    title.pack()

    label2 = tkinter.Label(win1, text='Password: ')
    label2.pack()

    password = tkinter.Entry(win1, width=25)
    password.pack()

    label3 = tkinter.Label(win1, text='Description: ')
    label3.pack()

    description = tkinter.Entry(win1, width=50)
    description.pack()

    confirm = tkinter.Button(win1, text='Enter', command=input_data)
    confirm.pack()

    win1.mainloop()


def view_pass():
    def cross_check():
        master_key_attempt = pass_w.get()
        attempt = hashing(master_key_attempt)
        if attempt == master_key:
            getpass_win.destroy()
            db = sqlite3.connect('pass_word_lib.sqlite')
            db.close()
            db = sqlite3.connect('pass_word_lib.sqlite')
            db.execute("CREATE TABLE IF NOT EXISTS pass(title TEXT ,password BYTES, description TEXT)")

            cursor = db.cursor()
            cursor.close()
            cursor = db.cursor()
            cursor.execute('SELECT *, oid FROM pass')
            records = cursor.fetchall()
            print_record = ''
            count = 0
            for r in records:
                count += 1
                string = str(r[1])
                pa = string.lstrip("(b'")
                pa = pa.rstrip("', <class 'bytes'>)")
                pa = decryption(pa)
                pa = pa.lstrip('b')
                print('pa: ', pa)
                print_record += str(count) + '  ' + 'Title: ' + str(r[0]) + '\n' + 'Password: ' + pa + '\n' + 'Description: ' + str(r[2]) + '\n' + 'oid: ' + str(r[3]) + '\n\n'
                print(str(r[3]))
                print(print_record)

            cursor.close()
            db.close()

            def delete_pass():
                num = del_entry.get()
                db = sqlite3.connect('pass_word_lib.sqlite')
                db.execute("CREATE TABLE IF NOT EXISTS pass(title TEXT ,password BYTES, description TEXT)")

                cursor = db.cursor()
                cursor.execute('SELECT *, oid FROM pass')
                records = cursor.fetchall()

                count = 0
                for record in records:
                    count += 1
                    if count == num:
                        db.execute("DELETE FROM pass WHERE oid=?", str(record[3]))

                cursor.close()
                db.close()

                win2.destroy()


            win2 = tkinter.Toplevel()
            win2.title('Your Saved Passwords')

            query_label = tkinter.Label(win2, text=print_record)
            query_label.pack()

            del_L = tkinter.Label(win2, text='Enter the number of password you would like to delete')
            del_L.pack()

            del_entry = tkinter.Entry(win2, width=5)
            del_entry.pack()

            del_key = tkinter.Button(win2, text='Delete', command=delete_pass)
            del_key.pack()

            win2.mainloop()
        else:
            getpass_win.destroy()
            sorrow = tkinter.Toplevel()
            sorrow.title('WRONG Master Key Entered')
            mes = tkinter.Label(sorrow, text="""Sorry, but you have Entered the wrong MASTER_KEY
            Please Try again with the correct key to access your previously saved passwords""")
            mes.pack()

    getpass_win = tkinter.Toplevel()
    getpass_win.title('confirm your MASTER-KEY pass')

    get_it = tkinter.Label(getpass_win, text='Enter your Master: ')
    get_it.pack()

    pass_w = tkinter.Entry(getpass_win, width=30, show='*')
    pass_w.pack()

    conf = tkinter.Button(getpass_win, text='Enter', command=cross_check)
    conf.pack()


# Init tkinter
root = tkinter.Tk()
root.title('Passwords')
root.geometry('370x120')

# Text Label
Label1 = tkinter.Label(root, text='''To add a password to the DataBase select "Add"
To view your passwords select "View"''')
Label1.pack()

# Frame for Buttons
Holder = tkinter.Frame(root)
Holder.pack()

# Buttons
add = tkinter.Button(Holder, text='Add password', command=add_pass)
add.pack()

see = tkinter.Button(Holder, text='View Password', command=view_pass)
see.pack()

root.mainloop()
