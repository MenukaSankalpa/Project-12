from flask import Flask, render_template
from flask_wtf import FlaskForm  

app = Flask(__name__, template_folder='templates')

@app.route('/')
def Hello():
    return render_template('index.html')

@app.route('/register')
def register1():
    return render_template('index.html')

@app.route('/login')
def login1():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard1(): 
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)