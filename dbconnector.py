""" database.py file """
from flask_sqlalchemy import SQLAlchemy
 
""" SQLAlchemy Instance """
db = SQLAlchemy()

class alumni_detail(db.Model):
    alumni_id=db.Column(db.Integer,primary_key=True)
    full_name=db.Column(db.String(100),nullable=False)
    gender=db.Column(db.String(10),nullable=False)
    phone_number=db.Column(db.Integer,nullable=False)
    email=db.Column(db.String(100),nullable=False)
    linkedin_url=db.Column(db.String(100),nullable=False)
    w_address=db.Column(db.String(100),nullable=False)
    position=db.Column(db.String(100),nullable=False)
    offer_internship=db.Column(db.String(100),nullable=False)
    internship_type=db.Column(db.String(100),nullable=False)

class student_detail(db.Model):
    student_id=db.Column(db.Integer,primary_key=True)
    full_name=db.Column(db.String(100),nullable=False)
    gender=db.Column(db.String(10),nullable=False)
    phone_number=db.Column(db.Integer,nullable=False)
    email=db.Column(db.String(100),nullable=False)
    linkedin_url=db.Column(db.String(100),nullable=False)
    branch=db.Column(db.String(100),nullable=False)
    main_skill=db.Column(db.String(100),nullable=False)
    cgpa=db.Column(db.Integer,nullable=False)
    age=db.Column(db.Integer,nullable=False)
    db.CheckConstraint("cgpa<=10",name="check_cgpa")