from PIL import Image 

my_image = Image.open("assets/images/splashscreen_background.png")

width, height = my_image.size

print(height)
