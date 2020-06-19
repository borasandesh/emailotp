import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart




def widget():  

    email=Label(mail,text="ENTER E-MAIL :",bg="skyblue" ,width=25)
    email.grid(row=0,column=0,padx=5,pady=5)
    email1= Entry(mail,textvariable=e,width=25)
    email1.grid(row=0, column=1, padx=5, pady=5)
    eButton= Button(mail,text="SEND OTP",width=10,command=mainc)
    eButton.grid(row=0, column=2, padx=5, pady=5)

    mail.msg = Label(mail, bg="skyblue")
    mail.msg.grid(row=1, column=0, padx=5, pady=5,columnspan=1)



    otp = Label(mail, text="ENTER OTP :", bg="skyblue", width=25)
    otp.grid(row=2, column=0, padx=10, pady=10)
    otp1 = Entry(mail,textvariable=v, width=25)
    otp1.grid(row=2, column=1, padx=5, pady=5)

    vButton = Button(mail, text="VERIFY", width=10, command=check)
    vButton.grid(row=2, column=2, padx=5, pady=5)

    mail.otpmsg= Label(mail,bg="skyblue")
    mail.otpmsg.grid(row=3, column=0, padx=5, pady=5,columnspan=1)



def mainc():
    num="0123456789"
    mail.sotp = ""
    r = e.get()



    for i in range(6):
        mail.sotp += num[int(random.random() * 10)]

    otpMsg = "YOUR OTP IS: " + mail.sotp

    messege = MIMEMultipart()
    messege['FROM'] = "OTP VALIDATOR (python_scripts)"
    messege['TO'] = r
    messege['Subject'] = "OTP VERIFICTION FROM SANDESH"

    messege.attach(MIMEText(otpMsg))

    smtp = smtplib.SMTP("smtp.gmail.com",587)

    smtp.starttls()

    semail= "#type your(sender)mail id here"

    spwd = "#your mail password"

    smtp.login(semail,spwd)

    smtp.sendmail(semail, r, messege.as_string())

    smtp.quit()

    r = '{}********{}'.format(r[0:2],r[-10:])

    mail.msg.config(text="OTP HAS BEEN SEND" + r)



def check():
    votp = v.get()

    s = mail.sotp

    if(votp==s):
        mail.otpmsg.config(text="Succefull")
    else:
        mail.otpmsg.config(text="failed")




mail = tk.Tk()
mail.title("verfification")
mail.geometry("500x150")
mail.resizable(False,False)
mail.config(bg="skyblue")


e= StringVar()
v= StringVar()
widget()

mainloop()
