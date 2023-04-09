from PIL import Image

image = Image.open(r"E:\Python 20 Projects\new_image.jpg")

print(f"Current image size: {image.size[0]} x {image.size[1]}")
new_image = image.resize((500,500))

new_image.save("new_image.jpg")
