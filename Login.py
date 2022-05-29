from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from main import Face_Recognization_System

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")


        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\ab.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\30.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        img1_lbl=Label(image=self.photoimage1,bg="black",borderwidth=0)
        img1_lbl.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

    #label
        username_lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white",
                             bg="black")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

#=============Icon Images
        img2 = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\30.png")
        img2 = img2.resize((25,25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)

        img2_lbl = Label(image=self.photoimage2, bg="black", borderwidth=0)
        img2_lbl.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\31.jpg")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)

        img2_lbl = Label(image=self.photoimage3, bg="black", borderwidth=0)
        img2_lbl.place(x=650, y=395, width=25, height=25)
#login button
        login_btn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="WHITE",activebackground="Red")
        login_btn.place(x=110,y=300,width=120,height=35)


#new user register
        reg_btn = Button(frame, text="  Create New Account", font=("times new roman", 10, "bold"),borderwidth=0,fg="white",
                           bg="black", activeforeground="WHITE", activebackground="black")
        reg_btn.place(x=15, y=350, width=160)


#forget password button
        forget_btn = Button(frame, text="Forget Password", font=("times new roman", 10, "bold"),borderwidth=0,fg="white",
                         bg="black", activeforeground="WHITE", activebackground="black")
        forget_btn.place(x=10, y=370, width=160)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required")
        elif self.txtuser.get()=="Arpita" and self.txtpass.get()=="abc":
            messagebox.showinfo("Successsfully Login!!")
        else:
            messagebox.showerror("Invalid","Invalid Username & Password")







if __name__ == "__main__":
    root = Tk()
    app = Login_window(root)
    root.mainloop()