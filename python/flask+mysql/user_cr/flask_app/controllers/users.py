from flask import Flask, render_template, request, redirect, session 
from flask_app.models.user import User
from flask_app import app

@app.route('/users')
def read_all():
    users_list = User.get_all()
    return render_template("read_all.html", users = users_list)


@app.route('/users/new')
def create_user():
    return render_template("create.html")

@app.route('/users/create', methods=['post'])
def create():
    User.save_in_db(request.form)
    return redirect("/users")
    