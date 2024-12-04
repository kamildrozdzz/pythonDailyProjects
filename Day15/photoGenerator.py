from PIL import Image

width = 400
height = 400

img = Image.new(mode = "CMYK", size = (width,height), color = (150,150,150,90))
img.show()
