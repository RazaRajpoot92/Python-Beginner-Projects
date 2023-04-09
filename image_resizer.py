"""
                     IMAGE RESIZER
    
    You need install Pillow, If you don't have.
    command : pip install Pillow

"""
from PIL import Image

image = Image.open("Enter image Path")
width = image[0]
length = image[1]
print(f"Current image size: {width} x {length}")
#Enter your specific image size.
new_image = image.resize((500,500))
#Save your image with your specific extension. eg. .png .jpeg etc.
new_image.save("new_image.png")
