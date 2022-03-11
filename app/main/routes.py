from flask import Flask, render_template, url_for, Blueprint, redirect, request

main = Blueprint('main', __name__)
    
# Home page
@main.route("/", methods=['GET','POST'])
def index():
    
    return render_template("index.html")