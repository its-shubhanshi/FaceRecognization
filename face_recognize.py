from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
import cv2
import mysql.connector
import numpy as np
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x1050+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="Face Recognition",font=("times new roman",35, "bold" ), bg="#f2d88f", fg="green")
        title_lbl.place(x=5, y=0, width=1355, height=50)

        img_top=Image.open(r"collage-images\a10.jpg")
        img_top=img_top.resize((650,700),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=5,y=55,width=650,height=700)


        
        img_bottom=Image.open(r"collage-images\a11.jpg")
        img_bottom=img_bottom.resize((650,700),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=660,y=55,width=650,height=700)

        #button
        btn_face=Button(f_lbl,text="Face Recognition", command=self.face_recog, cursor="hand2",font=("times new roman", 22, "bold"),bg="green",fg="white")
        btn_face.place(x=250,y=520,width=250,height=40)


#=====================attendenc ====================================
    def mark_attendence(self,i,r,n,d):
        with open("attendence.csv", "r+",newline="\n") as f :
            myDataList=f.readlines()
            name_List=[]
            for line in myDataList  :
                entry=line.split((","))
                name_List.append(entry[0])
            if((i not in name_List) and (r not in name_List) and (n not in name_List) and (d not in name_List)):
                now = datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {d},{dtString},{d1},Present")




        #=========== face recognitiion =====================

    def face_recog(self):
        def draw_boundray(img,classifier, scaleFactor, minNeighbours, color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image, scaleFactor,minNeighbours)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                    
                conn=mysql.connector.connect(host="localhost",username="root", password="12345", database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select name from student where id="+str(id))
                n=my_cursor.fetchone()
                n=str(n)
                    

                my_cursor.execute("select rollno from student where id="+str(id))
                r=my_cursor.fetchone()
                r=str(r)
      
                my_cursor.execute("select dep from student where id="+str(id))
                d=my_cursor.fetchone()
                d=str(d)

                my_cursor.execute("select id from student where id="+str(id))
                i=my_cursor.fetchone()
                i=str(i)
                

                if confidence>77:
                    cv2.putText(img,f"id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"rollno:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                   
                coord=[x,y,w,y]
            return coord
        def recognize(img,clf,faceCascade):
            coord= draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True :
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



            





















if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
