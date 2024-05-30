from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector; 
import cv2 

class HelpDesk:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1380x800+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",35, "bold" ), bg="maroon", fg="white")
        title_lbl.place(x=0, y=0, width=1380, height=50)

        #first img
        img_top=Image.open(r"collage-images\help2.jpg")
        img_top=img_top.resize((1360,700),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1360,height=700)

        dev_lbl=Label(self.root,text="Email : itsshubhanshi23@gmail.com",font=("times new roman",22, "bold" ), fg="darkblue", bg="white")
        dev_lbl.place(x=10, y=150)

        
        dev_lbl=Label(self.root,text="github : its-shubhanshi",font=("times new roman",22, "bold" ), fg="red", bg="white")
        dev_lbl.place(x=10, y=200)












if __name__ == "__main__":
    root=Tk()
    obj=HelpDesk(root)

    root.mainloop()
