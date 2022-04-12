from datetime import datetime
from app import db

class Reviews(db.Model):
    # Table name
    __tablename__ = 'reviews'

    """
    -- Columns and constraints --
    Overall rating (5stars)
    Overall rating (Description - Tell us about your overall university experience so far.)
    Job prospects (5stars)
    Job prospects (Description - How does your uni make efforts to increase your employability (careers department, work placements, transferable skills)?)
    Course and lecture (5 stars)
    Course and lecture (Description - What do you like most and least about the way your course(s) are taught?)
    Uni Facilities (5 stars)
    Uni Facilities (Description - How good are your university's facilities?)
    Student Support (5 stars)
    Student Support (Description - How good is the support offered by the uni? Think both academic (tutors/feedback) and personal (counselling, etc).)
    Local life (5 stars)
    Local life (Description - How good is the local life in your city?)
    """
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.Text(), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    overall_rating = db.Column(db.Integer, nullable=False)
    job_prospects_rating = db.Column(db.Integer, nullable=False)
    job_prospects_desc = db.Column(db.Text(), nullable=True)
    course_lecturer_rating = db.Column(db.Integer, nullable=False)
    course_lecturer_desc = db.Column(db.Text(), nullable=True)
    facilities_rating = db.Column(db.Integer, nullable=False)
    facilities_desc = db.Column(db.Text(), nullable=True)
    student_support_rating = db.Column(db.Integer, nullable=False)
    student_support_desc = db.Column(db.Text(), nullable=True)
    local_life_rating = db.Column(db.Integer, nullable=True)
    local_life_desc = db.Column(db.Text(), nullable=True)
    
    # Constructor
    def __init__(self, course, date, overall_rating, job_prospects_rating, job_prospects_desc,
                 course_lecturer_rating, course_lecturer_desc, facilities_rating, facilities_desc,
                 student_support_rating, student_support_desc, local_life_rating, local_life_desc):
        self.course = course
        self.date = date
        self.overall_rating = overall_rating
        self.job_prospects_rating = job_prospects_rating
        self.job_prospects_desc = job_prospects_desc
        self.course_lecturer_rating = course_lecturer_rating
        self.course_lecturer_desc = course_lecturer_desc
        self.facilities_rating = facilities_rating
        self.facilities_desc = facilities_desc
        self.student_support_rating = student_support_rating
        self.student_support_desc = student_support_desc
        self.local_life_rating = local_life_rating
        self.local_life_desc = local_life_desc
    
    def __repr__(self):
        return (f"Review('{self.course}', '{self.date}', '{self.overall_rating}', '{self.job_prospects_rating}', "
                f"'{self.job_prospects_desc}', '{self.course_lecturer_rating}', '{self.course_lecturer_desc}', '{self.facilities_rating}', "
                f"'{self.facilities_desc}', '{self.student_support_rating}', '{self.student_support_desc}', '{self.local_life_rating}', {self.local_life_desc}')")
