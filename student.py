from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector; 
import cv2 



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x1300+0+0")
        self.root.title("Face Recognition System")
    
     #============variable=====================
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_id=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_rollno=StringVar()
        self.var_phoneNo=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_division=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()



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
        title_lbl=Label(bg_img,text="Student Management System",font=("times new roman",35, "bold" ), bg="green", fg="white")
        title_lbl.place(x=0, y=0, width=1400, height=50)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=0,y=55,width=1380, height=700)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=4, relief=RIDGE, text="Student Details", font=("times  new roman", 22 , "bold"))
        Left_frame.place(x=10,y=10, width=650, height=700)

        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white", relief=RIDGE, text="Current Course  Information", font=("times new roman", 15, "bold"))
        current_course_frame.place(x=5,y=5,width=630,height=150)

        #developer

        dep_label=Label(current_course_frame,text='Department', font=("times new roman", 15, "bold") ,bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 13, "bold"),state="readonly",width=18)
        dep_combo["values"]=("Select Department", "computer", "IT", "CIVIL","Machanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1, padx=2,pady=10, sticky=W)

        #course
        course_label=Label(current_course_frame,text="Course",  font=("times new roman", 15, "bold"), bg="white")
        course_label.grid(row=0, column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,  textvariable=self.var_course, font=("times new roman", 13,"bold"),state="readonly",width=18)
        course_combo["values"]=("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year", font=("times new roman", 15, "bold"), bg="white")
        year_label.grid(row=1,column=0,padx=10, pady=10,sticky=W)
        year_Combo=ttk.Combobox(current_course_frame,  textvariable=self.var_year, font=("times new roman", 13, "bold"),state="readonly" ,width=18)
        year_Combo["values"]=("Select Year", "2021-2022","2022-2023","2023-2024","2024-2025")
        year_Combo.current(0)
        year_Combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(current_course_frame,text="Semester", font=("times new roman", 15, "bold"), bg="white")
        semester_label.grid(row=1,column=2,pady=10,sticky=W)
        semester_Combo=ttk.Combobox(current_course_frame,  textvariable=self.var_sem, font=("times new roman", 13, "bold"),state="readonly" ,width=18)
        semester_Combo["values"]=("Select Semester", "One","Two","Three","Four","Fifth",'Six',"Seven","Eight")
        semester_Combo.current(0)
        semester_Combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #class student information

        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white", relief=RIDGE,text="Class Student information", font=("times new roman", 15, "bold"))
        class_Student_frame.place(x=5,y=170,width=630,height=500)


        #student id
        studentID_label=Label(class_Student_frame,text="Student ID : ", font=("times new roman", 13, "bold"), bg="white" )
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,  textvariable=self.var_id, width=15, font=("times new roman", 13, "bold"))
        studentID_entry.grid(row=0,column=1,padx=10, pady=5,sticky=W)

        #studennt name
        student_name_label=Label(class_Student_frame,text="Student Name : ", font=("times new roman", 13, "bold"), bg="white" )
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry=ttk.Entry(class_Student_frame,  textvariable=self.var_name, width=15, font=("times new roman", 13, "bold"))
        student_name_entry.grid(row=0,column=3,padx=10, pady=5,sticky=W)

        #class division 
        
        class_Division_label=Label(class_Student_frame,text="Class Division : ", font=("times new roman", 13, "bold"), bg="white" )
        class_Division_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_Division_Combo=ttk.Combobox(class_Student_frame,  textvariable=self.var_division, font=("times new roman", 13, "bold"),state="readonly" ,width=14)
        class_Division_Combo["values"]=("A","B","C")
        class_Division_Combo.current(0)
        class_Division_Combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # roll number
        roll_no_label=Label(class_Student_frame,text="Roll No : ", font=("times new roman", 13, "bold"), bg="white" )
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame, textvariable=self.var_rollno, width=15, font=("times new roman", 13, "bold"))
        roll_no_entry.grid(row=1,column=3,padx=10, pady=5,sticky=W)

        # gender
        gender_label=Label(class_Student_frame,text="Gender : ", font=("times new roman", 13, "bold"), bg="white" )
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_Combo=ttk.Combobox(class_Student_frame,  textvariable=self.var_gender, font=("times new roman", 13, "bold"),state="readonly" ,width=14)
        gender_Combo["values"]=("Male","Female","Other")
        gender_Combo.current(0)
        gender_Combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # dob
        dob_label=Label(class_Student_frame,text="DOB : ", font=("times new roman", 13, "bold"), bg="white" )
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_Student_frame,  textvariable=self.var_dob, width=15, font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2,column=3,padx=10, pady=5,sticky=W)


        # email
        email_label=Label(class_Student_frame,text="Email ID : ", font=("times new roman", 13, "bold"), bg="white" )
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_Student_frame, textvariable=self.var_email, width=15, font=("times new roman", 13, "bold"))
        email_entry.grid(row=3,column=1,padx=10, pady=5,sticky=W)

        
        # phone no
        phone_no_label=Label(class_Student_frame, text="Phone No :", font=("times new roman", 13, "bold"), bg="white" )
        phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_no_entry=ttk.Entry(class_Student_frame, textvariable= self.var_phoneNo, width=15, font=("times new roman", 13, "bold"))
        phone_no_entry.grid(row=3,column=3,padx=10, pady=5,sticky=W)

        
        # Address
        address_label=Label(class_Student_frame,text="Address : ", font=("times new roman", 13, "bold"), bg="white" )
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_Student_frame, textvariable=self.var_address, width=15, font=("times new roman", 13, "bold"))
        address_entry.grid(row=4,column=1,padx=10, pady=5,sticky=W)

        
        # teacher name
        teacher_name_label=Label(class_Student_frame,text="Teacher Name : ", font=("times new roman", 13, "bold"), bg="white" )
        teacher_name_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_name_entry=ttk.Entry(class_Student_frame, textvariable=self.var_teacher, width=15, font=("times new roman", 13, "bold"))
        teacher_name_entry.grid(row=4,column=3,padx=10, pady=5,sticky=W)

        #radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1 ,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        #buttons frame

        btn_frame=Frame(class_Student_frame,bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0,y=210, width=630,height=50)

        save_btn=Button(btn_frame, text="Save", command=self.add_data ,width=15, font=("times new roman", 13,"bold"), bg="green", fg="white")
        save_btn.grid(row=0, column=0)
        
        update_btn=Button(btn_frame, text="Update", command=self.update_data ,width=15, font=("times new roman", 13,"bold"), bg="green", fg="white")
        update_btn.grid(row=0, column=1)
        
        delete_btn=Button(btn_frame, text="Delete", command=self.delete_data,  width=15, font=("times new roman", 13,"bold"), bg="green", fg="white")
        delete_btn.grid(row=0, column=2)
        
        reset_btn=Button(btn_frame, command=self.reset_data, text="Reset",width=15, font=("times new roman", 13,"bold"), bg="green", fg="white")
        reset_btn.grid(row=0, column=3)

        
        btn_frame1=Frame(class_Student_frame,bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0,y=260, width=620,height=100)

        take_btn=Button(btn_frame1, command=self.generate_dataset, text="Take Photo Sample",width=25, font=("times new roman", 13,"bold"), bg="green", fg="white")
        take_btn.grid(row=1, column=0,padx=5)

        update_photo_btn=Button(btn_frame1, text="Update Photo Sample",width=25, font=("times new roman", 13,"bold"), bg="green", fg="white")
        update_photo_btn.grid(row=1, column=1)


        #tight frame

        right_frame=LabelFrame(main_frame,bd=4, relief=RIDGE, text="Student Details", font=("times  new roman", 22 , "bold"))
        right_frame.place(x=660,y=10, width=650, height=580)

        #Search System

        
        Search_frame=LabelFrame(right_frame,bd=2,bg="white", relief=RIDGE, text="Search System", font=("times new roman", 15, "bold"))
        Search_frame.place(x=5,y=10,width=630,height=80)

        self.var_searchTX=StringVar()
        search_Combo=ttk.Combobox(Search_frame, textvariable=self.var_searchTX, font=("times new roman", 13, "bold"),state="readonly" ,width=18)
        search_Combo["values"]=("Select", "Roll_no","Phone_no")
        search_Combo.current(0)
        search_Combo.grid(row=0,column=0,padx=2,pady=10,sticky=W)

        self.var_search=StringVar()
        search_entry = ttk.Entry(Search_frame,textvariable=self.var_search,width=12,font=("verdana",12,"bold"))
        search_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        search_btn=Button(Search_frame, command=self.search_data, text="Search",width=14, font=("times new roman", 13,"bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=2,padx=4)
        
        showAll_btn=Button(Search_frame, command=self.fetch_data, text="Show All",width=14, font=("times new roman", 13,"bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=3)

        #-------------- table frame ----------

        table_frame=Frame(right_frame,bd=2,bg="white", relief=RIDGE)
        table_frame.place(x=5,y=100,width=630,height=250)

        scrollbar_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrollbar_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","name","id","course","year","sem","rollno","phoneNo","gender","dob","division","email","address","teacher","photo"),xscrollcommand=scrollbar_x.set,yscrollcommand=scrollbar_y.set)

        scrollbar_x.pack(side=BOTTOM,fill=X)
        scrollbar_y.pack(side=RIGHT,fill=Y)
        scrollbar_x.config(command=self.student_table.xview)
        scrollbar_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("rollno",text="RollNo")
        self.student_table.heading("phoneNo",text="PhoneNo")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("division",text="Division")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("rollno", width=100)
        self.student_table.column("phoneNo", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("division", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

#====================unction declartion =================

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root", password="12345", database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_id.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_rollno.get(),
                                                                                                                self.var_phoneNo.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_division.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                            ))
            
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added sucessfully",parent=self.root) 
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)

    #=====================fetch data================================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root", password="12345", database="face_recognizer")    
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END, values=i)
                conn.commit()
        conn.close();    

    #========================= get cursor=======================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_name.set(data[1]),
        self.var_id.set(data[2]),
        self.var_course.set(data[3]),
        self.var_year.set(data[4]),
        self.var_sem.set(data[5]),
        self.var_rollno.set(data[6]),
        self.var_phoneNo.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_division.set(data[10]),
        self.var_email.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

#========================update function==========================

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do yo want to update this student details", parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root", password="12345", database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dep=%s,name=%s, course=%s, year=%s, sem=%s, rollno=%s, phoneno=%s,gender=%s, dob=%s, email=%s, address=%s, teacher=%s, photo=%s , division=%s where id=%s",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_rollno.get(),
                                                                                                                self.var_phoneNo.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_division.get(),
                                                                                                                self.var_id.get()
                                                                                                            ))
                
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details sucessfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)

    # delete function
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error", "Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student details", parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root", password="12345", database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where id=%s "
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully delete student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)
                
           #======= reset function ======================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_id.set("")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_rollno.set("")
        self.var_phoneNo.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_division.set("A")
        self.var_email.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

#========================Generate data set take photo sample =================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root", password="12345", database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set dep=%s,name=%s, course=%s, year=%s, sem=%s, rollno=%s, phoneno=%s,gender=%s, dob=%s, email=%s, address=%s, teacher=%s, photo=%s , division=%s where id=%s",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_rollno.get(),
                                                                                                                self.var_phoneNo.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_division.get(),
                                                                                                                self.var_id.get()==id+1
                                                                                                            ))
                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            
            #============================ load front page open cv

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor 1.3
                    #  minimum neighbour 5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,frameM=cap.read()
                    if face_cropped(frameM) is not None :
                        img_id+=1
                        face=cv2.resize(face_cropped(frameM),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/"+"user"+"."+str(id)+"."+str(img_id)+".jpg" 
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croped Face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data set completed !!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)
            
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root", password="12345", database="face_recognizer")
                my_cursor = conn.cursor()
                sql="SELECT dep,name,id, course, year,sem,rollno ,phoneno, gender,dob,division,email,address,teacher,photo from student where rollno='"+str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


#===








                















if __name__ == "__main__":
    root=Tk()
    obj=Student(root)

    root.mainloop()
