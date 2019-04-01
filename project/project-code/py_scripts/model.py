from flask import render_template
def showModel():
    
    tst = "HELLO WORLD!"
    return render_template("showModel.html", prediction="Spam")