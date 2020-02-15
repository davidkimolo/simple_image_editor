# imports
import tkinter

# splashscreen class 
class SplashScreen(tkinter.Tk):
    """ this is the splashscreen, it is a child class of tkinter """
    def __init__(self):
        super().__init__()
        """ splashscreen attributes """
        self.title("Splashscreen")
        self.geometry("600x600")
        self.configure(bg = "sky blue")
        self.resizable(width = False, height = False)
        self.overrideredirect(True)




if __name__ == "__main__":
    # initialize splashscreen
    SplashScreen = SplashScreen()
    # run the splash screen
    SplashScreen.mainloop()
