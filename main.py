from tkinter import Tk

from dashboard import LMS


def main() -> None:
    root = Tk()
    app = LMS(root)
    root.mainloop()


if __name__ == "__main__":
    main()
