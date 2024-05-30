from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector; 
import cv2 
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1355x1300+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35, "bold" ), bg="maroon", fg="white")
        title_lbl.place(x=5, y=0, width=1355, height=50)

        img_top=Image.open(r"collage-images\a10.jpg")
        img_top=img_top.resize((1355,280),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=5,y=55,width=1355,height=280)

        #button

        btn_train=Button(self.root,text="TRAIN DATA", command=self.train_classifier, cursor="hand2",font=("times new roman", 22, "bold"),bg="red",fg="white")
        btn_train.place(x=5,y=337,width=1352,height=60)

        
        img_bottom=Image.open(r"collage-images\a11.jpg")
        img_bottom=img_bottom.resize((1355,280),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=5,y=400,width=1355,height=280)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   #grayscale image
            imgageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imgageNp)
            ids.append(id)
            cv2.imshow("Training", imgageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #======================== Train the classifier and save ================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed !!")


















if __name__ == "__main__":
    root=Tk()
    obj=Train(root)

    root.mainloop()

