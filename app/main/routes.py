from flask import render_template, Blueprint

main = Blueprint('main', __name__)
    
# Home page
@main.route("/", methods=['GET', 'POST'])
def index():
    
    return render_template("index.html")
