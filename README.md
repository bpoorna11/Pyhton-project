# Pyhton-project
from Tkinter import *
import Tkinter as tk
import os
root1=Tk()
root1.title("WELCOME TO THE JEHAN NUMA PALACE")
root1.geometry('+0+0')
a=PhotoImage(file="jehan-numa-palace_pool.gif")
Label(root1,image=a).grid(row=1,column=0,columnspan=5,rowspan=1,sticky=E+N+S+W)
Label(root1,text="Name:B.Poorna",font="Arial 20 bold").grid(row=2,column=0,sticky=W)
Label(root1,text="Enroll. no.: 161B064",font="Arial 20 bold").grid(row=4,column=0,sticky=W)
Label(root1,text="Batch: B3(BX)",font="Arial 20 bold").grid(row=5,column=0,sticky=W)
Label(root1,text="Mobile no: 9425678077",font="Arial 20 bold").grid(row=6,column=0,sticky=W)
Label(root1,text="e-mail: poornabhopal@gmail.com",font="Arial 20 bold").grid(row=8,column=0,sticky=W)
def mainfunc():
    root1.destroy()
    
    import sqlite3
    import tkMessageBox
    con=sqlite3.Connection("Emp")
    cur=con.cursor()
    cur.execute("create table if not exists Emp(name varchar(20),sex varchar(20),age number,nationality varchar(20),purpose varchar(20),mobile number,identity varchar(20),roomtype varchar(20),roomno number primary key)")    
    root=Tk()
    root.geometry('1920x1080+0+0')
    root.title("Hotel Jehan Numa Palace")
    Label(root,text="Hotel JEHAN-NUMA Booking system",bg='orange',font=("helveticas",'20',"bold")).grid(row=2,column=5)
    Label(root,text="Please enter your details",font="arial 20 bold").grid(row=10,column=0)
    Label(root,text="Enter Your Name",font='arial 15 bold').grid(row=15,column=0,sticky=W)
    e=Entry(root,width=25,bd=5,bg='orange')
    e.grid(row=15,column=5)
    Label(root,text="Select your gender",font='arial 15 bold').grid(row=20,column=0,sticky=W)
    opts = ['Select your gender','male', 'female','transgender']
    oMenuWidth = len(max(opts, key=len))
    v = StringVar(root)
    v.set("Select your gender")
    oMenu = OptionMenu(root, v, *opts)
    oMenu.config(width=oMenuWidth)
    oMenu.grid(row=20,column=5)
    Label(root,text="Enter your age",font='arial 15 bold').grid(row=25,column=0,sticky=W)
    f=Entry(root,width=25,bd=5,bg='orange')
    f.grid(row=25,column=5)
    Label(root,text="Enter your nationality",font='arial 15 bold').grid(row=30,column=0,sticky=W)
    g=Entry(root,width=25,bd=5,bg='orange')
    g.grid(row=30,column=5)
    Label(root,text="Purpose of visit",font='arial 15 bold').grid(row=35,column=0,sticky=W)
    h=Entry(root,width=25,bd=5,bg='orange')
    h.grid(row=35,column=5)
    Label(root,text="Enter your mobile number",font='arial 15 bold').grid(row=40,column=0,sticky=W)
    i=Entry(root,width=25,bd=5,bg='orange')
    i.grid(row=40,column=5)
    Label(root,text="Enter your identification",font="arial 20 bold").grid(row=10,column=6)
    x=IntVar()
    Radiobutton(root,text='driving licence no.',variable=x,value=1,font='arial 15 bold').grid(row=15,column=6,sticky=W)
    Radiobutton(root,text='aadhar card no.',variable=x,value=2,font='arial 15 bold').grid(row=20,column=6,sticky=W)
    Radiobutton(root,text='Pan card no.',variable=x,value=3,font='arial 15 bold').grid(row=25,column=6,sticky=W)
    Radiobutton(root,text='Voter ID card no.',variable=x,value=4,font='arial 15 bold').grid(row=30,column=6,sticky=W)
    Label(root,text="Enter one ID number :",font='arial 15 bold').grid(row=35,column=6,sticky=W)
    l=Entry(root,width=20,bd=5,bg='orange')
    l.grid(row=35,column=7)
    Label(root,text="Please select a room",font="arial 20 bold").grid(row=45,column=0)
    variable=StringVar()
    variable.set("Room type")
    w=Label(root,text="Please type the name of the room",font="arial 10 bold").grid(row=52,column=0)
    n=Entry(root,width=25,bd=5,bg='orange')
    n.grid(row=52,column=5)
    Label(root,text="Select room number",font="arial 20 bold").grid(row=60,column=0)
    var=IntVar()
    var.set("room no.")
    x=OptionMenu(root,var,"201","202","203","204","205","301","302","303","304","305").grid(row=62,column=0)
    
    def insert():
        a=(e.get(),v.get(),int(f.get()),g.get(),h.get(),int(i.get()),l.get(),n.get(),int(var.get()))
        cur.execute("insert into Emp values(?,?,?,?,?,?,?,?,?)",a)
        con.commit()
        tkMessageBox.showinfo('Insert ','Booking Complete')
        cur.execute("select * from Emp")
        a=cur.fetchall()
        
    def show():
        q=int(var.get())
        cur.execute("select * from Emp where roomno=?",(q,))
        a=cur.fetchall()
        tkMessageBox.showinfo('Show',a)
        print a
    def showall():
        gh=Tk()
        cur.execute("select * from Emp")
        a=cur.fetchall()
        #tkMessageBox.showinfo('Showall',a)
        count,r=0
        for i in a:
            r=r+1
            count=0
            for row in i:
                print row
                Label(gh,text=str(row)+' ').grid(row=r,column=count)
                count=count+1

        print a
        gh.mainloop()
        
    def viewroom1():
        root2=Toplevel()
        a=PhotoImage(file='hollywood_room.gif')
        Label(root2,image=a).grid(row=1,column=0,columnspan=5,rowspan=1,sticky=W)
        root2.mainloop()
    def viewroom2():
        root3=Toplevel()
        a=PhotoImage(file='single_room.gif')
        Label(root3,image=a).grid(row=1,column=0,columnspan=5,rowspan=1,sticky=W)
        root3.mainloop()
    def viewroom3():
        root4=Toplevel()
        a=PhotoImage(file='doublebed_room.gif')
        Label(root4,image=a).grid(row=1,column=0,columnspan=5,rowspan=1,sticky=W)
        root4.mainloop()
    def viewroom4():
        root5=Toplevel()
        a=PhotoImage(file='king_size_room.gif')
        Label(root5,image=a).grid(row=1,column=0,columnspan=5,rowspan=1,sticky=W)
        root5.mainloop()
    Button(root,text='Book',bd=5,height=2,width=8,command=insert,relief=RAISED).grid(row=65,column=4)
    Button(root,text='Show',bd=5,height=2,width=8,command=show,relief=RAISED).grid(row=65,column=5)
    Button(root,text='Show All',bd=5,height=2,width=8,command=showall,relief=RAISED).grid(row=65,column=6)
    Button(root,text="Bollywood room",width=12,command=viewroom1,bd=5).grid(row=53,column=0)
    Button(root,text="Single room",width=12,command=viewroom2,bd=5).grid(row=54,column=0)
    Button(root,text="DoubleBed room",width=12,command=viewroom3,bd=5).grid(row=55,column=0)
    Button(root,text="Suite room",width=12,command=viewroom4,bd=5).grid(row=56,column=0)
    
    root.mainloop()

Button(root1,text="Click to Proceed",bd=7,bg='orange',font="('Helveticas',16,'bold')",relief=RAISED,command=mainfunc).grid(row=10,column=3)
root1.mainloop()
