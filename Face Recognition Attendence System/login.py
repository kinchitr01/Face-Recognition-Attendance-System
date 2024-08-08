from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
from admin_student import student
from time import strftime
from datetime import datetime
from tkinter import messagebox
import mysql.connector
from admin_page import admin_page





class login:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendence System")
        self.root.iconbitmap(r"D:\D\Face Recognition Attendence System\Images\icon_atendance.ico")
        self.root.configure(bg='sky blue')
        self.var_user=StringVar()
        self.var_pass=StringVar()

        #bg_img
       # img2=Image.open(r"D:\Face Recognition Attendence System\Images\srki_cllg.jpg")
        #img2=img2.resize((1530,790),Image.ANTIALIAS)
        #self.photoimg2=ImageTk.PhotoImage(img2)

       # bg_img=Label(self.root,image=self.photoimg2)
        #bg_img.place(x=0,y=0,width=1530,height=790)

        #SRKI LOGO
        img=Image.open(r"D:\D\Face Recognition Attendence System\Images\SRKI_logo.png")
        img=img.resize((300,150),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=10,y=10,width=300,height=150)

         #---------------------time-----------------------------------
        def time():
            t = strftime('%H:%M:%S %p')
            lbl.config(text=t )
            lbl.after(1000, time)
        
        lbl = Label(font=("times new roman",14,"bold"),background="sky blue",foreground="red")
        lbl.place(x=10,y=160,width=110,height=50)
        time()

        title_lbl=Label(self.root,text="Face Recongnition Attendance System",font=("times new roman",35,"bold"), bg="sky blue",fg="red")
        title_lbl.place(x=370,y=10,width=800,height=150)
        title_lbl1=Label(self.root,text="By Kinchit Raval",font=("times new roman",20,"bold"), bg="sky blue",fg="red")
        title_lbl1.place(x=410,y=120,width=700,height=50)
       

        #Sarvajanik LOGO
        img1=Image.open(r"D:\D\Face Recognition Attendence System\Images\Sarvajanik_logo.png")
        img1=img1.resize((300,150),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=1220,y=10,width=300,height=150)

        frame=Frame(self.root,bg="White",relief="solid",bd=5)
        frame.place(x=610,y=220,width=340,height=450)

        imgl=Image.open(r"D:\D\Face Recognition Attendence System\Images\login.png")
        imgl=imgl.resize((100,100),Image.LANCZOS)
        self.photoimgl=ImageTk.PhotoImage(imgl)

        llbl=Label(self.root,image=self.photoimgl,bg="white",borderwidth=0)
        llbl.place(x=730,y=230,width=100,height=100)

        loginlbl=Label(frame,text="Admin Login",font=("times new roman",20,"bold"),fg="red",bg="white")
        loginlbl.place(x=90,y=100)

        userlbl=Label(frame,text="Username:",font=("times new roman",15,"bold"),fg="red",bg="white")
        userlbl.place(x=20,y=155)

        self.userentry=ttk.Entry(frame,textvariable=self.var_user,font=("times new roman",15,"bold"))
        self.userentry.place(x=120,y=155,width=200)

        passlbl=Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="red",bg="white")
        passlbl.place(x=20,y=220)

        self.passentry=ttk.Entry(frame,textvariable=self.var_pass,show="*",font=("times new roman",15,"bold"))
        self.passentry.place(x=120,y=220,width=200)

        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief="raised",fg="white",bg="orangered2",activeforeground="white",activebackground="orangered2")
        loginbtn.place(x=110,y=280,width=120,height=50)

    def login(self):
        if self.userentry.get()=="" or self.passentry.get()=="":
            messagebox.showerror("Error","All fields Required")
        conn=mysql.connector.connect(host="localhost",username="root",password="kinchit123",database="attendance_system")

        cur=conn.cursor()
        cur.execute("select * from admin where username=%s and password=%s",(
            self.var_user.get(),
            self.var_pass.get()
        ))
        row=cur.fetchone()
        if row==None:
           messagebox.showerror("Error","Username or Password Invalid")
           return
          
             
            
            
        else:
            self.new_window=Toplevel(self.root)
            self.app=admin_page(self.new_window)
          
        conn.commit()
        conn.close()
            

        


        


if __name__ == "__main__":
    root=tk.Tk()
    obj=login(root)
    root.mainloop()