from app import create_app

# Call the create_app function to create the app object
app = create_app()

if __name__ == '__main__':
    
    # Run the app
    app.run()