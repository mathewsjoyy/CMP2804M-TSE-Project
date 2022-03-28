from flask import render_template, Blueprint

main = Blueprint('main', __name__, template_folder='../templates', static_folder='../static')
    
# Home page
@main.route("/", methods=['GET'])
def index():
    
    return render_template("index.html")
