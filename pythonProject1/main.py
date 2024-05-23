import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *


def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['id'])
    e2.insert(0, select['products'])
    e3.insert(0, select['quantity'])

def Add():
    bazar_vokzal_id = e1.get()
    bazar_vokzal_products = e2.get()
    bazar_vokzal_quantity = e3.get()

    mysqldb = mysql.connector.connect(host="localhost",
                                      user="root",
                                      password="12345678",
                                      database="bazar_vokzal")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO baza (id,products,quantity) VALUES (%s, %s, %s)"
        val = (bazar_vokzal_id, bazar_vokzal_products, bazar_vokzal_quantity)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record added successfully...")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def update():
    bazar_vokzal_id = e1.get()
    bazar_vokzal_products = e2.get()
    bazar_vokzal_quantity = e3.get()
    mysqldb = mysql.connector.connect(host="localhost",
                                      user="root",
                                      password="12345678",
                                      database="bazar_vokzal")
    mycursor = mysqldb.cursor()

    try:
        sql = "Update baza set products= %s,quantity= %s where id= %s"
        val = (bazar_vokzal_id, bazar_vokzal_products, bazar_vokzal_quantity)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Updateddddd successfuly...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()

def delete():
    client_id = e1.get()

    mysqldb = mysql.connector.connect(host="localhost",
                                      user="root",
                                      password="12345678",
                                      database="bazar_vokzal")
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from baza where id = %s"
        val = (client_id,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Deleteeeee successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()

def show():
    mysqldb = mysql.connector.connect(host="localhost",
                                      user="root",
                                      password="12345678",
                                      database="bazar_vokzal")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT id, products, quantity FROM baza")
    records = mycursor.fetchall()
    print(records)

    for i, (id, products, quantity) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id, products, quantity))
        mysqldb.close()

root = Tk()
root.geometry("1280x720")
#root["bg"] = "gray"
global e1
global e2
global e3
global e4

tk.Label(root, font=(None, 30)).place(x=300, y=5)

tk.Label(root, text="ID").place(x=100, y=200)
Label(root, text="products").place(x=100, y=230)
Label(root, text="quantity").place(x=100, y=260)


e1 = Entry(root)
e1.place(x=200, y=200)

e2 = Entry(root)
e2.place(x=200, y=230)

e3 = Entry(root)
e3.place(x=200, y=260)


Button(root, text="Добавить", command=Add, height=3, width=13).place(x=600, y=450)
Button(root, text="update", command=update, height=3, width=13).place(x=480, y=450)
Button(root, text="Delete", command=delete, height=3, width=13).place(x=720, y=450)

cols = ('id', 'products', 'quantity')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=350, y=200)

show()
listBox.bind('<Double-Button-1>', GetValue)

root.mainloop()