from app import create_app
#from app.additionals.scrape import scrape_and_store_data # Used to scrape data from website
from app import db

# Call the create_app function to create the app object
app = create_app()

#app.app_context().push()

if __name__ == '__main__':
    # Scrape data and insert into db, should find better way to do this
    # E.g. add a flag to the command line to run this, but does the job for now
    #scrape_and_store_data(db)

    # Run the app
    app.run(debug=False)    # TODO CHANGE TO FALSE WHEN COMMITING TO HEROKU

