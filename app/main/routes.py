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
latest_posts = True    # Flag to check if we need to grab the latest posts
setup = True    # Flag to check if we need to setup the filter course dropdown
courses = ['ALL']    # List of all courses to allow user to filter by course
current_course_filter = 'ALL'    # Current course filter

@main.route("/reviews", methods=['GET', 'POST'])
def reviews():
    # Need to make this global so we can change it in the function
    global latest_posts, setup, current_course_filter
    
    # Paginate / Pagination is where we split items (posts/reviews) into separate pages for readability
    # and also to prevent longer loading times for each page
    page = request.args.get('page', 1, type=int)    # default 1
    
    # Grab 5 posts per page (default)
    if latest_posts:
        posts = Reviews.query.order_by(Reviews.date.desc()).paginate(page=page, per_page=5)
    else:
        posts = Reviews.query.order_by(Reviews.date.asc()).paginate(page=page, per_page=5)
    
    # Check if we receive a POST request
    if request.method == "POST":
        if request.form.get("latest"):
            if current_course_filter != 'ALL':    # If we have a course filter then filter by that
                posts = Reviews.query.filter_by(course=current_course_filter).order_by(Reviews.date.desc()).paginate(page=page, per_page=5)
            else:
                posts = Reviews.query.order_by(Reviews.date.desc()).paginate(page=page, per_page=5)
            latest_posts = True
        elif request.form.get("oldest"):
            if current_course_filter != 'ALL':
                posts = Reviews.query.filter_by(course=current_course_filter).order_by(Reviews.date.asc()).paginate(page=page, per_page=5)
            else:
                posts = Reviews.query.order_by(Reviews.date.asc()).paginate(page=page, per_page=5)
            latest_posts = False
        elif request.form.get("course_select"):  
            course_selection = request.form.get('course_select')
            current_course_filter = course_selection
            if course_selection == 'ALL':    # If we select 'ALL' then we want to grab all posts
                posts = Reviews.query.order_by(Reviews.date.desc()).paginate(page=page, per_page=5)
            else:
                posts = Reviews.query.filter_by(course=course_selection).order_by(Reviews.date.desc()).paginate(page=page, per_page=5)
    
    # Check if we need to setup the filter course dropdown
    if setup:
        for value in Reviews.query.distinct(Reviews.course):    # Grab all unique courses
            courses.append(value.course)
        setup = False
    
    return render_template("reviews.html", reviews=posts, courses=courses)

# Data insights page
@main.route("/insights")
def insights():
    return render_template("insights.html")

# Conclusions page
@main.route("/conclusions")
def conclusions():
    return render_template("conclusions.html")
