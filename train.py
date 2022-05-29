from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import cv2
import numpy as np



class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data")


        title_lbl = Label(self.root, text=" Train Data Set ",
                          font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\5.jpeg")
        img_top = img_top.resize((500, 330), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=48, width=500, height=330)

        # second Image
        img_top1 = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\4.jpg")
        img_top1 = img_top1.resize((500, 330), Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(self.root, image=self.photoimg_top1)
        f_lbl.place(x=500, y=48, width=500, height=330)

        # third image
        img_top1 = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\1.jpg")
        img_top1 = img_top1.resize((550, 330), Image.ANTIALIAS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(self.root, image=self.photoimg_top2)
        f_lbl.place(x=1000, y=48, width=550, height=330)
#button
        b1_1 = Button(self.root, text="TRAIN DATA", cursor="hand2",command=self.train_classifier,
                      font=("times new roman", 30, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)


#first image
        img_bottom = Image.open(r"C:\Users\Arpita\Desktop\Face Recognization Attendence System\Images\15.jpg")
        img_bottom = img_bottom.resize((1530, 340), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=340)


    def train_classifier(self):
        data_dir=("C:\\Users\\Arpita\\Desktop\\Face Recognization Attendence System\\data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #grey scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

#=train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed",parent=self.root)








if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()