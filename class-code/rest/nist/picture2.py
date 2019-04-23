from PIL import Image

def showPic():
    img = Image.open("./monkey.jpg")
    img.show()
