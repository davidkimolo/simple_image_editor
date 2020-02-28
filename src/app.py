# import
import splashscreen as ss 
import mainwindow as mw
import toplevel_create_image as tci 
from tkinter import filedialog
import PIL
from PIL import ImageTk, Image
import time

# initialize splashscreen
ss.SplashScreen = ss.SplashScreen()
# splashscreen variables
load_time = 100
# splashscreen_background_image
# to do -> set path to relative
splashscreen_background_image = ss.tkinter.PhotoImage(file = "assets/images/splashscreen_background.png")

# splashscreen_background_label
splashscreen_background_label = ss.tkinter.Label(ss.SplashScreen, image = splashscreen_background_image)
splashscreen_background_label.grid(row = 1, column = 0)

# splashscreen_progressbar_style
# to do -> make progressbar thin
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

def load_main_window():
    ss.SplashScreen.destroy()



# do action
ss.SplashScreen.after(load_time, load_progress_bar)
# load mainwindow openfunction
ss.SplashScreen.after(load_time+1, load_main_window)

# run splashscreen loop
ss.SplashScreen.mainloop()

# load main window
# initialization
mw.MainWindow = mw.MainWindow()
# mainwindow_menu_bar
mainwindow_menu_bar = mw.tkinter.Menu(mw.MainWindow, font = ("times", 10, "bold"), bg  = "#787878", fg = "white")

default_image = mw.tkinter.PhotoImage(file = "assets/images/splashscreen_background.png")

# default_canvas

load_image_canvas = mw.tkinter.Canvas(mw.MainWindow, height = 800, width = 800)
load_image_canvas.create_image(0,0, image = default_image, anchor = mw.tkinter.NW)
load_image_canvas.grid(row = 0, column = 1)

# open image
def open_the_image():
    image_path = filedialog.askopenfilename()
    open_image = Image.open(image_path)
    global converted
    converted = ImageTk.PhotoImage(open_image)
    return converted

# change_image
def change_image():

    open_the_image ()
    # load the image
    load_image_canvas = mw.tkinter.Canvas(mw.MainWindow, height = 800, width = 800)
    load_image_canvas.create_image(0,0, image = converted, anchor = mw.tkinter.NW)
    load_image_canvas.grid(row = 0, column = 1)

# initialize main window items
file_items = mw.tkinter.Menu(mainwindow_menu_bar)
edit_items = mw.tkinter.Menu(mainwindow_menu_bar)
image_items = mw.tkinter.Menu(mainwindow_menu_bar)
filters_items = mw.tkinter.Menu(mainwindow_menu_bar)
compositing_items = mw.tkinter.Menu(mainwindow_menu_bar)
help_items = mw.tkinter.Menu(mainwindow_menu_bar)

# add file items
file_items.add_command(label = "new", command = tci.TopLevelCreateImage)
file_items.add_command(label = "open", command = change_image)
file_items.add_command(label = "0pen as", command = "")
file_items.add_command(label = "save", command = "")
file_items.add_command(label = "save as ", command = "")
file_items.add_command(label = "export", command = "")
file_items.add_command(label = "exit", command = mw.MainWindow.quit)

# add edit items
edit_items.add_command(label = "undo", command = "")
edit_items.add_command(label = "redo", command = "")
edit_items.add_command(label = "copy", command = "")
edit_items.add_command(label = "paste", command = "")
# add image items
image_items.add_command(label = "brightness and contrast", command = "")
image_items.add_command(label = "black and white", command = "")
image_items.add_command(label = "image size", command = "")
image_items.add_command(label = "image rotation", command = "")
image_items.add_command(label = "crop", command = "")
# add filters items
filters_items.add_command(label = "pop", command = "")
filters_items.add_command(label = "cartoon", command = "")
filters_items.add_command(label = "lines", command = "")
# add compositing items
compositing_items.add_command(label = "new composition", command = "")
compositing_items.add_command(label = "composite from scene", command = "")
# add help items
help_items.add_command(label = "about", command = "")
help_items.add_command(label = "documentation", command = "")

# add menu items 
mainwindow_menu_bar.add_cascade(label = "File", menu = file_items)
mainwindow_menu_bar.add_cascade(label = "Edit", menu = edit_items)
mainwindow_menu_bar.add_cascade(label = "Image", menu = image_items)
mainwindow_menu_bar.add_cascade(label = "Filter", menu = filters_items)
mainwindow_menu_bar.add_cascade(label = "Compositing", menu = compositing_items)
mainwindow_menu_bar.add_cascade(label = "Help", menu = help_items)




# get_new_image
def get_new_image():
    
    the_new_image = mw.tkinter.PhotoImage(file = "assets/images/splashscreen_background.png")
    try:
        # initialized = tci.TopLevelCreateImage() 
        pass
    except:
        return the_new_image
    return the_new_image

the_image = get_new_image()

# assign the function to a variable

# load_image_canvas




# try


# add menu bar to window
mw.MainWindow.configure(menu = mainwindow_menu_bar)
load_image_canvas.update_idletasks()
load_image_canvas.update()
# run mainwindow loop
mw.MainWindow.mainloop()
