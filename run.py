from app import create_app

# Call the create_app function to create the app object
app = create_app()

if __name__ == '__main__':
    
    # Run the app, use debug=True to see the debug output, use debug=False to run in production
    app.run(debug=False)