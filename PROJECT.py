from Tkinter import *
import os
root=Tk()
root.title("WELCOME TO THE MARRIOTT HOTEL")
a=PhotoImage(file="Jehan_Numa_Logo.gif")
Label(root,image=a).grid(row=1,column=0,columnspan=5,rowspan=1,sticky=W+E)
Label(root,text="Name: B.Poorna",font="Arial 20 bold").grid(row=2,column=0,sticky=W)
Label(root,text="Enroll. no.: 161B064",font="Arial 20 bold").grid(row=4,column=0,sticky=W)
Label(root,text="Mobile no: 9425678077",font="Arial 20 bold").grid(row=6,column=0,sticky=W)
Label(root,text="E-mail: poornabhopal@gmail.com",font="Arial 20 bold").grid(row=8,column=0,sticky=W)
lb=Label(root,text="Batch: B3(BX)",font="Arial 20 bold")
lb.grid(row=10,column=0,sticky=W)
def fun():
    root.destroy()
    import imagebutton
lb.after(3000,fun)
root.mainloop()
