# import
import splashscreen as ss 

# initialize splashscreen
ss.SplashScreen = ss.SplashScreen()

# splashscreen_background_image
# to do -> set path to relative
splashscreen_background_image = ss.tkinter.PhotoImage(file = "/home/daudi/Desktop/simple_image_editor/src/assets/images/splashscreen_background.png")

# splashscreen_background_label
splashscreen_background_label = ss.tkinter.Label(ss.SplashScreen, image = splashscreen_background_image)
splashscreen_background_label.grid(row = 0, column = 0)

# run splashscreen loop
ss.SplashScreen.mainloop()