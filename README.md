# Simple image editor
This is a simple image editor with basic functionalities


## TO-DO
Create a splash splashscreen

      - Create a Window that cannot be resized (done)
      - Create window without quit, minimize, maximize button (done)
      - The window should have a background image (done)
      - The window should be transparent
      - The window should be centred (done)
      - Add a Progressbar (done)
      - 
Create Main Window

      - Menu (done)
      - load image canvas

Create new images

      - toplevel window to get the window settings
      - Use the settings to create the image
      - load the image on the main window canvas
      - Fix color picker from closing the create image window (maybe make it's own class)
      - Clear image after loading the first image(bug: when making a new image)
      - Show transparency checked boxes 
      - zoom in / out 
      - pad functionalities 
      - canvas scaling of the images (bug: only updated if the image is bigger)
      - canvas update when creating a new image 

``` python 

app.load_image_canvas.configure(mw.MainWindow) (correct error)
```