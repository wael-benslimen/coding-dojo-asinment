from flask import Flask, render_template, request, redirect, session
from random import randint

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'random_number' not in session:
        session['random_number'] = randint(1, 100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def num():
    user_guess = int(request.form['number'])
    session['number'] = user_guess
    random_number = session['random_number']
     
    if user_guess < random_number:
        feedback = "too low"
    elif user_guess > random_number:
        feedback = "too high"
    else:
        feedback = "correct"
        session.pop('random_number', None)

    return render_template('guess.html', feedback=feedback, random_number=random_number if feedback == "correct" else None)

if __name__ == "__main__":
    app.run(debug=True)
