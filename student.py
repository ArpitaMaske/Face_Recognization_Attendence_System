from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import sys






class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")

#variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_sid = StringVar()
        self.var_sname = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()



# first image
        img = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\17.jpg")
        img = img.resize((500, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=20, y=0, width=500, height=150)

# second Image
        img1 = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\18.jpg")
        img1 = img1.resize((500, 150), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=150)

# third image
        img2 = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\20.jpg")
        img2 = img2.resize((500, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=150)

# background image
        img3 = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\19.jpg")
        img3 = img3.resize((1530, 790), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=150, width=1530, height=790)

        title_lbl = Label(bg_img, text=" STUDENT ATTENDENCE  SYSTEM ",
                          font=("times new roman", 35, "bold"), bg="skyblue", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1480, height=600)

# left side label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\16.jpg")
        img_left = img_left.resize((500, 150), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

# current course

        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information",
                                          font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=150)

# Department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=("times new roman", 12, "bold"),
                                 width=20, state="readonly")
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical", "ENTC", "Instumental")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

# Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10 ,sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman", 12, "bold"), width=20, state="readonly")
        course_combo["values"] = ("Select Course","First Year","Second Year","Third Year","Final Year/BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10,sticky=W)

# Year

        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,
                                  font=("times new roman", 12, "bold"), width=17, state="readonly")
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

# Semester

        sem_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        sem_label.grid(row=1, column=2, padx=10, sticky=W)

        sem_combo = ttk.Combobox(current_course_frame, textvariable=self.var_sem, font=("times new roman", 12, "bold"),
                                 width=17, state="readonly")
        sem_combo["values"] = ("Select", "Semester-1", "Semester-2")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

# Class Student Information

        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information",
                                         font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=250, width=720, height=300)
# student id
        StudentID = Label(class_student_frame, text="StudentID : ", font=("times new roman", 12, "bold"), bg="white")
        StudentID.grid(row=0, column=0, padx=10, sticky=W)

        studentID_entry = Entry(class_student_frame,textvariable=self.var_sid,  width=20,
                                font=("times new roman", 12, "bold"), bg="white")
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

# student name
        student_name = Label(class_student_frame, text="Student Name : ", font=("times new roman", 12, "bold"),
                             bg="white")
        student_name.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        student_name_entry = Entry(class_student_frame,textvariable=self.var_sname,  width=20,
                                   font=("times new roman", 12, "bold"), bg="white")
        student_name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

# Class Division
        class_DIV = Label(class_student_frame, text="Class DIV : ", font=("times new roman", 12, "bold"),
                          bg="white")
        class_DIV.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        class_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div,
                                    font=("times new roman", 12, "bold"), width=17, state="readonly")
        class_combo["values"] = ("A", "B", "C")
        class_combo.current(0)
        class_combo.grid(row=1, column=1, padx=2, pady=5, sticky=W)
# Roll NO
        Roll_NO = Label(class_student_frame, text="Roll NO : ", font=("times new roman", 12, "bold"),
                        bg="white")
        Roll_NO.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        Roll_NO_entry = Entry(class_student_frame,textvariable=self.var_roll, width=20,
                              font=("times new roman", 12, "bold"), bg="white")
        Roll_NO_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

# Gender
        Gender = Label(class_student_frame, text=" Gender : ", font=("times new roman", 12, "bold"),
                       bg="white")
        Gender.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,
                                    font=("times new roman", 12, "bold"), width=17, state="readonly")
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=2, pady=5, sticky=W)

# Date of Birth
        DOB = Label(class_student_frame, text=" Date of Birth : ", font=("times new roman", 12, "bold"),
                    bg="white")
        DOB.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        DOB_entry = Entry(class_student_frame,textvariable=self.var_dob,  width=20,
                          font=("times new roman", 12, "bold"), bg="white")
        DOB_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

# Email
        Email = Label(class_student_frame, text=" Email_ID : ", font=("times new roman", 12, "bold"),
                      bg="white")
        Email.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        Email_entry = Entry(class_student_frame,textvariable=self.var_email,  width=20,
                            font=("times new roman", 12, "bold"), bg="white")
        Email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

# Phone NO
        Phone_NO = Label(class_student_frame, text=" Phone NO : ", font=("times new roman", 12, "bold"),
                         bg="white")
        Phone_NO.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        Phone_NO_entry = Entry(class_student_frame,textvariable=self.var_phone,  width=20,
                               font=("times new roman", 12, "bold"), bg="white")
        Phone_NO_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

# Address
        Address = Label(class_student_frame, text=" Address : ", font=("times new roman", 12, "bold"),
                        bg="white")
        Address.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        Address_entry = Entry(class_student_frame,textvariable=self.var_address,  width=20,
                              font=("times new roman", 12, "bold"), bg="white")
        Address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

# Proffessor Name
        Prof_name = Label(class_student_frame, text=" Professor Name : ", font=("times new roman", 12, "bold"),
                          bg="white")
        Prof_name.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        Prof_name_entry = Entry(class_student_frame,textvariable=self.var_teacher,  width=20,
                                font=("times new roman", 12, "bold"), bg="white")
        Prof_name_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

# radio buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",
                                    value="Yes")
        radiobtn1.grid(row=6, column=0)


        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",
                                    value="No")
        radiobtn1.grid(row=6, column=1)

# buttons frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=715, height=35)

        save_btn = Button(btn_frame, text="Save",command=self.add_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=17, font=("times new roman", 13, "bold"), bg="blue",
                            fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, width=17, font=("times new roman", 13, "bold"), bg="blue",
                            fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_date, width=17, font=("times new roman", 13, "bold"), bg="blue",
                           fg="white")
        reset_btn.grid(row=0, column=3)

# button frames for taking photo
        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=235, width=715, height=35)

        take_photo_btn = Button(btn_frame1,command=self.generate_dataset, text="Take Photo Sample", width=35, font=("times new roman", 13, "bold"),
                                bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=35,
                                  font=("times new roman", 13, "bold"),
                                  bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)



# right side label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)

        img_right = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\51.jpg")
        img_right = img_right.resize((500, 150), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=720, height=130)

# search system
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System :",
                                  font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=710, height=70)

        search_label = Label(search_frame, text=" Search By : ", font=("times new roman", 15, "bold"),
                             bg="skyblue")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

# search combo
        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), width=15, state="readonly")
        search_combo["values"] = ("Select", "Roll NO", "Phone NO")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        Search_entry = Entry(search_frame, width=15, font=("times new roman", 12, "bold"), bg="white")
        Search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        Search_btn = Button(search_frame, text="Search", width=12, font=("times new roman", 13, "bold"), bg="blue",
                            fg="white")
        Search_btn.grid(row=0, column=3, padx=4)

        ShowAll_btn = Button(search_frame, text="Show All", width=12, font=("times new roman", 13, "bold"), bg="blue",
                             fg="white")
        ShowAll_btn.grid(row=0, column=4, padx=4)

#table frame
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=325)

#scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","sid","sname","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)



        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Dep")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("sid", text="Student_ID")
        self.student_table.heading("sname", text="Student_Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll_No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone_No")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Professor_Name")
        self.student_table.heading("photo", text="Photo_Sample")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("sid", width=100)
        self.student_table.column("sname", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


#function declaration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_sid.get()=="" or self.var_sname.get=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="RECOMMENDED",database="face1")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_sem.get(),
                                                                                                self.var_sid.get(),
                                                                                                self.var_sname.get(),
                                                                                                self.var_div.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_teacher.get(),
                                                                                                self.var_radio1.get()
                                                                                             ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Succesfully!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

#fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="RECOMMENDED", database="face1")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


#get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_sid.set(data[4]),
        self.var_sname.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

#update function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_sid.get() == "" or self.var_sname.get == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update the student details",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="RECOMMENDED",
                                                   database="face1")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,StudentName=%s,Division=%s,RollNo=%s,Gender=%s,DateOfBirth=%s,Email=%s,PhoneNo=%s,Address=%s,ProfessorName=%s,PhotoSample=%s where StudentID=%s",(
                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                                                                                    self.var_sname.get(),
                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                    self.var_sid.get()
                                                                                                                                                                                                                ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

#delete function
    def delete_data(self):
        if self.var_sid.get=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to Delete ?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="RECOMMENDED",
                                                   database="face1")
                    my_cursor = conn.cursor()
                    sql="delete from student where StudentID=%s"
                    val=(self.var_sid.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

#reset
    def reset_date(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_sid.set("")
        self.var_sname.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

#generate data set / Take photo samples
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_sid.get() == "" or self.var_sname.get == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="RECOMMENDED",
                                                   database="face1")
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,StudentName=%s,Division=%s,RollNo=%s,Gender=%s,DateOfBirth=%s,Email=%s,PhoneNo=%s,Address=%s,ProfessorName=%s,PhotoSample=%s where StudentID=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_sname.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_sid.get()
                    ))

                conn.commit()
                self.fetch_data()
                self.reset_date()
                conn.close()

#load predefined data on face frontals from opencv
                face_classifier=cv2.CascadeClassifier("C:\\Users\\Arpita\\Desktop\\Face Recognization Attendence System\\haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5) #scaling factor =1.3 ,min factor=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                    face=cv2.resize(face_cropped(my_frame),(300,400))
                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completely!!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()