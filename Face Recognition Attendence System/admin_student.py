from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from tkcalendar import Calendar
import cv2
from time import strftime
from datetime import datetime
import os 
import numpy as np




class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendence System")
        self.root.iconbitmap(r"D:\D\Face Recognition Attendence System\Images\icon_atendance.ico")
        self.root.configure(bg='sky blue')

        #------------------------------variables----------------------------
        self.sname=StringVar()
        self.div=StringVar()
        self.roll=StringVar()        
        self.gen=StringVar()        
        self.dob=StringVar()        
        self.email=StringVar()        
        self.mobile=StringVar()        
        self.address=StringVar()        
        self.city=StringVar()
        self.dep=StringVar()
        self.single_drop=StringVar()
        self.single_data=StringVar()



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
        
        lbl = Label(self.root,font=("times new roman",14,"bold"),background="sky blue",foreground="red")
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

        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=15,y=170,width=1500,height=600)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Registration",font=("times new roman",12,"bold"))
        left_frame.place(x=7.5,y=10,width=720,height=580)

        #student course frame
        course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Course",font=("times new roman",12,"bold"))
        course_frame.place(x=5,y=5,width=700,height=60)
        
        #department_column
        dep_label=Label(course_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=2)

        dep_combo=ttk.Combobox(course_frame,textvariable=self.dep,font=("times new roman",12,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select Department","Computer Science","Microbiology","Biotechnology","Environmental Science","Chemistry","Admin")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

         #student Details frame
        sdetail_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        sdetail_frame.place(x=5,y=70,width=700,height=480)
        #sdetail_frame.place(x=5,y=160,width=700,height=390)

         #StudentName
        studID_label=Label(sdetail_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studID_label.grid(row=0,column=0,padx=2,pady=20)

        studname_entry=Entry(sdetail_frame,textvariable=self.sname,width=20,font=("times new roman",12,"bold"))
        studname_entry.grid(row=0,column=1,padx=20)

         #Class Division
        division_label=Label(sdetail_frame,text="Division:",font=("times new roman",12,"bold"),bg="white")
        division_label.grid(row=0,column=2,padx=2,pady=20)

        division_entry=Entry(sdetail_frame,textvariable=self.div,width=20,font=("times new roman",12,"bold"))
        division_entry.grid(row=0,column=3,padx=20)

         #Roll Number
        roll_label=Label(sdetail_frame,text="Roll Number:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=1,column=0,padx=2,pady=20)

        roll_entry=Entry(sdetail_frame,textvariable=self.roll,width=20,font=("times new roman",12,"bold"))
        roll_entry.grid(row=1,column=1,padx=10,pady=20)

         #Gender
        gender_label=Label(sdetail_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=1,column=2,padx=2,pady=20)

        gen_combo=ttk.Combobox(sdetail_frame,textvariable=self.gen,font=("times new roman",12,"bold"),width=17,state="read only")
        gen_combo["values"]=("Select Gender","Male","Female")
        gen_combo.current(0)
        gen_combo.grid(row=1,column=3,padx=20)

        #DOB

        def pick_date(event):
            global cal, date_window
            date_window=Toplevel()
            date_window.grab_set()
            date_window.title("Choose Date of Birth")
            date_window.geometry("250x220+590+370")
            cal= Calendar(date_window, selectmode="day", date_pattern="dd/mm/yyyy")
            cal.place(x=0, y=0)

            submit_btn=Button(date_window,text="Submit", command=grab_date)
            submit_btn.place(x=80,y=190)
        def grab_date():
            dob_entry.delete(0, END)
            dob_entry.insert(0, cal.get_date())
            date_window.destroy()

        dob_label=Label(sdetail_frame,text="Date of Birth:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=0,padx=2,pady=20)

        dob_entry=Entry(sdetail_frame,textvariable=self.dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=1,padx=20)
        dob_entry.bind("<1>", pick_date)

        #Email
        email_label=Label(sdetail_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=2,column=2,padx=2,pady=20)

        email_entry=Entry(sdetail_frame,textvariable=self.email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=2,column=3,padx=20)

        #Mobile
        mobile_label=Label(sdetail_frame,text="Mobile Number:",font=("times new roman",12,"bold"),bg="white")
        mobile_label.grid(row=3,column=0,padx=2,pady=20)

        mobile_entry=Entry(sdetail_frame,textvariable=self.mobile,width=20,font=("times new roman",12,"bold"))
        mobile_entry.grid(row=3,column=1,padx=20)

        #Address
        address_label=Label(sdetail_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=3,column=2,padx=2,pady=20)

        address_entry=Entry(sdetail_frame,textvariable=self.address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=3,column=3,padx=10,pady=20)

        #City
        city_label=Label(sdetail_frame,text="City:",font=("times new roman",12,"bold"),bg="white")
        city_label.grid(row=4,column=0,padx=2,pady=20)

        city_entry=Entry(sdetail_frame,textvariable=self.city,width=20,font=("times new roman",12,"bold"))
        city_entry.grid(row=4,column=1,padx=10,pady=20)

        #radio buttons
        self.var_radio_1=StringVar()
        radio1=ttk.Radiobutton(sdetail_frame,variable=self.var_radio_1,text="Take Photo Sample",value="Yes")
        radio1.grid(row=4,column=2,padx=10,pady=20)
        radio2=ttk.Radiobutton(sdetail_frame,variable=self.var_radio_1,text="No Photo Sample",value="No")
        radio2.grid(row=4,column=3,padx=10,pady=20)

        #Buttons Frame
        btn_frame=Frame(sdetail_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=2,y=340,width=690,height=40)

        save_btn=Button(btn_frame,text="SAVE",command=self.add_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="UPDATE",command=self.update_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="DELETE",command=self.delete_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="RESET",command=self.reset_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

         #Buttons Frame 2
        btn_frame=Frame(sdetail_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=2,y=380,width=690,height=70)

        take_photo_btn=Button(btn_frame,command=self.getphoto,text="TAKE PHOTO SAMPLE",width=37,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame,text="UPDATE PHOTO SAMPLE",width=37,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)

        
        

        #Right label frame 
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=740,height=580)

        #Search System
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Class Information",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=10,width=720,height=380)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=10)

        search_combo=ttk.Combobox(search_frame,textvariable=self.single_drop,font=("times new roman",12,"bold"),width=17,state="read only")
        search_combo["values"]=("Select value","Roll Number","StudentID")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10)

        search_entry=Entry(search_frame,textvariable=self.single_data,width=18,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10)



        search_btn=Button(search_frame,text="Search",command=self.fetch_data_one,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        show_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        show_btn.grid(row=0,column=4,padx=4)

        #table to show data
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=80,width=710,height=450)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("sid","sname","div","roll","gen","dob","email","mob","address","city","photo","dep"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("sid",text="Student ID")
        self.student_table.heading("sname",text="Student Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll Number")
        self.student_table.heading("gen",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("mob",text="Mobile")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("city",text="City")
        self.student_table.heading("photo",text="Photo Sample")
        self.student_table.heading("dep",text="Department")
        self.student_table["show"]="headings"

        self.student_table.column("sid",width=100)
        self.student_table.column("sname",width=130)
        self.student_table.column("div",width=60)
        self.student_table.column("roll",width=100)
        self.student_table.column("gen",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("mob",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("city",width=100)
        self.student_table.column("photo",width=100)
        self.student_table.column("dep",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_data)
        self.fetch_data()

    #functions
    def add_data(self):
        if self.sname.get()=="" or self.div.get()=="" or self.roll.get()=="" or self.gen.get()=="Select Gender" or self.dob.get()=="" or self.email.get()=="" or self.mobile.get()=="" or self.address.get()=="" or self.city.get()=="" or self.dep.get()=="Select Departement":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            #messagebox.showinfo("Success","Registration Sucessfull",parent=self.root)
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="kinchit123",database="attendance_system")
                
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student (student_name,division,roll_no,gender,dob,email,mobile,address,city,photo,department) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.sname.get(),
                                                                                                        self.div.get(),
                                                                                                        self.roll.get(),
                                                                                                        self.gen.get(),
                                                                                                        self.dob.get(),
                                                                                                        self.email.get(),
                                                                                                        self.mobile.get(),
                                                                                                        self.address.get(),
                                                                                                        self.city.get(),
                                                                                                        self.var_radio_1.get(),
                                                                                                        self.dep.get()

                                                                                               
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Registered!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #Fetch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="kinchit123",database="attendance_system")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        self.single_drop.set("Select value")
        self.single_data.set("")

    #Get values for editing
    def get_data(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.dep.set(data[11])
        self.sname.set(data[1])
        self.div.set(data[2])
        self.roll.set(data[3])
        self.gen.set(data[4])
        self.dob.set(data[5])
        self.email.set(data[6])
        self.mobile.set(data[7])
        self.address.set(data[8])
        self.city.set(data[9])
        self.var_radio_1.set(data[10])

    #update function
    def update_data(self):
        if self.sname.get()=="" or self.div.get()=="" or self.roll.get()=="" or self.gen.get()=="Select Gender" or self.dob.get()=="" or self.email.get()=="" or self.mobile.get()=="" or self.address.get()=="" or self.city.get()=="" or self.dep.get()=="Select Departement":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this details",parent=self.root)
                if update>0:
                   self.sid=StringVar()
                   cursor_focus=self.student_table.focus()
                   content=self.student_table.item(cursor_focus)
                   data=content["values"]
                   self.sid.set(data[0])


                   conn=mysql.connector.connect(host="localhost",username="root",password="kinchit123",database="attendance_system")
                   my_cursor=conn.cursor()
                   my_cursor.execute("update student set student_name=%s,division=%s,roll_no=%s,gender=%s,dob=%s,email=%s,mobile=%s,address=%s,city=%s,photo=%s,department=%s where Student_ID=%s",(
                                                                                                                                        
                                                                                                        self.sname.get(),
                                                                                                        self.div.get(),
                                                                                                        self.roll.get(),
                                                                                                        self.gen.get(),
                                                                                                        self.dob.get(),
                                                                                                        self.email.get(),
                                                                                                        self.mobile.get(),
                                                                                                        self.address.get(),
                                                                                                        self.city.get(),
                                                                                                        self.var_radio_1.get(),
                                                                                                        self.dep.get(),
                                                                                                        self.sid.get()

                        
                                                                                                                                        ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student Details Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    
    #delete function
    def delete_data(self):
        if self.sname.get()=="" or self.div.get()=="" or self.roll.get()=="" or self.gen.get()=="Select Gender" or self.dob.get()=="" or self.email.get()=="" or self.mobile.get()=="" or self.address.get()=="" or self.city.get()=="" or self.dep.get()=="Select Departement":
            messagebox.showerror("Error","Select Data First",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Are you sure you want to delete the data?",parent=self.root)
                if delete>0:
                    self.sid=StringVar()
                    cursor_focus=self.student_table.focus()
                    content=self.student_table.item(cursor_focus)
                    data=content["values"]
                    self.sid.set(data[0])
                    conn=mysql.connector.connect(host="localhost",username="root",password="kinchit123",database="attendance_system")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_ID=%s"
                    val=(self.sid.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Succesfully Deleted Data!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)           

    #reset
    def reset_data(self):
        self.dep.set("Select Department")
        self.sname.set("")
        self.div.set("")
        self.roll.set("")
        self.gen.set("Select Gender")
        self.dob.set("")
        self.email.set("")
        self.mobile.set("")
        self.address.set("")
        self.city.set("")
        self.var_radio_1.set("")
    
    #Fetch Data single data
    def fetch_data_one(self):
        dropdown=self.single_drop.get()
        #value = self.single_data.get()
        if(dropdown=="Roll Number"):
             conn=mysql.connector.connect(host="localhost",username="root",password="kinchit123",database="attendance_system")
             my_cursor=conn.cursor()
             sql = "Select * from student where roll_no=%s"
             value=(self.single_data.get(),)
             my_cursor.execute(sql,value)
             data=my_cursor.fetchall()
             self.student_table.delete(*self.student_table.get_children())
             if len(data)!=0:
                for i in data:
                    self.student_table.insert("",END,values=i)
             else:
                 self.student_table.insert("", END, values=("","","","No Record Found"))
             conn.commit()
             conn.close()
        elif(dropdown=="StudentID"):
            conn=mysql.connector.connect(host="localhost",username="root",password="kinchit123",database="attendance_system")
            my_cursor=conn.cursor()
            sql = "Select * from student where Student_ID=%s"
            value=(self.single_data.get(),)
            my_cursor.execute(sql,value)
            data=my_cursor.fetchall()
            self.student_table.delete(*self.student_table.get_children())
            if len(data)!=0:
                for i in data:
                    self.student_table.insert("",END,values=i)
            else:
                self.student_table.insert("", END, values=("","","","No Record Found"))
            conn.commit()
            conn.close()
        elif(dropdown=="Select value"):
            messagebox.showerror("Error","Select Data First",parent=self.root)

    #for add admin page
    # def register_page(self):
    #     self.root.destroy()
    #     face_root = tk.Tk()
    #     app = register(face_root)

   
        




        

       

    #---------------------- to get photo data set----------------------------
    def getphoto(self):
        if self.sname.get()=="" or self.div.get()=="" or self.roll.get()=="" or self.gen.get()=="Select Gender" or self.dob.get()=="" or self.email.get()=="" or self.mobile.get()=="" or self.address.get()=="" or self.city.get()=="" or self.dep.get()=="Select Departement":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                self.sid=StringVar()
                cursor_focus=self.student_table.focus()
                content=self.student_table.item(cursor_focus)
                data=content["values"]
                self.sid.set(data[0])
                conn=mysql.connector.connect(host="localhost",username="root",password="kinchit123",database="attendance_system")
                my_cursor=conn.cursor()
                id=self.sid.get()
                    
                my_cursor.execute("update student set student_name=%s,division=%s,roll_no=%s,gender=%s,dob=%s,email=%s,mobile=%s,address=%s,city=%s,photo=%s,department=%s where Student_ID=%s",(
                                                                                                                                        
                                                                                                        self.sname.get(),
                                                                                                        self.div.get(),
                                                                                                        self.roll.get(),
                                                                                                        self.gen.get(),
                                                                                                        self.dob.get(),
                                                                                                        self.email.get(),
                                                                                                        self.mobile.get(),
                                                                                                        self.address.get(),
                                                                                                        self.city.get(),
                                                                                                        self.var_radio_1.get(),
                                                                                                        self.dep.get(),
                                                                                                        self.sid.get()

                        
                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #------- algortihmn for frontal face detection-------

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_crop(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #minimum neighbor=5

                    for (x,y,w,h) in faces:
                        face_crop=img[y:y+h,x:x+w]
                        return face_crop

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_crop(my_frame) is not None:
                        img_id+=1
                        
                        face=cv2.resize(face_crop(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data_samples/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Data Set Succesfully Generated",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root) 


         
   
  
            


   
        


                 
        








if __name__ == "__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()