from tkinter import *      # python library used of GUI programming
from PIL import Image, ImageTk
from courses import *


class LMS:
    # default constructor of LMS class having orguments of self(bydefault) & root
    def __init__(self, root):
        self.root = root  # re-initilize the root ,, attribute
        # change the title of of application
        self.root.title("LMS")
        # change the size and (height, width, margan pading)
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")     # color of background

        # ==== Logo ======
        # this is due to resize the image
        self.logo = Image.open("img/logo-small.png")
        self.logo = self.logo.resize((40, 40), Image.ANTIALIAS)   # resizing the image
        self.logo = ImageTk.PhotoImage(self.logo)  # adding image with title,, dont know the path of image
        # self.logo = ImageTk.PhotoImage(file="img/logo-small.png")

        # ==== Title bar ======
        # set the title bar.. heading... darkblue background        "fg used for font"
        title_bar = Label(self.root, text="School Management System", compound=LEFT, padx=20, image=self.logo, font=(
            "goudy old style", 20, "bold"), bg="#0b5377", fg="white").place(x=0, y=0, relwidth=1, height=50)

        # ==== Main Frame ======
        M_Frame = LabelFrame(self.root, text="Menu", font=(
            "times new roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=1340, height=80)

        # ===== Buttons in the Menu =======
        but_courses = Button(M_Frame, text="Courses", font=("goudy old style", 15, "bold"), command=self.add_course,
                             bg="#0b5377", fg="white", cursor="hand2").place(x=20, y=5, height=40, width=200)
        but_teachers = Button(M_Frame, text="Teachers", font=("goudy old style", 15, "bold"),
                              bg="#0b5377", fg="white", cursor="hand2").place(x=240, y=5, height=40, width=200)
        but_students = Button(M_Frame, text="Students", font=("goudy old style", 15, "bold"),
                              bg="#0b5377", fg="white", cursor="hand2").place(x=460, y=5, height=40, width=200)
        but_result = Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"),
                            bg="#0b5377", fg="white", cursor="hand2").place(x=680, y=5, height=40, width=200)
        but_view = Button(M_Frame, text="View Students Results", font=("goudy old style", 15, "bold"),
                          bg="#0b5377", fg="white", cursor="hand2").place(x=900, y=5, height=40, width=200)
        but_logout = Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"),
                            bg="#0b5377", fg="white", cursor="hand2").place(x=1120, y=5, height=40, width=200)
        # but_exit = Button(M_Frame, text="Exit", font=("goudy old style",15,"bold"), bg="#0b5377", fg="white", cursor="hand2").place(x=1050, y=5, height=40, width=200)

        # this is due to resize the image
        self.main_img = Image.open("img/img2.png")
        self.main_img = self.main_img.resize(
            (920, 350), Image.ANTIALIAS)   # resizing the image
        # adding image with title,, dont know the path of image
        self.main_img = ImageTk.PhotoImage(self.main_img)

        # show the image on secreen
        self.label_main_img = Label(self.root, image=self.main_img).place(
            x=400, y=160, width=920, height=350)

        # ===== Update Details Widgets =====
        self.course_details = Label(self.root, text="Total Courses\n[0]", font=(
            "goudy old style", 20), bd=10, relief=RIDGE, bg="#e43b06")
        self.course_details.place(x=400, y=530, width=300, height=100)

        self.student_details = Label(self.root, text="Total Students\n[0]", font=(
            "goudy old style", 20), bd=10, relief=RIDGE, bg="#0676ad")
        self.student_details.place(x=710, y=530, width=300, height=100)

        self.result_details = Label(self.root, text="Total Results\n[0]", font=(
            "goudy old style", 20), bd=10, relief=RIDGE, bg="#038074")
        self.result_details.place(x=1020, y=530, width=300, height=100)

        # ==== Footer ====
        footer = Label(self.root, text="School Management System\nInfinity Solution", font=(
            "goudy old style", 15), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)

    #====== function for add course window ========
    # ==== call this function on course button using command ========
    def add_course(self):
        self.course_win = Toplevel(self.root)    # attribute for course window
        self.course_obj = CourseCls(self.course_win)   # object of CourseCls class


if __name__ == "__main__":     # it is using because i will deale with multiple files
    root = Tk()      # object of tkinter library
    # object of LMS class having arggument root(object of tkinter libraroy)
    obj_lms = LMS(root)

    root.mainloop()   # it for stop the window secren of tkinter
