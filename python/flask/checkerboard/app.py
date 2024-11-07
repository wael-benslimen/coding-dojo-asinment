from flask import Flask,render_template 
app = Flask(__name__)    
@app.route('/')         
def chekerbord8():
    return render_template('index.html', number=4)

@app.route('/<int:number>')
def cheker_num(number):
     return render_template('index.html', number = number)
 
@app.route('/<int:number>/<col1>/<col2>')
def cheker_color(number, col1, col2):
     return render_template('index.html', number = number, col1 = col1, col2 = col2)

@app.route('/<int:number>/<col1>')
def cheker_color1(number, col1):
     return render_template('index.html', number = number, col1 = col1)
if __name__=="__main__":
    app.run(debug=True)   