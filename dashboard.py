from tkinter import *      # python library used of GUI programming
from PIL import Image, ImageTk


class LMS:
    # default constructor of LMS class having orguments of self(bydefault) & root
    def __init__(self, root):
        self.root = root  # re-initilize the root ,, attribute
        # change the title of of application
        self.root.title("School Management System")
        # change the size and (height, width, margan pading)
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")     # color of background

        #==== Logo ======
        self.logo = ImageTk.PhotoImage(file="img/logo-small.png")    # adding image with title

        #==== Title bar ======
        # set the title bar.. heading... darkblue background
        title = Label(self.root, text="School Management System", compound=LEFT, padx=20, image=self.logo, font=(
            "goudy old style", 20, "bold"), bg="darkblue", fg="white").place(x=0, y=0, relwidth=1, height=50)

        #==== Main Frame ======
        M_Frame = LabelFrame(self.root, text="Menu", font=("times new roman",15), bg="white")
        M_Frame.place(x=10, y=70, width=1340, height=80)

        #===== Buttons in the Menu =======
        but_courses = Button(M_Frame, text="Courses", font=("goudy old style",15,"bold"), bg="#0b5377", fg="white", cursor="hand2").place(x=20, y=5, height=40, width=200)
        but_teachers = Button(M_Frame, text="Teachers", font=("goudy old style",15,"bold"), bg="#0b5377", fg="white", cursor="hand2").place(x=240, y=5, height=40, width=200)
        but_students = Button(M_Frame, text="Students", font=("goudy old style",15,"bold"), bg="#0b5377", fg="white", cursor="hand2").place(x=460, y=5, height=40, width=200)
        but_result = Button(M_Frame, text="Result", font=("goudy old style",15,"bold"), bg="#0b5377", fg="white", cursor="hand2").place(x=680, y=5, height=40, width=200)
        but_view = Button(M_Frame, text="View Students Results", font=("goudy old style",15,"bold"), bg="#0b5377", fg="white", cursor="hand2").place(x=900, y=5, height=40, width=200)
        but_logout = Button(M_Frame, text="Logout", font=("goudy old style",15,"bold"), bg="#0b5377", fg="white", cursor="hand2").place(x=1120, y=5, height=40, width=200)
        # but_exit = Button(M_Frame, text="Exit", font=("goudy old style",15,"bold"), bg="#0b5377", fg="white", cursor="hand2").place(x=1050, y=5, height=40, width=200)

if __name__ == "__main__":     # it is using because i will deale with multiple files
    root = Tk()      # object of tkinter library
    # object of LMS class having arggument root(object of tkinter libraroy)
    obj_lms = LMS(root)

    root.mainloop()   # it for stop the window secren of tkinter
