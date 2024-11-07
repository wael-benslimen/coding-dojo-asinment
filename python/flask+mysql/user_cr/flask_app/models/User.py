from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = "users_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        
        
    @classmethod
    def get_all(cls):
        query = "select * from users"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def save_in_db(cls,data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%s, %s, %s)"
        values = (data['name'], data['last_name'], data['email'])
        return connectToMySQL(cls.db).query_db(query, values)