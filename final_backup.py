import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
import os.path
import tkinter.messagebox
from tkinter import ttk
import datetime as dt
import time
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from PIL import ImageDraw
import PIL
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from PIL import EpsImagePlugin
import tkinter.messagebox as MessageBox
import mysql.connector
from string import digits
import os
import requests
import io
#from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload
# ========================================Function=================================
def cleardate():
    entDeliveryDate.delete(0, 'end')
    entCustomerName.delete(0, 'end')
    entPhoneNo.delete(0, 'end')
    entSL.delete(0, 'end')
    entSLtwo.delete(0, 'end')
    entSCH.delete(0, 'end')
    entSCHtwo.delete(0, 'end')
    entSS.delete(0, 'end')
    entSStwo.delete(0, 'end')
    entST.delete(0, 'end')
    entSTtwo.delete(0, 'end')
    entSN.delete(0, 'end')
    entSNtwo.delete(0, 'end')
    entSW.delete(0, 'end')
    entSWtwo.delete(0, 'end')
    entPL.delete(0, 'end')
    entPLtwo.delete(0, 'end')
    entPW.delete(0, 'end')
    entPWtwo.delete(0, 'end')
    entPH.delete(0, 'end')
    entPHtwo.delete(0, 'end')
    entPM.delete(0, 'end')
    entPMtwo.delete(0, 'end')
    entPG.delete(0, 'end')
    entPGtwo.delete(0, 'end')
    entShirt.delete(0, 'end')
    entCoat.delete(0, 'end')
    entKurta.delete(0, 'end')
    entPant.delete(0, 'end')
    entOther.delete(0, 'end')
    c.delete('all')


def insert():
    name = entCustomerName.get()
    phone = int(entPhoneNo.get())
    sl = entSL.get()
    sl2 = entSLtwo.get()
    sch = entSCH.get()
    sch2 = entSCHtwo.get()
    ss = entSS.get()
    ss2 = entSStwo.get()
    st = entST.get()
    st2 = entSTtwo.get()
    sn = entSN.get()
    sn2 = entSNtwo.get()
    sw = entSW.get()
    sw2 = entSWtwo.get()
    shirt = entShirt.get()
    coat = entCoat.get()
    kurta = entKurta.get()
    pant = entPant.get()
    pl = entPL.get()
    pl2 = entPLtwo.get()
    pw = entPW.get()
    pw2 = entPWtwo.get()
    ph = entPH.get()
    ph2 = entPHtwo.get()
    pm = entPM.get()
    pm2 = entPMtwo.get()
    pg = entPG.get()
    pg2 = entPGtwo.get()
    other = entOther.get()
    deliverydate = (entDeliveryDate.get())
    date = (entOrderdate.get())

    try:
        con = sqlite3.connect('king.db')
        cur = con.cursor()
        mysql_query = """INSERT INTO data1 (name,phone,sl,sl2,sch,sch2,ss,ss2,st,st2,sn,sn2,sw,sw2,shirt,coat,pl,pl2,pw,pw2,ph,ph2,pm,pm2,pg,pg2,kurta,pant,other,date,deliverydate) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) """
        values = (
        name, phone, sl, sl2, sch, sch2, ss, ss2, st, st2, sn, sn2, sw, sw2, shirt, coat, pl, pl2, pw, pw2, ph, ph2, pm,
        pm2, pg, pg2, kurta, pant, other, date, deliverydate)
        print(date)
        # cursor = connection.cursor()
        cur.execute(mysql_query, values)
        last_id = cur.lastrowid
        filename = str(last_id) + '.png'

        image1.save(filename)
        con.commit()
        print('Success')
        cleardate()
        DisplayData()
        con.close()
        MessageBox.showinfo("Success", "Record has been inserted")
    except Exception as e:
        MessageBox.showerror("Data Not Insert ", "Record Not Insert")

def update():
    try:
        con = sqlite3.connect('king.db')
        cur = con.cursor()
        viewInfo = root.customer_table.focus()
        learnerData = root.customer_table.item(viewInfo)
        row = learnerData['values']
        cur.execute("update data1 set name=?,phone=?,sl=?,sl2=?,sch=?,sch2=?,ss=?,ss2=?,st=?,st2=?,sn=?,sn2=?,sw=?,sw2=?,shirt=?,coat=?,pl=?,pl2=?,pw=?,pw2=?,ph=?,ph2=?,pm=?,pm2=?,pg=?,pg2=?,kurta=?,pant=?,other=?,date=?,deliverydate=? where id=?",(
        root.name.get(),
        root.phone.get(),
        root.sl.get(),
        root.SLtwo.get(),
        root.sch.get(),
        root.SCHtwo.get(),
        root.ss.get(),
        root.SStwo.get(),
        root.st.get(),
        root.STtwo.get(),
        root.sn.get(),
        root.SNtwo.get(),
        root.sw.get(),
        root.SWtwo.get(),
        root.shirt.get(),
        root.coat.get(),
        root.pl.get(),
        root.PLtwo.get(),
        root.pw.get(),
        root.PWtwo.get(),
        root.ph.get(),
        root.PHtwo.get(),
        root.pm.get(),
        root.PMtwo.get(),
        root.pg.get(),
        root.PGtwo.get(),
        root.kurta.get(),
        root.pant.get(),
        root.other.get(),
        root.Orderdate.get(),
        root.DeliveryDate.get(),
        row[0]
        ))
        con.commit()
        filename=str(row[0])+'.png'
        os.remove(filename)
        image1.save(filename)

        DisplayData()
        cleardate()
        con.close()
        MessageBox.showinfo("Data Entry Form","Record Updates Successfully")
    except Exception as e:
        MessageBox.showerror("Failed","Not Updated" )


def search():
    try:
        query = entSearchBy.get()
        query = query.strip()
        selections = []
        for child in root.customer_table.get_children():
            child_values = root.customer_table.item(child)['values']
            child_values_n = [str(i).lower() for i in child_values]
            print(child_values_n)
            if query.lower() in child_values_n:
                print(root.customer_table.item(child)['values'])
                selections.append(child)
        print('search completed')
        root.customer_table.selection_set(selections)
        if len(selections) <= 0:
            MessageBox.showinfo("Data Entry Form", "No such record found")
    except:
        MessageBox.showerror("Data Entry Form", "Error")


def DisplayData():
    con = sqlite3.connect('king.db')
    cursor = con.cursor()
    cursor.execute("select * from data1 ORDER BY id DESC")
    results = cursor.fetchall()
    if len(results) != 0:
        root.customer_table.delete(*root.customer_table.get_children())
        for row in results:
            root.customer_table.insert('', END, values=row)
    else:
        MessageBox.showerror("Data Entry Form", "No Data to show")


def TraineeInfo(ev):
    c.delete('all')
    viewInfo = root.customer_table.focus()
    learnerData = root.customer_table.item(viewInfo)
    row = learnerData['values']
    print(row)
    root.name.set(row[1])
    root.phone.set(row[2])
    root.sl.set(row[3])
    root.SLtwo.set(row[4])
    root.sch.set(row[5])
    root.SCHtwo.set(row[6])
    root.ss.set(row[7])
    root.SStwo.set(row[8])
    root.st.set(row[9])
    root.STtwo.set(row[10])
    root.sn.set(row[11])
    root.SNtwo.set(row[12])
    root.sw.set(row[13])
    root.SWtwo.set(row[14])
    root.shirt.set(row[15])
    root.coat.set(row[16])
    root.pl.set(row[17])
    root.PLtwo.set(row[18])
    root.pw.set(row[19])
    root.PWtwo.set(row[20])
    root.ph.set(row[21])
    root.PHtwo.set(row[22])
    root.pm.set(row[23])
    root.PMtwo.set(row[24])
    root.pg.set(row[25])
    root.PGtwo.set(row[26])
    root.kurta.set(row[27])
    root.pant.set(row[28])
    root.other.set(row[29])
    root.Orderdate.set(row[30])
    root.DeliveryDate.set(row[31])
    print('yooo')
    global my_image
    my_image = PhotoImage(file=str(row[0]) + '.png')
    c.create_image(0, 0, anchor=NW, image=my_image)
    global image_on_canvas
    image_on_canvas = c.create_image(0, 0, anchor='nw', image=my_image)
    c.itemconfig()


def delete():
    con = sqlite3.connect('king.db')
    cur = con.cursor()
    viewInfo = root.customer_table.focus()
    learnerData = root.customer_table.item(viewInfo)
    row = learnerData['values']
    cur.execute("delete from data1 where id=?",[row[0]])
    con.commit()
    filename = str(row[0]) + '.png'
    os.remove(filename)
    DisplayData()
    cleardate()
    con.close()
    MessageBox.showinfo("Data Entry Form","Record Successfully Deleted")

def upload_database():
    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)
    folder = '1sLXpnOATCWJGBeMe98tt9sc8ZJ4jSU9s'
    dir = os.getcwd()
    print(dir)

    filepath = os.path.join(dir, 'king.db')

    file_list = drive.ListFile({'q': f"'{folder}' in parents and trashed=false"}).GetList()

    try:
        for file1 in file_list:
            if file1['title'] == 'kingdata.db':
                file1.Delete()

    except:
        pass

    gfile = drive.CreateFile({'parents': [{'id': folder}], 'title': 'kingdata.db'})
    gfile.SetContentFile(filepath)
    gfile.Upload()
    MessageBox.showinfo("success","data uploaded successfully")


def download_database():
    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)
    folder = '1sLXpnOATCWJGBeMe98tt9sc8ZJ4jSU9s'

    print("file download: king.db")

    file_list = drive.ListFile({'q':f"'{folder}' in parents and trashed=false"}).GetList()
    print(len(file_list))
    for index, file in enumerate(file_list):
        print(index+1,'file downloaded: ', file['title'])
        file.GetContentFile(file['title'])

    MessageBox.showinfo("Data Download Form", "Record Successfully Download")


def eraser():
    c.delete('all')


def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    c.create_line(x1, y1, x2, y2, fill='black', width=5)
    draw.line([x1, y1, x2, y2], fill='black', width=5)

def correct_n(inp):
    if inp.isdigit():
        return True
    elif inp=="":
        return True
    else:
        MessageBox.showerror("Error!! ", "Type digits only")
        return False

def correct_f(inp):
    allowed = set(digits).union('.')
    if inp.isdigit():
        return True
    elif all(c in allowed for c in inp):
        return True
    else:
        MessageBox.showerror("Error!! ", "Type digits and one decimal only")
        return False

def correct_s(inp):
    if inp.isalpha():
        return True
    elif inp == "":
        return True
    else:
        MessageBox.showerror("Error!! ", "Type Characters only")
        return False


def click(event):
    entSearchBy.config(state=NORMAL)
    entSearchBy.delete(0,END)

def click_m(event):
    entOther.config(state=NORMAL)
    entOther.delete(0,END)


from tkinter import *
root = Tk()
root.title('King Tailors')
dir = os.getcwd()
print(dir)

path = os.path.join(dir, 'icon.ico')
root.iconbitmap(path)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(str(screen_width)+"x"+str(screen_height))

title = Label(root, text="King Tailors", bd=2, relief=GROOVE, font=("times new roman", 30, "bold"),
              bg="#800000", fg="white", highlightbackground="white", highlightthickness=3, pady=2)
title.grid(row=0,columnspan=5, sticky="nsew")

frame1 = tk.Frame(root, bd=3, bg='white', relief=tk.GROOVE)
frame2 = tk.Frame(root, bd=3, relief=tk.GROOVE)

frame1.grid(row=1, column=0, columnspan=2,sticky="nsew")
frame2.grid(row=1, column=3,sticky="nsew")

root.grid_columnconfigure(0, weight=2,uniform="fred")
root.grid_columnconfigure(1, weight=2,uniform="fred")
#root.grid_columnconfigure(2, weight=1,uniform="fred")
root.grid_columnconfigure(3, weight=3,uniform="fred")
#root.grid_columnconfigure(4, weight=1,uniform="fred")
#root.grid_columnconfigure(5, weight=1,uniform="group1")
root.grid_rowconfigure(0, minsize=30)
root.grid_rowconfigure(1, weight=1)

o_date = dt.datetime.now()
data = str(o_date).split(" ")[0].split("-")
format_date = f"{data[2]}/{data[1]}/{data[0]}"
# root.format_date = f"{o_date:%d %b %y}"
#format_date = o_date
root.Orderdate=StringVar()

Orderdate = Label(frame1, text="Order Date", bg="white", fg="black")
Orderdate.grid(row=0,pady=7, padx=5, column=0, sticky="nsew")
Orderdate.config(font=("times new roman", 14, "bold"))

entOrderdate = Entry(frame1,textvariable=root.Orderdate, text="Order Date", bd=3, font=("times new roman", 14, "bold"))
entOrderdate.insert(END, format_date)
#entOrderdate.config(state='readonly')
entOrderdate.grid(row=0,column=1,sticky="nsew",pady=7,padx=10,columnspan=2)

root.DeliveryDate=StringVar()
DeliveryDate = Label(frame1, text="Delivery Date", font=("times new roman", 14, "bold"), bg="white",fg="black")
DeliveryDate.grid(row=0,column=4, pady=7, padx=2, sticky="nsew")

entDeliveryDate = DateEntry(frame1, textvariable=root.DeliveryDate, text="Delivery Date", bd=3, font=("times new roman", 14, "bold"))
entDeliveryDate.grid(row=0,column=5,sticky="nsew",pady=7, padx=10,columnspan=2)

root.name=StringVar()
name = Label(frame1, text="Name", font=("times new roman", 14, "bold"), bg="white",fg="black",width=25)
name.grid(row=1,pady=7, padx=1, column=0, sticky="nsew")


entCustomerName = Entry(frame1,textvariable=root.name, bd=3, font=("times new roman", 14, "bold"))
entCustomerName.grid(row=1,column=1,sticky="nsew",pady=7,padx=10,columnspan=2)
# reg = root.register(correct_s)
# entCustomerName.config(validate="key",validatecommand=(reg,'%P'))

root.phone=StringVar()
name = Label(frame1, text="Phone No", font=("times new roman", 14, "bold"), bg="white",fg="black",width=25)
name.grid(row=1,column=4, pady=7, padx=5, sticky="e")


entPhoneNo = Entry(frame1,textvariable=root.phone, bd=3,font=("times new roman", 14, "bold"))
entPhoneNo.grid(row=1,column=5,sticky="nsew",pady=7, padx=10,columnspan=2)
reg = root.register(correct_n)
entPhoneNo.config(validate="key",validatecommand=(reg,'%P'))

root.sl = StringVar()

sl = Label(frame1, text="S.L", font=("times new roman", 14, "bold"), fg="black",width=5)
sl.grid(row=2,pady=7, padx=10, column=0, sticky="nsew")

entSL = Entry(frame1, textvariable=root.sl,  bd=3, bg="white", font=("times new roman", 14, "bold"))
entSL.grid(row=2,column=1,sticky="nsew",pady=7,padx=10)
reg = root.register(correct_f)
entSL.config(validate="key",validatecommand=(reg,'%P'))


root.SLtwo = StringVar()

entSLtwo = Entry(frame1, textvariable=root.SLtwo, bd=3, bg="white", font=("times new roman", 14, "bold"))
entSLtwo.grid(row=2,pady=7, padx=10, column=2, sticky="nsew")
reg = root.register(correct_f)
entSLtwo.config(validate="key",validatecommand=(reg,'%P'))

root.pl = StringVar()
pl = Label(frame1, text="P.L", font=("times new roman", 14, "bold"), fg="black")

pl.grid(row=2,pady=7, padx=10, column=4, sticky="nsew")
entPL = Entry(frame1, textvariable=root.pl,  bd=3, bg="white", font=("times new roman", 14, "bold"))
entPL.grid(row=2,pady=7, padx=10, column=5, sticky="nsew")
reg = root.register(correct_f)
entPL.config(validate="key",validatecommand=(reg,'%P'))

root.PLtwo = StringVar()

entPLtwo = Entry(frame1, textvariable=root.PLtwo, bd=3, bg="white", font=("times new roman", 14, "bold"))
entPLtwo.grid(row=2,pady=7, padx=10, column=6, sticky="nsew")
reg = root.register(correct_f)
entPLtwo.config(validate="key",validatecommand=(reg,'%P'))

root.sch = StringVar()

sch = Label(frame1, text="S.CH", font=("times new roman", 14, "bold"), fg="black")
sch.grid(row=3,pady=7, padx=10, column=0, sticky="nsew")

entSCH = Entry(frame1, textvariable=root.sch,  bd=3, bg="white", font=("times new roman", 14, "bold"))
entSCH.grid(row=3,column=1,sticky="nsew",pady=7,padx=10)
reg = root.register(correct_f)
entSCH.config(validate="key",validatecommand=(reg,'%P'))

root.SCHtwo = StringVar()

entSCHtwo = Entry(frame1, textvariable=root.SCHtwo, bd=3, bg="white", font=("times new roman", 14, "bold"))
entSCHtwo.grid(row=3,pady=7, padx=10, column=2, sticky="nsew")
reg = root.register(correct_f)
entSCHtwo.config(validate="key",validatecommand=(reg,'%P'))

root.pw = StringVar()

pw = Label(frame1, text="P.W", font=("times new roman", 14, "bold"), fg="black")
pw.grid(row=3,pady=7, padx=10, column=4, sticky="nsew")

entPW = Entry(frame1, textvariable=root.pw,  bd=3, bg="white", font=("times new roman", 14, "bold"))
entPW.grid(row=3,pady=7, padx=10, column=5, sticky="nsew")
reg = root.register(correct_f)
entPW.config(validate="key",validatecommand=(reg,'%P'))

root.PWtwo = StringVar()
entPWtwo = Entry(frame1, textvariable=root.PWtwo, bd=3, bg="white", font=("times new roman", 14, "bold"))
entPWtwo.grid(row=3,pady=7, padx=10, column=6, sticky="nsew")
reg = root.register(correct_f)
entPWtwo.config(validate="key",validatecommand=(reg,'%P'))

root.ss = StringVar()

ss = Label(frame1, text="S.S", font=("times new roman", 14, "bold"), fg="black")
ss.grid(row=4,pady=7, padx=10, column=0, sticky="nsew")

entSS = Entry(frame1, textvariable=root.ss, bd=3, bg="white", font=("times new roman", 14, "bold"))
entSS.grid(row=4,column=1,sticky="nsew",pady=7,padx=10)
reg = root.register(correct_f)
entSS.config(validate="key",validatecommand=(reg,'%P'))

root.SStwo = StringVar()

entSStwo = Entry(frame1, textvariable=root.SStwo, bd=3, bg="white", font=("times new roman", 14, "bold"))
entSStwo.grid(row=4,pady=7, padx=10, column=2, sticky="nsew")
reg = root.register(correct_f)
entSStwo.config(validate="key",validatecommand=(reg,'%P'))

root.ph = StringVar()

ph = Label(frame1, text="P.H", font=("times new roman", 14, "bold"), fg="black")
ph.grid(row=4,pady=7, padx=10, column=4, sticky="nsew")

entPH = Entry(frame1, textvariable=root.ph, bd=3, bg="white", font=("times new roman", 14, "bold"))
entPH.grid(row=4,pady=7, padx=10, column=5, sticky="nsew")
reg = root.register(correct_f)
entPH.config(validate="key",validatecommand=(reg,'%P'))

root.PHtwo = StringVar()

entPHtwo = Entry(frame1, textvariable=root.PHtwo, bd=3, bg="white", font=("times new roman", 14, "bold"))
entPHtwo.grid(row=4,pady=7, padx=10, column=6, sticky="nsew")
reg = root.register(correct_f)
entPHtwo.config(validate="key",validatecommand=(reg,'%P'))

root.st = StringVar()

st = Label(frame1, text="S.T", font=("times new roman", 14, "bold"), fg="black")
st.grid(row=5,pady=7, padx=10, column=0, sticky="nsew")
entST = Entry(frame1, textvariable=root.st,  bd=3, bg="white", font=("times new roman", 14, "bold"))
entST.grid(row=5,column=1,sticky="nsew",pady=7,padx=10)
reg = root.register(correct_f)
entST.config(validate="key",validatecommand=(reg,'%P'))

root.STtwo = StringVar()

entSTtwo = Entry(frame1, textvariable=root.STtwo, bd=3, bg="white", font=("times new roman", 14, "bold"))
entSTtwo.grid(row=5,pady=7, padx=10, column=2, sticky="nsew")
reg = root.register(correct_f)
entSTtwo.config(validate="key",validatecommand=(reg,'%P'))

root.pm = StringVar()

pm = Label(frame1, text="P.M", font=("times new roman", 14, "bold"), fg="black")
pm.grid(row=5,pady=7, padx=10, column=4, sticky="nsew")

entPM = Entry(frame1, textvariable=root.pm,  bd=3, bg="white", font=("times new roman", 14, "bold"))
entPM.grid(row=5,pady=7, padx=10, column=5, sticky="nsew")
reg = root.register(correct_f)
entPM.config(validate="key",validatecommand=(reg,'%P'))

root.PMtwo = StringVar()

entPMtwo = Entry(frame1, textvariable=root.PMtwo, bd=3, bg="white", font=("times new roman", 14, "bold"))
entPMtwo.grid(row=5,pady=7, padx=10, column=6, sticky="nsew")
reg = root.register(correct_f)
entPMtwo.config(validate="key",validatecommand=(reg,'%P'))

root.sn = StringVar()

sn = Label(frame1, text="S.N", font=("times new roman", 14, "bold"), fg="black")
sn.grid(row=6,pady=7, padx=10, column=0, sticky="nsew")

entSN = Entry(frame1, textvariable=root.sn,  bd=3, bg="white", font=("times new roman", 14, "bold"))
entSN.grid(row=6,column=1,sticky="nsew",pady=7,padx=10)
reg = root.register(correct_f)
entSN.config(validate="key",validatecommand=(reg,'%P'))

root.SNtwo = StringVar()

entSNtwo = Entry(frame1, textvariable=root.SNtwo, bd=3, bg="white", font=("times new roman", 14, "bold"))
entSNtwo.grid(row=6,pady=7, padx=10, column=2, sticky="nsew")
reg = root.register(correct_f)
entSNtwo.config(validate="key",validatecommand=(reg,'%P'))

root.pg = StringVar()

pg = Label(frame1, text="P.G", font=("times new roman", 14, "bold"), fg="black")
pg.grid(row=6,pady=7, padx=10, column=4, sticky="nsew")

entPG = Entry(frame1, textvariable=root.pg,  bd=3, bg="white", font=("times new roman", 14, "bold"))
entPG.grid(row=6,pady=7, padx=10, column=5, sticky="nsew")
reg = root.register(correct_f)
entPG.config(validate="key",validatecommand=(reg,'%P'))

root.PGtwo = StringVar()

entPGtwo = Entry(frame1, textvariable=root.PGtwo, bd=3, bg="white", font=("times new roman", 14, "bold"))
entPGtwo.grid(row=6,pady=7, padx=10, column=6, sticky="nsew")
reg = root.register(correct_f)
entPGtwo.config(validate="key",validatecommand=(reg,'%P'))

root.sw = StringVar()
sw = Label(frame1, text="S.W", font=("times new roman", 14, "bold"), fg="black")
sw.grid(row=7,pady=7, padx=10, column=0, sticky="nsew")

entSW = Entry(frame1, textvariable=root.sw,  bd=3, bg="white", font=("times new roman", 14, "bold"))
entSW.grid(row=7,column=1,sticky="nsew",pady=7,padx=10)
reg = root.register(correct_f)
entSW.config(validate="key",validatecommand=(reg,'%P'))

root.SWtwo = StringVar()

entSWtwo = Entry(frame1, textvariable=root.SWtwo, bd=3, bg="white", font=("times new roman", 14, "bold"))
entSWtwo.grid(row=7,pady=7, padx=10, column=2, sticky="nsew")
reg = root.register(correct_f)
entSWtwo.config(validate="key",validatecommand=(reg,'%P'))

root.kurta = StringVar()
kurta = Label(frame1, text="Kurta", font=("times new roman", 14, "bold"), fg="black")

kurta.grid(row=7,pady=7, padx=10, column=4, sticky="nsew")

entKurta = Entry(frame1, textvariable=root.kurta, bd=3, bg="white", font=("times new roman", 14, "bold"))
entKurta.grid(row=7,pady=7, padx=10, column=5, sticky="nsew")
reg = root.register(correct_n)
entKurta.config(validate="key",validatecommand=(reg,'%P'))

root.shirt = StringVar()
shirt = Label(frame1, text="Shirt", font=("times new roman", 14, "bold"), fg="black")
shirt.grid(row=8,pady=7, padx=10, column=0, sticky="nsew")

entShirt = Entry(frame1, textvariable=root.shirt,  bd=3, bg="white", font=("times new roman", 14, "bold"))
entShirt.grid(row=8,pady=7, padx=10, column=1, sticky="nsew")
reg = root.register(correct_n)
entShirt.config(validate="key",validatecommand=(reg,'%P'))

root.pant = StringVar()

pant = Label(frame1, text="Pant", font=("times new roman", 14, "bold"), fg="black")
pant.grid(row=8,pady=7, padx=10, column=4, sticky="nsew")

entPant = Entry(frame1, textvariable=root.pant,  bd=3, bg="white", font=("times new roman", 14, "bold"))
entPant.grid(row=8,pady=7, padx=10, column=5, sticky="nsew")
reg = root.register(correct_n)
entPant.config(validate="key",validatecommand=(reg,'%P'))

root.coat = StringVar()
coat = Label(frame1, text="Coat", font=("times new roman", 14, "bold"),  fg="black")
coat.grid(row=9,pady=7, padx=10, column=0, sticky="nsew")

entCoat = Entry(frame1, textvariable=root.coat,  bg="white", bd=3, font=("times new roman", 14, "bold"))
entCoat.grid(row=9,pady=7, padx=10, column=1, sticky="nsew")
reg = root.register(correct_n)
entCoat.config(validate="key",validatecommand=(reg,'%P'))

root.other = StringVar()

other = Label(frame1, text="Draw Desired Design..", font=("times new roman", 14, "bold"), fg="white",bg="#800000")
other.grid(row=9,pady=7, padx=10, column=5, columnspan=2,sticky="nsew")
#
# entOther = Entry(frame1, textvariable=root.other,  bd=3, bg="white", font=("times new roman", 12, "bold"))
# entOther.grid(row=9,pady=7, padx=5, column=5, sticky="nsew")
# reg = root.register(correct_s)
# entOther.config(validate="key",validatecommand=(reg,'%P'))
entOther = Entry(frame1, textvariable=root.other,  bd=3, bg="white", font=("times new roman", 14, "bold"),justify="center")
entOther.insert(0,'Type any suggestions here (optional)..')
entOther.config(state=DISABLED)
entOther.bind("<Button-1>",click_m)
entOther.grid(row=11,pady=7, padx=10, column=0,columnspan=3, sticky="nsew")
entOther.config(highlightbackground="#800000")

# ==================================Canvas==============================================
c = Canvas(frame1, bg='white',height=100,bd=5,highlightbackground = "black", highlightcolor= "black")
# c.pack()
c.grid(row=11, column=5,columnspan=2,padx=10)


image1 = PIL.Image.new("RGB", (230, 170), (255, 255, 255))
draw = ImageDraw.Draw(image1)
#c.pack(expand=YES,fill=BOTH)
c.bind('<B1-Motion>', paint)

# ==================================Button==============================================

Add = Button(frame1, text='Add', font='arial 10 bold', bd=5, fg="white",bg="#800000",command=insert)
# Add.grid(row=13, column=0)
Add.grid(row=14,column=0,sticky="nsew",padx=10,pady=10)

Update = Button(frame1, text='Update', font='arial 10 bold', bd=5,fg="white", bg="#800000",command=update)
# Update.grid(row=13, column=1)
Update.grid(row=14,column=1,sticky="nsew",padx=10,pady=10)

Delete = Button(frame1, text='Delete', font='arial 10 bold', bd=5, fg="white", bg="#800000",command=delete)
# Delete.grid(row=13, column=3)
Delete.grid(row=14,column=2,sticky="nsew",padx=10,pady=10)

ClearData = Button(frame1, text='Clear', font= 'arial 10 bold', bd=5, fg="white",bg="#800000", command=cleardate)
# ClearData.grid(row=13, column=4)
ClearData.grid(row=14,column=3,sticky="nsew",padx=10,pady=10)

# =========================Using for Canves Button========================================
eraser_button = Button(frame1, text='Eraser', font='arial 10 bold', bd=5, fg="white",bg="#800000",command=eraser)
# eraser_button.grid(row=0, column=25)
eraser_button.grid(row=14,column=5,sticky="nsew",padx=10,pady=10)

clear_button = Button(frame1, text='All Clear!', font='arial 10 bold', bd=5, fg="white",bg="#800000" )
# clear_button.grid(row=0, column=25)
clear_button.grid(row=14,column=6,sticky="nsew",padx=5,pady=10)




n_cols = 7
n_rows = 14

for i in range(n_cols):
    frame1.grid_columnconfigure(i,weight=1,uniform="fred")
#frame1.grid_columnconfigure(7,minsize=20)
for i in range(n_rows):
    frame1.grid_rowconfigure(i,weight=1)


# lblSearchBy = Label(frame2, text="Search By", font=("times new roman", 10, "bold"), bg="white", fg="black")
# lblSearchBy.grid(row=0, column=0, pady=10, padx=4, sticky="nsew")
entSearchBy = Entry(frame2, bd=3, font=("times new roman", 14, "bold"),justify='center')
entSearchBy.insert(0,'Search here')
entSearchBy.config(state=DISABLED)
entSearchBy.bind("<Button-1>",click)
entSearchBy.grid(row=0,column=0,sticky="nsew",pady=10,padx=20)

search = Button(frame2, text='Search', font='arial 10 bold', bd=5, fg="white",bg="#800000",command=search)
search.grid(row=0,column=1,sticky="nsew",padx=10,pady=10)
searchAll = Button(frame2, text='Refresh', font='arial 10 bold', bd=5, fg="white",bg="#800000",command=DisplayData)
searchAll.grid(row=0,column=2,sticky="nsew",padx=10,pady=10)
Save = Button(frame2, text='Save', font='arial 10 bold', bd=5,fg="white",bg="#800000",command=upload_database)
Save.grid(row=0,column=3,sticky="nsew",padx=12,pady=10)
Download = Button(frame2, text='Download', font='arial 10 bold', bd=5,fg="white",bg="#800000",command=download_database)
Download.grid(row=0,column=4,sticky="nsew",padx=1,pady=10)

# # ===================Table View=====================
table_frame = Frame(frame2, bd=5, relief=GROOVE, bg="white")
table_frame.grid(row=1,columnspan=6,column=0,sticky="nsew")
scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
scroll_y = Scrollbar(table_frame, orient=VERTICAL)
root.customer_table = ttk.Treeview(table_frame, columns=(
    "Id", "Name", "Phone", "SL", "SLTWO", "SCH", "SCHTWO", "SS", "SSTWO", "ST", "STTWO", "SN", "SNTWO", "SW",
    "SWTWO", "SHIRT", "COAT", "PL", "PLTWO", "PW",
    "PWTWO", "PH", "PHTWO", "PM", "PMTWO", "PG", "PGTWO" ,"KURTA", "PANT", "OTHERS","DATE",
    "DELIVERYDATE"),
                                   xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=root.customer_table.xview)
scroll_y.config(command=root.customer_table.yview)
root.customer_table.heading("Id", text="Customer ID")
root.customer_table.column("Id",anchor='center')
root.customer_table.heading("Name", text="Customer Name")
root.customer_table.column("Name",anchor='center')
root.customer_table.heading("Phone", text="Phone No")
root.customer_table.column("Phone",anchor='center')
root.customer_table.heading("SL", text="S.L")
root.customer_table.column("SL",anchor='center')
root.customer_table.heading("SLTWO", text="S.L Two")
root.customer_table.column("SLTWO",anchor='center')
root.customer_table.heading("SCH", text="S.CH")
root.customer_table.column("SCH",anchor='center')
root.customer_table.heading("SCHTWO", text="S.CH Two")
root.customer_table.column("SCHTWO",anchor='center')
root.customer_table.heading("SS", text="S.S")
root.customer_table.column("SS",anchor='center')
root.customer_table.heading("SSTWO", text="S.S Two")
root.customer_table.column("SSTWO",anchor='center')
root.customer_table.heading("ST", text="S.T")
root.customer_table.column("ST",anchor='center')
root.customer_table.heading("STTWO", text="S.T Two")
root.customer_table.column("STTWO",anchor='center')
root.customer_table.heading("SN", text="S.N Two")
root.customer_table.column("SN",anchor='center')
root.customer_table.heading("SNTWO", text="S.N Two")
root.customer_table.column("SNTWO",anchor='center')
root.customer_table.heading("SW", text="S.W")
root.customer_table.column("SW",anchor='center')
root.customer_table.heading("SWTWO", text="S.W Two")
root.customer_table.column("SWTWO",anchor='center')
root.customer_table.heading("SHIRT", text="Shirt")
root.customer_table.column("SHIRT",anchor='center')
root.customer_table.heading("COAT", text="Coat")
root.customer_table.column("COAT",anchor='center')

root.customer_table.heading("PL", text="P.L")
root.customer_table.column("PL",anchor='center')
root.customer_table.heading("PLTWO", text="P.L Two")
root.customer_table.column("PLTWO",anchor='center')
root.customer_table.heading("PW", text="P.W")
root.customer_table.column("PW",anchor='center')
root.customer_table.heading("PWTWO", text="P.W Two")
root.customer_table.column("PWTWO",anchor='center')
root.customer_table.heading("PH", text="P.H")
root.customer_table.column("PH",anchor='center')
root.customer_table.heading("PHTWO", text="P.H Two")
root.customer_table.column("PHTWO",anchor='center')
root.customer_table.heading("PM", text="P.M")
root.customer_table.column("PM",anchor='center')
root.customer_table.heading("PMTWO", text="P.M Two")
root.customer_table.column("PMTWO",anchor='center')
root.customer_table.heading("PG", text="P.G")
root.customer_table.column("PG",anchor='center')
root.customer_table.heading("PGTWO", text="P.G Two")
root.customer_table.column("PGTWO",anchor='center')
root.customer_table.heading("KURTA", text="Kurta")
root.customer_table.column("KURTA",anchor='center')
root.customer_table.heading("PANT", text="Pant")
root.customer_table.column("PANT",anchor='center')
root.customer_table.heading("OTHERS", text="other")
root.customer_table.column("OTHERS",anchor='center')

# root.customer_table.heading("OTHERS", text="Other")
# root.customer_table.column("OTHERS",anchor='center')

root.customer_table.heading("DATE", text="Date")
root.customer_table.column("DATE",anchor='center')
root.customer_table.heading("DELIVERYDATE", text="Delivery Date")
root.customer_table.column("DELIVERYDATE",anchor='center')
root.customer_table['show'] = 'headings'
root.customer_table.pack(fill=BOTH, expand=2)
root.customer_table.bind("<ButtonRelease-1>",TraineeInfo)
# root.customer_table.bind("<ButtonRelease-1>")


frame2.grid_columnconfigure(0,weight=2,uniform="group1")
frame2.grid_columnconfigure(1,weight=1,uniform="group1")
frame2.grid_columnconfigure(2,weight=1,uniform="group1")
frame2.grid_columnconfigure(3,weight=1,uniform="group1")
frame2.grid_columnconfigure(4,weight=1,uniform="group1")
frame2.grid_columnconfigure(5,minsize=10)
frame2.grid_rowconfigure(1,weight=1)

root.mainloop()
#
