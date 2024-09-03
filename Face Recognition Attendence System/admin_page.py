from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
from admin_student import student
from time import strftime
from datetime import datetime
import os
import cv2
import numpy as np
from tkinter import messagebox
from register import register


class admin_page:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendence System")
        self.root.iconbitmap(r"D:\D\Face Recognition Attendence System\Images\icon_atendance.ico")
        self.root.configure(bg='sky blue')

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
        # title_lbl1=Label(self.root,text="By Kinchit Raval",font=("times new roman",20,"bold"), bg="sky blue",fg="red")
        # title_lbl1.place(x=410,y=120,width=700,height=50)
       

        #Sarvajanik LOGO
        img1=Image.open(r"D:\D\Face Recognition Attendence System\Images\Sarvajanik_logo.png")
        img1=img1.resize((300,150),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=1220,y=10,width=300,height=150)

        #student manage
        img3=Image.open(r"D:\D\Face Recognition Attendence System\Images\Login.png")
        img3=img3.resize((220,220),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b1=Button(self.root,image=self.photoimg3,command=self.admin_student,cursor="hand2")
        b1.place(x=250,y=250,width=220,height=220)

        b1_l=Button(self.root,text="Student Management",command=self.admin_student,cursor="hand2",font=("times new roman",15,"bold"), bg="dark blue",fg="white")
        b1_l.place(x=240,y=470,width=230,height=40)

        #train data
        b2_l=Button(self.root,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",30,"bold"), bg="white",fg="black")
        b2_l.place(x=600,y=250,width=230,height=250)
        b3_l=Button(self.root,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"), bg="dark blue",fg="white")
        b3_l.place(x=600,y=470,width=230,height=40)
        

        #admin 
        img4=Image.open(r"D:\D\Face Recognition Attendence System\Images\add_admin.png")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b2=Button(self.root,image=self.photoimg4,command=self.admin_add,cursor="hand2")
        b2.place(x=940,y=250,width=220,height=220)

        b1_l=Button(self.root,text="Add Admin",command=self.admin_add,cursor="hand2",font=("times new roman",15,"bold"), bg="dark blue",fg="white")
        b1_l.place(x=940,y=470,width=230,height=40)

    #funtions
    def admin_student(self):
         self.new_window=Toplevel(self.root)
         self.app=student(self.new_window)
        # self.root.destroy()  # Destroy the current admin window
        # new_window = Tk()
        # self.app = student(new_window)

     #train data
    def train_data(self):
        data_dir=("data_samples")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #Grayscale Image
            imagenp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split(".")[1])

            faces.append(imagenp)
            ids.append(id)
            cv2.imshow("Training",imagenp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

    #for training classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("Trained_data.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training DataSet Completed!")
    #add admin
    def admin_add(self):
        self.new_window=Toplevel(self.root)
        self.app=register(self.new_window)


    


        




        


if __name__ == "__main__":
    root=Tk()
    obj=admin_page(root)
    root.mainloop()