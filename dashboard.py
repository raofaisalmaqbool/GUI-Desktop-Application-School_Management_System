from tkinter import *      # python library used of GUI programming

class LMS:
    def __init__(self, root):   # default constructor of LMS class having orguments of self(bydefault) & root
        pass

if __name__ == "__main__":     # it is using because i will deale with multiple files
    root = Tk()      # object of tkinter library
    obj_lms = LMS(root)   # object of LMS class having arggument root(object of tkinter libraroy)

    root.mainloop()   # it for stop the window secren of tkinter