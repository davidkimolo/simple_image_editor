# import
import splashscreen as ss 
import time

# initialize splashscreen
ss.SplashScreen = ss.SplashScreen()
# splashscreen variables
load_time = 100
# splashscreen_background_image
# to do -> set path to relative
splashscreen_background_image = ss.tkinter.PhotoImage(file = "/home/daudi/Desktop/simple_image_editor/src/assets/images/splashscreen_background.png")

# splashscreen_background_label
splashscreen_background_label = ss.tkinter.Label(ss.SplashScreen, image = splashscreen_background_image)
splashscreen_background_label.grid(row = 0, column = 0)

# splashscreen_progressbar_style
splashscreen_progressbar_style = ss.ttk.Style(ss.SplashScreen)
# set theme
splashscreen_progressbar_style.theme_use("default")
# configure theme
splashscreen_progressbar_style.configure("black.Horizontal.TProgressbar", background = "green")

# splashscreen_progressbar
splashscreen_progressbar = ss.ttk.Progressbar(ss.SplashScreen, length = 600, maximum = load_time,
                                                style = "black.Horizontal.TProgressbar")
splashscreen_progressbar.grid(row = 0, column = 0)
# load progressbar
def load_progress_bar():
    count_timer = 0
    while(count_timer < load_time):
        splashscreen_progressbar.step(1)
        splashscreen_progressbar.update_idletasks()
        time.sleep(0.02)
        splashscreen_progressbar["value"] = count_timer
        count_timer += 1

# do action
ss.SplashScreen.after(load_time, load_progress_bar)

# run splashscreen loop
ss.SplashScreen.mainloop()