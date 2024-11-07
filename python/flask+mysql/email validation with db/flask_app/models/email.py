import re
from flask import flash
from flask_app import app, DATABASE
from flask_app.config.mysglconnection import  connectToMySQL
regex  = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class Email():
    def __init__(self, email):
        self.email = email
        
    
    @classmethod
    def get_all(cls):
        query = "select email from table1"
        results = connectToMySQL(DATABASE).query_db(query)
        emails = []
        for email in results:
            emails.append(cls(email))
        return emails
    
    
    @classmethod
    def save_in_db(cls,data):
        query = "INSERT INTO table1 (email) VALUES (%s)"
        values = (data['email'])
        resault = connectToMySQL(DATABASE).query_db(query, values)
        return resault
    
    
    
    @staticmethod
    def everifcation(object):
        valid = True
        if not regex.match(object["email"]):
            flash("wrong")
            valid = False
           
        return valid
    
    
    