from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from time import strftime
from datetime import datetime
import os
import tkinter
from train import Train
from face_recognization import Face_Recognization
from attendence import Attendence
from developer import Developer
from help import Help



class Face_Recognization_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System")


#first image
        img=Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\2.jpg")
        img=img.resize((500,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=20,y=0,width=500,height=150)

#second Image
        img1 = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\6.jpg")
        img1 = img1.resize((500, 150), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=150)

#third image
        img2 = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\3.jpg")
        img2 = img2.resize((500, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=150)


#background image
        img3 = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\7.jpg")
        img3 = img3.resize((1530, 790), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=150, width=1530, height=790)

        title_lbl=Label(bg_img,text=" FACE  RECOGNIZATION  ATTENDENCE  SYSTEM ",font=("times new roman",35,"bold"),bg="skyblue",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

#time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl = Label(title_lbl, font=("times new roman", 15, "bold"),
                          bg="skyblue", fg="red")
        lbl.place(x=0, y=0, width=110, height=50)
        time()
#student button
        img4 = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\8.jpg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1 = Button(bg_img, text="STUDENT DETAILS",command=self.student_details, cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)


#detect face
        img5 = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\4.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="FACE DETECTOR ", cursor="hand2",command=self.face_data, font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)

#attendencce details
        img6 = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\10.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.attendence_data)
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="ATTENDANCE", cursor="hand2",command=self.attendence_data ,font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)

# Help
        img7 = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\12.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7,command=self.help_data, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="HELP DESK",command=self.help_data, cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)

# Train face button
        img8 = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\1.jpg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b1.place(x=200, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="TRAIN DATA ", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=200, y=580, width=220, height=40)

# Photos face button
        img9 = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\15.jpg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="PHOTOS ", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=500, y=580, width=220, height=40)

# Developer face button
        img10 = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\13.jpg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10,command=self.developer_data, cursor="hand2")
        b1.place(x=800, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="DEVELOPER ",command=self.developer_data, cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=800, y=580, width=220, height=40)

# exit face button
        img11 = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\16.jpg")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11,command=self.iExit, cursor="hand2")
        b1.place(x=1100, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="EXIT ",command=self.iExit, cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=1100, y=580, width=220, height=40)


    def open_img(self):
        os.startfile(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognization System","Do you really want to exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


#function buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognization(self.new_window)

    def attendence_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendence(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognization_System(root)
    root.mainloop()
