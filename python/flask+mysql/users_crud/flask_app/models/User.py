from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import db

class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        
        
    @classmethod
    def get_all(cls):
        query = "select * from users"
        results = connectToMySQL(db).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM users WHERE id = %(id)s"
        # data = {"id": id}
        resault = connectToMySQL(db).query_db(query, {"id": id})
        return cls(resault[0])
    
    @classmethod
    def save_in_db(cls,data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%s, %s, %s)"
        values = (data['name'], data['last_name'], data['email'])
        return connectToMySQL(db).query_db(query, values)
    
    @classmethod
    def delete(cls, id):
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL(db).query_db(query,id)