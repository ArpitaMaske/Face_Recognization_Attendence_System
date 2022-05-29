from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import sys
import os
import csv
from tkinter import filedialog




mydata=[]

class Attendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendence System")

# variables
        self.var_atten = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendence = StringVar()

# first image
        img = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\8.jpg")
        img = img.resize((800, 200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

# second Image
        img1 = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\18.jpg")
        img1 = img1.resize((800, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)

# background image
        img3 = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\19.jpg")
        img3 = img3.resize((1530, 790), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=790)

        title_lbl = Label(bg_img, text=" Attendence Management System ",
                          font=("times new roman", 35, "bold"), bg="skyblue", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1480, height=600)

# left side label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendence Details",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=500)

        img_left = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\16.jpg")
        img_left = img_left.resize((500, 150), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        left_inside_frame = Frame(Left_frame, bd=2,relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=135, width=720, height=300)

# attendence id
        attendence_id = Label(left_inside_frame, text="AttendenceID : ", font=("times new roman", 12, "bold"), bg="white")
        attendence_id.grid(row=0, column=0, padx=10, sticky=W)

        attendence_id_entry = Entry(left_inside_frame,textvariable=self.var_atten,  width=20,
                                font=("times new roman", 12, "bold"), bg="white")
        attendence_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

# student name
        student_name = Label(left_inside_frame, text="Student Name : ", font=("times new roman", 12, "bold"),
                             bg="white")
        student_name.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        student_name_entry = Entry(left_inside_frame,textvariable=self.var_name,  width=20,
                                   font=("times new roman", 12, "bold"), bg="white")
        student_name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

# Roll NO
        Roll_NO = Label(left_inside_frame, text="Roll NO : ", font=("times new roman", 12, "bold"),
                        bg="white")
        Roll_NO.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        Roll_NO_entry = Entry(left_inside_frame,textvariable=self.var_roll, width=20,
                              font=("times new roman", 12, "bold"), bg="white")
        Roll_NO_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)


# Date
        Date = Label(left_inside_frame, text="Date : ", font=("times new roman", 12, "bold"),
                          bg="white")
        Date.grid(row=1, column=0)

        Date_entry = Entry(left_inside_frame,textvariable=self.var_date, width=20,
                              font=("times new roman", 12, "bold"), bg="white")
        Date_entry.grid(row=1, column=1, padx=10,pady=8)

# Department
        Dep = Label(left_inside_frame, text="Department ", font=("times new roman", 12, "bold"),
                     bg="white")
        Dep.grid(row=1, column=2)

        Dep_entry = Entry(left_inside_frame,textvariable=self.var_dep, width=20,
                           font=("times new roman", 12, "bold"), bg="white")
        Dep_entry.grid(row=1, column=3, padx=8,pady=10)

#time
        time = Label(left_inside_frame, text="Time : ", font=("times new roman", 12, "bold"),
                    bg="white")
        time.grid(row=2, column=0)

        time_entry = Entry(left_inside_frame,textvariable=self.var_time, width=20,
                          font=("times new roman", 12, "bold"), bg="white")
        time_entry.grid(row=2, column=1, padx=8)

#attendence status
        attendence_status = Label(left_inside_frame, text="Attendence Status : ", font=("times new roman", 12, "bold"),
                          bg="white")
        attendence_status.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        attendence_combo = ttk.Combobox(left_inside_frame,textvariable=self.var_attendence,
                                   font=("times new roman", 12, "bold"), width=17, state="readonly")
        attendence_combo["values"] = ("Status", "Present", "Absent")
        attendence_combo.current(0)
        attendence_combo.grid(row=3, column=1, padx=10, pady=8, sticky=W)

# buttons frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=250, width=715, height=35)

        save_btn = Button(btn_frame, text="Import CSV",command=self.importCSV, width=17, font=("times new roman", 13, "bold"),
                          bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export CSV",  width=17,command=self.exportCSV,
                            font=("times new roman", 13, "bold"), bg="blue",
                            fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update",  width=17,
                            font=("times new roman", 13, "bold"), bg="blue",
                            fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data,  width=17,
                           font=("times new roman", 13, "bold"), bg="blue",
                           fg="white")
        reset_btn.grid(row=0, column=3)

    # right side label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendence Details",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)


        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)

 # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.Attendence_table = ttk.Treeview(table_frame, column=("id","roll","name","department","time","date","attendence"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Attendence_table.xview)
        scroll_y.config(command=self.Attendence_table.yview)

        self.Attendence_table.heading("id",text="AttendenceID")
        self.Attendence_table.heading("roll", text="RollNo")
        self.Attendence_table.heading("name", text="StudentName")
        self.Attendence_table.heading("department", text="Dep")
        self.Attendence_table.heading("time", text="Time")
        self.Attendence_table.heading("date", text="Date")
        self.Attendence_table.heading("attendence", text="Attendence")
        self.Attendence_table["show"] = "headings"

        self.Attendence_table.column("id", width=100)
        self.Attendence_table.column("roll", width=100)
        self.Attendence_table.column("name", width=100)
        self.Attendence_table.column("department", width=100)
        self.Attendence_table.column("time", width=100)
        self.Attendence_table.column("date", width=100)
        self.Attendence_table.column("attendence", width=100)

        self.Attendence_table.pack(fill=BOTH,expand=1)
        self.Attendence_table.bind("<ButtonRelease>",self.get_cursor)

#fetch data
    def fetchData(self,rows):
        self.Attendence_table.delete(*Attendence_table.get_children())
        for i in rows:
            self.Attendence_table.insert("",END,values=i)

    def importCSV(self):

        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetype=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",
                                         filetype=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

#get cursor
    def get_cursor(self,event=""):
        cursor_row=self.Attendence_table.focus()
        content=self.Attendence_table.item(cursor_row)
        row=content['values']
        self.var_atten.set(row[0])
        self.var_roll.set(row[1])
        self.var_name.set(row[2])
        self.var_dep.set(row[3])
        self.var_time.set(row[4])
        self.var_date.set(row[5])
        self.var_attendence.set(row[6])

#reset
    def reset_data(self):
        self.var_atten.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendence.set("")











if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()