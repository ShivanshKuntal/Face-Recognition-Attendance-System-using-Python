from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("VTOP Face Attendance System")
        
        # ==========variables============
        
        self.var_school=StringVar()
        self.var_course=StringVar() 
        self.var_year=StringVar() 
        self.var_semester=StringVar() 
        self.var_regnum=StringVar() 
        self.var_name=StringVar() 
        self.var_gender=StringVar() 
        self.var_dob=StringVar() 
        self.var_emailid=StringVar() 
        self.var_phonenum=StringVar() 
        self.var_address=StringVar() 
        self.var_facultyname=StringVar() 
        
        
        
        
        
        #blue bar pic in header
        img=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\face_recognition_system\face_recognition system\college_images\collegepic.jpg")
        img=img.resize((1370,190),Image.ADAPTIVE)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1370,height=90)
        #logo image
        img1=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\face_recognition_system\face_recognition system\college_images\logo.jpg")
        img1=img1.resize((155,90),Image.ADAPTIVE)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=155,height=90)
        
        #bg image
        img2=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\face_recognition_system\face_recognition system\college_images\bg.jpg")
        img2=img2.resize((1530,710),Image.ADAPTIVE)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0,y=90,width=1530,height=610)
        #title i am hiding it for now as i have text on image only
        title_lbl=Label(f_lbl,text="STUDENT MANAGEMENT SYSTEM                              ",font=("times new roman",20,"bold"),bg="white",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=0,y=40,width=1500,height=650)
        
        #left label frame
        
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("time new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=545)
         
        #current course
        
        Current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("time new roman",12,"bold"),fg="dark blue")
        Current_course_frame.place(x=5,y=10,width=640,height=115)
        # School
        school_label=Label(Current_course_frame,text="School :", font=("times new roman",12,"bold"),bg="white")
        school_label.grid(row=0,column=0,padx=10,pady=0,sticky=W)
        
        school_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_school,font=("times new roman",10,),state="read only")
        school_combo['values']=("Select School","SASL","SCSE","SEEE")
        school_combo.current(0)
        school_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        #Course
        course_label=Label(Current_course_frame,text="Course :", font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,pady=0,sticky=W)
        
        course_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_course,font=("times new roman",10,),state="read only")
        course_combo['values']=("Select Course","B.Tech Aerospace Engineering","B.Tech Bioengineering","B.Tech Computer Science & Engineering","B.Tech CSE(Artificial Intelligence & Machine Learning)","B.Tech CSE(Cyber Security & Digital Forensics)","B.Tech CSE(Cloud Computing & Automation)","B.Tech CSE (E-Commerce Technology)","B.Tech CSE (Education Technology)","B.Tech CSE(Gaming Technology)","B.Tech CSE(Health Informatics)","B.Tech Electronics & Communication Engineering","B.Tech ECE(Artificial Intelligence & Cybernetics)","B.Tech Mechanical Engineering","B.Tech Mechanical Engineering (Artificial Intelligence & Robotics)","BBA (Bachelor of Business Administration)","B.Arch","M.Tech Artificial Intelligence","M.Tech CSE(Cyber Security )","M.Tech CSE(Computational and Data Science)","M.Sc. Biotechnology","M.Tech Computer Science & Engineering (Cyber Security & Digital Forensics )","M.Tech Artificial Intelligence  & Data Science","M.Tech VLSI Design","MBA (Master of Business Administration)","MCA (Master of Computer Applications)","Ph.D Programmes")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=5,pady=10,sticky=W)
        #Year of Student
        year_label=Label(Current_course_frame,text="Year :", font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,pady=0,sticky=W)
        
        year_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_year,font=("times new roman",10,),state="read only")
        year_combo['values']=("Select Year","1","2","3","4")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        #Semester
        semester_label=Label(Current_course_frame,text="Semester :", font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,pady=0,sticky=W)
        
        semester_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_semester,font=("times new roman",10,),state="read only")
        semester_combo['values']=("Select Semester","Winter Semester 2023-24","Interim Semester 2023-24","Fall Semester 2023-24","Summer Semester 2022-2023","Winter Semester 2022-23")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        
        
        #Class Student Information 
        
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("time new roman",12,"bold"),fg="dark blue")
        class_student_frame.place(x=5,y=130,width=640,height=315)
        
        #Student ID ( REG NUM )
        studentId_label=Label(class_student_frame,text="VTOP ID :", font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=7,sticky=W)
        
        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_regnum,width=15,font=("times new roman",10,))
        studentid_entry.grid(row=0,column=1,padx=10,sticky=W)
        
        #Student Name
        studentId_label=Label(class_student_frame,text="Student Name :", font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=2,padx=10,pady=7,sticky=W)
        
        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=15,font=("times new roman",10,))
        studentid_entry.grid(row=0,column=3,padx=10,sticky=W)
        
        #Gender
        studentId_label=Label(class_student_frame,text="Gender :", font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=1,column=0,padx=10,pady=7,sticky=W)
        
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",10,),state="read only",width=12)
        gender_combo['values']=("Select Gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        

        #right label frame
        
        #Date Of Birth
        studentId_label=Label(class_student_frame,text="Date of Birth :", font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=1,column=2,padx=10,pady=7,sticky=W)
        
        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=15,font=("times new roman",10,))
        studentid_entry.grid(row=1,column=3,padx=10,sticky=W)
        
        #Email ID
        studentId_label=Label(class_student_frame,text="Email ID :", font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=2,column=0,padx=10,pady=7,sticky=W)
        
        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_emailid,width=15,font=("times new roman",10,))
        studentid_entry.grid(row=2,column=1,padx=10,sticky=W)
        
        #Phone Number
        studentId_label=Label(class_student_frame,text="Phone Number :", font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=2,column=2,padx=10,pady=7,sticky=W)
        
        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_phonenum,width=15,font=("times new roman",10,))
        studentid_entry.grid(row=2,column=3,padx=10,sticky=W)
         
        #Address
        studentId_label=Label(class_student_frame,text="Address :", font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=3,column=0,padx=10,pady=7,sticky=W)
        
        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=15,font=("times new roman",10,))
        studentid_entry.grid(row=3,column=1,padx=10,sticky=W)
        
        
        #Faculty Name
        studentId_label=Label(class_student_frame,text="Registration Number :", font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=3,column=2,padx=10,pady=7,sticky=W)
        
        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_facultyname,width=15,font=("times new roman",10,))
        studentid_entry.grid(row=3,column=3,padx=10,sticky=W)
        
        # radio Buttons
        
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes",)
        radiobtn1.grid(row=4,column=0,)
        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Hide Photo Sample",value="No",)
        radiobtn2.grid(row=4,column=1)
        
        # buttons frame
        
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=25,y=190,width=575,height=31)
        
        save_btn=Button(btn_frame,text="Save Data",command=self.add_data,width=17,font=("Source code pro",10,"bold"),bg="navy blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        Update_btn=Button(btn_frame,text="Update Data",command=self.update_data,width=17,font=("Source code pro",10,"bold"),bg="navy blue",fg="white")
        Update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete Data",command=self.delete_data,width=17,font=("Source code pro",10,"bold"),bg="navy blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="RESET",command=self.reset_data,width=17,font=("Source code pro",10,"bold"),bg="navy blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=25,y=220,width=575,height=31)
        
        take_photo_btn=Button(btn_frame1,text="Take Photo Of the Student",command=self.generate_dataset,width=35,font=("Source code pro",10,"bold"),bg="navy blue",fg="white")
        take_photo_btn.grid(row=0,column=0)
      
        update_photo_btn=Button(btn_frame1,text="Update Photo of the Student",width=35,font=("Source code pro",10,"bold"),bg="navy blue",fg="white")
        update_photo_btn.grid(row=0,column=1)
        
        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Source code pro",12,"bold"))
        Right_frame.place(x=680,y=10,width=660,height=545)
        
        #---------------view student details and search system---------------------
        
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("time new roman",12,"bold"),fg="dark blue")
        search_frame.place(x=5,y=10,width=640,height=75)
        
        search_lbl=Label(search_frame,text="Search By: ",font=("times new roman",12,"bold"),bg="navy blue",fg="white")
        search_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",10,),state="read only")
        search_combo['values']=("Select","School","Course","Year","Semester","Registration Number","Name","Gender","Faculty Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=0,pady=0,sticky=W) 
        
        searchkaro_entry=ttk.Entry(search_frame,width=20,font=("times new roman",10,))
        searchkaro_entry.grid(row=0,column=3,padx=10,pady=0,sticky=W)

        search_btn=Button(search_frame,text="Search Data",width=12,font=("Source code pro",10,"bold"),bg="navy blue",fg="white")
        search_btn.grid(row=0,column=4,padx=3)
        
        showall_btn=Button(search_frame,text="Show All",width=12,font=("Source code pro",10,"bold"),bg="navy blue",fg="white")
        showall_btn.grid(row=0,column=5,padx=3)
        # ========table frame===========
        
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE,)
        table_frame.place(x=5,y=95,width=640,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("Registration Number","Student Name","Gender","Date of Birth","EmailID","Phone Number","Address","Faculty Name","Place","Sample","Sample1","Sample2","Sample3"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("Registration Number",text="School")
        self.student_table.heading("Student Name",text="Course")
        self.student_table.heading("Gender",text="Year")
        self.student_table.heading("Date of Birth",text="Semester")
        self.student_table.heading("EmailID",text="VTOP ID")
        self.student_table.heading("Phone Number",text="Student Name")
        self.student_table.heading("Address",text="Gender")
        self.student_table.heading("Faculty Name",text="Date of Birth")
        self.student_table.heading("Place",text="Email ID")
        self.student_table.heading("Sample",text="Mobile Number")
        self.student_table.heading("Sample1",text="Address")
        self.student_table.heading("Sample2",text="Registration Number")
        self.student_table.heading("Sample3",text="Photo Available")
        self.student_table["show"]="headings"
        
        self.student_table.column("Registration Number",width="120")
        self.student_table.column("Student Name",width="120")
        self.student_table.column("Gender",width="120")
        self.student_table.column("Date of Birth",width="120")
        self.student_table.column("EmailID",width="120")
        self.student_table.column("Phone Number",width="120")
        self.student_table.column("Address",width="120")
        self.student_table.column("Faculty Name",width="120")
        self.student_table.column("Place",width="120")
        self.student_table.column("Sample",width="120")
        self.student_table.column("Sample1",width="120")
        self.student_table.column("Sample2",width="120")
        self.student_table.column("Sample3",width="120")
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        
        back_btn = Button(self.root, text="←", command=self.close_window)
        back_btn.place(x=10, y=100) 

    def close_window(self):
        self.root.destroy()
        
        
    # ===========all fields are required error message=======
    def add_data(self):
        if self.var_school.get()=="Select School" or self.var_name.get()=="" or self.var_regnum.get()=="" or self.var_address.get()=="" or self.var_course.get()=="" or self.var_dob.get()=="" or self.var_emailid.get()=="":
                messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                 conn=mysql.connector.connect(host='localhost',user='root',password='amnesia',database='face_recognizer')
                 my_cursor=conn.cursor()
                 my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_school.get( ),
                                                                                                        self.var_course.get( ),
                                                                                                        self.var_year.get( ),
                                                                                                        self.var_semester.get( ),
                                                                                                        self.var_regnum.get( ),
                                                                                                        self.var_name.get( ),
                                                                                                        self.var_gender.get( ),
                                                                                                        self.var_dob.get( ),
                                                                                                        self.var_emailid.get( ),
                                                                                                        self.var_phonenum.get( ),
                                                                                                        self.var_address.get( ),
                                                                                                        self.var_facultyname.get( ),
                                                                                                        self.var_radio1.get()
                                      
                                                                       ))
        
        
                 conn.commit()
                 self.fetch_data()
                 conn.close()
                 messagebox.showinfo("Success","Student Details has been added",parent=self.root)
            except Exception as es:
                 messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)

    # ============fetch data==========================
    def fetch_data(self):
         conn=mysql.connector.connect(host='localhost',user='root',password='amnesia',database='face_recognizer')
         my_cursor=conn.cursor()
         my_cursor.execute("select * from student")
         data=my_cursor.fetchall()
         
         if len(data)!=0:
             self.student_table.delete(*self.student_table.get_children())
             for i in data:
                 self.student_table.insert("",END,values=i)
             conn.commit()
         conn.close()
         
         
        #  =======get cursor=============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_school.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_regnum.set(data[4]),
        self.var_name.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_dob.set(data[7]),
        self.var_emailid.set(data[8]),
        self.var_phonenum.set(data[9]),
        self.var_address.set(data[10]),
        self.var_facultyname.set(data[11]),
        self.var_radio1.set(data[12])
        
        
        
        #============update function================
        
    def update_data(self):
            if self.var_school.get()=="Select School" or self.var_name.get()=="" or self.var_regnum.get()=="" or self.var_address.get()=="" or self.var_course.get()=="" or self.var_dob.get()=="" or self.var_emailid.get()=="":
                messagebox.showerror("Error","All Fields are Required",parent=self.root)
            else:
                try:
                    update=messagebox.askyesnocancel("Update","Do you want to Update Student Details?",parent=self.root)
                    if update>0:
                        conn=mysql.connector.connect(host='localhost',user='root',password='amnesia',database='face_recognizer')
                        my_cursor=conn.cursor()
                        my_cursor.execute("update student set school=%s,course=%s,year=%s,semester=%s,name=%s,gender=%s,dob=%s,emailid=%s,phonenum=%s,address=%s,facultyname=%s,photosample=%s where regnum=%s",(
                            
                                                                                                                                                                                                  self.var_school.get( ),
                                                                                                                                                                                                  self.var_course.get( ),
                                                                                                                                                                                                  self.var_year.get( ),
                                                                                                                                                                                                  self.var_semester.get( ),
                                                                                                                                                                                                  self.var_name.get( ),
                                                                                                                                                                                                  self.var_gender.get( ),
                                                                                                                                                                                                  self.var_dob.get( ),
                                                                                                                                                                                                  self.var_emailid.get( ),
                                                                                                                                                                                                  self.var_phonenum.get( ),
                                                                                                                                                                                                  self.var_address.get( ),
                                                                                                                                                                                                  self.var_facultyname.get( ),
                                                                                                                                                                                                  self.var_radio1.get(),
                                                                                                                                                                                                  self.var_regnum.get( )
                            
                                                                                                                                                                                                                                ))
                        
                    else:
                      if not update:
                         return
                    messagebox.showinfo("Success","Student Details Successfully Updated",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()        
                except Exception as es:
                    messagebox.showerror("Error",f"Student Details was Failed!:{str(es)}",parent=self.root)   
            
        
    # ============================Delete Function==========================================
    
    def delete_data(self):
        if self.var_regnum.get()=="":
            messagebox.showerror("Error","Student VIT Registration Number is Required",parent=self.root)
        else: 
            try:
                delete=messagebox.askyesnocancel("Student Delete Option","Do You Want to Delete Student Record?",parent=self.root)
                if delete>0:
                        conn=mysql.connector.connect(host='localhost',user='root',password='amnesia',database='face_recognizer')
                        my_cursor=conn.cursor()
                        sql="delete from student where regnum=%s"
                        val=(self.var_regnum.get(),)
                        my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Deleted","Successfully Deleted Student Records",parent=self.root)
            except Exception as es:
                    messagebox.showerror("Error",f"Student Details Deletion was Failed!:{str(es)}",parent=self.root)
                
    # ========reset function================
    
    def reset_data(self):
        self.var_school.set("Select School"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_regnum.set(""),
        self.var_name.set(""),
        self.var_gender.set("Select Your Gender"),
        self.var_dob.set(""),
        self.var_emailid.set(""),
        self.var_phonenum.set(""),
        self.var_address.set(""),
        self.var_facultyname.set(""),
        self.var_radio1.set("Select Photo ")
    
    
    # ========Generate Data Set Take Photo Samples==========
    
    def generate_dataset(self):
        if self.var_school.get()=="Select School" or self.var_name.get()=="" or self.var_regnum.get()=="" or self.var_address.get()=="" or self.var_course.get()=="" or self.var_dob.get()=="" or self.var_emailid.get()=="":
                messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='amnesia',database='face_recognizer')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set school=%s,course=%s,year=%s,semester=%s,name=%s,gender=%s,dob=%s,emailid=%s,phonenum=%s,address=%s,facultyname=%s,photosample=%s where regnum=%s",(
                            
                                                                                                                                                                                                  self.var_school.get( ),
                                                                                                                                                                                                  self.var_course.get( ),
                                                                                                                                                                                                  self.var_year.get( ),
                                                                                                                                                                                                  self.var_semester.get( ),
                                                                                                                                                                                                  self.var_name.get( ),
                                                                                                                                                                                                  self.var_gender.get( ),
                                                                                                                                                                                                  self.var_dob.get( ),
                                                                                                                                                                                                  self.var_emailid.get( ),
                                                                                                                                                                                                  self.var_phonenum.get( ),
                                                                                                                                                                                                  self.var_address.get( ),
                                                                                                                                                                                                  self.var_facultyname.get( ),
                                                                                                                                                                                                  self.var_radio1.get(),
                                                                                                                                                                                                  self.var_regnum.get( )==id+1
                                                                                                                                                                                                ))
                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                
                # =========load predefined data on face frontals from opencv======
                
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor = 1.3 ( default hota hai)
                    #minimum Neighbour=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap =cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,myframe=cap.read()
                    if face_cropped(myframe) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(myframe),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="face_recognition system/data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Student Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Datasets Completed Successfully!")
             
            except Exception as es:
                messagebox.showerror("Error",f"Couldn't Update Student's Photo!{str(es)}",parent=self.root)
               
        




              
        
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()        
        # ========================function declaration========
        
            