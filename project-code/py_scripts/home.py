from flask import Flask, render_template, request
import connexion

def home():
    return(render_template("home.html"))
