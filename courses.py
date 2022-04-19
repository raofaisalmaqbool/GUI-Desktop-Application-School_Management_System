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


       

if __name__ == "__main__":     # it is using because i will deale with multiple files
    root = Tk()      # object of tkinter library
    # object of LMS class having arggument root(object of tkinter libraroy)
    obj_lms = CourseCls(root)

    root.mainloop()   # it for stop the window secren of tkinter