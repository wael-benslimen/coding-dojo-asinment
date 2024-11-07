from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 
from flask_app import DATABASE
class Dojo:  
    def __init__(self,data):
        self.name=data["name"]
        self.location=data["location"]
        self.laguage=data["laguage"]
        self.comment=data["comment"]
        self.created_at=data["created_at"]
        self.updated_at=data['updated_at']
        self.id=data["id"]  

    @staticmethod
    def validate(data):  
        # length  name
        is_valid=True 
        if len(data['name'])<3: 
            flash("name must a lot 3 character","name")
            is_valid=False 
        #must choose a dojo loction
   
        if len(data['location'])==0:
            flash("must choose a dojo location","location") 
            is_valid=False  
        # mmust  chose a favorite language 
        if len(data['laguage'])==0: 
            flash("must choose a favorite language ","laguage") 
            is_valid=False 
        return is_valid
        #  ajoute le donne dans  basse 'dojos' 
    @classmethod 
    def creat(cls,data):
        query="insert into  dojos (name,location,laguage,comment) values (%(name)s,%(location)s,%(laguage)s,%(comment)s); "
        result=connectToMySQL(DATABASE).query_db(query,data)
        return result
    @classmethod 
    def get_dojos(cls,data): 
        query="select * from dojos where id=%(id)s"
        result=connectToMySQL(DATABASE).query_db(query,data)
        print(result)
        dojos=result[0]
        return dojos



