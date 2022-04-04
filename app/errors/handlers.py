from flask import Blueprint, render_template

errors = Blueprint('errors', __name__, template_folder='../templates', static_folder='../static')

# For custom error pages
@errors.app_errorhandler(404) # Specify what error to handle
def error_404(error):
    return render_template('site-errors/404.html'), 404

@errors.app_errorhandler(500)
def error_500(error):
    return render_template('site-errors/500.html'), 500
