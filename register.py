from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from tkinter import messagebox



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")



#Bg Image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\ab.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

#left image
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\02.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

#frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="Register Here",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

#label and entry
#row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white",fg="black")
        l_name.place(x=370, y=100)

        self.txt_lname=ttk.Entry(frame,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

#row2
        contact = Label(frame, text="Contact Number", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=170)

        contact_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        contact_entry.place(x=50, y=200, width=250)

        email = Label(frame, text="Email ID", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

#row3
        security = Label(frame, text="Selct security Questions", font=("times new roman", 15, "bold"), bg="white")
        security.place(x=50, y=240)

        self.combo_security_Q=ttk.Combobox(frame,font=("times new roman",15,"bold"))
        self.combo_security_Q["values"]=("Select","your birth place","your pet name","your bike name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        security_A.place(x=370, y=240)

        self.txt_security=ttk.Entry(frame,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

#row4
        pwd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        pwd.place(x=50, y=310)

        pwd_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        pwd_entry.place(x=50, y=340, width=250)

        confirm_pwd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pwd.place(x=370, y=310)

        self.txt_confirm_pwd = ttk.Entry(frame, font=("times new roman", 15))
        self.txt_confirm_pwd.place(x=370, y=340, width=250)

#check button
        checkbtn=Checkbutton(frame,text="I Agree The Terms $ Condition",font=("times new roman", 15, "bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=400)


#buttons
        img=Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\r.png")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=450,width=200)

        img1 = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\login.jpg")
        img1 = img1.resize((200, 45), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2")
        b1.place(x=400, y=450, width=200)



if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()