# imports
import tkinter
from tkinter import ttk
# splashscreen class 
class MainWindow(tkinter.Tk):
    """ this is the splashscreen, it is a child class of tkinter """
    def __init__(self):
        super().__init__()
        """ splashscreen attributes """
        self.title("Simple Image Editor")
        # to-do -> correctly senter the window
        self.geometry("800x800+600+100")
        self.configure(bg = "#656966")
        self.attributes("-zoomed", True)

if __name__ == "__main__":
    # initialize splashscreen
    MainWindow = MainWindow()
    # run the splash screen
    MainWindow.mainloop()
