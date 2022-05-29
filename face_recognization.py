from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import mysql.connector
import cv2
import numpy as np
from time import strftime
from datetime import datetime



class Face_Recognization:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Detactor")



        title_lbl = Label(self.root, text=" FACE RECOGNIZATION ",
                          font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)
#1image
        img_top = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\01.jpg")
        img_top = img_top.resize((650, 750), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=750)
#2image
        img_bottom = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\2.jpg")
        img_bottom = img_bottom.resize((950, 770), Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_top1)
        f_lbl.place(x=650, y=55, width=950, height=770)

#button
        b1_1 = Button(f_lbl, text="FACE RECOGNIZATION", cursor="hand2",command=self.face_recog,
                      font=("times new roman", 13, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=500, y=620, width=200, height=40)

#attendence
    def mark_attendence(self,n,i,a,e,k):
        with open("abc.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((n not in name_list) and (i not in name_list) and (a not in name_list) and (e not in name_list) and (k not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{m},{k},{n},{e},{dtString},{d1},Present")


#face recognization
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="RECOMMENDED",
                                               database="face1")
                my_cursor = conn.cursor()

                my_cursor.execute("select StudentName from student where StudentID="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select StudentName from student where StudentID="+str(id))
                k = my_cursor.fetchone()
                k = "+".join(k)

                my_cursor.execute("select RollNo from student where StudentID="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Dep from student where StudentID="+str(id))
                e = my_cursor.fetchone()
                e = "+".join(e)






                if confidence>80:

                    cv2.putText(img, f"StudentName:{r}", (x, y - 60), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"StudentID:{k}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"RollNo:{n}", (x, y - 40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Dep:{e}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    self.mark_attendence(i,k,n,e)

                else:
                    cv2.rectangle(img,(x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img,"Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord=[x,y,w,y]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognization",img)

            if cv2.waitKey(1)==13:
                break
            video_cap.release()
            cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognization(root)
    root.mainloop()