from flask import request,render_template,redirect,session
from flask_app.model.dojo_model import Dojo
from flask_app import app 
######################################################## 
@app.route("/")  
def gete():
    return render_template("dojo_survey.html")  
@app.route("/resulte")
def resultttt(): 
    return render_template("resulta.html") 
##################################################################
@app.route("/dojo",methods=["POST"])
def get(): 
    if (Dojo.validate(request.form)==True):

        new_dojos={"name":request.form["name"], 
                "location":request.form["location"],
                "laguage":request.form["laguage"],
                "comment":request.form["comment"]
                } 
        session["resulat"]=Dojo.creat(new_dojos) 
    else:
        return redirect("/") 
    return redirect("/result")

# #####################################################
@app.route("/result") 
def result():   
    id=session["resulat"]
    data={ "id":id}
    return render_template("resulta.html",dojo=Dojo.get_dojos(data))