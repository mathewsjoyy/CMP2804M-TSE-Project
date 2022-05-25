from app import create_app
from app import db

# Call the create_app function to create the app object
app = create_app()

if __name__ == '__main__':

    # Run the app
    app.run(debug=False)

