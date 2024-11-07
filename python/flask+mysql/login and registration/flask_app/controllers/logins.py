from flask import flash
from flask_app import app
from flask_app.models.register import Register
from flask_app.models.login import Login
from flask_bcrypt import Bcrypt
from flask import render_template, redirect, session, request


bcrypt = Bcrypt(app)


#main rout
@app.route('/')
def main():
    return render_template('login_register.html')
    

@app.route('/register', methods=['POST'])
def create_user():
    if not Register.validate(request.form):
        return redirect('/')

    if not Register.email_in_db(request.form['email']):
        return redirect('/')

    pw_hush = bcrypt.generate_password_hash(request.form['pw'])

    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "pw": pw_hush
    }

    Register.save_in_db(data)

    return redirect('/logout')
 
@app.route('/login', methods=['POST'])
def login():
    if not Login.email_in_db(request.form['login_email']):
        flash('Invalid email. Please try again.')
        return redirect('/')

    if not Login.password_in_db(request.form['login_email'], request.form['login_pw']):
        flash('Incorrect password. Please try again.')
        return redirect('/')

    session["connected_email"] = request.form['login_email']
    session["id"] = Login.user_id(request.form['login_email'])
    return redirect('/logout') 


@app.route('/logout')
def logout():
    return render_template("logout.html")

@app.route('/clear')
def clear():
    print('8'*50)
    print(session["id"])
    print('8'*50)
    session.clear()
    return redirect('/')

