from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
from tkinter import messagebox
import mysql.connector



class register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendence System")
        self.root.iconbitmap(r"D:\D\Face Recognition Attendence System\Images\icon_atendance.ico")
        self.root.configure(bg='sky blue')

        #------------------variables--------------------------
        self.var_fullname=StringVar()
        self.var_user=StringVar()
        self.var_email=StringVar()
        self.var_contact=StringVar()
        self.var_pass=StringVar()
        self.var_cpass=StringVar()
        

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
        frame.place(x=400,y=200,width=900,height=550)

        imgl=Image.open(r"D:\D\Face Recognition Attendence System\Images\login.png")
        imgl=imgl.resize((100,100),Image.LANCZOS)
        self.photoimgl=ImageTk.PhotoImage(imgl)

        llbl=Label(self.root,image=self.photoimgl,bg="white",borderwidth=0)
        llbl.place(x=800,y=210,width=100,height=100)

        loginlbl=Label(frame,text="Admin Registration",font=("times new roman",20,"bold"),fg="red",bg="white")
        loginlbl.place(x=330,y=100)

        #full name
        fnlbl=Label(frame,text="Full Name:",font=("times new roman",15,"bold"),fg="red",bg="white")
        fnlbl.place(x=80,y=155)

        self.fnentry=ttk.Entry(frame,textvariable=self.var_fullname,font=("times new roman",15,"bold"))
        self.fnentry.place(x=180,y=155,width=200)

        #username
        userlbl=Label(frame,text="Username:",font=("times new roman",15,"bold"),fg="red",bg="white")
        userlbl.place(x=450,y=155)

        self.userentry=ttk.Entry(frame,textvariable=self.var_user,font=("times new roman",15,"bold"))
        self.userentry.place(x=550,y=155,width=200)

        #email
        emaillbl=Label(frame,text="Email:",font=("times new roman",15,"bold"),fg="red",bg="white")
        emaillbl.place(x=80,y=220)

        self.emailentry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.emailentry.place(x=180,y=220,width=200)

        #conctact
        contactlbl=Label(frame,text="Contact:",font=("times new roman",15,"bold"),fg="red",bg="white")
        contactlbl.place(x=450,y=220)

        self.contactentry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.contactentry.place(x=550,y=220,width=200)

        #password
        passlbl=Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="red",bg="white")
        passlbl.place(x=80,y=285)

        self.passentry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.passentry.place(x=180,y=285,width=200)

        #cpassword
        cpasslbl=Label(frame,text="Confirm Password:",font=("times new roman",15,"bold"),fg="red",bg="white")
        cpasslbl.place(x=450,y=285)

        self.cpassentry=ttk.Entry(frame,textvariable=self.var_cpass,font=("times new roman",15,"bold"))
        self.cpassentry.place(x=620,y=285,width=200)

        loginbtn=Button(frame,command=self.register,text="Register",font=("times new roman",15,"bold"),bd=3,relief="raised",fg="white",bg="orangered2",activeforeground="white",activebackground="orangered2")
        loginbtn.place(x=360,y=350,width=120,height=40)

    def register(self):
        if self.var_fullname.get()=="" or self.var_user.get()=="" or self.var_email.get()=="" or self.var_contact.get()=="" or self.var_pass.get()=="" or self.var_cpass.get()=="":
            messagebox.showerror("Error","All Fields Required")
        elif self.var_pass.get()!=self.var_cpass.get():
            messagebox.showerror("Error","Password and confirm password must be same")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="kinchit123",database="attendance_system")

            cur=conn.cursor()
            cur.execute("insert into admin (admin_name,username,email,contact,password) values(%s,%s,%s,%s,%s)",(
                self.var_fullname.get(),
                self.var_user.get(),
                self.var_email.get(),
                self.var_contact.get(),
                self.var_pass.get()
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")
          
        


        


if __name__ == "__main__":
    root=Tk()
    obj=register(root)
    root.mainloop()