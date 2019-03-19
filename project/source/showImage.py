from PIL import Image
from flask import send_file
def showImage():
    img = Image.open("monkey.jpg")
    return send_file(img,attachment_filename="monkey.jpg",mimetype="image/jpg")
