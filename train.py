from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("VTOP Student Face Dataset Training Portal")
        
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
        
        
        # TITLE
        title_lbl=Label(self.root,text="VTOP FACE DATA TRAINING PORTAL                          ",font=("times new roman",20,"bold"),bg="white",fg="dark blue")
        title_lbl.place(x=0,y=130,width=1530,height=45) 
        
        #Centre label frame
        
        main_frame=Frame(f_lbl,bd=4,bg="white")
        main_frame.place(x=100,y=90,width=1500,height=650)
        
        center_frame=LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,font=("time new roman",12,"bold"),fg="Navy blue")
        center_frame.place(x=140,y=30,width=900,height=345)
        

        
        
        # text inside the guidlines
    
        center_label=Label(center_frame,text="DIRECTIVE: OBSERVE GUIDELINES", font=("times new roman",16,"bold"),bg="white",fg="RED")
        center_label.grid(row=0,column=0,padx=280,pady=0,sticky=W)

        center_label=Label(center_frame,text="STEP: 1", font=("times new roman",12,"bold"),bg="white",fg="DARK Green")
        center_label.grid(row=1,column=0,padx=20,pady=9,sticky=W)
        center_label=Label(center_frame,text="Login Using Your Username and Password.", font=("times new roman",11,"bold"),bg="white",fg="black")
        center_label.grid(row=2,column=0,padx=20,pady=0,sticky=W)
        center_label2=Label(center_frame,text="STEP: 2", font=("times new roman",12,"bold"),bg="white",fg="DARK Green")
        center_label2.grid(row=3,column=0,padx=20,pady=9,sticky=W)
        center_label2=Label(center_frame,text="Click On Student Details Option from the VIT Bhopal Face Attedance System Dashboard.", font=("times new roman",11,"bold"),bg="white",fg="black")
        center_label2.grid(row=4,column=0,padx=20,pady=0,sticky=W)
        center_label3=Label(center_frame,text="STEP: 3", font=("times new roman",12,"bold"),bg="white",fg="DARK Green")
        center_label3.grid(row=5,column=0,padx=20,pady=9,sticky=W)
        center_label3=Label(center_frame,text="Enter Your Current Course Information and Class Student Information.", font=("times new roman",11,"bold"),bg="white",fg="black")
        center_label3.grid(row=6,column=0,padx=20,pady=0,sticky=W)
        center_label4=Label(center_frame,text="STEP: 4", font=("times new roman",12,"bold"),bg="white",fg="DARK Green")
        center_label4.grid(row=7,column=0,padx=20,pady=9,sticky=W)
        center_label4=Label(center_frame,text="Click On Take Photo Of the Student and Wait till 15 Secs to Let Camera Take Your Photos.", font=("times new roman",11,"bold"),bg="white",fg="black")
        center_label4.grid(row=8,column=0,padx=20,pady=0,sticky=W)

 
        
        
        # button
        b1_1=Button(self.root,text="TRAIN STUDENT FACE DATA",command=self.train_classifier,cursor="hand2",font=("time new roman",11,"bold"),bg="navy blue",fg="white")
        b1_1.place(x=590,y=580,width=220,height=40)

        back_btn = Button(self.root, text="←", command=self.close_window)
        back_btn.place(x=10, y=100) 

    def close_window(self):
        self.root.destroy()
        

 # ==================Create Function of Training===================
    def train_classifier(self):
        data_dir=("face_recognition system/data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
        #=================Train Classifier=============
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Student Dataset Successfully Trained!",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()