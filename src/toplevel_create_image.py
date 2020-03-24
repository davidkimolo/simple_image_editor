# imports
import mainwindow as mw 
import PIL 
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
import app 
# top level window class

class TopLevelCreateImage():
    """ this will create a top level window where you can create settings for new images """
    def __init__(self):
        """ create top level window object """
        toplevel_create_image = mw.tkinter.Toplevel(mw.MainWindow, bg = "#a1a1a1")
        """ top level window attributes"""
        toplevel_create_image.title("create new image")
        toplevel_create_image.geometry("800x600+600+200")
        toplevel_create_image.resizable(width = False, height = False)
        self. top_down = 60

        # UI
        image_width_label = mw.tkinter.Label(toplevel_create_image, text = "Width: ",
                                            font = ("", 15), bg = "#a1a1a1", fg = "white")
        image_width_label.grid(row = 0, column = 0, padx = 20, pady  = 20)
        image_height_label = mw.tkinter.Label(toplevel_create_image, text = "Height: ",
                                                font = ("", 15), bg = "#a1a1a1", fg = "white")
        image_height_label.grid(row = 1, column = 0)

        # text box image size 
        image_width_text_box = mw.tkinter.Text(toplevel_create_image, width = 20, height = 2,
                                                bg  = "grey", fg = "white")
        image_width_text_box.grid(row = 0, column = 1, pady = 20)

        image_height_text_box = mw.tkinter.Text(toplevel_create_image, width = 20, height = 2,
                                                bg  = "grey", fg = "white")
        image_height_text_box.grid(row = 1, column = 1)

        # color mode
        color_mode_combo_box = mw.tkinter.Label(toplevel_create_image, text = "color mode: ",
                                                font = ("", 15), bg = "#a1a1a1", fg = "white")
        color_mode_combo_box.grid(row = 2, column = 0, padx = 20, pady  = 20)

        # image_color_mode_text = mw.tkinter.Text(toplevel_create_image, width = 20, height = 2,
        #                                         bg  = "grey", fg = "white")
        # image_color_mode_text.grid(row = 2, column = 1)

        color_mode_combo_box = ttk.Combobox(toplevel_create_image, values = [
            "RGB",
            "RGBA",
            "CYMA"
        ])
        color_mode_combo_box.current(0)
        color_mode_combo_box.grid(row = 2, column = 1)

        # background color
        image_background_color_label = mw.tkinter.Label(toplevel_create_image, text = "red: ",
                                                font = ("", 15), bg = "#a1a1a1", fg = "white")
        image_background_color_label.grid(row = 3, column = 0, padx = 30)

        image_background_color_text_red = mw.tkinter.Text(toplevel_create_image, width = 20, height = 2,
                                                bg  = "grey", fg = "white")
        image_background_color_text_red.grid(row = 3, column = 1)
# -----------------------------------------------------------------------------------------------------------
        image_background_color_label = mw.tkinter.Label(toplevel_create_image, text = "green: ",
                                                font = ("", 15), bg = "#a1a1a1", fg = "white")
        image_background_color_label.grid(row = 4, column = 0, padx = 30)

        image_background_color_text_green = mw.tkinter.Text(toplevel_create_image, width = 20, height = 2,
                                                bg  = "grey", fg = "white")
        image_background_color_text_green.grid(row = 4, column = 1)

# ----------------------------------------------------------------------------------------------------------
        image_background_color_label = mw.tkinter.Label(toplevel_create_image, text = "blue: ",
                                                font = ("", 15), bg = "#a1a1a1", fg = "white")
        image_background_color_label.grid(row = 5, column = 0, padx = 30)

        image_background_color_text_blue = mw.tkinter.Text(toplevel_create_image, width = 20, height = 2,
                                                bg  = "grey", fg = "white")
        image_background_color_text_blue.grid(row = 5, column = 1)
        # create_new_image
        def create_new_image():
            new_image = Image.new(mode = (color_mode_combo_box.get()),
                                size = (int(image_width_text_box.get("1.0", mw.tkinter.END)),
                                int(image_height_text_box.get("1.0", mw.tkinter.END)) ),
                                color =  ((int(image_background_color_text_red.get("1.0", mw.tkinter.END))),
                                        (int(image_background_color_text_green.get("1.0", mw.tkinter.END))),
                                        (int(image_background_color_text_blue.get("1.0", mw.tkinter.END)))))
            #  get new image properties
            the_width, the_height = new_image.size
            # to-do clear the image
            new_image_compatible = ImageTk.PhotoImage(new_image)
            # load the image on the canvas 
            app.default_image_canvas.delete("all")
            # app.default_image_canvas = mw.tkinter.Canvas(toplevel_create_image, height = the_height, width = the_width)
            app.default_image_canvas.create_image(0,0, image = new_image_compatible, anchor = mw.tkinter.NW)
            # app.load_image_canvas.grid(row = 0, column = 1)
            toplevel_create_image.destroy()
            # to-do - correct error
            app.default_image_canvas.configure(mw.MainWindow)
            


        # create_image_button
        create_image_button = mw.tkinter.Button(toplevel_create_image, text = "create image",
                                                bg = "grey", fg = "white", font = ("times", 13,"bold"),
                                                command = create_new_image)
        create_image_button.grid(row = 6, column = 0, padx = 40, pady = 20)

# initialize main window
if __name__ == "__main__":
    pass 
    # mw.MainWindow = mw.MainWindow()
    # run main window
    # mw.MainWindow.mainloop()