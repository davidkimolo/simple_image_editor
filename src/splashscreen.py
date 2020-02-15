# imports
import tkinter
from tkinter import ttk
# splashscreen class 
class SplashScreen(tkinter.Tk):
    """ this is the splashscreen, it is a child class of tkinter """
    def __init__(self):
        super().__init__()
        """ splashscreen attributes """
        self.title("Splashscreen")
        # to-do -> correctly senter the window
        self.geometry("600x600+600+250")
        self.configure(bg = "sky blue")
        self.resizable(width = False, height = False)
        self.overrideredirect(True)
        self.wait_visibility()
        self.attributes("-alpha", 0.5)




if __name__ == "__main__":
    # initialize splashscreen
    SplashScreen = SplashScreen()
    # run the splash screen
    SplashScreen.mainloop()
