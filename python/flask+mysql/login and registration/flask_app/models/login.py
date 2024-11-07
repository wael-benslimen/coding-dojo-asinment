from flask import flash
from flask_app import app
from flask_app.models.register import Register
from flask_bcrypt import Bcrypt
from flask import render_template, redirect, session, request
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

bcrypt = Bcrypt(app)

class Login:
    def __init__(self, login_email, login_pw):
        self.login_email = login_email
        self.login_pw = login_pw

    
    
    
    @staticmethod
    def user_id(email):
        query = 'select id from users where email = %(email)s'
        results = connectToMySQL(DATABASE).query_db(query, {'email': email})
        return results
        
    
      
    @staticmethod
    def email_in_db(email):
        query = 'SELECT * FROM users WHERE email = %(email)s'
        results = connectToMySQL(DATABASE).query_db(query, {'email': email})
        return bool(results) 
    
    
    
    @staticmethod
    def password_in_db(email, pw):
        query = 'SELECT pw FROM users WHERE email = %(email)s'
        results = connectToMySQL(DATABASE).query_db(query, {'email': email})

        if results:
            hashed_password = results[0]['pw']
            if bcrypt.check_password_hash(hashed_password, pw):
                return True
        return False

        

        