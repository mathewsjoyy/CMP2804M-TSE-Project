from flask import render_template, Blueprint, request
from app.models import Reviews

main = Blueprint('main', __name__, template_folder='../templates', static_folder='../static')
    
# Home page
@main.route("/")
@main.route("/home")
def index():
    
    # Grab 3 featured reviews, which are the most recent 5 star reviews
    posts = Reviews.query.filter_by(overall_rating=5).order_by(Reviews.date.desc()).limit(3)
    
    return render_template("index.html", reviews=posts)

# Reviews page
@main.route("/reviews")
def reviews():
    # Paginate / Pagination is where we split items (posts/reviews) into separate pages for readability
    # and also to prevent longer loading times for each page
    page = request.args.get('page', 1, type=int)    # default 1
    
    # Grab 5 posts per page (default)
    posts = Reviews.query.order_by(Reviews.date.desc()).paginate(page=page, per_page=5)
    
    return render_template("reviews.html", reviews=posts)

# Data insights page
@main.route("/insights")
def insights():
    return render_template("insights.html")

# Conclusions page
@main.route("/conclusions")
def conclusions():
    return render_template("conclusions.html")
