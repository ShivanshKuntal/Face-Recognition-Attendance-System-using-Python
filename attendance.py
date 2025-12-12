# import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog

myData=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("VITBPL Student Face Attendance System")

        #===================variables==========================
        self.var_atten_regnum=StringVar() 
        self.var_atten_course=StringVar() 
        self.var_atten_name=StringVar() 
        self.var_atten_year=StringVar() 
        self.var_atten_slot=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
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
        f_lbl.place(x=0,y=128,width=1370,height=720)      
        
        
        
   


        # TITLE
        title_lbl=Label(self.root,text="VITBPL FACE ATTENDANCE PORTAL                         ",font=("times new roman",20,"bold"),bg="white",fg="dark blue")
        title_lbl.place(x=0,y=90,width=1530,height=45) 
        
        
        #========================Section Creating==================================

        # Creating Frame 
        main_frame = Frame(f_lbl,bd=2,bg="white") #bd mean border 
        main_frame.place(x=5,y=55,width=1355,height=510)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=660,height=480)
        
        left_inside_frame = Frame(left_frame,relief=RIDGE,bd=2,bg="white") #bd mean border 
        left_inside_frame.place(x=10,y=65,width=630,height=270)
        
         #Label Entry

        # registration number
        regnumLabel=Label(left_inside_frame,text="Registration Number :", font=("times new roman",12,"bold"),bg="white")
        regnumLabel.grid(row=0,column=0,padx=10,pady=7,sticky=W)
        
        atten_regnum=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_regnum,font=("times new roman",10,))
        atten_regnum.grid(row=0,column=1,padx=10,sticky=W)
        
        # student name
        nameLabel=Label(left_inside_frame,text="Student Name :", font=("times new roman",12,"bold"),bg="white")
        nameLabel.grid(row=0,column=2,padx=10,pady=7,sticky=W)
        
        atten_name=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=15,font=("times new roman",10,))
        atten_name.grid(row=0,column=3,padx=10,sticky=W)
        
        # student year
        yearLabel=Label(left_inside_frame,text="Year :", font=("times new roman",12,"bold"),bg="white")
        yearLabel.grid(row=1,column=0,padx=10,pady=7,sticky=W)
        
        atten_year=ttk.Entry(left_inside_frame,textvariable=self.var_atten_year,width=15,font=("times new roman",10,))
        atten_year.grid(row=1,column=1,padx=10,sticky=W)
        
        # student slot
        semLabel=Label(left_inside_frame,text="Slot :", font=("times new roman",12,"bold"),bg="white")
        semLabel.grid(row=1,column=2,padx=10,pady=7,sticky=W)
        
        atten_sem=ttk.Entry(left_inside_frame,textvariable=self.var_atten_slot,width=15,font=("times new roman",10,))
        atten_sem.grid(row=1,column=3,padx=10,sticky=W)
        
        # student time in
        timeLabel=Label(left_inside_frame,text="Time :", font=("times new roman",12,"bold"),bg="white")
        timeLabel.grid(row=2,column=0,padx=10,pady=7,sticky=W)
        
        atten_time=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=15,font=("times new roman",10,))
        atten_time.grid(row=2,column=1,padx=10,sticky=W)
        
        #student date of attendance

        dateLabel=Label(left_inside_frame,text=" Date :", font=("times new roman",12,"bold"),bg="white")
        dateLabel.grid(row=2,column=2,padx=10,pady=7,sticky=W)
        
        atten_date=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=15,font=("times new roman",10,))
        atten_date.grid(row=2,column=3,padx=10,sticky=W)
        
        #student's attendance status
        attendancelabel=Label(left_inside_frame,text="Attendance Status :", font=("times new roman",12,"bold"),bg="white")
        attendancelabel.grid(row=3,column=0,padx=10,pady=7,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman",10,),state="read only",width=12)
        self.atten_status['values']=("Select Status","Present","Absent","On-Duty")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        studentId_label=Label(left_inside_frame,text=" Course :", font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=3,column=2,padx=10,pady=7,sticky=W)
        
        studentid_entry=ttk.Entry(left_inside_frame,width=15,font=("times new roman",10,))
        studentid_entry.grid(row=3,column=3,padx=10,sticky=W)

        # buttons frame
        
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=25,y=190,width=575,height=31)
        
        save_btn=Button(btn_frame,text="Import CSV ",command=self.importCsv,width=17,font=("Source code pro",10,"bold"),bg="navy blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        Update_btn=Button(btn_frame,text="Export CSV ",command=self.exportCsv,width=17,font=("Source code pro",10,"bold"),bg="navy blue",fg="white")
        Update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Update ",command=self.update_data,width=17,font=("Source code pro",10,"bold"),bg="navy blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="RESET",command=self.reset_data,width=17,font=("Source code pro",10,"bold"),bg="navy blue",fg="white")
        reset_btn.grid(row=0,column=3)
  
         #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("Source code pro",12,"bold"),fg="navyblue")
        Right_frame.place(x=680,y=10,width=660,height=480)
        
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=15,y=15,width=623,height=405)
        
        
        #=====scroll bar table==================
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("regnum","name","year","slot","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("regnum",text="Registration Number")
        self.AttendanceReportTable.heading("name",text="Student Name")
        self.AttendanceReportTable.heading("year",text="Year")
        self.AttendanceReportTable.heading("slot",text="Slot")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance Status")
        
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("regnum",width=120)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("year",width=100)
        self.AttendanceReportTable.column("slot",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=115)
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


        back_btn = Button(self.root, text="←", command=self.close_window)
        back_btn.place(x=10, y=100) 


        
    def close_window(self):
        self.root.destroy()

#=============================fetch data=================================
    def fetchData(self,rows):
       
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #import csv button
    def importCsv(self):
        
        global myData
        myData.clear() #changes for double
        filename = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV file", "*.csv"), ("All Files", "*.*")),
            parent=self.root)
    
        if not filename:  # User clicked cancel or closed the dialog
            return
    
        try:
            with open(filename, 'r') as myFile:
                csvread = csv.reader(myFile)
                myData = list(csvread)
            self.fetchData(myData)
        except Exception as e:
            messagebox.showerror("Error", f"Error reading CSV file: {e}")



    def exportCsv(self):
        global myData
    
    # Check if there is data to export
        if not myData:
            messagebox.showerror("No data", "No data found to export", parent=self.root)
            return 
    
        try:
            filename = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save CSV",
                defaultextension=".csv",
                filetypes=(("CSV file", "*.csv"), ("All Files", "*.*")),
                parent=self.root)
        
            if not filename:  # User clicked cancel or closed the dialog
                return
        
            with open(filename, 'w', newline='') as myFile:
                csvwriter = csv.writer(myFile,delimiter=",")
                csvwriter.writerows(myData)
                

        
            messagebox.showinfo("Success", "CSV file has been exported successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error exporting CSV file: {e}")

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_atten_regnum.set(rows[0])  
        self.var_atten_name.set(rows[1])  
        self.var_atten_year.set(rows[2])  
        self.var_atten_slot.set(rows[3])  
        self.var_atten_time.set(rows[4])  
        self.var_atten_date.set(rows[5])  
        self.var_atten_attendance.set(rows[6])  

    def reset_data(self):
        self.var_atten_regnum.set("")  
        self.var_atten_name.set("")  
        self.var_atten_year.set("")  
        self.var_atten_slot.set("")  
        self.var_atten_time.set("")  
        self.var_atten_date.set("")  
        self.var_atten_attendance.set("") 
        
    def update_data(self):
        selected_item = self.AttendanceReportTable.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a record to update", parent=self.root)
            return
    
    # Get the index of the selected item
        index = self.AttendanceReportTable.index(selected_item)
    
    # Get the values from the entry fields
        updated_data = [
            self.var_atten_regnum.get(),
            self.var_atten_name.get(),
            self.var_atten_year.get(),
            self.var_atten_slot.get(),
            self.var_atten_time.get(),
            self.var_atten_date.get(),
            self.var_atten_attendance.get()
        ]
    
    # Update myData with the updated values
        myData[index] = updated_data
    
    # Refresh the Treeview
        self.fetchData(myData)
    
        messagebox.showinfo("Success", "Record updated successfully!")



        
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()  