from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
import re

regex  = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Register:
    def __init__(self, first_name, last_name, email, pw, cpw):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.pw = pw
    
    @classmethod
    def save_in_db(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, pw) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pw)s)"
        resault = connectToMySQL(DATABASE).query_db(query, data)
        return resault
    
    @classmethod
    def get_all_emails(cls):
        query = "SELECT email FROM users"
        results = connectToMySQL(DATABASE).query_db(query)
        emails = []
        for email in results:
            emails.append(email['email'])  # Extract email from dictionary
        return emails
    
    @staticmethod
    def validate_email(email):
        if not regex.match(email):
            flash("Email is invalid. Please enter a valid email address.")
            return False
        return True

    @staticmethod
    def email_in_db(email):
        valid = True
        emails = Register.get_all_emails()
        if email in emails:
            flash("This email is already registered. Please use a different email.")
            valid = False
        return valid

    @staticmethod
    def validate(data):
        valid = True
        if len(data['last_name']) < 2 :
            flash("First name should be 2 or more characters long.")
            valid = False
        if len(data['first_name']) < 2 :
            flash("Last name should be 2 or more characters long.")
            valid = False
        if not Register.validate_email(data['email']):
            valid = False
        if data['pw'] != data['cpw'] :
            flash("Your confirm password doesn't match.")
            valid = False
        return valid
