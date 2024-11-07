from flask import Flask,render_template 
app = Flask(__name__)    
@app.route('/play/<int:num>')          
def hello_world(num):
    return  render_template('index.html', number=num) 

@app.route('/play')
def play():
    return render_template('index.html', number=3)

@app.route('/play/<int:num>/<col>')
def color(num, col):
    return render_template('index.html', number=num, col=col)





if __name__=="__main__":    
    app.run(debug=True)    