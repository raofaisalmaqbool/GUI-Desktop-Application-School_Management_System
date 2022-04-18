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

        # set the title bar.. heading... darkblue background
        title = Label(self.root, text="School Management System", font=(
            "goudy old style", 20, "bold"), bg="darkblue", fg="white").place(x=0, y=0, relwidth=1, height=50)


if __name__ == "__main__":     # it is using because i will deale with multiple files
    root = Tk()      # object of tkinter library
    # object of LMS class having arggument root(object of tkinter libraroy)
    obj_lms = LMS(root)

    root.mainloop()   # it for stop the window secren of tkinter
