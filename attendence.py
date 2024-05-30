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
import csv
from tkinter import filedialog
from tkinter import messagebox

mydata=[]

class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x1050+0+0")
        self.root.title("Face Recognition System")


        #==============================text  variables===========================

        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendence=StringVar()
       
        

#first img
        img=Image.open("C:/Users/Hii Sir/Desktop/FaceRecognization/collage-images/st1.jpg")
        img=img.resize((360,80),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=360,height=80)

        #seconnd img

        img1=Image.open("C:/Users/Hii Sir/Desktop/FaceRecognization/collage-images/s2.jpg")
        img1=img1.resize((360,80),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=360,y=0,width=360,height=80)

        #third img
        img2=Image.open("C:/Users/Hii Sir/Desktop/FaceRecognization/collage-images/st3.jpg")
        img2=img2.resize((360,80),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=720,y=0,width=360,height=80)

        #fourth img        
        img3=Image.open("C:/Users/Hii Sir/Desktop/FaceRecognization/collage-images/st4.jpg")
        img3=img3.resize((360,80),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1080,y=0,width=360,height=80)


    
        #bg image
        img4=Image.open("C:/Users/Hii Sir/Desktop/FaceRecognization/collage-images/bg.jpg")
        img4=img4.resize((1400,555),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=80,width=1400,height=700)
        title_lbl=Label(bg_img,text="Attendence System",font=("times new roman",35, "bold" ), bg="green", fg="white")
        title_lbl.place(x=0, y=0, width=1400, height=50)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=0,y=55,width=1380, height=700)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=4, relief=RIDGE, text=" Student Attendence Details", font=("times  new roman", 22 , "bold"))
        Left_frame.place(x=10,y=10, width=650, height=700)

        
        Left_Inside_frame=LabelFrame(Left_frame,bd=2, relief=RIDGE, bg="white")
        Left_Inside_frame.place(x=5,y=10, width=630, height=700)

        attendenceID_label=Label(Left_Inside_frame, text="Attendence ID : ", font=("times new roman", 13, "bold"), bg="white" )
        attendenceID_label.grid(row=0,column=0,padx=10,pady=15,sticky=W)

        attendenceID_entry=ttk.Entry(Left_Inside_frame, textvariable=self.var_atten_id, width=15, font=("times new roman", 13, "bold"))
        attendenceID_entry.grid(row=0,column=1,padx=10, pady=15,sticky=W)

        # roll number
        rollNo_label=Label(Left_Inside_frame,text="Roll : ", font=("times new roman", 13, "bold"), bg="white" )
        rollNo_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        rollNo_entry=ttk.Entry(Left_Inside_frame, textvariable=self.var_atten_id, width=15, font=("times new roman", 13, "bold"))
        rollNo_entry.grid(row=0,column=3,padx=10, pady=5,sticky=W)


        name_label=Label(Left_Inside_frame,text="Name : ", font=("times new roman", 13, "bold"), bg="white" )
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(Left_Inside_frame,textvariable=self.var_atten_name,  width=15, font=("times new roman", 13, "bold"))
        name_entry.grid(row=1,column=1,padx=10, pady=5,sticky=W)

        depLabel=Label(Left_Inside_frame,text='Department', font=("times new roman", 15, "bold") ,bg="white")
        depLabel.grid(row=1,column=2,padx=10,sticky=W)
        depart_entry=ttk.Entry(Left_Inside_frame, textvariable=self.var_atten_dep, width=15, font=("times new roman", 13, "bold"))
        depart_entry.grid(row=1,column=3,padx=10, pady=5,sticky=W)

        date_label=Label(Left_Inside_frame,text="Date : ", font=("times new roman", 13, "bold"), bg="white" )
        date_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        date_entry=ttk.Entry(Left_Inside_frame,textvariable=self.var_atten_date,  width=15, font=("times new roman", 13, "bold"))
        date_entry.grid(row=2,column=1,padx=10, pady=5,sticky=W)

        time_label=Label(Left_Inside_frame,text="Time : ", font=("times new roman", 13, "bold"), bg="white" )
        time_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        time_entry=ttk.Entry(Left_Inside_frame,textvariable=self.var_atten_time,  width=15, font=("times new roman", 13, "bold"))
        time_entry.grid(row=2,column=3,padx=10, pady=5,sticky=W)

        status_label=Label(Left_Inside_frame,text='Attendence', font=("times new roman", 15, "bold") ,bg="white")
        status_label.grid(row=3,column=0,padx=10,sticky=W)
        
        self.status_combo=ttk.Combobox(Left_Inside_frame,textvariable=self.var_atten_attendence,  font=("times new roman", 13, "bold"),state="readonly",width=15)
        self.status_combo["values"]=("Status", "Present" , "Absent")
        self.status_combo.current(0)
        self.status_combo.grid(row=3,column=1, padx=2,pady=10, sticky=W)


         #buttons frame

        btn_frame=Frame(Left_Inside_frame,bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0,y=210, width=620,height=50)

        importCSV_btn=Button(btn_frame, command=self.importCsv, text="Import csv",width=15, font=("times new roman", 13,"bold"), bg="darkblue", fg="white")
        importCSV_btn.grid(row=0, column=0)
        
        exportCSV_btn=Button(btn_frame, command=self.exportCsv, text="Export csv",width=15, font=("times new roman", 13,"bold"), bg="darkblue", fg="white")
        exportCSV_btn.grid(row=0, column=1)
        
        update_btn=Button(btn_frame, command=self.exportCsv, text="Update",  width=15, font=("times new roman", 13,"bold"), bg="darkblue", fg="white")
        update_btn.grid(row=0, column=2)
        
        reset_btn=Button(btn_frame,command=self.reset_data, text="Reset",width=15, font=("times new roman", 13,"bold"), bg="darkblue", fg="white")
        reset_btn.grid(row=0, column=3)




 #right frame

        right_frame=LabelFrame(main_frame,bd=4, relief=RIDGE, text="Attendence Details", font=("times  new roman", 22 , "bold"))
        right_frame.place(x=660,y=10, width=650, height=580)
    #============table data ===========================

        table_frame=Frame(right_frame,bd=2,bg="white", relief=RIDGE)
        table_frame.place(x=5,y=10,width=630,height=250)

        scrollbar_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrollbar_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendenceReportTable=ttk.Treeview(table_frame,column=("id","department","name","time","date","roll","attendence"),xscrollcommand=scrollbar_x.set,yscrollcommand=scrollbar_y.set)

        scrollbar_x.pack(side=BOTTOM,fill=X)
        scrollbar_y.pack(side=RIGHT,fill=Y)
        scrollbar_x.config(command=self.AttendenceReportTable.xview)
        scrollbar_y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id",text="AttendenceId")
        self.AttendenceReportTable.heading("department",text="Department")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("roll",text="Roll")
        self.AttendenceReportTable.heading("attendence",text="Attendence")

        self.AttendenceReportTable["show"]="headings"

        self.AttendenceReportTable.column("id",width=120)
        self.AttendenceReportTable.column("department",width=120)
        self.AttendenceReportTable.column("name",width=120)
        self.AttendenceReportTable.column("time",width=120)
        self.AttendenceReportTable.column("date",width=120)
        self.AttendenceReportTable.column("roll",width=120)
        self.AttendenceReportTable.column("attendence",width=120)

        self.AttendenceReportTable.pack(fill=BOTH,expand=1)
        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)


        #===================================fetchh data ===========================

    def fetchData(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)
    
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myFile:
            csvread=csv.reader(myFile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #======================== export csv

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data", "No data found to export", parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myFile:
                exp_write=csv.writer(myFile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data exported to "+os.path.basename(fln))
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}",parent=self.root)
        
    def get_cursor(self, event=""):
        cursor_row=self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0]),
        self.var_atten_dep.set(rows[1]),
        self.var_atten_name.set(rows[2]),
        self.var_atten_time.set(rows[3]),
        self.var_atten_date.set(rows[4]),
        self.var_atten_roll.set(rows[5]),
        self.var_atten_attendence.set(rows[6])
            
            
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_dep.set("")
        self.var_atten_name.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_roll.set("")
        self.var_atten_attendence.set("Status")
    







    









        




        



 






if __name__ == "__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()
