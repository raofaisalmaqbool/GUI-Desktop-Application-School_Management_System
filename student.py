from cProfile import label
from tkinter import *
# from tokenize import String      # python library used of GUI programming
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pymysql as mq
from project_db import insert_student, fetch_all_students, fetch_student_by_roll, update_student, delete_student, search_students


class StudentCls:
    # default constructor of LMS class having orguments of self(bydefault) & root
    def __init__(self, root):
        self.root = root  # re-initilize the root ,, attribute
        # change the title of of application
        self.root.title("LMS")
        # change the size and (height, width, margan pading)
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")     # color of background
        self.root.focus_force()

        # ==== Title bar ======
        # set the title bar.. heading... darkblue background         "fg used for font"
        title_bar = Label(self.root, text="Manage Student Details", font=(
            "goudy old style", 20, "bold"), bg="#0b5377", fg="white").place(x=10, y=15, width=1180, height=35)

        # ======= Variables ==========   will store the given value form user
        self.var_rollno = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contect = StringVar()
        self.var_course = StringVar()
        self.var_atdn_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()

        # =========== Label of input fields (fields titles) =============
        Student_Rollno = Label(self.root, text="Roll No", font=(
            "goudy old style", 15, "bold"), bg="white", fg="black").place(x=10, y=80)
        Student_Name = Label(self.root, text="Name", font=(
            "goudy old style", 15, "bold"), bg="white", fg="black").place(x=10, y=120)
        Student_Email = Label(self.root, text="Email", font=(
            "goudy old style", 15, "bold"), bg="white", fg="black").place(x=10, y=160)
        Student_Gender = Label(self.root, text="Gender", font=(
            "goudy old style", 15, "bold"), bg="white", fg="black").place(x=10, y=200)
        Student_State = Label(self.root, text="State", font=(
            "goudy old style", 15, "bold"), bg="white", fg="black").place(x=10, y=240)
        Student_Address = Label(self.root, text="Address", font=(
            "goudy old style", 15, "bold"), bg="white", fg="black").place(x=10, y=280)

        # =========== input fields ============  textvariable is keyword
        self.input_rollno = Entry(self.root, textvariable=self.var_rollno, font=(
            "goudy old style", 15, "bold"), bg="lightyellow", fg="black")
        # will show input fields
        self.input_rollno.place(x=150, y=80, width=200)
        input_name = Entry(self.root, textvariable=self.var_name, font=(
            "goudy old style", 15, "bold"), bg="lightyellow", fg="black").place(x=150, y=120, width=200)
        input_email = Entry(self.root, textvariable=self.var_email, font=(
            "goudy old style", 15, "bold"), bg="lightyellow", fg="black").place(x=150, y=160, width=200)
        self.input_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select","Male","Female"), font=(
            "goudy old style", 15, "bold"), state="readonly", justify=CENTER)
        self.input_gender.place(x=150, y=200, width=200)
        self.input_gender.current(0)
        input_state = Entry(self.root, textvariable=self.var_state, font=(
            "goudy old style", 15, "bold"), bg="lightyellow", fg="black").place(x=150, y=240, width=200)
        self.input_address = Text(self.root, font=(
            "goudy old style", 15, "bold"), bg="lightyellow", fg="black")
        self.input_address.place(x=150, y=280, height=30, width=200)


        # ========== operational buttons ============
        self.btn_save = Button(self.root, text="Save", font=(
            "goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.save)
        self.btn_save.place(x=150, y=400, width=110, height=40)
        self.btn_update = Button(self.root, text="Update", font=(
            "goudy old style", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2", command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)
        self.btn_delete = Button(self.root, text="Delete", font=(
            "goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2", command=self.delete_row)
        self.btn_delete.place(x=390, y=400, width=110, height=40)
        self.btn_clear = Button(self.root, text="Clear", font=(
            "goudy old style", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2", command=self.clear_data)
        self.btn_clear.place(x=510, y=400, width=110, height=40)

        # ========== Search Area ============
        self.var_search = StringVar()
        Course_Name = Label(self.root, text="Roll No / Name", font=(
            "goudy old style", 15, "bold"), bg="white", fg="black").place(x=660, y=80)
        input_Course_Name = Entry(self.root, textvariable=self.var_search,font=(
            "goudy old style", 15, "bold"), bg="lightyellow", fg="black").place(x=810, y=80, width=250)
        btn_Course_Search = Button(self.root, text="Search", font=(
            "goudy old style", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2", command=self.search_bar).place(x=1090, y=80, width=100, height=27)

        # ======= content / record of courses ========
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=660, y=120, height=320, width=530)

        # ========= create table frame inside the course content ========
        # make scroll bar inside table frame
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)

        # ======= create table layout ========
        self.courseTable = ttk.Treeview(self.C_Frame, columns=(
            "sid", "roll_no", "name", "email", "gender", "state", "address"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)    # showing side bar
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.courseTable.xview)   # for view x and y of scrol bar
        scrolly.config(command=self.courseTable.yview)   # this will move up and down, left and right easily

        self.courseTable.heading("sid", text="ID")       # create table heading
        self.courseTable.heading("roll_no", text="Roll No")
        self.courseTable.heading("name", text="Name")
        self.courseTable.heading("email", text="Email")
        self.courseTable.heading("gender", text="Gender")
        self.courseTable.heading("state", text="State")
        self.courseTable.heading("address", text="Address")

        # show only heading colomn not extra one
        self.courseTable["show"] = "headings"

        self.courseTable.column("sid", width=10)       # create table colomn
        self.courseTable.column("roll_no", width=80)
        self.courseTable.column("name", width=120)
        self.courseTable.column("email", width=150)
        self.courseTable.column("gender", width=70)
        self.courseTable.column("state", width=100)
        self.courseTable.column("address", width=150)

        self.courseTable.pack(fill=BOTH, expand=1)    # show create table layout

        self.courseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()


    #==========  backend functions start ============

    def save(self):
        try:
            if self.var_rollno.get() == "" or self.var_name.get() == "":
                messagebox.showerror("Error","Roll No and Name are required", parent=self.root)
                return

            roll_no = self.var_rollno.get()
            existing = fetch_student_by_roll(roll_no)
            if existing is not None:
                messagebox.showerror("Error","Student with this Roll No already exists", parent=self.root)
                return

            name_val = self.var_name.get()
            email_val = self.var_email.get()
            gender_val = self.var_gender.get()
            state_val = self.var_state.get()
            address_val = self.input_address.get("1.0", END).strip()
            data = (roll_no, name_val, email_val, gender_val, state_val, address_val)

            insert_student(data)
            self.show()
            messagebox.showinfo("Success","Student added successfully", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    # ===== This will show the data in the table ========
    def show(self):   # 1st
        try:
            rows = fetch_all_students()
            self.courseTable.delete(*self.courseTable.get_children())     # will delete all pre childern element of table 
            for row in rows:    # will show the data in tabel by itreating
                self.courseTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)


    # =========== this is for show table data in the fields for update ========
    def get_data(self, evnt):    #2nd   # for binding event one argument is mendetory "evnt"
        self.input_rollno.config(state="readonly")
        r=self.courseTable.focus()
        content = self.courseTable.item(r)
        row = content["values"]

        if not row:
            return

        self.var_rollno.set(row[1])     # using set function hear
        self.var_name.set(row[2])
        self.var_email.set(row[3])
        self.var_gender.set(row[4])
        self.var_state.set(row[5])

        self.input_address.delete('1.0', END)
        self.input_address.insert(END, row[6])


    def update(self):
        try:
            if self.var_rollno.get()=="":    # validation
                messagebox.showerror("Error","Please select a student", parent=self.root)
            else:
                roll_no = self.var_rollno.get()
                name_val = self.var_name.get()
                email_val = self.var_email.get()
                gender_val = self.var_gender.get()
                state_val = self.var_state.get()
                address_val = self.input_address.get("1.0", END).strip()
                data = (name_val, email_val, gender_val, state_val, address_val, roll_no)

                update_student(data)
                self.show()
                messagebox.showinfo("Success","Record Updated Successfully!!!!!", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)


# ======== this function is for clear the field data and enter new data ======= 
    def clear_data(self):
        self.show()
        self.var_rollno.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_state.set("")
        self.var_search.set("")
        self.input_address.delete('1.0', END)
        self.input_rollno.config(state=NORMAL)    # state was readonly but now its normal


# ========= this function is work for delete record from table =======
    def delete_row(self):
        try:
            if self.var_rollno.get()=="":
                messagebox.showerror("error", "Please select any student to delete", parent=self.root)
            else:
                op = messagebox.askyesno("Confirm", "Are you want to delete", parent=self.root)
                if op == True:
                    var = self.var_rollno.get()
                    delete_student(var)
                    self.clear_data()
                    self.show()
                    self.input_rollno.config(state=NORMAL)
                    messagebox.showinfo("Success","Record deleted", parent=self.root)

        except Exception as ex:
            pass


    def search_bar(self):
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Alert","Please enter something", parent=self.root)
            else:
                in_data = self.var_search.get()
                rows = search_students(in_data)
                # print(rows)
                self.courseTable.delete(*self.courseTable.get_children())     # will delete all pre childern element of table 
                for row in rows:    # will show the data in tabel by itreating
                    self.courseTable.insert('', END, values=row)
                # self.input_rollno.config(state=NORMAL)
                
        except Exception as ex:
            print(ex)
        



if __name__ == "__main__":     # it is using because i will deale with multiple files
    root = Tk()      # object of tkinter library
    # object of LMS class having arggument root(object of tkinter libraroy)
    obj_lms = StudentCls(root)

    root.mainloop()   # it for stop the window secren of tkinter
