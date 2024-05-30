from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector; 
import cv2 

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x1300+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="DEVLOPER",font=("times new roman",35, "bold" ), bg="green", fg="white")
        title_lbl.place(x=0, y=0, width=1380, height=50)

        #first img
        img_top=Image.open("C:/Users/Hii Sir/Desktop/FaceRecognization/collage-images/971.jpg")
        img_top=img_top.resize((1000,700),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1000,height=700)

        main_frame=Frame(self.root,bd=2,bg="#f2a36a")
        main_frame.place(x=900,y=50,width=1320, height=700)

        dev_lbl=Label(main_frame,text="Name : Shubhanshi Srivastava",font=("times new roman",18, "bold" ), fg="darkblue", bg="white")
        dev_lbl.place(x=10, y=260)
     
        dev_lbl=Label(main_frame,text="Branch : Computer Science & Engg.",font=("times new roman",18, "bold" ), fg="darkblue", bg="white")
        dev_lbl.place(x=10, y=300)

        
        dev_lbl=Label(main_frame,text="Year : Final Year / 8th sem",font=("times new roman",18, "bold" ), fg="darkgreen", bg="white")
        dev_lbl.place(x=10, y=340)
        
        
        dev_lbl=Label(main_frame,text="Profile : Full stack developer",font=("times new roman",18, "bold" ), fg="red", bg="white")
        dev_lbl.place(x=10, y=380)

        dev_lbl=Label(main_frame,text="Contact me : itsshubhanshi23@gmail.com",font=("times new roman",18, "bold" ), fg="darkblue", bg="white")
        dev_lbl.place(x=10, y=420)

        img_profile=Image.open("C:/Users/Hii Sir/Desktop/FaceRecognization/collage-images/pic6.jpg")
        img_profile=img_profile.resize((220,220),Image.LANCZOS)
        self.photoimg_profile=ImageTk.PhotoImage(img_profile)

        f_lbl=Label(self.root,image=self.photoimg_profile)
        f_lbl.place(x=1020,y=70,width=220,height=220)













if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)

    root.mainloop()
