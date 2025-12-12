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


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("VITBPL Student Face Recognition System")
        
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
        img2=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\face_recognition_system\face_recognition system\college_images\bg1.jpg")
        img2=img2.resize((1530,710),Image.ADAPTIVE)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0,y=128,width=1370,height=720)        
        
   


        # TITLE
        title_lbl=Label(self.root,text="VIT BHOPAL STUDENT FACE RECOGNITION SYSTEM                          ",font=("times new roman",15,"bold"),bg="#01001f",fg="white")
        title_lbl.place(x=0,y=90,width=1530,height=45) 
        
        
         # button
        b1_1=Button(self.root,text="VITBPL FACE DETECTOR ",command=self.face_recog,cursor="hand2",font=("time new roman",15,"bold"),bg="#01001f",fg="white")
        b1_1.place(x=120,y=532,width=341,height=85)

        back_btn = Button(self.root, text="←", command=self.close_window)
        back_btn.place(x=10, y=100) 



    def close_window(self):
        self.root.destroy()
        
          #=====================Attendance===================

    def mark_attendance(self,i,n,r):
        with open("face_recognition system/attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list)) and ((n not in name_list)) and (( r not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {n}, {r}, {dtString}, {d1}, Present")


        

    
   #================face recognition==================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(username='root', password='amnesia',host='localhost',database='face_recognizer',port=3306)
                cursor = conn.cursor()

                cursor.execute("select name from student where regnum="+str(id))
                n=cursor.fetchone()
                n="+".join(n)

                cursor.execute("select course from student where regnum="+str(id))
                r=cursor.fetchone()
                r="+".join(r)

                cursor.execute("select facultyname from student where regnum="+str(id))
                i=cursor.fetchone()
                i="+".join(i)



                if confidence > 77:
                    cv2.putText(img,f"Student Registration Number :{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.4,(64,15,223),1)
                    cv2.putText(img,f"Student Name :{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.4,(64,15,223),1)
                    cv2.putText(img,f"Student Course :{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.4,(64,15,223),1)
                    self.mark_attendance(i,n,r)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),2)    

                coord=[x,y,w,y]
            
            return coord 
        
           


        #==========recognize===============
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Detector",img)

            if cv2.waitKey(1) == 13:
             break
        videoCap.release()
        cv2.destroyAllWindows()


    
    

                          
                        
                    
                    

        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()  