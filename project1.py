import tkinter as tk
import mysql.connector
def Withdrawal():
    dep=tk.Tk()
    mydb=mysql.connector.connect(host="localhost", user="root", passwd="1234", charset="utf8",database="bank123")
    mycursor=mydb.cursor()
    Acc=tk.Label(dep,text="Enter the account number for withdrawal ")
    Acc.pack()
    Acno=tk.Entry(dep)
    Acno.pack()
    sub=tk.Button(dep,text="submit",command=lambda: withd(Acno))
    sub.pack()   
def withd(Acno):
    try:
        dep=tk.Tk()
        mydb=mysql.connector.connect(host="localhost", user="root", passwd="1234", charset="utf8",database="bank123")
        mycursor=mydb.cursor()
        mycursor.execute("select * from bank where AccNo={}".format(Acno.get()))
        result=mycursor.fetchall()
        lable1a=tk.Label(dep,text="Account No. :")
        lable2a=tk.Label(dep,text="Name:")
        lable3a=tk.Label(dep,text="Telephone No. :")
        lable4a=tk.Label(dep,text="Balance") 
        lable1b=tk.Label(dep,text=result[0][0])
        lable2b=tk.Label(dep,text=result[0][1])
        lable3b=tk.Label(dep,text=result[0][2])
        lable4b=tk.Label(dep,text=result[0][3])
        lable1a.grid(row=2,column=0)
        lable2a.grid(row=3,column=0)
        lable3a.grid(row=4,column=0)
        lable4a.grid(row=5,column=0)
        lable1b.grid(row=2,column=1)
        lable2b.grid(row=3,column=1)
        lable3b.grid(row=4,column=1)
        lable4b.grid(row=5,column=1)
        Al=tk.Label(dep,text="Enter the amount to to withdraw")
        Al.grid(row=6,column=0)
        Amt=tk.Entry(dep)
        Amt.grid(row=6,column=1)
        depositbutton=tk.Button(dep,text="withdraw",command=lambda: with2(Amt,Acno))
        depositbutton.grid(row=7,column=1)                               
    except:
        x=tk.Label(dep,text="record not found")
        x.pack()
def with2(Amt,Acno):
    mydb=mysql.connector.connect(host="localhost", user="root", passwd="1234", charset="utf8",database="bank123")
    mycursor=mydb.cursor()
    dep=tk.Tk()
    mycursor.execute("update bank set BalanceAmt=BalanceAmt-{} where accno={}".format(Amt.get(), Acno.get()))
    mydb.commit()
    mycursor.execute("select * from bank where AccNo={}".format(Acno.get()))
    result=mycursor.fetchall()
    lable1a=tk.Label(dep,text="Account No. :")
    lable2a=tk.Label(dep,text="Name:")
    lable3a=tk.Label(dep,text="Telephone No. :")
    lable4a=tk.Label(dep,text="Balance") 
    lable1b=tk.Label(dep,text=result[0][0])
    lable2b=tk.Label(dep,text=result[0][1])
    lable3b=tk.Label(dep,text=result[0][2])
    lable4b=tk.Label(dep,text=result[0][3])
    lable1a.grid(row=2,column=0)
    lable2a.grid(row=3,column=0)
    lable3a.grid(row=4,column=0)
    lable4a.grid(row=5,column=0)
    lable1b.grid(row=2,column=1)
    lable2b.grid(row=3,column=1)
    lable3b.grid(row=4,column=1)
    lable4b.grid(row=5,column=1)


def Transactions():
    t=tk.Tk()
    mainmenu=tk.Label(t,text="=========================================\n***** transactions menu*****\n=========================================\n=========================================")
    mainmenu.pack()
    button1 = tk.Button(t,text="1:deposit",width=25,command=deposit)
    button2 = tk.Button(t,text="2: withdraw",width=25,command=Withdrawal)
    button1.pack()
    button2.pack()
def deposit():
    dep=tk.Tk()
    mydb=mysql.connector.connect(host="localhost", user="root", passwd="1234", charset="utf8",database="bank123")
    mycursor=mydb.cursor()
    Acc=tk.Label(dep,text="Enter the account number for deposit ")
    Acc.pack()
    Acno=tk.Entry(dep)
    Acno.pack()
    sub=tk.Button(dep,text="submit",command=lambda: dept(Acno))
    sub.pack()   
def dept(Acno):
    try:
        dep=tk.Tk()
        mydb=mysql.connector.connect(host="localhost", user="root", passwd="1234", charset="utf8",database="bank123")
        mycursor=mydb.cursor()
        mycursor.execute("select * from bank where AccNo={}".format(Acno.get()))
        result=mycursor.fetchall()
        lable1a=tk.Label(dep,text="Account No. :")
        lable2a=tk.Label(dep,text="Name:")
        lable3a=tk.Label(dep,text="Telephone No. :")
        lable4a=tk.Label(dep,text="Balance") 
        lable1b=tk.Label(dep,text=result[0][0])
        lable2b=tk.Label(dep,text=result[0][1])
        lable3b=tk.Label(dep,text=result[0][2])
        lable4b=tk.Label(dep,text=result[0][3])
        lable1a.grid(row=2,column=0)
        lable2a.grid(row=3,column=0)
        lable3a.grid(row=4,column=0)
        lable4a.grid(row=5,column=0)
        lable1b.grid(row=2,column=1)
        lable2b.grid(row=3,column=1)
        lable3b.grid(row=4,column=1)
        lable4b.grid(row=5,column=1)
        Al=tk.Label(dep,text="Enter the amount to to deposit")
        Al.grid(row=6,column=0)
        Amt=tk.Entry(dep)
        Amt.grid(row=6,column=1)
        depositbutton=tk.Button(dep,text="deposit",command=lambda: deposit2(Amt,Acno))
        depositbutton.grid(row=7,column=1)                               
    except:
        x=tk.Label(dep,text="record not found")
        x.pack()
def deposit2(Amt,Acno):
    mydb=mysql.connector.connect(host="localhost", user="root", passwd="1234", charset="utf8",database="bank123")
    mycursor=mydb.cursor()
    dep=tk.Tk()
    mycursor.execute("update bank set BalanceAmt=BalanceAmt+{} where accno={}".format(Amt.get(), Acno.get()))
    mydb.commit()
    mycursor.execute("select * from bank where AccNo={}".format(Acno.get()))
    result=mycursor.fetchall()
    lable1a=tk.Label(dep,text="Account No. :")
    lable2a=tk.Label(dep,text="Name:")
    lable3a=tk.Label(dep,text="Telephone No. :")
    lable4a=tk.Label(dep,text="Balance") 
    lable1b=tk.Label(dep,text=result[0][0])
    lable2b=tk.Label(dep,text=result[0][1])
    lable3b=tk.Label(dep,text=result[0][2])
    lable4b=tk.Label(dep,text=result[0][3])
    lable1a.grid(row=2,column=0)
    lable2a.grid(row=3,column=0)
    lable3a.grid(row=4,column=0)
    lable4a.grid(row=5,column=0)
    lable1b.grid(row=2,column=1)
    lable2b.grid(row=3,column=1)
    lable3b.grid(row=4,column=1)
    lable4b.grid(row=5,column=1)

def listed(a,b,c,d):
    record=[]
    record.append(a.get())
    record.append(b.get())
    record.append(c.get())
    record.append(d.get())
    mydb=mysql.connector.connect(host="localhost",user="root", passwd="1234",charset="utf8",database="Bank123")
    mycursor=mydb.cursor()
    query="insert into Bank (accno, AccName, telno, Balanceamt) values(%s,%s,%s,%s)"
    mycursor.execute(query,record)
    mydb.commit()
    new=tk.Tk()
    c=tk.Label(new,text="record saved")
    c.pack()
def New_Account():
    new=tk.Tk()
    a=tk.Label(new,text="Enter account number:")
    n=tk.Label(new,text="Enter account name:")
    t=tk.Label(new,text="enter telephone no:")
    am=tk.Label(new,text="enter Openeing balance:")
    a.grid(row=0,column=0)
    ea= tk.Entry(new)
    ea.grid(row=0,column=1)
    n.grid(row=3,column=0)
    en= tk.Entry(new)
    en.grid(row=3,column=1)
    t.grid(row=5,column=0)
    te= tk.Entry(new)
    te.grid(row=5,column=1)
    am.grid(row=7,column=0)
    eam=tk.Entry(new)
    eam.grid(row=7,column=1)
    sub=tk.Button(new,text="submit",command=lambda: listed(ea,en,te,eam))
    sub.grid(row=9)
    new.mainloop()
def search(a):
    try:
        Acno=a.get()
        mydb=mysql.connector.connect(host="localhost",user="root", passwd="1234",charset="utf8",database="Bank123")
        mycursor=mydb.cursor()
        mycursor.execute("select * from bank where AccNo={}".format(Acno))
        result=mycursor.fetchall()
        res=tk.Tk()
        statement=tk.Label(res,text="record found")
        lable1a=tk.Label(res,text="Account No. :")
        lable2a=tk.Label(res,text="Name:")
        lable3a=tk.Label(res,text="Telephone No. :")
        lable4a=tk.Label(res,text="Balance") 
        lable1b=tk.Label(res,text=result[0][0])
        lable2b=tk.Label(res,text=result[0][1])
        lable3b=tk.Label(res,text=result[0][2])
        lable4b=tk.Label(res,text=result[0][3])
        statement.grid()
        lable1a.grid(row=2,column=0)
        lable2a.grid(row=3,column=0)
        lable3a.grid(row=4,column=0)
        lable4a.grid(row=5,column=0)
        lable1b.grid(row=2,column=1)
        lable2b.grid(row=3,column=1)
        lable3b.grid(row=4,column=1)
        lable4b.grid(row=5,column=1)
    except:
        res=tk.Tk()
        acc=tk.Label(res,text="record not found")
        acc.pack()
def search_account():
    s=tk.Tk()
    acc=tk.Label(s,text="Enter account number to search for:")
    acc.grid(row=0,column=0)
    eacc= tk.Entry(s)
    eacc.grid(row=0,column=1)
    sub=tk.Button(s,text="Continue",command=lambda: search(eacc))
    sub.grid(row=3,column=1)
    s.mainloop()     

w=tk.Tk()
mainmenu=tk.Label(text="=========================================\n***** Welcome to Future Tech Banking*****\n=========================================\n=========================================")
mainmenu.pack()
button1 = tk.Button(text="1:Open an Account",width=25,command=New_Account)
button2 = tk.Button(text="2: Search for Customer",width=25,command=search_account)
button3 = tk.Button(text="3: Transactions",width=25,command=Transactions)
button4 = tk.Button(text="4: Exit",width=25,command=w.destroy)
mainmenu1=tk.Label(text="***** MAIN MENU******")
mainmenu1.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
w.mainloop()
