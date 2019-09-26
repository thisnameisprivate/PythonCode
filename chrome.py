import tesserocr
from PIL import Image
image = Image.open('D:/image.png')
print(tesserocr.image_to_text(image))





