from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route("/dojo")
def dojo():
    return "dojo"

@app.route('/say')
def say():
    return "hi"
@app.route("/say/flask")
def hi_flask():
    return "hi flask"

@app.route('/say/michael')
def hi_michael():
    return "hi michael"

@app.route('/say/jhon')
def jhon():
    return "hi jhon"

@app.route('/rep/<name>/<int:num>') 
def rep(name, num):
    return f"{name * num}"







if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
