import sys
import time
from datetime import datetime
from bs4 import BeautifulSoup
import regex as re
import requests
import random
from app.models import Reviews

# Stores all scraped data
DATA = []

def clean_data(var, is_num: bool = False) -> tuple[str, int]:
    """
    Performs basic data cleaning on the data passed in
    and returns the cleaned data, or None if the data is not valid
    """
    if var is None:
        return None

    var = var.rstrip()

    if var == "":
        return None

    if is_num:
        var = int(var)
        return var

    var = str(var)
    return var

def connect_to_page(page_num: int) -> BeautifulSoup:
    """
    Connects to the page and returns the html data
    """
    
    # Define the url to connect to
    url = 'https://www.whatuni.com/university-course-reviews/university-of-lincoln/3747/?pageno={page_num}'.format(page_num=page_num)

    # List of user agents to randomly choose from to avoid being blocked
    user_agent_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    ]

    # Pick a random user agent
    user_agent = random.choice(user_agent_list)

    # Set the headers
    headers = {'User-Agent': user_agent}

    # Get the page
    connection = requests.get(url, headers=headers)

    # Check if the page has been successfully retrieved
    if connection.status_code != 200:
        print("Error: Status code is not 200 (connection failed)")
        sys.exit(0)
        
    # Get the page content
    soup = BeautifulSoup(connection.content, features='lxml')
    return soup

def scrape_data() -> None:
    """
    Main function to scrape the data from the desired website
    scraping for the given target categories
    """

    # Define the categories we want to scrape
    target_categories = {"OVERALL UNIVERSITY RATING": ["overall_rating"],
                            "Job Prospects": ["job_prospects_rating", "job_prospects_response"],
                            "Course and Lecturers": ["course_lecturer_rating", "course_lecturer_response"],
                            "Uni Facilities": ["facilities_rating", "facilities_response"],
                            "Student Support": ["student_suppport_rating", "student_support_response"],
                            "Local life": ["local_life_rating", "local_life_response"]}
    
    # Loop through amount of desired pages
    for page_num in range(1, 42):
        soup = connect_to_page(page_num)

        # Gets all reviews containers
        reviews = soup.find_all('div', class_='rlst_row')
        
        # Loop through each review and grab desired data
        for review in reviews:
            # Flag to check if review is valid, a review is valid if we have gotten all the data (11 targets) we want from it
            valid = 0
            
            # Store temporary data for a review
            datum = {}

            # Grab the date of the review, convert from string to datetime and then to desired format
            datum['date'] = datetime.strftime(datetime.strptime(clean_data(str(review.find('div', class_='rev_dte').text)), '%d %b %y'), '%Y-%m-%d')

            if review.find('h3') is None:   # Some reviews don't have a course (we don't want these reviews)
                datum['course'] = clean_data(review.find('h3').text)
            else:
                continue    # Skip this review

            # Get html data for each rating category for this review e.g. overall rating, student support rating etc.
            rating_categories = review.find_all('div', class_='rate_new')

            # Loop through each rating category and grab desired data, if there is no data for a category, it will be skipped entirely
            # (1. The category 2. The rating 3. The question response
            for category in rating_categories:
                try:
                    for key in target_categories:
                        if category.find('span', class_='cat_rat').text == key:
                            # Grab the rating number
                            datum[target_categories[key][0]] = clean_data(str(category.find('span', class_=re.compile('ml5 rat rat*')))[-10], True)
                            valid += 1
                            
                            # If there is a response to the question, get the response
                            if category.find('p', class_='rev_dec') is None and key != "OVERALL UNIVERSITY RATING":
                                datum[target_categories[key][1]] = clean_data(str(category.find('p', class_='rev_dec').text))
                                valid += 1
                except Exception:   # Catch categories that have no category rating heading (we don't want these anyway)
                    continue
            
            # Append the temporary data if we have gotten desired data to the global data
            if valid == 11:
                global DATA
                DATA.append(datum)

        # Wait some amount of time before connecting to the next page, to avoid getting blocked
        time.sleep(1.0)

        print(f"Page {page_num} has been scraped.")

# Pass in database object and check if there is a valid connection
def connectToDatabase(databaseObject) -> bool:
    if databaseObject.session():
        print("Connected to database")
        return True
    else:
        print("Could not connect to database")
        return False

# Calls the scrape function to scrape required data, and pushes the data to passed in database object
def scrape_and_store_data(databaseObject) -> None:
    scrape_data()
    
    if connectToDatabase(databaseObject):
        # Insert all data into the database
        for review in DATA:
            try:
                # Check if review is already in the database from same user
                if (databaseObject.session.query(Reviews).filter(Reviews.date == review['date']).count() > 0 and
                    databaseObject.session.query(Reviews).filter(Reviews.course == review['course']).count() > 0 and
                    databaseObject.session.query(Reviews).filter(Reviews.overall_rating == review['overall_rating']).count() > 0):
                    print("Review already exists, review rejected\n")
                    continue
                else:
                    data = Reviews(review['course'], review['date'], review['overall_rating'], review['job_prospects_rating'],
                                   review['job_prospects_response'], review['course_lecturer_rating'], review['course_lecturer_response'],
                                   review['facilities_rating'], review['facilities_response'], review['student_suppport_rating'],
                                   review['student_support_response'], review['local_life_rating'], review['local_life_response'])
                    databaseObject.session.add(data)
                    databaseObject.session.commit()
            except Exception as e:
                print("Could not insert review: " + str(review) + str(e))
                continue
    else:
        print("Could not connect to database.")
