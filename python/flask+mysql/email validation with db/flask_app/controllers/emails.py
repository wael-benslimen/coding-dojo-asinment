from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models.email import Email
from flask_bcrypt import Bcrypt


@app.route('/')
def index():
   return render_template('email_form.html')


@app.route('/valid')
def show_all():
    email_lists = Email.get_all()
    return render_template("valid.html", email_lists = email_lists)


@app.route('/prosses', methods = ['post'])
def emailentry():
    if not Email.everifcation(request.form):
        return redirect('/')
    else:
        Email.save_in_db(request.form)
        return redirect('/valid')

    
