from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from PIL import  ImageFilter
import webbrowser




class Help:
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("VTOP Face Attendance System")

        # Blue bar pic in header
        img = Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\face_recognition_system\face_recognition system\college_images\collegepic.jpg")
        img = img.resize((1370, 190), Image.ADAPTIVE)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1370, height=90)

        # Logo image
        img1 = Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\face_recognition_system\face_recognition system\college_images\logo.jpg")
        img1 = img1.resize((155, 90), Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=155, height=90)

        # Background image
        img2 = Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\face_recognition_system\face_recognition system\college_images\bg.jpg")
        img2 = img2.resize((1530, 710), Image.ADAPTIVE)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=0, y=90, width=1530, height=610)

        # TITLE
        title_lbl = Label(self.root, text="HELP DESK                      ", font=("times new roman", 20, "bold"), bg="white", fg="RED")
        title_lbl.place(x=0, y=130, width=1530, height=45)

        # Developer contact details
        dev_label = Label(self.root, text=" Contact Details for help!:", font=("times new roman", 18, "bold"), fg="blue", bg="white")
        dev_label.place(x=10, y=200)

        email_label = Label(self.root, text="Email: shivanshkuntal2022@vitbopal.ac.in", font=("times new roman", 16), fg="black", bg="white")
        email_label.place(x=30, y=240)

        phone_label = Label(self.root, text="Phone no: 9618242101", font=("times new roman", 16), fg="black", bg="white")
        phone_label.place(x=30, y=270)

        # Guidelines
        guideline_label = Label(self.root, text="Guidelines:", font=("times new roman", 18, "bold"), fg="blue", bg="white")
        guideline_label.place(x=10, y=310)

        guidelines_text = Text(self.root, font=("times new roman", 14), wrap=WORD, height=10, width=100)
        guidelines_text.insert(END, 
            """1. Always keep your login details confidential.
2. Face recognition issues: Ensure good lighting and clear view of your face. Update your profile picture if needed
3. Follow the attendance marking process carefully.
4. In case of any issues, contact the support team.
5. User Manual: [Link to user manual]
6. FAQs: [Link to FAQs page]"""
        )
        guidelines_text.place(x=30, y=350)

        
        back_btn = Button(self.root, text="←", command=self.close_window)
        back_btn.place(x=10, y=100) 

    def close_window(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()