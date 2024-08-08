from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os 
import numpy as np
import mysql.connector
import cv2
import cv2.face
from tkinter import messagebox
import time
from time import strftime
from datetime import datetime
import csv
from win32com.client import Dispatch




class attendance:
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
        title_lbl1=Label(self.root,text="By Kinchit Raval",font=("times new roman",20,"bold"), bg="sky blue",fg="red")
        title_lbl1.place(x=410,y=120,width=700,height=50)

        #Sarvajanik LOGO
        img1=Image.open(r"D:\D\Face Recognition Attendence System\Images\Sarvajanik_logo.png")
        img1=img1.resize((300,150),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=1220,y=10,width=300,height=150)

        #Attendance button
        img3=Image.open(r"D:\D\Face Recognition Attendence System\Images\attendance.jpg")
        img3=img3.resize((220,220),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b1=Button(image=self.photoimg3,command=self.face_recognize,cursor="hand2")
        b1.place(x=250,y=250,width=220,height=220)

        b1_l=Button(text="For Attendance data click here",cursor="hand2",font=("times new roman",15,"bold"), bg="dark blue",fg="white")
        b1_l.place(x=250,y=470,width=220,height=40)

        #--------------------for attendance-----------------------------------
    def speak(self,str1):
        speak=Dispatch(("SAPI.SpVoice"))
        speak.Speak(str1)

    def mark_attendance(self,i,r,n,d):
        if i=="" and r=="" and n =="" and d=="":
            self.speak("Unknow face")
        else:
            now=datetime.now()
            d1=now.strftime("%d-%m-%Y")
            dtstring=now.strftime("%H:%M:%S")
            col_names=["Student ID","Roll No","Student Name","Department","Time","Date","Attendance"]
            attend=[i,r,n,d,str(dtstring),str(d1),"Present"]
            #messagebox.showinfo("Values",attend)
            self.speak("Thank You Attendance Taken")
            exist=os.path.isfile("Attendance/Attendance_"+d1+".csv")
            if exist:
                with open("Attendance/Attendance_"+d1+".csv","+a") as csvfile:
                    wr=csv.writer(csvfile)
                    wr.writerow(attend)
                csvfile.close()
                
            else:
                with open("Attendance/Attendance_"+d1+".csv","+a") as csvfile:
                    wr=csv.writer(csvfile)
                    wr.writerow(col_names)
                    wr.writerow(attend)
                csvfile.close()

        
       
            


       
        # with open("attendance.csv","r+",newline="\n") as f:
        #         mydatalist=f.readlines()
        #         name_list=[]
        #         for line in mydatalist:
        #             entry=line.split((","))
        #             name_list.append(entry[0])
        #         if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                   
        #             f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},Present")
        #             self.speak("Thank You Attendance Taken")
                    
                    

                


               

        #----------------------face recognition----------------------------------

    def face_recognize(self):
        self.s=""
        self.ro=""
        self.na=""
        self.dep=""
        def draw_boundary(img,classifier,scaleFactor,minNeighbor,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbor)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="kinchit123",database="attendance_system")
                #for name
                my_cursor=conn.cursor()
                my_cursor.execute("select student_name from student where Student_ID="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                #for roll number
                my_cursor=conn.cursor()
                my_cursor.execute("select roll_no from student where Student_ID="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                #for department
                my_cursor=conn.cursor()
                my_cursor.execute("select department from student where Student_ID="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                #for sid
                i=id
                
                
                


                if confidence>77:
                    cv2.putText(img,f"Student ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)
                    self.s=i
                    self.ro=r
                    self.na=n
                    self.dep=d
                    #self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)

                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCassade):
            coord=draw_boundary(img,faceCassade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCassade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("Trained_data.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCassade)
            cv2.imshow("Welcome,Press P for Attendance",img)

            k=cv2.waitKey(1)

            if k==ord("p"):
                self.mark_attendance(self.s,self.ro,self.na,self.dep)
                #messagebox.showinfo("Values",self.s)
            if k%256==27:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj=attendance(root)
    root.mainloop()
