from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
import tkinter
import os
from student import Student
from train import Train
from face_recognize import Face_Recognition
from attendence import Attendence
from developer import Developer
from helpDesk import HelpDesk



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x1050+0+0")
        self.root.title("Face Recognition System")


        #first img
        img=Image.open("C:/Users/Hii Sir/Desktop/FaceRecognization/collage-images/a2.jpg")
        img=img.resize((360,150),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=360,height=150)

        #seconnd img

        img1=Image.open("C:/Users/Hii Sir/Desktop/FaceRecognization/collage-images/a3.jpg")
        img1=img1.resize((360,150),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=360,y=0,width=360,height=150)

        #third img
        img2=Image.open("C:/Users/Hii Sir/Desktop/FaceRecognization/collage-images/a7.jpg")
        img2=img2.resize((360,150),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=720,y=0,width=360,height=150)

        #fourth img        
        img3=Image.open("C:/Users/Hii Sir/Desktop/FaceRecognization/collage-images/a4.jpg")
        img3=img3.resize((360,150),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1080,y=0,width=360,height=150)


        #bg image
        img4=Image.open("C:/Users/Hii Sir/Desktop/FaceRecognization/collage-images/bg.jpg")
        img4=img4.resize((1400,555),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=150,width=1400,height=555)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",35, "bold" ), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1400, height=45)

        # student button

        img5=Image.open("C:/Users/Hii Sir/Desktop/FaceRecognization/collage-images/student-information.png")
        img5=img5.resize((180,180),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.student_details, cursor="hand2")
        b1.place(x=100,y=100,width=180,height=180)

        b1=Button(bg_img,text="Student Details",command=self.student_details, cursor="hand2",font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b1.place(x=100,y=280,width=180,height=40)

        # face detection button

        img6=Image.open("C:/Users/Hii Sir/Desktop/FaceRecognization/collage-images/a7.jpg")
        img6=img6.resize((180,180),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b2=Button(bg_img,image=self.photoimg6, command=self.face_data, cursor="hand2")
        b2.place(x=400,y=100,width=180,height=180)

        b2=Button(bg_img,text="Face Detector", command=self.face_data, cursor="hand2",font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b2.place(x=400,y=280,width=180,height=40)

        # Attendence button

        img7=Image.open("C:/Users/Hii Sir/Desktop/FaceRecognization/collage-images/attendence.jpg")
        img7=img7.resize((180,180),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b3=Button(bg_img,image=self.photoimg7, command=self.attendence_datesheet, cursor="hand2")
        b3.place(x=700,y=100,width=180,height=180)

        b3=Button(bg_img,text="Attendence", command=self.attendence_datesheet, cursor="hand2",font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b3.place(x=700,y=280,width=180,height=40)

        # Help Desk button

        img8=Image.open("C:/Users/Hii Sir/Desktop/FaceRecognization/collage-images/help.jpg")
        img8=img8.resize((180,180),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b4=Button(bg_img,image=self.photoimg8, command=self.help_Desk, cursor="hand2")
        b4.place(x=1000,y=100,width=180,height=180)

        b4=Button(bg_img,text="Help Desk", command=self.help_Desk, cursor="hand2",font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b4.place(x=1000,y=280,width=180,height=40)

        # Train button

        img9=Image.open("C:/Users/Hii Sir/Desktop/FaceRecognization/collage-images/train.jpg")
        img9=img9.resize((180,180),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b5=Button(bg_img,image=self.photoimg9, command=self.train_data, cursor="hand2")
        b5.place(x=100,y=350,width=180,height=180)

        b5=Button(bg_img,text="Train Data", command=self.train_data, cursor="hand2",font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b5.place(x=100,y=500,width=180,height=40)

        # Photos button

        img10=Image.open("C:/Users/Hii Sir/Desktop/FaceRecognization/collage-images/a6.jpg")
        img10=img10.resize((180,180),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b6=Button(bg_img,image=self.photoimg10, command=self.open_img, cursor="hand2")
        b6.place(x=400,y=350,width=180,height=180)

        b6=Button(bg_img,text="Photos", command=self.open_img, cursor="hand2",font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b6.place(x=400,y=500,width=180,height=40)

        # Developer button

        img11=Image.open("C:/Users/Hii Sir/Desktop/FaceRecognization/collage-images/developer.jpg")
        img11=img11.resize((180,180),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b7=Button(bg_img, command=self.developer_Team, image=self.photoimg11, cursor="hand2")
        b7.place(x=700,y=350,width=180,height=180)

        b7=Button(bg_img, command=self.developer_Team, text="Developer", cursor="hand2",font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b7.place(x=700,y=500,width=180,height=40)

        # exit button

        img12=Image.open(r"collage-images\exit.jpg")
        img12=img12.resize((180,180),Image.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b8=Button(bg_img,image=self.photoimg12, command=self.iExit, cursor="hand2")
        b8.place(x=1000,y=350,width=180,height=180)

        b8=Button(bg_img,text="Exit", command=self.iExit, cursor="hand2",font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b8.place(x=1000,y=500,width=180,height=40)


    def open_img(self):
        os.startfile("data")


    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition", "Are you sure exit this project")
        if self.iExit>0:
            self.root.destroy()
        else:
            return

#==============================functions button===========================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendence_datesheet(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)
    
    def developer_Team(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def help_Desk(self):
        self.new_window=Toplevel(self.root)
        self.app=HelpDesk(self.new_window)
    
    
    
        

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
