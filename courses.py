from tkinter import *      # python library used of GUI programming
from PIL import Image, ImageTk


class CourseCls:
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
        title_bar = Label(self.root, text="Manage Course Details",font=(
            "goudy old style", 20, "bold"), bg="#0b5377", fg="white").place(x=10, y=15, width=1180, height=35)

        # ======= Variables ==========   will store the given value form user
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()

        # =========== Label of input fields (fields titles) =============
        Course_Name = Label(self.root, text="Course Name",font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=10, y=60)
        Course_Duration = Label(self.root, text="Duration",font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=10, y=100)
        Course_Charges = Label(self.root, text="Charges",font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=10, y=140)
        Course_Description = Label(self.root, text="Description",font=("goudy old style", 15, "bold"),bg="white", fg="black").place(x=10, y=180)

        # =========== input fields ============  textvariable is keyword
        self.input_Name = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15, "bold"),bg="lightyellow", fg="black")
        self.input_Name.place(x=150, y=60, width=200)    # will show input fields
        input_Duration = Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 15, "bold"),bg="lightyellow", fg="black").place(x=150, y=100, width=200)
        input_Charges = Entry(self.root, textvariable=self.var_charges, font=("goudy old style", 15, "bold"),bg="lightyellow", fg="black").place(x=150, y=140, width=200)
        self.input_Description = Text(self.root, font=("goudy old style", 15, "bold"),bg="lightyellow", fg="black")
        self.input_Description.place(x=150, y=180, height=100, width=470)

        # ========== operational buttons ============
        self.btn_save = Button(self.root, text="Save", font=("goudy old style", 15, "bold"),bg="#2196f3", fg="white", cursor="hand2")
        self.btn_save.place(x=150, y=400, width=110, height=40)
        self.btn_update = Button(self.root, text="Update", font=("goudy old style", 15, "bold"),bg="#4caf50", fg="white", cursor="hand2")
        self.btn_update.place(x=270, y=400, width=110, height=40)
        self.btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"),bg="#f44336", fg="white", cursor="hand2")
        self.btn_delete.place(x=390, y=400, width=110, height=40)
        self.btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"),bg="#607d8b", fg="white", cursor="hand2")
        self.btn_clear.place(x=510, y=400, width=110, height=40)



if __name__ == "__main__":     # it is using because i will deale with multiple files
    root = Tk()      # object of tkinter library
    # object of LMS class having arggument root(object of tkinter libraroy)
    obj_lms = CourseCls(root)

    root.mainloop()   # it for stop the window secren of tkinter