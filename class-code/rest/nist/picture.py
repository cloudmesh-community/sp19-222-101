from flask import jsonify
from PIL import Image

def showPic():
    img = Image.open("./image.png")
    img.show()
