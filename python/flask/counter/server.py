from flask import Flask, render_template, request, redirect, session 
app = Flask(__name__)    
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def counter():
    if 'i' in session:
        session['i'] = session.get('i')+1
    else:
        session['i'] = 1
    return render_template('index.html')

@app.route('/reset')
def clear_session():
    session.clear()
    return redirect ('/')


@app.route('/add2')
def counter2():
    if 'i' in session:
        session['i'] = session.get('i')+2
    else:
        session['i'] = 1
    return render_template('index.html')






if __name__=="__main__":   
    app.run(debug=True)  