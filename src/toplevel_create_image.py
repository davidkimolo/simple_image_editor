# imports
import mainwindow as mw 
import PIL 
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
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
        image_background_color_label = mw.tkinter.Label(toplevel_create_image, text = "Background color: ",
                                                font = ("", 15), bg = "#a1a1a1", fg = "white")
        image_background_color_label.grid(row = 3, column = 0, padx = 30)

        image_background_color_text = mw.tkinter.Text(toplevel_create_image, width = 20, height = 2,
                                                bg  = "grey", fg = "white")
        image_background_color_text.grid(row = 3, column = 1)

        # create_new_image
        def create_new_image():
            new_image = Image.new(mode = (color_mode_combo_box.get()),
                                size = (int(image_width_text_box.get("1.0", mw.tkinter.END)),
                                int(image_height_text_box.get("1.0", mw.tkinter.END)) ),
                                color =  (255, 255, 255, 0))
            new_image.show()
            new_image_compatible = ImageTk.PhotoImage(new_image)
            toplevel_create_image.destroy()
            return new_image_compatible

        
        # create_image_button
        create_image_button = mw.tkinter.Button(toplevel_create_image, text = "create image",
                                                bg = "grey", fg = "white", font = ("times", 13,"bold"),
                                                command = create_new_image)
        create_image_button.grid(row = 4, column = 0, padx = 40, pady = 20)

# initialize main window
if __name__ == "__main__":
    mw.MainWindow = mw.MainWindow()
    # run main window
    mw.MainWindow.mainloop()