import tkinter as tk 
import mainwindow as mw 
import PIL 
from PIL import Image 
from PIL import ImageTk 
import toplevel_create_image as tci 

class actions():
    """ actions constructor """
    def __init__(self):
        """ actions attributes """
        self.new_image = None 
    
    # create image function
    def create_image(self):
        the_new_image = self.new_image
        the_new_image = Image.new(mode = (tci.top_level_ui.color_mode_combo_box.get()),
                                size = (int(image_width_text_box.get("1.0", mw.tkinter.END)),
                                int(image_height_text_box.get("1.0", mw.tkinter.END)) ),
                                color =  ((int(image_background_color_text_red.get("1.0", mw.tkinter.END))),
                                        (int(image_background_color_text_green.get("1.0", mw.tkinter.END))),
                                        (int(image_background_color_text_blue.get("1.0", mw.tkinter.END)))))
        """
        def create_new_image():
            new_image = Image.new(mode = (color_mode_combo_box.get()),
                                size = (int(image_width_text_box.get("1.0", mw.tkinter.END)),
                                int(image_height_text_box.get("1.0", mw.tkinter.END)) ),
                                color =  ((int(image_background_color_text_red.get("1.0", mw.tkinter.END))),
                                        (int(image_background_color_text_green.get("1.0", mw.tkinter.END))),
                                        (int(image_background_color_text_blue.get("1.0", mw.tkinter.END)))))
            # to-do clear the image
            new_image_compatible = ImageTk.PhotoImage(new_image)
            # load the image on the canvas 
            app.load_image_canvas.delete("all")
            app.load_image_canvas.create_image(0,0, image = new_image_compatible, anchor = mw.tkinter.NW)
            # app.load_image_canvas.grid(row = 0, column = 1)
            toplevel_create_image.destroy()
            # to-do - correct error
            app.load_image_canvas.configure(mw.MainWindow)
            """
