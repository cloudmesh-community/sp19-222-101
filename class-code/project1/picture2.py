from PIL import Image

def showPic():
    img = Image.open("./monkey.jpg")
    img.show()
    return "Here is your monkey!"
